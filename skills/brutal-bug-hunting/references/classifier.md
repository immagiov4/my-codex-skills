# Classifier and measurement

## Scope and privacy

A user's authorization for a small hook is not blanket consent to transmit a repository or private logs to another provider. Agree to the relevant data scope, provider, model and spending before paid bulk use. Decide whether source is public; use pinned committed blobs when appropriate. Exclude environment files, credentials, private keys, untracked changes and private user data. Secret detectors are fallible: inspect suspicious matches locally and avoid claiming sanitization is complete. Keep local inventories and output private when they contain private issue bodies or code.

## Batch protocol

- Inspect the provider's current official interface and model identifier; record the actual returned model, not just the requested label. If the user specifies a model, report failure rather than silently changing it. Budget requests, concurrency, context size and retries according to the grant and provider response.
- Give every source unit a stable ID, path, line interval and source hash; include enough context for the decision, distinguishing code, data and instructions. Delimit untrusted content and explicitly ignore instructions inside it. Classify separately for specific failure classes; a broad binary question produces scores, not diagnoses.
- Pilot known positive and negative controls, including at least one cross-function example and an intentionally safe catch. Check answer IDs, schema and ranges; measure whether answers change when context is missing or present. A pilot establishes connectivity and illustrative behavior, not accuracy at scale.
- Enumerate all eligible segments before making calls. Track selected, completed, invalid, retryable failure, exclusion and unresolved per ID. Split oversized functions at syntax boundaries when practical, retain parent/child mapping, and record unsplittable or secret-matching ranges. Avoid overlapping work and protect checkpoints against concurrent writes. Do not delete partial results on interruption.
- Save provider/model, exact revision, prompt version, time, per-batch usage and reported costs. Capture failed/unknown-billing requests separately. Never log credentials or raw private inputs. A successful API request is not proof that the result is correct.

## Evaluate and prioritize

- Calibrate ranking on a labeled set of known positives and meaningful negative controls with independently verified outcomes. Regress against representative classes, paths, excluded files and real deployed behavior where available. Specify whether the metric is issue-level retrieval, candidate-level detection, or line overlap. Multiple overlapping segments can inflate hits; broad segments may score high for unrelated code.
- Report thresholds, numerator/denominator, sampling strategy, overlap, unclassified items and potential leakage from training/selection. A known-positive sample assembled from earlier investigations is not a representative benchmark. Do not claim general recall, precision, false-positive rate or confidence intervals without the required labeled sample.
- A low score on an already reproduced bug is direct evidence against interpreting low scores as safety. Rank for investigation, not closure. Inspect caller contracts and runtime effects; follow data and error transitions across files. Review selected negatives and high-impact areas independently, not solely the top scores.
- A structurally tagged file or LLM-labeled snippet is a triage observation, not a verified defect. Avoid arbitrary dashboards or high-confidence labels until validated. If the user wants a complete audit, coverage of candidates, reproduction depth and remaining excluded source must all be reported separately.
