"""Check the configured knowledge location and a missing checkout."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class MemoryHookTest(unittest.TestCase):
    def test_checkout_with_spaces_and_missing_guide(self):
        with tempfile.TemporaryDirectory(prefix="knowledge test ") as directory:
            root = Path(directory)
            guide = root / "docs" / "agent-memory.md"
            guide.parent.mkdir()
            guide.write_text("# Memory procedure\n", encoding="utf-8")
            command = [sys.executable, str(Path(__file__).with_name("remind.py")),
                       "--knowledge-root", str(root)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(str(guide.resolve()), result.stdout)
            guide.unlink()
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
