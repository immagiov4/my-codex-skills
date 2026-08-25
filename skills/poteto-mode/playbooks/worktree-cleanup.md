### Worktree and simulator cleanup

**You own the disk and the safety gate.** Prune merged or abandoned git worktrees and stale iOS simulators to reclaim space. Deletion is irreversible, so every step guards against deleting something in use or holding uncommitted work.

1. Snapshot and audit. Use the host's native disk-space command, then run `scripts/worktree-audit.sh` when Bash is available. The script gets paths from `git worktree list` and reports size, age, merge state, uncommitted work, and pull-request state. On Windows, resolve every candidate to an absolute path before any later removal.
2. The bucket is advice, not permission. Cross-check candidates against active Codex tasks, running agents, open pull requests, and anything the user says to keep.
3. Verify usage before deleting. Inspect uncertain worktrees with read-only Git commands. Do not scan private transcript directories. A worktree used by a current task stays.
4. Pause on irreversible loss. Show tracked and untracked changes before removing a dirty worktree. Get the user's decision for any tracked edits or uncertain scratch files.
5. Prune only the confirmed exact paths. Use `git worktree remove <absolute-path>` for clean worktrees. Use `--force` only with explicit approval for that exact dirty path. If ignored files remain, remove them with the host shell only after resolving and checking that the absolute target is the confirmed worktree. Then run `git worktree prune` and re-list.
6. Treat simulators, IDE data, and package caches as separate scopes. Inspect them first and delete only the exact categories the user named.

This is the one playbook that deletes user state with no code review to catch a slip, so the gates above are the review.

**Reply:** `df -h /` before and after with space reclaimed, the worktrees pruned, and a one-line reason for each held back (in-use by which chat, or uncommitted work).
