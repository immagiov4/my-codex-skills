#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd "$script_dir/.." && pwd)"
source_root="$repository_root/skills"
codex_root="${CODEX_HOME:-$HOME/.codex}"
target_root="$codex_root/skills"

mkdir -p "$target_root"
cp -R "$source_root"/. "$target_root"/

printf 'Installed Codex skills in %s\n' "$target_root"
