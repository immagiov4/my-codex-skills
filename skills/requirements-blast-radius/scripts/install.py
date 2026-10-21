"""Install this skill and merge its prompt hook into existing client settings."""
import argparse
import json
import os
from pathlib import Path
import shutil


def merge_hook(path, command, backup):
    original = path.read_bytes() if path.exists() else b'{}'
    settings = json.loads(original)
    groups = settings.setdefault('hooks', {}).setdefault('UserPromptSubmit', [])
    if any(handler.get('command') == command for group in groups for handler in group.get('hooks', [])):
        return
    backup.mkdir(parents=True, exist_ok=True)
    target = backup / (path.parent.name + '-' + path.name)
    if target.exists():
        raise FileExistsError('Choose a fresh backup directory for each installation.')
    target.write_bytes(original)
    groups.append({'hooks': [{'type': 'command', 'command': command}]})
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.requirements-tmp')
    temp.write_text(json.dumps(settings, indent=2) + '\n', encoding='utf-8')
    json.loads(temp.read_text())
    temp.replace(path)
    actual = json.loads(path.read_text())
    if actual != settings:
        raise ValueError('Installed settings differ from requested settings')


def install(source, home, client, backup):
    source = source.resolve()
    destination = home / 'skills' / source.name
    same_directory = destination.resolve() == source
    if destination.exists() and not same_directory:
        old = backup / (home.name + '-skill')
        if old.exists():
            raise FileExistsError('Choose a fresh backup directory.')
        old.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(destination, old)
        expected = (home / 'skills').resolve() / source.name
        if destination.resolve() != expected:
            raise ValueError('Skill destination resolves outside its owned directory')
        shutil.rmtree(destination)
    if not same_directory:
        shutil.copytree(source, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    command = 'bun "' + (destination / 'scripts' / 'prompt-hook.cjs').as_posix() + '"'
    merge_hook(home / ('settings.json' if client == 'claude' else 'hooks.json'), command, backup)
    for path in source.rglob('*'):
        if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
            if path.read_bytes() != (destination / path.relative_to(source)).read_bytes():
                raise ValueError('Installed skill differs from source')
    print(str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claude-home', type=Path, default=Path.home()/'.claude')
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home()/'.codex')))
    parser.add_argument('--backup-dir', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    install(source, args.claude_home.resolve(), 'claude', args.backup_dir.resolve()/'claude')
    install(source, args.codex_home.resolve(), 'codex', args.backup_dir.resolve()/'codex')


if __name__ == '__main__':
    main()
