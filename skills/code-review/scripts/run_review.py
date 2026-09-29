"""Revisione locale seriale con sessioni indipendenti e prove verificabili."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

MODEL = "gpt-6.1-sol"
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("before", "after", "diff.patch", "contract.md", "manifest.json")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fingerprint(case):
    result = {}
    for path in sorted(case.rglob("*")):
        require(not path.is_symlink(), f"Collegamento nel caso: {path.name}")
        require(path.resolve().is_relative_to(case), "Percorso esterno al caso")
        if path.is_file():
            result[path.relative_to(case).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def unchanged(case, frozen):
    require(fingerprint(case) == frozen, "Il contenuto del caso è stato alterato")


def changed_paths(case):
    before = {p.relative_to(case / "before").as_posix(): p.read_bytes()
              for p in (case / "before").rglob("*") if p.is_file()}
    after = {p.relative_to(case / "after").as_posix(): p.read_bytes()
             for p in (case / "after").rglob("*") if p.is_file()}
    return sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))


def validate(value, schema):
    """Valida il sottoinsieme JSON Schema usato dalle risposte."""
    kind = schema["type"]
    expected = {"object": dict, "array": list, "string": str, "integer": int}[kind]
    require(type(value) is expected, f"Tipo JSON atteso: {kind}")
    if "enum" in schema:
        require(value in schema["enum"], "Valore fuori enumerazione")
    if kind == "object":
        require(set(value) == set(schema["required"]), "Campi JSON mancanti o aggiunti")
        for name, child in value.items():
            validate(child, schema["properties"][name])
    elif kind == "array":
        for child in value:
            validate(child, schema["items"])
    elif kind == "string":
        require(bool(value.strip()), "Testo vuoto")
    else:
        require(value >= schema.get("minimum", 0), "Numero fuori intervallo")


def location(case, finding, changed):
    relative = finding["file"]
    side = "after" if (case / "after" / relative).exists() else "before"
    path = case / side / relative
    require(relative in changed and Path(relative).as_posix() == relative,
            "Rilievo fuori dai percorsi modificati")
    require(path.resolve().is_relative_to(case / side) and path.is_file(), "Rilievo senza sorgente")
    lines = len(path.read_text(encoding="utf-8").splitlines())
    require(1 <= finding["line_start"] <= finding["line_end"] <= lines,
            "Intervallo del rilievo fuori dal sorgente")
    return side


def validate_search(case, response, changed, schema):
    validate(response, schema)
    ids = [finding["id"] for finding in response["findings"]]
    require(len(ids) == len(set(ids)), "Identificatori duplicati")
    for finding in response["findings"]:
        location(case, finding, changed)
    covered = [entry["file"] for entry in response["coverage"]]
    require(len(covered) == len(set(covered)) and set(covered) == set(changed),
            "Copertura diversa dai percorsi modificati")
    for entry in response["coverage"]:
        require(bool(entry["aspects"]), "Copertura senza aspetti esaminati")


def effective_context(thread_id, effort):
    require(isinstance(thread_id, str) and thread_id and
            all(c.isalnum() or c == "-" for c in thread_id), "Identificatore sessione invalido")
    sessions = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "sessions"
    contexts = []
    for path in sessions.rglob(f"*{thread_id}*.jsonl"):
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                record = json.loads(line)
                if record.get("type") == "turn_context":
                    payload = record["payload"]
                    require(payload.get("approval_policy") == "never", "Politica di approvazione effettiva diversa")
                    contexts.append({"model": payload.get("model"),
                                     "effort": payload.get("effort", payload.get("reasoning_effort")),
                                     "sandbox": payload.get("sandbox_policy")})
    require(bool(contexts), "Contesto effettivo della sessione assente")
    for context in contexts:
        check_model(context, effort)
        require(isinstance(context["sandbox"], dict) and
                context["sandbox"].get("type") == "read-only", "Protezione effettiva diversa dalla sola lettura")
    # Il registro conserva solo il tipo di protezione, mai il contenuto integrale della sessione.
    return {"model": MODEL, "effort": effort, "sandbox": "read-only"}


def check_model(context, effort):
    require(context["model"] == MODEL and context["effort"] == effort,
            "Modello o ragionamento effettivo diverso da quello richiesto")


def check_completion(exit_code, events):
    require(exit_code == 0, f"Codex terminato con codice {exit_code}")
    require(not any(e.get("type") in ("error", "turn.failed") for e in events),
            "Sessione Codex fallita")
    completed = [e for e in events if e.get("type") == "turn.completed"]
    require(len(completed) == 1 and isinstance(completed[0].get("usage"), dict),
            "Completamento o consumo della sessione assente")
    return completed[0]["usage"]


def run_call(args, frozen, label, prompt, schema_path, metrics):
    unchanged(args.case, frozen)
    response_path = args.output / f"{label}.json"
    command = [args.codex, "--no-daemon", "-a", "never",
               "-c", 'windows.sandbox="unelevated"', "-c", f'review_model="{MODEL}"',
               "-c", f'model_reasoning_effort="{args.effort}"', "exec", "--ignore-user-config", "-m", MODEL,
               "--sandbox", "read-only", "--skip-git-repo-check", "--json",
               "--output-schema", str(schema_path), "-o", str(response_path), "-"]
    started = time.monotonic()
    record = {"stage": label, "requested_model": MODEL, "requested_effort": args.effort,
              "exit_code": None, "elapsed_seconds": None, "usage": None, "effective": None}
    metrics["calls"].append(record)
    process = subprocess.Popen(command, cwd=args.case, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               encoding="utf-8", errors="strict")
    try:
        stdout, stderr = process.communicate(prompt, timeout=args.timeout_seconds)
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        process.kill()
        stdout, stderr = process.communicate()
        record["timed_out"] = True
    finally:
        record["elapsed_seconds"] = round(time.monotonic() - started, 3)
        record["exit_code"] = process.returncode
        unchanged(args.case, frozen)
    (args.output / f"{label}.events.jsonl").write_text(stdout, encoding="utf-8")
    # stderr può contenere dettagli dell'account: nel rapporto entra solo la sua presenza.
    record["stderr_present"] = bool(stderr)
    require(not record.get("timed_out"), "Tempo massimo della sessione raggiunto")
    events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
    record["usage"] = check_completion(process.returncode, events)
    threads = [e.get("thread_id") for e in events if e.get("type") == "thread.started"]
    require(len(threads) == 1, "Sessione indipendente non identificata")
    require(threads[0] not in metrics["thread_ids"], "Contesto di sessione riutilizzato")
    metrics["thread_ids"].append(threads[0])
    record["effective"] = effective_context(threads[0], args.effort)
    return json.loads(response_path.read_text(encoding="utf-8"))


def prompt_base(case, changed):
    return f"""Esegui un audit locale in italiano, in sola lettura, su questo caso: {case}.
Leggi solo before/, after/, diff.patch, contract.md, manifest.json e gli AGENTS.md inclusi nel caso.
Il contratto definisce il comportamento voluto. Rispetta le istruzioni applicabili
e le decisioni autorizzate riportate nel contratto; conserva i conflitti irrisolti nei limiti.
Usa solo letture del caso: nessuna rete, account, configurazione, compilazione, test,
scrittura con strumenti o delega. Restituisci soltanto il JSON richiesto.
Percorsi modificati: {json.dumps(changed)}.
Ogni rilievo descrive un difetto concreto con causa, condizione di attivazione,
conseguenza e prova nel sorgente e nella differenza. Indica il percorso relativo ad after/
e righe reali di after/. Se il file è eliminato e assente in after/, usa le righe
del file esistente in before/ e indica nell'evidenza che sono riferite a before/.
Copri ogni percorso modificato una volta, con aspetti esaminati e prove specifiche.
Distingui i difetti dalle preferenze; registra i limiti dell'esame statico.
"""


def verify_response(case, response, candidates, changed, schema):
    validate(response, schema)
    candidate_ids = {c["id"] for c in candidates}
    decision_ids = [d["id"] for d in response["decisions"]]
    require(len(decision_ids) == len(set(decision_ids)) and set(decision_ids) == candidate_ids,
            "Decisioni mancanti, duplicate o relative a un altro candidato")
    accepted = response["accepted_findings"]
    accepted_ids = [f["id"] for f in accepted]
    require(len(accepted_ids) == len(set(accepted_ids)) and set(accepted_ids) <= candidate_ids,
            "Rilievi accettati duplicati o sconosciuti")
    canonical_ids = {d["canonical_id"] for d in response["decisions"] if d["decision"] == "accept"}
    require(canonical_ids == set(accepted_ids), "Rilievi incoerenti con le decisioni")
    decisions_by_id = {d["id"]: d for d in response["decisions"]}
    for canonical_id in accepted_ids:
        own = decisions_by_id[canonical_id]
        require(own["decision"] == "accept" and own["canonical_id"] == canonical_id,
                "Rilievo canonico privo della propria decisione accept")
    for decision in response["decisions"]:
        if decision["decision"] != "accept":
            require(decision["canonical_id"] == "-", "Decisione esclusa con riferimento canonico")
    for finding in accepted:
        location(case, finding, changed)
    return accepted


def totals(metrics):
    calls = metrics["calls"]
    usages = [call["usage"] for call in calls if isinstance(call.get("usage"), dict)]
    keys = sorted({key for usage in usages for key, value in usage.items() if type(value) is int})
    return {"elapsed_seconds": round(sum(call.get("elapsed_seconds") or 0 for call in calls), 3),
            "usage": {key: sum(usage.get(key, 0) for usage in usages) for key in keys}}


def main(args):
    args.case = args.case.resolve()
    args.output = args.output.resolve()
    require(args.case.is_dir(), "Caso assente")
    require(not args.output.is_relative_to(args.case) and not args.case.is_relative_to(args.output),
            "Risultati e caso devono stare in cartelle separate")
    require(all((args.case / name).exists() for name in REQUIRED), "Caso incompleto")
    require((args.case / "before").is_dir() and (args.case / "after").is_dir(), "Sorgenti assenti")
    require(args.effort != "xhigh" or bool(args.effort_reason and args.effort_reason.strip()),
            "xhigh richiede una motivazione esplicita con --effort-reason")
    require(math.isfinite(args.timeout_seconds) and args.timeout_seconds > 0, "Tempo massimo invalido")
    require(not args.output.exists(), "La cartella dei risultati deve essere nuova")
    frozen = fingerprint(args.case)
    changed = changed_paths(args.case)
    manifest = json.loads((args.case / "manifest.json").read_text(encoding="utf-8"))
    require(isinstance(manifest, dict) and isinstance(manifest.get("changed_files"), list) and
            sorted(manifest["changed_files"]) == changed, "Manifesto diverso dai percorsi modificati")
    args.output.mkdir(parents=True)
    schemas = {name: json.loads((ROOT / "references" / f"{name}.schema.json").read_text(encoding="utf-8"))
               for name in ("report", "verification")}
    metrics = {"status": "running", "case_fingerprint": frozen, "changed_paths": changed,
               "effort_reason": args.effort_reason, "calls": [], "thread_ids": []}
    accepted, decisions, coverage, limitations = [], [], [], []
    try:
        base = prompt_base(args.case, changed)
        candidates = []
        for index, focus in enumerate(("contratto e correttezza", "flussi, regressioni e sicurezza"), 1):
            response = run_call(args, frozen, f"search-{index}", base +
                                f"\nRicerca indipendente: {focus}. Prefissa gli ID con S{index}-.",
                                ROOT / "references/report.schema.json", metrics)
            validate_search(args.case, response, changed, schemas["report"])
            require(all(f["id"].startswith(f"S{index}-") for f in response["findings"]), "Prefisso ID errato")
            candidates.extend(response["findings"])
            coverage.append({"search": index, "files": response["coverage"]})
            limitations.extend(response["limitations"])
        require(len({c["id"] for c in candidates}) == len(candidates), "ID duplicati fra ricerche")
        response = run_call(args, frozen, "verify", base +
            "\nVerifica autonomamente ogni candidato contro sorgenti e differenza. "
            "Decidi accept, reject o unverified per ogni ID con prove specifiche. "
            "Deduplica solo difetti con uguale causa, attivazione e conseguenza dimostrate. "
            "accepted_findings contiene i rilievi dimostrati, con posizione controllata e un ID "
            "originale canonico. Ogni decisione accept indica quel canonical_id; "
            "il candidato canonico ha una propria decisione accept riferita a sé stesso; "
            "reject e unverified indicano canonical_id '-'. Mantieni distinti difetti diversi.\n" +
            json.dumps(candidates, ensure_ascii=False), ROOT / "references/verification.schema.json", metrics)
        accepted.extend(verify_response(args.case, response, candidates, changed, schemas["verification"]))
        decisions.extend(response["decisions"])
        limitations.extend(response["limitations"])
        findings = sorted(accepted, key=lambda f: (f["severity"], f["file"], f["line_start"], f["id"]))
        limitations = list(dict.fromkeys(limitations))
        save(args.output / "findings.json", {"findings": findings, "decisions": decisions,
                                             "coverage": coverage, "limitations": limitations})
        lines = ["# Revisione locale", "", f"Rilievi confermati: {len(findings)}. Candidati: {len(candidates)}.",
                 "", "Risultati da lettura statica dei sorgenti.", ""]
        for field in ("target", "base", "head"):
            if field in manifest:
                lines.append(f"{field}: {manifest[field]}")
        summary = totals(metrics)
        lines += [f"Somma delle durate delle chiamate seriali: {summary['elapsed_seconds']} secondi.",
                  f"Consumo totale registrato: {json.dumps(summary['usage'], ensure_ascii=False)}.", ""]
        for finding in findings:
            side = location(args.case, finding, changed)
            lines += [f"- {finding['severity']} {side}/{finding['file']}:{finding['line_start']} — {finding['title']}",
                      f"  {finding['trigger']} → {finding['consequence']}", f"  Prova: {finding['evidence']}",
                      f"  Contratto: {finding['contract_basis']}"]
        unverified = sum(d["decision"] == "unverified" for d in decisions)
        lines += ["", f"Candidati da verificare: {unverified}."]
        lines += ["", "## Copertura", ""]
        for search in coverage:
            for entry in search["files"]:
                lines.append(f"- Ricerca {search['search']}, {entry['file']}: " +
                             "; ".join(entry["aspects"]) + f". Prova: {entry['evidence']}")
        lines += ["", "## Limiti", ""] + [f"- {limit}" for limit in limitations]
        (args.output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        metrics["status"] = "complete"
    except Exception as error:
        metrics["status"] = "failed"
        metrics["failure"] = str(error)
        raise
    finally:
        metrics["totals"] = totals(metrics)
        save(args.output / "metrics.json", metrics)


def selfcheck():
    events = [{"type": "turn.completed", "usage": {"input_tokens": 7}}]
    with tempfile.TemporaryDirectory() as folder:
        case = Path(folder)
        (case / "after").mkdir()
        source = case / "after/a.py"
        source.write_text("print(1)\n", encoding="utf-8")
        frozen = fingerprint(case)
        source.write_text("print(2)\n", encoding="utf-8")
        invalid = {"id": "S1-1", "severity": "P2", "file": "a.py", "line_start": 2, "line_end": 2,
                   "title": "difetto", "trigger": "input", "consequence": "errore", "evidence": "riga",
                   "contract_basis": "contratto"}
        verification = {"decisions": [{"id": "S1-1", "decision": "accept", "evidence": "riga",
                                       "canonical_id": "S1-1"}], "accepted_findings": [invalid], "limitations": []}
        schema = json.loads((ROOT / "references/verification.schema.json").read_text(encoding="utf-8"))
        first = {**invalid, "id": "A", "line_start": 1, "line_end": 1}
        second = {**first, "id": "B"}
        contradictory = {"decisions": [{"id": "A", "decision": "reject", "evidence": "escluso", "canonical_id": "-"},
                                        {"id": "B", "decision": "accept", "evidence": "prova", "canonical_id": "A"}],
                         "accepted_findings": [first], "limitations": []}
        checks = [lambda: check_completion(1, events), lambda: unchanged(case, frozen),
                  lambda: check_model({"model": "other", "effort": "medium"}, "medium"),
                  lambda: verify_response(case, contradictory, [first, second], ["a.py"], schema),
                  lambda: verify_response(case, verification, [invalid], ["a.py"], schema)]
        for check in checks:
            try:
                check()
            except ValueError:
                continue
            raise AssertionError("Controllo di sicurezza aggirato")
        valid = {**contradictory, "decisions": [{"id": name, "decision": "accept", "evidence": "prova",
                                                 "canonical_id": "A"} for name in ("A", "B")]}
        require(verify_response(case, valid, [first, second], ["a.py"], schema) == [first], "Dedup valida respinta")
        (case / "before").mkdir()
        source.rename(case / "before/a.py")
        require(location(case, first, ["a.py"]) == "before", "Localizzazione eliminazione errata")
        require(verify_response(case, valid, [first, second], ["a.py"], schema) == [first], "Eliminazione valida respinta")
        try:
            location(case, invalid, ["a.py"])
        except ValueError:
            pass
        else:
            raise AssertionError("Intervallo invalido del file eliminato accettato")
    print("Autoverifica superata: sicurezza, integrità canonica, dedup valida e localizzazione eliminazioni.")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selfcheck"]:
        selfcheck()
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--case", type=Path, required=True)
        parser.add_argument("--output", type=Path, required=True)
        parser.add_argument("--codex", required=True)
        parser.add_argument("--timeout-seconds", type=float, required=True)
        parser.add_argument("--effort", choices=("medium", "xhigh"), default="medium")
        parser.add_argument("--effort-reason")
        try:
            main(parser.parse_args())
        except Exception as error:
            print(f"Revisione interrotta: {error}", file=sys.stderr)
            sys.exit(1)
