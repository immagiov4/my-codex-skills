# Mercury native memory hook

This optional Codex `UserPromptSubmit` hook selects relevant preferences from the current native memory archive and supplies their complete text as developer context before each user turn. It uses `inception/mercury-decide` through OpenRouter, Python 3.9 or newer and the standard library. The native memory system remains enabled and owns its archive and automatic summary. The hook runs once per user message, with no daemon, Docker container, database or self-hosted service.

## Install

Set `OPENROUTER_API_KEY` in the environment used by Codex. On Windows the hook can also read this named variable from the current user's persistent Environment registry key, allowing an already-running desktop app to use it. Keep credentials outside this repository.

From a clone of this repository, run:

```sh
python hooks/mercury-memory/install.py
```

The installer resolves `$CODEX_HOME`, falling back to `~/.codex`. Use `--codex-home /absolute/path` for a different installation. It copies the runtime into that directory, merges one handler into `hooks.json`, preserves other handlers and backs up the previous file. Review and trust **Mercury native memory** through Codex `/hooks`, then start a new local chat. The same user-level hook applies to local CLI and desktop Codex sessions on that machine. Cloud-orchestrated Work chats have different hook support; see the [official hook documentation](https://learn.chatgpt.com/docs/hooks).

The collection's regular skill installer and plugin distribute skills. Installing this hook is a separate explicit action because it sends private memory and conversation content to the configured API provider. Carry this directory to another machine, set that machine's API key and run the installer there; its native memory stays local to that machine.

## Native source and selection

Each invocation reads `$CODEX_HOME/memories/MEMORY.md`. It indexes `User preferences` bullets together with their owning task-group scope, applicability and source lines. Other technical and historical native memory remains available through Codex's usual lookup. The API receives the current message, current directory, up to four recent user/assistant messages with an 8,000-character history budget, and the preference candidates. File contents and unrelated chats are not collected.

Each candidate gets a relevance score from zero to one. All active entries at or above **0.65** are included, without a top-k cutoff. Historical permission does not authorize current actions. The injected wrapper preserves scope, identifies native provenance and gives current instructions and the current native summary precedence over old entries. Mandatory instructions already supplied by Codex remain available independently of Mercury's scores.

An optional private reviewed view can preserve a manually consolidated preference set derived from this native archive. Its JSON has `native_sha256` and `memories`; each memory has `id`, `scope`, `text`, and optional `status`, `source_ids` and `source_lines`. Install it with `--reviewed-view /private/path/view.json`. It is used only while its SHA-256 matches the exact current `MEMORY.md`. A native update switches retrieval to the freshly parsed native preferences; review and reinstall the view to consolidate the new version. Private memory text is never distributed in this repository.

## Settings, receipts and failure behavior

Local settings live in `$CODEX_HOME/mercury-memory/settings.json`. The defaults in `hook.py` are the authoritative setting definitions. The HTTP socket timeout is six seconds, with no retry inside a user turn; the Codex handler deadline is ten seconds. An API error, missing key, invalid response or timeout produces an availability warning and lets the user's task proceed with native Codex memory. Disable retrieval with `"enabled": false` in settings.

Every attempted retrieval writes a separate receipt under `$CODEX_HOME/mercury-memory/receipts/`. Successful receipts contain native source hash, source mode, scores, selected memory text, provider usage, elapsed time and the exact injected context. Failed receipts contain status, error type, elapsed time and metadata collected before the failure. These private receipts make delivery inspectable; a Codex session rollout establishes that the hook output actually reached the model. The prompt is represented by a hash in the receipt. Receipt files are retained locally until the owner removes them; inspect directory size during routine maintenance. Missing or unsupported transcript data means selection uses the current message without history.

Run the checks with:

```sh
python -m unittest discover -s hooks/mercury-memory -p 'test_*.py'
```

Remove only this handler with:

```sh
python hooks/mercury-memory/install.py --remove
```

Private settings, receipts and backups remain available after removal. Existing hook definitions and native memory files are preserved.
