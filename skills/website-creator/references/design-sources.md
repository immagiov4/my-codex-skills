# Design sources

The direction workflow is an original Codex adaptation. It adds subject-based composition selection and a visual review to the tutorial recipe library; it retains the library's implementation procedures.

| Source | Consulted revision | Applied contribution |
|---|---|---|
| [Anthropic Frontend Design](https://github.com/anthropics/skills/blob/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/frontend-design/SKILL.md) | `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`, checked 2026-09-30 | Grounding in subject matter, deliberate type and composition, plan review, and calibration against recurring generated treatments |
| [Impeccable](https://github.com/pbakaus/impeccable/tree/0d6b47ea19b63afe15e3f93a44d5d9fbbc6fd275/.agents/skills/impeccable) by Peter Bakāus | `0d6b47ea19b63afe15e3f93a44d5d9fbbc6fd275`, skill version 4.4.0, checked 2026-09-30 | Product truth versus visual direction, composition alternatives, critique of category reflexes, bounded verification, and deterministic detector findings |

The installed Impeccable Node detector used by `check-design.mjs` is supplied by the local Impeccable installation. The helper delegates to it and does not reproduce its implementation. Engine availability and supported commands are verified at invocation.

Both upstream works are distributed under Apache License 2.0. The shared terms are retained in [licenses/apache-2.0.txt](../licenses/apache-2.0.txt). The linked direction reference is rewritten and combined for this collection; upstream setup commands, interactive direction boards, and installation hooks remain with their owning project.
