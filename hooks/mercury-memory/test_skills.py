"""Exercise skill suggestions and the Claude Code memory client."""
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import hook

NATIVE = "# Task Group: Writing\nscope: Editing skills\napplies_to: any skill\n## User preferences\n- Write skills in English.\n"


def respond(scores_by_name):
    """Fake decision endpoint: score each question by the entry name in its instructions."""
    def urlopen(request, timeout):
        payload = json.loads(request.data)
        answers = {}
        for key, question in payload["questions"].items():
            score = next((value for name, value in scores_by_name.items() if name in question["instructions"]), 0.0)
            answers[key] = {"noul": score}
        return io.StringIO(json.dumps({"answers": answers, "model": payload["model"]}))
    return urlopen


def write_skill(root, name, description):
    folder = root / name
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text("---\nname: %s\ndescription: %s\n---\nBody.\n" % (name, description), encoding="utf-8")


class SkillSuggestionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        (self.home / "memories").mkdir()
        (self.home / "memories" / "MEMORY.md").write_text(NATIVE, encoding="utf-8")
        write_skill(self.home / "skills", "issue-writer", "Use before creating a GitHub issue.")
        write_skill(self.home / "skills", "unrelated", "Draw diagrams.")
        self.event = {"hook_event_name": "UserPromptSubmit", "prompt": "Open an issue for the bug.",
                      "session_id": "s", "turn_id": "t"}

    def test_skill_above_threshold_is_suggested_with_its_own_model(self):
        seen = []
        fake = respond({"issue-writer": 0.9, "unrelated": 0.1, "Write skills": 0.1})
        def recording(request, timeout):
            seen.append(json.loads(request.data)["model"])
            return fake(request, timeout)
        with patch.object(hook, "api_key", return_value="k"), patch.object(hook.urllib.request, "urlopen", recording):
            context = hook.run(self.event, self.home)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("issue-writer", context)
        self.assertIn("skills/issue-writer/SKILL.md", context)
        self.assertNotIn("unrelated", context)
        self.assertEqual(sorted(seen), sorted([hook.MODEL, hook.SKILL_MODEL]))
        receipt = hook.read_json(self.home / "mercury-memory/receipts/t.json")
        self.assertEqual(receipt["suggested_skills"], ["issue-writer"])

    def test_every_skill_above_threshold_is_suggested_by_default(self):
        write_skill(self.home / "skills", "bug-triage", "Use when a bug is reported.")
        write_skill(self.home / "skills", "repro-steps", "Use to write reproduction steps.")
        fake = respond({"issue-writer": 0.9, "bug-triage": 0.85, "repro-steps": 0.8, "unrelated": 0.1})
        with patch.object(hook, "api_key", return_value="k"), patch.object(hook.urllib.request, "urlopen", fake):
            hook.run(self.event, self.home)
        receipt = hook.read_json(self.home / "mercury-memory/receipts/t.json")
        self.assertEqual(receipt["suggested_skills"], ["issue-writer", "bug-triage", "repro-steps"])

    def test_skill_failure_keeps_memories(self):
        memory_only = respond({"Write skills": 0.9})
        def failing_skills(request, timeout):
            if json.loads(request.data)["model"] == hook.SKILL_MODEL:
                raise TimeoutError
            return memory_only(request, timeout)
        with patch.object(hook, "api_key", return_value="k"), patch.object(hook.urllib.request, "urlopen", failing_skills):
            context = hook.run(self.event, self.home)["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Write skills in English", context)
        self.assertEqual(hook.read_json(self.home / "mercury-memory/receipts/t.json")["skill_error"], "TimeoutError")


class ClaudeClientTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.home = root / "state"
        memory = root / "project" / "memory"
        memory.mkdir(parents=True)
        (memory / "MEMORY.md").write_text("- index only\n", encoding="utf-8")
        (memory / "tier.md").write_text("---\nname: tier-lock\ndescription: model tier\n---\nOnly the default tier.\n", encoding="utf-8")
        (memory / "lang.md").write_text("---\nname: language\ndescription: reply language\n---\nReply in Italian.\n", encoding="utf-8")
        transcript = root / "project" / "session.jsonl"
        transcript.write_text(json.dumps({"type": "user", "message": {"content": "earlier question"}}) + "\n", encoding="utf-8")
        hook.write_json(self.home / "mercury-memory" / "settings.json", {"pinned": ["tier-lock"], "skills_enabled": False})
        self.event = {"hook_event_name": "UserPromptSubmit", "prompt": "Reply please.", "session_id": "s",
                      "turn_id": "c", "transcript_path": str(transcript)}

    def test_retrieved_and_pinned_memories(self):
        with patch.object(hook, "api_key", return_value="k"), patch.object(
                hook.urllib.request, "urlopen", respond({"language": 0.9})):
            context = hook.run(self.event, self.home, "claude")["hookSpecificOutput"]["additionalContext"]
        self.assertIn("Only the default tier.", context)
        self.assertIn("Reply in Italian.", context)
        self.assertNotIn("index only", context)

    def test_pinned_memory_survives_provider_failure(self):
        with patch.object(hook, "api_key", return_value="k"), patch.object(
                hook.urllib.request, "urlopen", side_effect=TimeoutError):
            result = hook.run(self.event, self.home, "claude")
        self.assertIn("Only the default tier.", result["hookSpecificOutput"]["additionalContext"])
        self.assertIn("systemMessage", result)


class ClaudeInstallTests(unittest.TestCase):
    def test_install_is_idempotent_and_removable(self):
        import install
        with tempfile.TemporaryDirectory() as temp:
            home = Path(temp)
            hook.write_json(home / "settings.json", {"hooks": {"UserPromptSubmit": [{"hooks": [{"type": "command", "command": "other"}]}]}})
            for _ in range(2):
                install.install_claude(home)
            commands = [h["command"] for g in hook.read_json(home / "settings.json")["hooks"]["UserPromptSubmit"] for h in g["hooks"]]
            self.assertEqual(len(commands), 2)
            self.assertTrue(commands[1].endswith("--client claude"))
            install.install_claude(home, remove=True)
            commands = [h["command"] for g in hook.read_json(home / "settings.json")["hooks"]["UserPromptSubmit"] for h in g["hooks"]]
            self.assertEqual(commands, ["other"])


if __name__ == "__main__":
    unittest.main()
