---
name: codex-adapter
description: Translation layer between Codex conventions and Claude Code. Load BEFORE running any skill, prompt, or instruction written for Codex (mentions $skill-name, AGENTS.md, .codex/, codex exec, spawn_agent, update_plan, apply_patch, ~/.codex/skills, openai.yaml), or when a skill ported from my-codex-skills references tools Claude Code does not have.
---

# Codex → Claude Code adapter

Load this first, then follow the Codex-style skill/instruction using the mappings below. Do not edit the Codex skill; translate at execution time.

## Procedure

1. Read the Codex skill/instruction fully.
2. Scan it for Codex-specific terms (table below). Substitute silently; mention a substitution to the user only if it changes behavior.
3. If a term has no row here, pick the closest Claude Code equivalent, and say which you chose.
4. Execute the skill as written, with substitutions applied.

## Invocation syntax

| Codex | Claude Code |
|---|---|
| `$skill-name` (in user text or in another skill) | `Skill` tool with `skill: "skill-name"` (or `/skill-name`) |
| "use the X skill" | same: invoke `X` via `Skill` |
| `agents/openai.yaml` metadata | ignore (UI metadata only); the `SKILL.md` frontmatter is what matters |
| implicit skill triggering via description | same, via the skills list |

## Files and paths

| Codex | Claude Code |
|---|---|
| `AGENTS.md` | `CLAUDE.md` in the same directory. If only `AGENTS.md` exists, read it as the project instructions; when creating/editing, prefer `CLAUDE.md` and keep `AGENTS.md` in sync only if the repo already uses it |
| `~/.codex/skills/`, `.codex/skills/` | `~/.claude/skills/`, `.claude/skills/` |
| `.codex/` (project config, verification skills, etc.) | `.claude/` |
| `~/.codex/config.toml` | `~/.claude/settings.json` (different schema; do not copy keys blindly) |
| `~/.agents/skills` | also readable; leave in place |

## Tools

| Codex tool / phrase | Claude Code |
|---|---|
| `shell` / `shell_command` | `Bash` (POSIX) or `PowerShell` on Windows |
| `apply_patch` | `Edit` (partial change) / `Write` (new or full file) |
| `update_plan` | `TaskCreate`/todo tracking if available, else a short checklist in the reply |
| `view_image` | `Read` on the image path |
| `request_user_input` / "ask the user" | `AskUserQuestion` only when blocked on a user decision; otherwise pick a default |
| web search / browsing | `WebSearch`, `WebFetch`, or the browser tools |
| `spawn_agent` / `wait_agent` / `send_input` / `close_agent` | `Agent` tool (subagent) + `SendMessage` to continue one. Spawn only if the user asked for subagents or the skill explicitly requires parallel agents; otherwise do the work inline |
| "background agent", "delegate to a worker" | `Agent` with `run_in_background` |
| `multi_tool_use.parallel` | several tool calls in one message |
| `codex exec "<prompt>"` (nested Codex run) | `Agent` subagent with the same prompt. Only shell out to `codex exec` if the skill's point is a *second-model* review and the `codex` CLI is installed (`Get-Command codex`); ask before doing it |
| `codex review` | the `code-review` skill |

## Model / reasoning wording

- "high reasoning effort", "gpt-5-codex", model names: ignore or map to the session's current model; never switch models just because a Codex skill names one.
- "sandbox: workspace-write / approvals: on-request": Claude Code uses its own permission modes; do not try to emulate. If an action needs approval, just request it normally.

## Behavioral differences to respect

- Codex skills may say "do not ask questions, proceed autonomously". Still follow the safety/confirmation rules of this session for destructive or outward-facing actions (push, publish, delete, send).
- Codex skills often assume `$ARGUMENTS`-less free-text input. Treat the user's message as the input.
- Relative links inside a skill (`references/foo.md`) are relative to the skill directory: `~/.claude/skills/<name>/`. Read them with `Read` when the skill says to.
- Windows host: translate bash snippets to PowerShell only if they fail under the Bash tool.

## Known skills needing the most adaptation

- `code-review` (nested `codex exec`, AGENTS.md); name also collides with the built-in `code-review`, so prefer invoking the built-in unless the user asks for the Codex version explicitly.
- `interrogate` (multi-model reviewers → subagents).
- `create-verification-skill`, `maintain-verification-skill` (write into `.codex/` → write into `.claude/`).
- `setup-matt-pocock-skills`, `writing-for-agents`, `receiving-pr-reviews`, `problem-to-github-issue`, `engineering-workflow`, `orchestrate-nous-backlog` (AGENTS.md → CLAUDE.md).
