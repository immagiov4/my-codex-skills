---
name: engineering-workflow
description: Route non-trivial software work through discovery, architecture, implementation, verification, review, and small living documentation. Use when a coding task needs more than a direct local edit or when the right workflow is unclear.
---

# Engineering workflow

Use this router for non-trivial engineering work. Follow repository instructions before this skill.

## Shape the request

For a new project, feature, or unclear change, start with `$grill-with-docs`. Use a narrower skill when the missing piece is clear.

```text
unknown factual question          -> $research
decision needs an experiment      -> $prototype
domain language is unclear        -> $domain-modeling
dependent unknowns span sessions  -> $wayfinder
manual setup or migration         -> $wizard
```

Ask the user only for a product decision, preference, authorization, or fact you cannot discover safely.

## Ground unfamiliar code

Use `$how` before changing a subsystem you do not understand. Add `$why` when historical intent or a prior trade-off can change the answer. Use `$teach` when the user wants a progressive explanation.

## Settle the architecture

Use `$codebase-design` for module, interface, depth, seam, adapter, leverage, and locality. Use `$architect` when a consequential implementation crosses module seams or would be expensive to reshape later. Use `$arena` only when competing designs could produce materially different results.

## Preserve decisions when needed

Do not write a spec merely because work exists. Use `$to-spec` when settled decisions must survive the current task. Use `$to-tickets` when the work needs independently verifiable vertical slices.

When dispatching a ticket to a subagent, include the exact installed skill path beside each governed step. A fresh subagent may not inherit the parent's loaded skill instructions.

```text
documentation step      -> <skills-dir>/docs-doc/SKILL.md
user-facing prose       -> <skills-dir>/unslop/SKILL.md
module design           -> <skills-dir>/codebase-design/SKILL.md
cheap regression seam   -> <skills-dir>/tdd/SKILL.md
diagram                 -> <skills-dir>/diagram-design/SKILL.md
```

Give the subagent the repository instructions, exact scope, output path, and completion check. Re-send those pointers when work moves to a fresh agent or task.

## Implement in checkable units

1. Ground the affected system.
2. State a falsifiable definition of done.
3. Settle important data and interface shapes.
4. Make the smallest useful change.
5. Use `$tdd` when there is a cheap, meaningful test seam.
6. Verify the real artifact before starting the next unit.
7. Remove dead weight before adding abstractions.
8. Use `$figure-it-out` only when no narrower workflow fits a large task.

## Verify

Self-report is not proof. Prefer tests, CLI or API behavior, runtime traces, browser interaction, screenshots, diffs, and state before and after the action.

Use one honest outcome.

```text
VERIFIED
NOT VERIFIED
INCONCLUSIVE
```

Never report `INCONCLUSIVE` as success. When a project has a controllable runtime, use its verification skill and feature map.

## Review

For a meaningful change, verify first and then use `$code-review`. For high-risk, cross-cutting, shared-state, public-interface, migration, or architecture-heavy work, add `$blast-radius` and `$interrogate`.

Use `$show-me-your-work` when a long autonomous run needs a decision trail. Judge review findings against the code and the user's goal before applying them.

## Write for humans

Apply `$unslop` to user-facing engineering prose. Use `$bro` when the user asks for a simpler restatement. Use `$docs-doc` for durable technical documentation.

Keep permanent documentation small. `AGENTS.md` routes agents. `CONTEXT.md` defines domain terms. `docs/system-map.md` records stable ownership, dependencies, flows, invariants, and major entry points. Create an ADR only for a surprising, hard-to-reverse decision made through a real trade-off.

After a meaningful feature or refactor, use `$maintain-system-map`. Update documentation when the system's meaning changed, not because lines changed.

## Respect Git authorization

Read repository Git rules before any state change. Do not initialize a repository, create or switch branches, commit, push, merge, open a pull request, or rewrite history unless the user authorized that action and the repository permits it. Read-only Git commands are fine when they support the task.

Use the exact `@codex review` trigger for GitHub reviews. Send implementation and fix instructions through the active Codex task, not through pull-request comments: any other `@codex` mention starts a private Cloud task and adds noise to the public pull request.

After publishing a Codex Cloud result to a pull request, remove any auto-added `[Codex Task](https://chatgpt.com/codex/...)` footer from the pull-request body and verify it is absent. Preserve the rest of the description; private task URLs are not durable pull-request metadata.
