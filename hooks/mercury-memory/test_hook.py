"""Exercise native source freshness, selection, failure and non-destructive installation."""
import io
import http.client
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from unittest.mock import patch

import hook
import install

NATIVE = "# Task Group: Writing\nscope: Editing skills\napplies_to: any skill\n## User preferences\n- Write skills in English.\n## Reusable knowledge\n- A historical fact.\n"


class NativeMemoryHookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        (self.home / "memories").mkdir()
        (self.home / "memories" / "MEMORY.md").write_text(NATIVE, encoding="utf-8")
        self.event = {"hook_event_name": "UserPromptSubmit", "prompt": "Prepare a skill example.",
                      "session_id": "example", "turn_id": "example-turn"}

    def answer(self, score):
        entries, _, _ = hook.load_memories(self.home)
        return {"answers": {entry["id"]: {"noul": score} for entry in entries}, "usage": {"input_tokens": 50}}

    def test_actual_output_exact_threshold_and_receipt(self):
        with patch.object(hook, "api_key", return_value="test"), patch.object(
                hook.urllib.request, "urlopen", return_value=io.StringIO(json.dumps(self.answer(0.65)))):
            result = hook.run(self.event, self.home)
        context = result["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Write skills in English", context)
        receipt = hook.read_json(self.home / "mercury-memory/receipts/example-turn.json")
        self.assertEqual(receipt["additional_context_sha256"], hook.digest(context.encode()))
        self.assertEqual(receipt["selected"][0]["source_lines"], [5])

    def test_below_threshold(self):
        with patch.object(hook, "api_key", return_value="test"), patch.object(
                hook.urllib.request, "urlopen", return_value=io.StringIO(json.dumps(self.answer(0.649)))):
            result = hook.run(self.event, self.home)
        self.assertEqual(result["hookSpecificOutput"]["additionalContext"], "")

    def test_timeout_never_blocks_and_records_failure(self):
        with patch.object(hook, "api_key", return_value="test"), patch.object(
                hook.urllib.request, "urlopen", side_effect=TimeoutError):
            result = hook.run(self.event, self.home)
        self.assertNotIn("decision", result)
        self.assertIn("systemMessage", result)
        self.assertEqual(hook.read_json(self.home / "mercury-memory/receipts/example-turn.json")["status"], "unavailable")

    def test_truncated_http_response_records_nonblocking_failure(self):
        with patch.object(hook, "api_key", return_value="test"), patch.object(
                hook.urllib.request, "urlopen", side_effect=http.client.IncompleteRead(b"partial")):
            result = hook.run(self.event, self.home)
        self.assertNotIn("decision", result)
        self.assertIn("systemMessage", result)
        receipt = hook.read_json(self.home / "mercury-memory/receipts/example-turn.json")
        self.assertEqual(receipt["status"], "unavailable")
        self.assertEqual(receipt["error_type"], "IncompleteRead")

    def test_invalid_partial_response_is_rejected(self):
        for response in ({"answers": {}}, self.answer(float("nan")), self.answer(True),
                         self.answer(float("inf")), self.answer(10**400),
                         None, [], {"answers": []}, {"answers": {"id": []}}):
            with self.assertRaises(ValueError):
                hook.scores_from(response, [entry["id"] for entry in hook.native_preferences(NATIVE.encode())])

    def test_malformed_provider_shape_is_nonblocking(self):
        with patch.object(hook, "api_key", return_value="test"), patch.object(
                hook.urllib.request, "urlopen", return_value=io.StringIO('{"answers":[]}')):
            result = hook.run(self.event, self.home)
        self.assertEqual(result["hookSpecificOutput"]["additionalContext"], "")
        self.assertIn("systemMessage", result)

    def test_native_drift_excludes_outdated_view(self):
        hook.write_json(self.home / "mercury-memory/reviewed-view.json",
                        {"native_sha256": hook.digest((self.home / "memories/MEMORY.md").read_bytes()),
                         "memories": [{"id": "reviewed", "scope": "Writing", "text": "Reviewed rule"}]})
        self.assertEqual(hook.load_memories(self.home)[2], "reviewed_native_view")
        (self.home / "memories/MEMORY.md").write_text(NATIVE + "\n# Task Group: Other\n## User preferences\n- New native rule.\n", encoding="utf-8")
        entries, _, mode = hook.load_memories(self.home)
        self.assertEqual(mode, "live_native_preferences_view_outdated")
        self.assertEqual(len(entries), 2)
        self.assertNotIn("reviewed", [entry["id"] for entry in entries])

    def test_installer_preserves_other_hooks_and_native_bytes(self):
        original = {"description": "Keep", "hooks": {"Stop": [{"hooks": [{"type": "command", "command": "other"}]}],
                   "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "existing"}]}]}}
        hook.write_json(self.home / "hooks.json", original)
        before = (self.home / "memories/MEMORY.md").read_bytes()
        install.install(self.home)
        install.install(self.home)
        current = hook.read_json(self.home / "hooks.json")
        self.assertEqual(len(current["hooks"]["UserPromptSubmit"]), 2)
        self.assertEqual(current["hooks"]["Stop"], original["hooks"]["Stop"])
        install.configure(self.home, remove=True)
        self.assertEqual(hook.read_json(self.home / "hooks.json"), original)
        self.assertEqual(before, (self.home / "memories/MEMORY.md").read_bytes())

    def test_history_is_local_recent_text_not_injected_context(self):
        path = self.home / "transcript.jsonl"
        messages = [("developer", "private injected context"), ("user", "# AGENTS.md instructions\nRules"),
                    ("user", "Previous real question"), ("assistant", "Previous answer"),
                    ("user", self.event["prompt"])]
        path.write_text("\n".join(json.dumps({"type": "response_item", "payload": {"type": "message", "role": role,
                         "content": [{"type": "input_text", "text": text}]}}) for role, text in messages), encoding="utf-8")
        history = hook.recent_history(dict(self.event, transcript_path=str(path)), hook.DEFAULTS)
        self.assertEqual([item["text"] for item in history], ["Previous real question", "Previous answer"])

    def test_installed_command_handles_spaces_in_paths(self):
        script = self.home / "owner's directory with spaces" / "probe.py"
        script.parent.mkdir()
        script.write_text("import json,sys\nprint(json.dumps(json.load(sys.stdin)))\n", encoding="utf-8")
        command = install.command_for(Path(sys.executable), script)
        shell = ["powershell", "-NoProfile", "-NonInteractive", "-Command", command] if sys.platform == "win32" else ["sh", "-c", command]
        result = subprocess.run(shell, input='{"probe":true}', capture_output=True,
                                text=True, encoding="utf-8", timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"probe": True})

    def test_repeat_install_and_remove_with_apostrophe_in_home(self):
        home = self.home / "owner's Codex"
        (home / "memories").mkdir(parents=True)
        (home / "memories/MEMORY.md").write_text(NATIVE, encoding="utf-8")
        install.install(home)
        install.install(home)
        groups = hook.read_json(home / "hooks.json")["hooks"]["UserPromptSubmit"]
        self.assertEqual(len(groups), 1)
        install.configure(home, remove=True)
        self.assertEqual(hook.read_json(home / "hooks.json")["hooks"]["UserPromptSubmit"], [])

    def test_custom_home_reaches_runtime_without_environment_override(self):
        install.install(self.home)
        hook.write_json(self.home / "mercury-memory/settings.json", {"enabled": False})
        group = hook.read_json(self.home / "hooks.json")["hooks"]["UserPromptSubmit"][-1]
        command = group["hooks"][0]["command"]
        shell = ["powershell", "-NoProfile", "-NonInteractive", "-Command", command] if sys.platform == "win32" else ["sh", "-c", command]
        result = subprocess.run(shell, input=json.dumps(self.event), capture_output=True,
                                text=True, encoding="utf-8", timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {})


if __name__ == "__main__":
    unittest.main()
