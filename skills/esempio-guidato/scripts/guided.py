#!/usr/bin/env python3
"""Local bridge between a Codex task and its guided code walkthrough page."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import math
import os
import queue
import secrets
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath


MAX_TEXT_BYTES = 2 * 1024 * 1024
MAX_REQUEST_BYTES = 6 * 1024 * 1024
WEB_DIR = Path(__file__).resolve().parent.parent / "web" / "dist"
DIAGRAM_VALIDATOR = WEB_DIR.parent / "src" / "diagram_validation.mjs"


def validate_diagram(source: object) -> str:
    if not isinstance(source, str) or not source.strip() or len(source.encode("utf-8")) > MAX_TEXT_BYTES:
        raise ValueError("Diagramma mancante o non valido")
    node = shutil.which("node")
    if not node:
        raise ValueError("Node.js necessario per verificare il diagramma")
    result = subprocess.run([node, str(DIAGRAM_VALIDATOR)], input=source, text=True, encoding="utf-8", capture_output=True)
    if result.returncode or result.stdout != "valid":
        raise ValueError("Diagramma Mermaid non valido: usa flowchart senza configurazione o callback")
    return source.strip()


def write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class GuidedServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, session_dir: Path):
        port_file = session_dir / "port.txt"
        port = int(port_file.read_text(encoding="ascii")) if port_file.exists() else 0
        super().__init__(("127.0.0.1", port), GuidedHandler)
        self.session_dir = session_dir
        self.config = read_json(session_dir / "config.json")
        self.root = Path(self.config["root"]).resolve()
        self.state_path = session_dir / "state.json"
        self.state = read_json(self.state_path)
        self.state.setdefault("diagram", None)
        self.lock = threading.Lock()
        self.events: queue.Queue[dict] = queue.Queue()
        self.notes_path = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "esempio-guidato" / "notes" / f"{sha256(os.path.normcase(str(self.root)))}.json"
        if self.state["awaitingAnswer"]:
            question = next(message for message in reversed(self.state["messages"]) if message["role"] == "user")
            self.events.put({"type": "question", "text": question["text"], "stepId": question["stepId"]})
        elif self.state["released"] and not self.state["finished"]:
            self.events.put({"type": "next", "stepId": self.state["currentStepId"]})

    def safe_path(self, name: str, *, allow_root: bool = False) -> Path:
        if not isinstance(name, str) or "\x00" in name:
            raise ValueError("Percorso non valido")
        normalized = name.replace("\\", "/")
        parts = PurePosixPath(normalized).parts
        if normalized.startswith("/") or ".." in parts or (parts and ":" in parts[0]):
            raise ValueError("Percorso fuori dal progetto")
        if not normalized and not allow_root:
            raise ValueError("Percorso mancante")
        candidate = self.root.joinpath(*parts).resolve()
        if not candidate.is_relative_to(self.root):
            raise ValueError("Percorso fuori dal progetto")
        return candidate

    def read_file(self, name: str, *, allow_missing: bool = False) -> str:
        path = self.safe_path(name)
        if allow_missing and not path.exists():
            return ""
        if not path.is_file() or path.stat().st_size > MAX_TEXT_BYTES:
            raise ValueError("File non leggibile nella pagina")
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("File di testo non riconosciuto") from exc

    def save(self) -> None:
        write_json(self.state_path, self.state)

    def update_diagram(self, source: str) -> None:
        previous = self.state["diagram"]
        revision = previous["revision"] if previous else 0
        if not previous or source != previous["source"]:
            revision += 1
        self.state["diagram"] = {"source": source, "revision": revision, "stepId": self.state["currentStepId"]}

    def list_files(self) -> list[dict]:
        files = []
        directories = [self.root]
        visited = {self.root}
        while directories:
            with os.scandir(directories.pop()) as entries:
                for entry in entries:
                    if entry.name == ".git" or entry.is_symlink():
                        continue
                    path = Path(entry.path)
                    if entry.is_dir(follow_symlinks=False):
                        resolved = path.resolve()
                        if resolved.is_relative_to(self.root) and resolved not in visited:
                            visited.add(resolved)
                            directories.append(path)
                    elif entry.is_file(follow_symlinks=False):
                        files.append({"name": entry.name, "path": path.relative_to(self.root).as_posix()})
        return sorted(files, key=lambda file: file["path"].casefold())

    def read_notes(self) -> dict:
        with self.lock:
            return read_json(self.notes_path) if self.notes_path.exists() else {"text": "", "position": None}

    def save_notes(self, payload: dict) -> None:
        text, position = payload.get("text"), payload.get("position")
        if not isinstance(text, str) or len(text.encode("utf-8")) > MAX_TEXT_BYTES:
            raise ValueError("Note non valide")
        if position is not None:
            if not isinstance(position, dict) or set(position) != {"x", "y"}:
                raise ValueError("Posizione non valida")
            if any(isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0 for value in position.values()):
                raise ValueError("Posizione non valida")
        with self.lock:
            self.notes_path.parent.mkdir(parents=True, exist_ok=True)
            write_json(self.notes_path, {"text": text, "position": position})

    def capture(self, name: str) -> dict:
        content = self.read_file(name, allow_missing=True)
        snapshot_id = uuid.uuid4().hex
        write_json(
            self.session_dir / "snapshots" / f"{snapshot_id}.json",
            {"file": name, "content": content},
        )
        return {"snapshotId": snapshot_id, "sha256": sha256(content)}

    def publish(self, payload: dict) -> dict:
        diagram = validate_diagram(payload.get("diagram"))
        kind = payload.get("kind")
        if kind not in ("exploration", "change"):
            raise ValueError("Tipo di passo non valido")
        name = payload.get("file")
        after = self.read_file(name)
        lines = after.splitlines()
        start, end = payload.get("startLine"), payload.get("endLine")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Righe non valide")
        if start < 1 or end < start or end > max(1, len(lines)):
            raise ValueError("Righe fuori dal file")
        for field in ("title", "overview", "why"):
            if not isinstance(payload.get(field), str) or not payload[field].strip():
                raise ValueError(f"Campo {field} mancante")
        annotations = payload.get("annotations")
        if not isinstance(annotations, list) or not annotations:
            raise ValueError("Spiegazioni delle righe mancanti")
        before = None
        changed_after_lines: set[int] = set()
        if kind == "change":
            snapshot_id = payload.get("snapshotId")
            if not isinstance(snapshot_id, str) or not snapshot_id.isalnum():
                raise ValueError("Acquisizione precedente mancante")
            snapshot_path = self.session_dir / "snapshots" / f"{snapshot_id}.json"
            if not snapshot_path.is_file():
                raise ValueError("Acquisizione precedente sconosciuta")
            snapshot = read_json(snapshot_path)
            if snapshot["file"] != name:
                raise ValueError("L'acquisizione riguarda un altro file")
            before = snapshot["content"]
            if before == after:
                raise ValueError("Il file non presenta modifiche")
            matcher = difflib.SequenceMatcher(a=before.splitlines(), b=lines, autojunk=False)
            for operation, _i1, _i2, j1, j2 in matcher.get_opcodes():
                if operation != "equal":
                    if j1 == j2:
                        changed_after_lines.add(min(max(1, j1 + 1), max(1, len(lines))))
                    else:
                        changed_after_lines.update(range(j1 + 1, j2 + 1))
            if any(line < start or line > end for line in changed_after_lines):
                raise ValueError("Il passo deve comprendere tutte le righe modificate")
        for annotation in annotations:
            if not isinstance(annotation, dict) or not isinstance(annotation.get("line"), int):
                raise ValueError("Spiegazione di riga non valida")
            if not isinstance(annotation.get("explanation"), str) or not annotation["explanation"].strip():
                raise ValueError("Testo della spiegazione mancante")
            side = annotation.get("side", "after")
            source = before.splitlines() if side == "before" and before is not None else lines
            if side not in ("after", "before") or (side == "before" and before is None):
                raise ValueError("Lato della spiegazione non valido")
            if annotation["line"] < 1 or annotation["line"] > len(source):
                raise ValueError("Spiegazione fuori dal file")
        step = {
            "id": uuid.uuid4().hex,
            "index": len(self.state["steps"]) + 1,
            "kind": kind,
            "title": payload["title"].strip(),
            "overview": payload["overview"].strip(),
            "why": payload["why"].strip(),
            "file": name,
            "startLine": start,
            "endLine": end,
            "annotations": annotations,
            "before": before,
            "after": after,
            "sha256": sha256(after),
        }
        with self.lock:
            if self.state["finished"]:
                raise ValueError("Percorso già concluso")
            write_json(self.session_dir / "steps" / f"{step['id']}.json", step)
            self.state["steps"].append({key: value for key, value in step.items() if key not in ("before", "after")})
            self.state["currentStepId"] = step["id"]
            self.update_diagram(diagram)
            self.state["released"] = False
            self.state["awaitingAnswer"] = False
            self.save()
        return {"stepId": step["id"], "index": step["index"]}


class GuidedHandler(BaseHTTPRequestHandler):
    server: GuidedServer

    def log_message(self, format: str, *args: object) -> None:
        pass

    def send_json(self, status: int, value: object) -> None:
        body = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def authorized(self) -> bool:
        return secrets.compare_digest(
            self.headers.get("X-Guided-Token", ""), self.server.config["token"]
        )

    def body_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length < 1 or length > MAX_REQUEST_BYTES:
            raise ValueError("Richiesta troppo grande o vuota")
        payload = json.loads(self.rfile.read(length))
        if not isinstance(payload, dict):
            raise ValueError("Richiesta non valida")
        return payload

    def do_GET(self) -> None:
        url = urllib.parse.urlsplit(self.path)
        if url.path.startswith("/api/"):
            if not self.authorized():
                self.send_json(403, {"error": "Accesso negato"})
                return
            try:
                params = urllib.parse.parse_qs(url.query)
                if url.path == "/api/state":
                    with self.server.lock:
                        self.send_json(200, self.server.state)
                elif url.path == "/api/step":
                    step_id = params.get("id", [""])[0]
                    with self.server.lock:
                        known = any(step["id"] == step_id for step in self.server.state["steps"])
                    if not known:
                        raise ValueError("Passo sconosciuto")
                    self.send_json(200, read_json(self.server.session_dir / "steps" / f"{step_id}.json"))
                elif url.path == "/api/file":
                    name = params.get("path", [""])[0]
                    self.send_json(200, {"path": name, "content": self.server.read_file(name)})
                elif url.path == "/api/files":
                    self.send_json(200, {"files": self.server.list_files()})
                elif url.path == "/api/notes":
                    self.send_json(200, self.server.read_notes())
                elif url.path == "/api/children":
                    name = params.get("path", [""])[0]
                    directory = self.server.safe_path(name, allow_root=True)
                    if not directory.is_dir():
                        raise ValueError("Cartella non valida")
                    children = []
                    for entry in directory.iterdir():
                        if entry.name == ".git" or entry.is_symlink():
                            continue
                        relative = entry.relative_to(self.server.root).as_posix()
                        children.append({"name": entry.name, "path": relative, "directory": entry.is_dir()})
                    children.sort(key=lambda child: (not child["directory"], child["name"].casefold()))
                    self.send_json(200, {"children": children})
                elif url.path == "/api/agent/wait":
                    try:
                        event = self.server.events.get(timeout=25)
                        with self.server.lock:
                            event = {**event, "diagram": self.server.state["diagram"]}
                        self.send_json(200, {"event": event})
                    except queue.Empty:
                        self.send_json(200, {"event": None})
                else:
                    self.send_json(404, {"error": "Risorsa sconosciuta"})
            except (ValueError, OSError, json.JSONDecodeError):
                self.send_json(400, {"error": "Richiesta non valida"})
            return
        assets = {"/": "index.html", "/index.html": "index.html", "/main.js": "main.js", "/style.css": "style.css"}
        filename = assets.get(url.path)
        if filename is None and url.path.startswith("/assets/"):
            filename = urllib.parse.unquote(url.path.lstrip("/"))
        if filename is None:
            self.send_error(404)
            return
        asset = (WEB_DIR / filename).resolve()
        if not asset.is_relative_to(WEB_DIR.resolve()) or not asset.is_file():
            self.send_error(503)
            return
        content = asset.read_bytes()
        mime = "text/html" if filename.endswith(".html") else "text/css" if filename.endswith(".css") else "text/javascript"
        self.send_response(200)
        self.send_header("Content-Type", f"{mime}; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self) -> None:
        if not self.authorized():
            self.send_json(403, {"error": "Accesso negato"})
            return
        try:
            payload = self.body_json()
            if self.path == "/api/agent/capture":
                result = self.server.capture(payload.get("file"))
            elif self.path == "/api/notes":
                self.server.save_notes(payload)
                result = {"ok": True}
            elif self.path == "/api/agent/publish":
                result = self.server.publish(payload)
            elif self.path == "/api/agent/diagram":
                source = validate_diagram(payload.get("source"))
                with self.server.lock:
                    self.server.update_diagram(source)
                    self.server.save()
                result = {"ok": True}
            elif self.path == "/api/agent/answer":
                answer = payload.get("text")
                if not isinstance(answer, str) or not answer.strip():
                    raise ValueError("Risposta mancante")
                diagram = validate_diagram(payload["diagram"]) if "diagram" in payload else None
                with self.server.lock:
                    if diagram is not None:
                        self.server.update_diagram(diagram)
                    self.server.state["messages"].append({"role": "agent", "text": answer.strip(), "stepId": self.server.state["currentStepId"]})
                    self.server.state["awaitingAnswer"] = False
                    self.server.save()
                result = {"ok": True}
            elif self.path == "/api/agent/finish":
                with self.server.lock:
                    self.server.state["finished"] = True
                    self.server.state["summary"] = str(payload.get("summary", "")).strip()
                    self.server.save()
                result = {"ok": True}
            elif self.path == "/api/agent/stop":
                result = {"ok": True}
                threading.Thread(target=self.server.shutdown, daemon=True).start()
            elif self.path == "/api/event":
                kind = payload.get("type")
                with self.server.lock:
                    if not self.server.state["currentStepId"] or self.server.state["finished"]:
                        raise ValueError("Nessun passo attivo")
                    if kind == "next":
                        if self.server.state["released"] or self.server.state["awaitingAnswer"]:
                            raise ValueError("Passo già sbloccato o risposta in attesa")
                        self.server.state["released"] = True
                        event = {"type": "next", "stepId": self.server.state["currentStepId"]}
                    elif kind == "question":
                        question = payload.get("text")
                        if not isinstance(question, str) or not question.strip() or len(question) > 4000:
                            raise ValueError("Domanda non valida")
                        if self.server.state["awaitingAnswer"]:
                            raise ValueError("Risposta precedente in attesa")
                        self.server.state["awaitingAnswer"] = True
                        self.server.state["messages"].append({"role": "user", "text": question.strip(), "stepId": self.server.state["currentStepId"]})
                        event = {"type": "question", "text": question.strip(), "stepId": self.server.state["currentStepId"]}
                    else:
                        raise ValueError("Azione sconosciuta")
                    self.server.save()
                    self.server.events.put(event)
                result = {"ok": True}
            else:
                self.send_json(404, {"error": "Risorsa sconosciuta"})
                return
            self.send_json(200, result)
        except (ValueError, OSError, json.JSONDecodeError) as error:
            message = str(error) if self.path.startswith("/api/agent/") else "Richiesta non valida"
            self.send_json(400, {"error": message})


def agent_request(session_dir: Path, method: str, endpoint: str, payload: dict | None = None) -> dict:
    config = read_json(session_dir / "config.json")
    port = (session_dir / "port.txt").read_text(encoding="ascii").strip()
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"http://127.0.0.1:{port}{endpoint}", data=data, method=method,
        headers={"X-Guided-Token": config["token"], "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        try:
            detail = json.load(error).get("error", "Richiesta non riuscita")
        except (ValueError, OSError):
            detail = "Richiesta non riuscita"
        raise ValueError(detail) from error


def start_session(root: Path, goal: str, open_browser: bool) -> None:
    if not root.is_dir():
        raise ValueError("La cartella del progetto non esiste")
    if not WEB_DIR.is_dir():
        raise ValueError("Pagina web da costruire")
    session_dir = Path(tempfile.mkdtemp(prefix="codex-esempio-guidato-"))
    (session_dir / "snapshots").mkdir()
    (session_dir / "steps").mkdir()
    token = secrets.token_urlsafe(32)
    write_json(session_dir / "config.json", {"root": str(root.resolve()), "goal": goal, "token": token})
    write_json(session_dir / "state.json", {
        "goal": goal, "rootName": root.name, "currentStepId": None, "steps": [],
        "messages": [], "released": False, "awaitingAnswer": False,
        "finished": False, "summary": "",
    })
    creationflags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    log = (session_dir / "server.log").open("wb")
    try:
        subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "serve", "--session", str(session_dir)],
            stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
            creationflags=creationflags, start_new_session=os.name != "nt",
        )
    finally:
        log.close()
    port_file = session_dir / "port.txt"
    for _ in range(100):
        if port_file.is_file():
            break
        time.sleep(0.1)
    if not port_file.is_file():
        raise RuntimeError("La pagina locale non si è avviata")
    port = port_file.read_text(encoding="ascii").strip()
    url = f"http://127.0.0.1:{port}/#{token}"
    if open_browser:
        webbrowser.open(url)
    print(json.dumps({"session": str(session_dir), "url": url}, ensure_ascii=False))


def serve(session_dir: Path) -> None:
    server = GuidedServer(session_dir)
    (session_dir / "port.txt").write_text(str(server.server_address[1]), encoding="ascii")
    server.serve_forever()
    server.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    start = commands.add_parser("start", help="Apri una sessione sul progetto")
    start.add_argument("--root", type=Path, required=True)
    start.add_argument("--goal", required=True)
    start.add_argument("--no-open", action="store_true")
    for name in ("serve", "capture", "publish", "answer", "diagram", "wait", "finish", "stop", "state"):
        command = commands.add_parser(name)
        command.add_argument("--session", type=Path, required=True)
        if name == "capture":
            command.add_argument("--file", required=True)
        if name == "publish":
            command.add_argument("--input", type=Path, required=True)
        if name in ("answer", "finish", "diagram"):
            command.add_argument("--input", type=Path, required=True)
        if name == "answer":
            command.add_argument("--diagram", type=Path)
    args = parser.parse_args()
    if args.command == "start":
        start_session(args.root, args.goal, not args.no_open)
    elif args.command == "serve":
        serve(args.session)
    elif args.command == "capture":
        print(json.dumps(agent_request(args.session, "POST", "/api/agent/capture", {"file": args.file})))
    elif args.command == "publish":
        print(json.dumps(agent_request(args.session, "POST", "/api/agent/publish", read_json(args.input))))
    elif args.command in ("answer", "finish"):
        field = "text" if args.command == "answer" else "summary"
        endpoint = "/api/agent/answer" if args.command == "answer" else "/api/agent/finish"
        payload = {field: args.input.read_text(encoding="utf-8")}
        if args.command == "answer" and args.diagram:
            payload["diagram"] = args.diagram.read_text(encoding="utf-8")
        print(json.dumps(agent_request(args.session, "POST", endpoint, payload)))
    elif args.command == "diagram":
        print(json.dumps(agent_request(args.session, "POST", "/api/agent/diagram", {"source": args.input.read_text(encoding="utf-8")})))
    elif args.command == "wait":
        while True:
            result = agent_request(args.session, "GET", "/api/agent/wait")
            if result["event"] is not None:
                print(json.dumps(result["event"], ensure_ascii=False), flush=True)
                break
    elif args.command == "state":
        print(json.dumps(agent_request(args.session, "GET", "/api/state"), ensure_ascii=False))
    elif args.command == "stop":
        print(json.dumps(agent_request(args.session, "POST", "/api/agent/stop", {})))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, urllib.error.URLError, urllib.error.HTTPError) as error:
        print(f"Errore: {error}", file=sys.stderr)
        raise SystemExit(1) from error
