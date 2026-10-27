# Discovery and coverage

## Inventories

- Pin the exact checkout, deployed version where relevant, and the base used for each measurement. Record uncommitted files without touching them. Enumerate tracked source by language and directory; separately inventory tests, SQL/migrations, configuration, scripts and build artifacts. Say what was not parsed. If production differs, trace the actual deployed code before calling a production cause confirmed.
- Page through all requested issue states with a date cutoff for “recent”; include closed issues where requested. Count unique IDs and compare to an independent count where possible. Distinguish titles, bodies, comments, timeline and PRs actually obtained. A snapshot may change while paging. Never claim individual semantic classification because all issue bodies were fetched: save per-issue category or `unclassified` and validate its ID set.
- Group reported failure patterns by contract and outcome, not just surface or symptom. A closed ticket proves neither its fix nor its present-day regression. Cross-link existing tickets and avoid creating duplicates.

## Structural discovery

1. Reuse installed analyzers, linters, parser, call graph and dependency graph; inspect what they actually analyze. Regex rapidly locates candidate tokens but ignores types, nested scopes, aliases and control flow. Use parser-aware analysis for catch/throw, return/await, resolved calls, switch branches, cancellation and data ownership. Structural matches still require context.
2. Trace entry point → preparation → side effect → confirmation → state update → UI → recovery. Identify code and data ownership at every boundary. Follow both the direct call and sibling consumers; inspect the actual output, not just the presence of a handler.
3. Build an import/call graph to locate downstream effects and reverse callers. Record counts: files discovered/parsed, imports/calls resolved/unresolved, and graph assumptions. Interfaces, runtime dispatch, hooks, SQL, events, network calls and generated code can escape a static graph. Never describe resolution percentage as runtime or bug coverage.
4. Identify priority boundaries from actual issue history and application behavior: costly data; transaction commit/rollback; async cancellation/late effects; success notifications; retries/leases; request mapping; timeouts; provider degradation; source fidelity; and production-transformed artifacts. Do not let selection by a keyword erase other files from the denominator.
5. For scans, store unique IDs, path, line range, revision, selection reason, disposition, evidence pointer, confidence and overlap. Use programmatic deduplication/counting. Test an analyzer against small positive and negative examples before using its output. Record errors, unsupported files, skipped ranges, and changes since the pinned revision.

## Adversarial review of evidence

For high-risk paths, try to disprove the candidate: inspect actual caller, existing recovery, schema constraints and intentional fallback. Verify version/feature flags and independently inspect reported results before publication. Contrast unit mocks with actual build artifacts and production protocols. A failing test at an artificial seam establishes only that seam; show the concrete conditions needed for a user-facing path.
