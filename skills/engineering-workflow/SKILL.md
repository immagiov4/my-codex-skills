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

Ask the user for a product decision, preference, authorization, or fact you cannot discover safely.

For a complaint about existing behavior, restate it as **Observed / Expected** and get the user's confirmation before planning a fix whenever the wording leaves room for two readings. Before calling existing behavior a defect, find out why it is there: a specific constant or an unusual rule is a sign of intent, so check its history (blame, the PR or issue that introduced it) and ask when the reason stays unclear. Repair the defect inside the feature; changing or removing the feature itself is the user's decision.

## Ground unfamiliar code

Use `$how` before changing a subsystem you do not understand. Add `$why` when historical intent or a prior trade-off can change the answer. Use `$teach` when the user wants a progressive explanation.

## Settle the architecture

Use `$codebase-design` for module, interface, depth, seam, adapter, leverage, and locality. Use `$architect` when a consequential implementation crosses module seams or would be expensive to reshape later. When behavior depends on a lifecycle with several phases (loading, ready, playing, transitioning), model it as an explicit state machine or a pure reducer, so illegal transitions cannot happen.

## Preserve decisions when needed

Do not write a spec merely because work exists. Use `$to-spec` when settled decisions must survive the current task. Use `$to-tickets` when the work needs independently verifiable vertical slices.

When dispatching a ticket to a subagent, include the exact installed skill path beside each governed step. A fresh subagent may not inherit the parent's loaded skill instructions.

```text
human-facing writing    -> <skills-dir>/writing-for-humans/SKILL.md
module design           -> <skills-dir>/codebase-design/SKILL.md
cheap regression seam   -> <skills-dir>/tdd/SKILL.md
diagram                 -> <skills-dir>/diagram-design/SKILL.md
code review             -> <skills-dir>/code-review/SKILL.md
```

Give the subagent the repository instructions, exact scope, output path, and completion check. Re-send those pointers when work moves to a fresh agent or task. Run it on the model, reasoning effort and service tier the user authorized, and tell it to do the work itself: it keeps that model and tier and starts no agents of its own. After launch, check the model and options the task actually runs with.

## Implement in checkable units

1. Ground the affected system.
2. State a falsifiable definition of done. When success depends on an external service or interface, test the smallest complete user path early, including entry to the result from the requested account or device. Verify any prerequisite that requires completed setup as soon as that setup permits it; treat each unobserved boundary as unresolved.
3. Settle important data and interface shapes.
4. Make the smallest useful change.
5. Use `$tdd` when there is a cheap, meaningful test seam.
6. Verify the real artifact before starting the next unit. Measure with the configuration production actually resolves (models, voices, flags) and state it beside the numbers.
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

Encode each agreed behavior as a **requirement test** named after the decision (for example "captions lead the voice by 1.3 s"). The tests are the record of the decision, so documentation stays small. When a change breaks a requirement test, stop and classify it: collateral damage gets repaired; a change to the requirement goes to the user, and the test changes only with that approval.

For time-based or visual behavior, show evidence a person can judge: a before/after video with audio and a visible clock, on the same real case, saying what to look at. Label any constructed fixture as constructed. Reuse one shared capture command instead of writing new capture scripts per change.

## Review

For a meaningful change, verify first and then use `$code-review` as the default code review. It owns the structured local CLI procedure with GPT-6.1 Sol, candidate verification, coverage, and consumption records. Follow its model-authorization check before starting the CLI.

Use `$receiving-pr-reviews` before applying findings. For high-risk, cross-cutting, shared-state, public-interface, migration, or architecture-heavy work, add `$blast-radius`.

Merge only on green checks from a run that already contains the current target branch; if the target moved, update and wait again.

Use `$show-me-your-work` when a long autonomous run needs a decision trail. Judge review findings against the code and the user's goal before applying them.

## Write for humans

Apply `$writing-for-humans` to engineering explanations, documentation and PR prose, including its independent review for substantive writing. Use `$bro` when the user asks for a simpler restatement.

Keep permanent documentation small. `AGENTS.md` routes agents. The project glossary (`GLOSSARY.md` or existing `CONTEXT.md`, following the configured layout) defines domain terms. `docs/system-map.md` records stable ownership, dependencies, flows, invariants, and major entry points. Create an ADR only for a surprising, hard-to-reverse decision made through a real trade-off.

After a meaningful feature or refactor, use `$maintain-system-map`. Update documentation when the system's meaning changed, not because lines changed.

## Learn from a session

When the user asks for a retrospective, use `$retro` to identify evidence-backed improvements to navigation, checks, instructions, tool cost, and information access. It presents proposals; implementing them follows the user's authorization. Prefer turning a repeated correction into a hook, a check or a test over adding more instruction text; use `$skill-learning-patterns` to fold it into the owning skill.

## Respect Git authorization

Read repository Git rules before any state change. Do not initialize a repository, create or switch branches, commit, push, merge, open a pull request, or rewrite history unless the user authorized that action and the repository permits it. Read-only Git commands are fine when they support the task.

Use the exact `@codex review` trigger for GitHub reviews. Send implementation and fix instructions through the active Codex task, not through pull-request comments: any other `@codex` mention starts a private Cloud task and adds noise to the public pull request.

After publishing a Codex Cloud result to a pull request, remove any auto-added `[Codex Task](https://chatgpt.com/codex/...)` footer from the pull-request body and verify it is absent. Preserve the rest of the description; private task URLs are not durable pull-request metadata.
