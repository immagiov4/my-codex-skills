#!/usr/bin/env python3
"""Exercise the local walkthrough bridge against a disposable project."""

from __future__ import annotations

import json
import os
import tempfile
import threading
import urllib.error
import urllib.request
from pathlib import Path

from guided import GuidedServer, write_json


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="esempio-guidato-check-") as temporary:
        base = Path(temporary)
        root = base / "project"
        root.mkdir()
        os.environ["CODEX_HOME"] = str(base / "codex-home")
        source = root / "cart.py"
        source.write_text("def total(prices):\n    return sum(prices)\n", encoding="utf-8")
        (root / "nested").mkdir()
        (root / "nested" / "cart.test.py").write_text("# test\n", encoding="utf-8")
        (root / ".git").mkdir()
        (root / ".git" / "private.txt").write_text("not a project file\n", encoding="utf-8")
        session = base / "session"
        session.mkdir()
        (session / "snapshots").mkdir()
        (session / "steps").mkdir()
        token = "local-test-token"
        write_json(session / "config.json", {"root": str(root), "goal": "Aggiorna il totale", "token": token})
        write_json(session / "state.json", {
            "goal": "Aggiorna il totale", "rootName": root.name, "currentStepId": None,
            "steps": [], "messages": [], "released": False, "awaitingAnswer": False,
            "finished": False, "summary": "",
        })
        server = GuidedServer(session)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        origin = f"http://127.0.0.1:{server.server_address[1]}"

        def request(path: str, payload: dict | None = None, *, authorized: bool = True) -> dict:
            headers = {"Content-Type": "application/json"}
            if authorized:
                headers["X-Guided-Token"] = token
            data = None if payload is None else json.dumps(payload).encode("utf-8")
            method = "POST" if payload is not None else "GET"
            with urllib.request.urlopen(urllib.request.Request(origin + path, data=data, headers=headers, method=method), timeout=5) as response:
                return json.load(response)

        try:
            assert request("/api/files")["files"] == [
                {"name": "cart.py", "path": "cart.py"},
                {"name": "cart.test.py", "path": "nested/cart.test.py"},
            ]
            notes = {"text": "Le mie note\nSeconda riga", "position": {"x": 160, "y": 90}}
            assert request("/api/notes")["text"] == ""
            request("/api/notes", notes)
            assert request("/api/notes") == notes
            reopened = GuidedServer(session)
            try:
                assert reopened.read_notes() == notes
            finally:
                reopened.server_close()
            for invalid in [{"text": 123, "position": None}, {"text": "test", "position": {"x": -1, "y": 0}}, {"text": "test", "position": {"x": True, "y": 0}}]:
                try:
                    request("/api/notes", invalid)
                    raise AssertionError("Note non valide accettate")
                except urllib.error.HTTPError as error:
                    assert error.code == 400
            assert request("/api/notes") == notes
            try:
                request("/api/file?path=cart.py", authorized=False)
                raise AssertionError("La pagina ha letto il progetto senza token")
            except urllib.error.HTTPError as error:
                assert error.code == 403
            try:
                request("/api/file?path=..%2Fconfig.json")
                raise AssertionError("Un percorso fuori dal progetto è stato accettato")
            except urllib.error.HTTPError as error:
                assert error.code == 400

            first = request("/api/agent/publish", {
                "kind": "exploration", "title": "La somma", "overview": "La funzione somma i prezzi.",
                "why": "Qui nasce il risultato.", "file": "cart.py", "startLine": 1, "endLine": 2,
                "annotations": [{"line": 2, "explanation": "sum legge la sequenza."}],
                "diagram": 'flowchart LR\n  prices["Prezzi"] --> total["Totale"]',
            })
            assert request("/api/state")["currentStepId"] == first["stepId"]
            original_diagram = request("/api/state")["diagram"]
            assert original_diagram["revision"] == 1
            assert request(f"/api/step?id={first['stepId']}")["after"] == source.read_text(encoding="utf-8")

            request("/api/event", {"type": "question", "text": "Perché sum?"})
            assert request("/api/agent/wait")["event"]["type"] == "question"
            assert request("/api/state")["awaitingAnswer"]
            expanded_diagram = original_diagram["source"] + '\n  sum["sum"] -->|calcola| total'
            request("/api/agent/answer", {"text": "sum restituisce la somma.", "diagram": expanded_diagram})
            assert not request("/api/state")["awaitingAnswer"]
            assert request("/api/state")["diagram"]["revision"] == 2
            for invalid in ['flowchart LR\n a["mancante"', 'flowchart LR\n %%{init: {"securityLevel": "loose"}}%%\n a-->b', 'flowchart LR\n a-->b\n click a callback', 'classDiagram\n class A']:
                try:
                    request("/api/agent/diagram", {"source": invalid})
                    raise AssertionError("Diagramma non valido accettato")
                except urllib.error.HTTPError as error:
                    assert error.code == 400
                assert request("/api/state")["diagram"]["source"] == expanded_diagram
            request("/api/event", {"type": "next"})
            assert request("/api/agent/wait")["event"]["type"] == "next"

            snapshot = request("/api/agent/capture", {"file": "cart.py"})
            source.write_text("def total(prices):\n    return round(sum(prices), 2)\n", encoding="utf-8")
            second = request("/api/agent/publish", {
                "kind": "change", "title": "Arrotondamento", "overview": "Il totale ha due decimali.",
                "why": "Qui viene restituito il totale.", "file": "cart.py", "startLine": 2, "endLine": 2,
                "snapshotId": snapshot["snapshotId"],
                "annotations": [{"line": 2, "explanation": "round arrotonda il risultato."}],
                "diagram": expanded_diagram + '\n  total --> rounded["Arrotondato"]',
            })
            change = request(f"/api/step?id={second['stepId']}")
            assert "return sum(prices)" in change["before"]
            assert "return round(sum(prices), 2)" in change["after"]
            assert len(request("/api/state")["steps"]) == 2
            diagram = request("/api/state")["diagram"]
            assert 'sum["sum"]' in diagram["source"]
            assert diagram["stepId"] == second["stepId"] and diagram["revision"] == 3
            reopened = GuidedServer(session)
            try:
                assert reopened.state["diagram"] == diagram
            finally:
                reopened.server_close()
            request("/api/agent/diagram", {"source": diagram["source"]})
            assert request("/api/state")["diagram"] == diagram
            request("/api/agent/finish", {"summary": "Modifica completata."})
            assert request("/api/state")["finished"]
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)
    print("Verifica del collegamento locale riuscita")


if __name__ == "__main__":
    main()
