"""Install or remove the portable Mercury native-memory hook without other hook changes."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import re
import shlex
import shutil
import sys

from hook import codex_home, DEFAULTS, digest, read_json, write_json

STATUS_MESSAGE = "Mercury native memory"
HOOK_TIMEOUT_SECONDS = DEFAULTS["request_timeout_seconds"] + 4


def command_for(python, script, home=None):
    paths = [str(python), str(script)]
    if home is not None:
        paths.extend(["--codex-home", str(home)])
    if sys.platform == "win32":
        # Codex uses PowerShell; a quoted executable needs the call operator.
        return "& " + " ".join("'" + path.replace("\\", "/").replace("'", "''") + "'" for path in paths)
    return shlex.join(paths)


def owned(handler, target):
    if handler.get("statusMessage") != STATUS_MESSAGE:
        return False
    command = handler.get("command", "")
    if sys.platform == "win32":
        tokens = [part.replace("''", "'") for part in re.findall(r"'((?:[^']|'')*)'", command)]
    else:
        tokens = shlex.split(command)
    return str(target).replace("\\", "/") in [token.replace("\\", "/") for token in tokens]


def configure(home, remove=False):
    path = home / "hooks.json"
    existing = read_json(path) if path.exists() else {"hooks": {}}
    target = home / "hooks" / "mercury-memory" / "hook.py"
    groups = existing.setdefault("hooks", {}).setdefault("UserPromptSubmit", [])
    for group in groups:
        group["hooks"] = [handler for handler in group.get("hooks", []) if not owned(handler, target)]
    groups[:] = [group for group in groups if group.get("hooks")]
    if not remove:
        groups.append({"hooks": [{"type": "command", "command": command_for(Path(sys.executable), target, home),
                                  "timeout": HOOK_TIMEOUT_SECONDS, "statusMessage": STATUS_MESSAGE,
                                  "additionalContextLimit": 0}]})
    if path.exists():
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = home / "mercury-memory" / "backups" / (timestamp + "-hooks.json")
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup)
    write_json(path, existing)
    return target


def install(home, reviewed_view=None):
    home.mkdir(parents=True, exist_ok=True)
    if not (home / "memories" / "MEMORY.md").is_file():
        raise ValueError("Generate native Codex memory before installing this hook")
    if reviewed_view:
        view = read_json(reviewed_view)
        current = digest((home / "memories" / "MEMORY.md").read_bytes())
        if view.get("native_sha256") != current or not isinstance(view.get("memories"), list):
            raise ValueError("Reviewed view does not match current native memory")
        write_json(home / "mercury-memory" / "reviewed-view.json", view)
    target = home / "hooks" / "mercury-memory" / "hook.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).with_name("hook.py")
    if source.resolve() != target.resolve():
        shutil.copy2(source, target)
    settings = home / "mercury-memory" / "settings.json"
    if not settings.exists():
        write_json(settings, DEFAULTS)
    configure(home)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=codex_home())
    parser.add_argument("--reviewed-view", type=Path,
                        help="Private optional JSON: native_sha256 and memories, never a repository file")
    parser.add_argument("--remove", action="store_true")
    args = parser.parse_args()
    home = args.codex_home.resolve()
    if args.remove:
        configure(home, remove=True)
        print("Mercury handler removed. Private receipts and settings retained.")
    else:
        target = install(home, args.reviewed_view)
        print("Installed " + str(target))
        print("Review and trust Mercury native memory in Codex /hooks, then start a new session.")


if __name__ == "__main__":
    main()
