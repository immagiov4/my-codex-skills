# Mercury memory and skill hook

This optional `UserPromptSubmit` hook runs once per user message, for Codex or Claude Code. It does two things through OpenRouter decision models:

- **Memories:** selects the relevant ones and injects their full text.
- **Skills:** suggests at most two skills that match the message, as an explicit "load this skill" note, because agents rarely load skills on their own.

It needs Python 3.9 or newer and the standard library only: no daemon, container or database. Each client keeps its own memory system; the hook only reads it.

## Install

Set `OPENROUTER_API_KEY` in the environment used by Codex. On Windows the hook can also read this named variable from the current user's persistent Environment registry key, allowing an already-running desktop app to use it. Keep credentials outside this repository.

From a clone of this repository, run:

```sh
python hooks/mercury-memory/install.py
```

The installer resolves `$CODEX_HOME`, falling back to `~/.codex`. Use `--codex-home /absolute/path` for a different installation. It copies the runtime into that directory, merges one handler into `hooks.json`, preserves other handlers and backs up the previous file. Review and trust **Mercury native memory** through Codex `/hooks`, then start a new local chat. The same user-level hook applies to local CLI and desktop Codex sessions on that machine. Cloud-orchestrated Work chats have different hook support; see the [official hook documentation](https://learn.chatgpt.com/docs/hooks).

The collection's regular skill installer and plugin distribute skills. Installing this hook is a separate explicit action because it sends private memory and conversation content to the configured API provider. Carry this directory to another machine, set that machine's API key and run the installer there; its native memory stays local to that machine.

### Claude Code

```sh
python hooks/mercury-memory/install.py --client claude
```

This copies the runtime to `~/.claude/hooks/mercury-memory/` and adds one handler to `~/.claude/settings.json`, preserving the other handlers. Settings and receipts live in `~/.claude/mercury-memory/`. Claude Code memories are the Markdown files next to the session transcript (`<project>/memory/*.md`, the `MEMORY.md` index excluded), plus any `memory_dirs` in settings. Memories listed by name in `pinned` are injected on every turn, even when the provider is unavailable.

## Models

The models were picked by comparing decision models on labeled prompt sets: 19 prompts against 77 skills, and 15 prompts against 30 memories.

| Use | Model | Result |
| --- | --- | --- |
| Memories | `perplexity/pplx-decider-flash-v1.2` | 17/19 expected memories at 0.65, 9 extra; Mercury: 14/19, 18 extra |
| Skills | `perplexity/pplx-decider-v1.2` | 15/16 prompts matched, 5 wrong suggestions, none on small talk; Mercury: 18 wrong |

The two requests run in parallel, and large candidate sets are split into parallel batches (`batch_size`, 80). A Claude Code store of 30 memories and 77 skills takes about 1.5 s and $0.0006 per message; a Codex archive of 396 preferences and 138 skills takes about 3.5 s and $0.0023. Change them with `memory_model` and `skill_model` in settings.

## Skills

Candidates are the user skills (`$CODEX_HOME/skills` or `~/.claude/skills`), plus the skills of the repository that contains the current directory (`.agents/skills` or `.claude/skills`) and any `skill_dirs`. Only the name and description are sent. Each suggestion carries the `SKILL.md` path, so skills kept out of the agent's catalog to save context (`allow_implicit_invocation: false` or `disable-model-invocation: true`) stay reachable through the hook. A skill is suggested at **0.75** or above, at most `max_skills` (2). A skill failure never drops memories. Disable suggestions with `"skills_enabled": false`.

## Native source and selection

Each invocation reads `$CODEX_HOME/memories/MEMORY.md`. It indexes `User preferences` bullets together with their owning task-group scope, applicability and source lines. Other technical and historical native memory remains available through Codex's usual lookup. The API receives the current message, current directory, up to four recent user/assistant messages with an 8,000-character history budget, and the preference candidates. History is read backwards within the final 1 MiB of the transcript, so large archives and tool/image records cannot make each invocation rescan the whole chat. Messages outside that window are omitted; if it contains no complete messages, selection uses the current message alone. File contents and unrelated chats are not collected.

Each candidate gets a relevance score from zero to one. All active entries at or above **0.65** are included, without a top-k cutoff. Historical permission does not authorize current actions. The injected wrapper preserves scope, identifies native provenance and gives current instructions and the current native summary precedence over old entries. Mandatory instructions already supplied by Codex remain available independently of Mercury's scores.

An optional private reviewed view can preserve a manually consolidated preference set derived from this native archive. Its JSON has `native_sha256` and `memories`; each memory has `id`, `scope`, `text`, and optional `status`, `source_ids` and `source_lines`. Install it with `--reviewed-view /private/path/view.json`. It is used only while its SHA-256 matches the exact current `MEMORY.md`. A native update switches retrieval to the freshly parsed native preferences; review and reinstall the view to consolidate the new version. Private memory text is never distributed in this repository.

## Settings, receipts and failure behavior

Local settings live in `$CODEX_HOME/mercury-memory/settings.json`. The defaults in `hook.py` are the authoritative setting definitions. The entire retrieval has an eight-second deadline, including archive loading, history extraction, DNS, TLS and response-body reading. The HTTP socket timeout is also eight seconds, with no retry inside a user turn; the handler deadline is twelve seconds, leaving time for process startup and receipt output. A deadline expires without injecting partial results; the one-shot hook process exits without waiting for its background retrieval thread. An API error, missing key, invalid response or timeout produces an availability warning and lets the user's task proceed with native Codex memory. Disable retrieval with `"enabled": false` in settings.

Every attempted retrieval writes a separate receipt under `$CODEX_HOME/mercury-memory/receipts/`. Successful receipts contain native source hash, source mode, scores, selected memory text, provider usage, elapsed time and the exact injected context. Failed receipts contain status, error type and elapsed time. They also include source and request metadata when the retrieval worker returns it; a total-deadline receipt contains only invocation metadata because the worker has not returned. These private receipts make delivery inspectable; a Codex session rollout establishes that the hook output actually reached the model. The prompt is represented by a hash in the receipt. Receipt files are retained locally until the owner removes them; inspect directory size during routine maintenance. Missing or unsupported transcript data means selection uses the current message without history.

Run the checks with:

```sh
python -m unittest discover -s hooks/mercury-memory -p 'test_*.py'
```

Remove only this handler with:

```sh
python hooks/mercury-memory/install.py --remove
```

Private settings, receipts and backups remain available after removal. Existing hook definitions and native memory files are preserved.
