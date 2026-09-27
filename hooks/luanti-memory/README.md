# Luanti memory hook

This Codex `UserPromptSubmit` command hook points the agent at a local Luanti knowledge checkout before each turn. The agent determines relevance from the conversation, reads the relevant knowledge and follows the checkout's `docs/agent-memory.md` procedure to update and publish useful findings.

## Install

Keep a clone of this repository and your knowledge repository on the machine running Codex. Python 3 is required. The knowledge checkout must contain `docs/agent-memory.md`, which owns the consultation and publication procedure and records the owner's actual Git authorization.

Add this handler to `UserPromptSubmit` in `$CODEX_HOME/hooks.json` (normally `~/.codex/hooks.json`), replacing the three absolute paths with your Python executable, this script and your knowledge checkout. Merge it with any existing handlers:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"/absolute/path/to/python\" \"/absolute/path/to/my-codex-skills/hooks/luanti-memory/remind.py\" --knowledge-root \"/absolute/path/to/knowledge-checkout\"",
            "timeout": 5,
            "statusMessage": "Luanti shared memory"
          }
        ]
      }
    ]
  }
}
```

On Windows, use forward slashes in the JSON paths, including the drive letter. Run the configured command once to check that it prints a pointer to the correct checkout. Review and trust the handler through Codex's `/hooks` interface, then start a new session. See the [Codex hook documentation](https://learn.chatgpt.com/docs/hooks).

For agents that load persistent instructions, add a pointer to the same `docs/agent-memory.md` in their `AGENTS.md`. The knowledge and publication rules stay in the knowledge repository, so they can change independently of this hook.

The hook is installed explicitly because it needs a private checkout chosen by its owner. The collection's skill installer and plugin distribute skills, while this directory provides the optional hook separately.
