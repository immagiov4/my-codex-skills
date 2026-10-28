# Third-party notices

## Website Creator design references

The former `website-creator` collection has moved to the Geppetto [website-tools bucket](https://github.com/immagiov4/llm-memories/tree/main/buckets/website-tools). Its [provenance and licenses](https://github.com/immagiov4/llm-memories/blob/main/buckets/website-tools/NOTICE.md) retain the Apache-2.0 adaptations, source revisions, tutorial attribution and media-rights distinctions. This repository retains a routing skill; the original collection remains available in Git history.

Several skills are adapted from public MIT-licensed projects. Their instructions have been edited for Codex and for this collection's workflow. The original authors do not endorse these adaptations.

## PStack

Source: [backnotprop/pstack](https://github.com/backnotprop/pstack)

Copyright 2026 Lauren Tan. MIT License. See [`licenses/PSTACK-MIT.txt`](licenses/PSTACK-MIT.txt).

The local collection includes adapted PStack workflows such as `architect`, `blast-radius`, `bro`, `create-verification-skill`, `figure-it-out`, `how`, `maintain-verification-skill`, `poteto-mode`, `show-me-your-work`, `writing-for-humans` (incorporating `unslop`), `why`, and the `principle-*` skills.

`benchmark-checklist` is adapted from `skills/benchmark-checklist/SKILL.md` at PStack revision `f51fdeba3d803ef90e4eaa4a95ffb4e76008ab37`, Git blob `e901d1fdbc9ffce53e94d6514be7d9a22e771a1a`. The identical procedure is in `cursor/plugins` at revision `99b609a72323b70204eab407c622f436e858e112`, path `pstack/skills/benchmark-checklist/SKILL.md`. The adaptation maps explicit invocation to Codex metadata, routes the three playbooks to this collection's existing `poteto-mode`, and adds Windows observation guidance. The measurement questions, run counts, and verdict rules are unchanged. A copy of the MIT notice accompanies the skill in `skills/benchmark-checklist/LICENSE.txt` so copy installations retain it.

## Matt Pocock's skills

Source: [mattpocock/skills](https://github.com/mattpocock/skills)

Reviewed against upstream revision [`6fd9479`](https://github.com/mattpocock/skills/commit/6fd947921b935b7e1e69293a200400f0fdd5c15f) on 2026-10-06. The adaptations support both glossary naming conventions and retain this collection's Codex invocation, writing, testing, and authorization rules.

Copyright 2026 Matt Pocock. MIT License. See [`licenses/MATTPOCOCK-MIT.txt`](licenses/MATTPOCOCK-MIT.txt).

The local collection includes adapted engineering and writing workflows from this project, including `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `grill-with-docs`, `grilling`, `handoff`, `prototype`, `research`, `retro`, `setup-matt-pocock-skills`, `tdd`, `teach`, `to-spec`, `to-tickets`, `wayfinder`, `wizard`, and `writing-for-agents`.

## Qwen Code

Source: [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code), Apache License 2.0.

`code-review` uses an original Python coordinator and Italian instructions informed by Qwen Code's independent search, candidate verification, and coverage workflow. [Method provenance](skills/code-review/references/qwen-method.md) links the documentation and implementation at the revision studied.

## Draht

Source: [draht-dev/draht](https://github.com/draht-dev/draht)

Copyright 2026 Oskar Freye. Copyright 2025 Mario Zechner. MIT License. See [`licenses/DRAHT-MIT.txt`](licenses/DRAHT-MIT.txt).

Some verification, review, debugging, and workflow instructions share material or lineage with Draht's public skill collection.

## Agent Skills by Addy Osmani

Source: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

Copyright 2025 Addy Osmani. MIT License. See [`licenses/ADDYOSMANI-MIT.txt`](licenses/ADDYOSMANI-MIT.txt).

`web-performance` adapts the metric-honesty rules and measurement workflow from `performance-optimization`, `/webperf`, and the web performance auditor. It removes Claude-specific commands, personas, and hooks.

## No AI Slop

Source: [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)

Copyright 2026 Peter Yang. MIT License. See [`licenses/NO-AI-SLOP-MIT.txt`](licenses/NO-AI-SLOP-MIT.txt).

`writing-for-humans` incorporates the former `docs-doc` adaptation of its audit boundary, voice-preservation rule, portability test, and prose-pattern checks that were not already present in this collection.

## e-bash

Source: [OleksandrKucherenko/e-bash](https://github.com/OleksandrKucherenko/e-bash/tree/26d905b30c65d57c6707049c8ace9aba2d20fe61/.claude/skills/skill-learning).

Copyright (c) 2017-current Oleksandr Kucherenko. MIT License. See [`licenses/E-BASH-MIT.txt`](licenses/E-BASH-MIT.txt).

`skill-learning-patterns` adapts the learning recognition, validation, and contribution workflow for Codex. Its [source notes](skills/skill-learning-patterns/references/sources.md) also identify the Hermes refinement and collection-maintenance mechanisms studied for the adaptation.
