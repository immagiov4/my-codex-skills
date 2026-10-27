# Failure-boundary patterns

Use these as hypotheses to test, not as a checklist of automatic bugs. Every finding needs an actual contract, caller and impact.

## User work and ownership

- Follow costly input from upload to staging, durable commit, refresh, cleanup and user-visible result. For each failure or cancellation, ask what is already committed and who owns each ID and object. A refresh failure is not automatically an import failure. A response mismatch, project switch, late completion or stale callback must not authorize deletion of someone else's data. Test exact ownership/adoption and timing; a mocked mismatched response alone does not show a real backend can emit it.
- Recovery and deduplication need identity stronger than coincidentally similar content. Test partial retries, tombstones, already-deleted items, preserved legacy input and completion markers. Separate a missing recovered note from proven deletion of its original.
- On revision conflicts or remote deletion, inspect queued writes, local dirty state, snapshot hydration and navigation/unmount. A debounce timer alone does not prove an actual browser loses data; reproduce a concrete user-edit path.

## Diagnostics, state and success

- Compare every distinct failure at its origin with the public response, private diagnostic, durable record and eventual retry feedback. Generic messages can be appropriate publicly while the technical cause and stable sanitized field path are retained privately. Verify both the original failure and cleanup failure when both occur. No raw prompts, documents, credentials or chain of thought belong in diagnostic output by default.
- Look for error-as-empty, timeout-as-success, premature success before persistence, rejected promises discarded by event handlers, status defaults, and degraded fallback treated as a confirmed capability. Trace shared global indicators and intentional best-effort paths before claiming no feedback. A 204 response has no JSON body; test protocol status and client expectations together.
- For final-attempt fallback, check whether the actual final cause is recorded and whether prior attempts can differ. Preserve the desired fallback while testing private observability. Rejected or invalid sources must not count as valid evidence merely because an earlier raw array was nonempty; compare normalization and validation ordering.

## Retries, timeouts and asynchronous work

- Determine if requests have a real timeout, cancellation signal and owner; test transient and permanent failures, exhausted retries, outages, terminal error, recovery, late success and shutdown. Check whether the retry shares a durable result or unchanged feedback. A finite observation of repeated attempts is not proof of an infinite outage in production.
- On leases, test explicit lost ownership separately from heartbeat exceptions. If an awaited side effect cannot be canceled, test whether the owning loop and shutdown remain blocked and whether the late effect can commit. Idempotence and database isolation matter; never assume abort cancels a transaction without exercising it.
- Separate actual provider unavailability from no results and optional enrichment from required evidence. An explicit opt-in fallback is not automatically a missing failover; policy changes need a decision.

## Reproduction strength

Use the real function or delivered artifact, injecting only the failing boundary. Assert the trigger and consequence: for example `commit → refresh failure → deletion`, a prompt input → schema → normalization → empty result, or two events ordered across a deferred promise. A passing characterization can demonstrate current broken behavior; a red regression asserts the desired contract and must fail before a fix. State which mocks were used, whether UI/backend/storage were exercised, and whether a production event was observed. A proxy 200 does not establish browser receipt, parsing or rendering. Test generated workers/worklets and browser bundles as shipped when a build transformation is part of the defect.
