---
name: maintain-system-map
description: Keep docs/system-map.md synchronized with meaningful architectural changes while avoiding documentation churn.
---

# Maintain system map

1. Read the relevant diff and the current `docs/system-map.md`.
2. Determine whether the change altered any of the following:
   - concepts;
   - ownership;
   - subsystem/module boundaries;
   - dependency direction;
   - important data/control flows;
   - invariants;
   - major entry points;
   - user-visible feature topology.
3. If none changed, do nothing. Stop here.
4. If something changed, edit only the smallest necessary section of
   `docs/system-map.md`.
5. Do not document individual functions/classes merely because they were
   touched.
6. Do not duplicate information obvious from one source file.
7. Prefer stable concepts and relations over implementation trivia.
8. If a surprising, hard-to-reverse decision represents a genuine trade-off,
   suggest an ADR under `docs/adr/` instead of bloating `system-map.md`.
