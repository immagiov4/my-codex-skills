---
name: web-performance
description: "Measure and diagnose browser-facing web performance with Lighthouse, runtime traces, field data, build artifacts, or source inspection. Use for performance audits, Core Web Vitals, slow loading or interactions, bundle regressions, and evidence-based optimization."
---

# Web performance

Measure before recommending an optimization. Static source inspection can find suspicious patterns, but it cannot measure Core Web Vitals or prove user impact.

Use this skill for browser-facing applications and routes. Do not invoke it for an ordinary code review without a performance question or a credible performance-sensitive change.

## Choose the evidence mode

- Use **measured mode** when you can run the application, inspect a live URL with a compatible browser tool, or read a Lighthouse, PageSpeed Insights, CrUX, or performance-trace artifact.
- Use **source mode** when runtime measurement is unavailable. Mark every result as `potential impact` and leave numeric scorecards unmeasured.

Before capturing data or parsing an artifact, read [references/measurement.md](references/measurement.md).

## Set the scope

Identify the route or user flow, the rendering stack, and the performance symptom. Read repository instructions and use existing project scripts before adding or downloading tools.

Record the measurement conditions that affect comparison, including the URL, commit, build mode, device or throttling profile, cache state, authentication state, and user flow. Do not inspect cookies, tokens, or browser storage. Do not run load tests against shared or production infrastructure without explicit authorization.

## Measure honestly

Label every number by source:

- **Field** for real-user monitoring or CrUX.
- **Lab** for Lighthouse or another synthetic run.
- **Trace** for an observed browser performance recording.
- **Build** for bundle sizes and build artifacts.

Field, lab, trace, and build data answer different questions. Never substitute one for another. Repeat noisy measurements enough to estimate variation, and compare results under the same conditions. Distinguish cold-cache and warm-cache results.

Use a product budget supplied by the repository or user. Do not invent bundle, latency, memory, or score limits. You may classify Core Web Vitals with the current thresholds published by web.dev, but keep those external standards separate from product requirements.

## Find the bottleneck

Trace a measured symptom to the responsible request, task, component, query, asset, or build input. Rank findings by observed user impact, confidence, and the cost of verification. A framework-specific recommendation must match the detected stack.

In source mode, state what evidence is missing and give the smallest measurement that could confirm or reject each important suspicion.

## Optimize only when requested

Treat each optimization as a hypothesis. Change one cause at a time when practical, preserve correctness, and rerun the same measurement. Keep a change only when the result beats normal run-to-run variation and nearby correctness checks remain green. Remove or recommend reverting changes that are neutral or worse.

Do not add caching, concurrency, pagination, timeouts, retry policies, or other quantitative behavior without the authorization required by the repository.

## Report

Return:

1. The scope and measurement conditions.
2. A scorecard containing only measured values, each with its source.
3. Ranked findings with evidence and code locations where available.
4. The next experiment for any important unverified suspicion.
5. Before and after results for implemented optimizations.

Use `VERIFIED`, `NOT VERIFIED`, or `INCONCLUSIVE`. A source-only audit is never `VERIFIED` performance.
