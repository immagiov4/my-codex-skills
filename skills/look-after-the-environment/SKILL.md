---
name: look-after-the-environment
description: Reuse compatible tools, dependencies, browsers and test data before installing them. Clean up temporary artifacts and worktrees, or present named Windows directories for the maintainer's explicit deletion approval.
---

## Before installing

Identify the exact version, platform and entry point the project expects from its lockfile, tool configuration or existing scripts. Check the project, PATH and the package manager's shared cache or store. Reuse a compatible installation through its supported entry point. A tool on PATH does not satisfy a project-local import unless the project supports that resolution.

Use the configured package manager and its shared store for missing packages. Keep each project's own lockfile and dependency resolution. On Windows, hard links require the same volume. For Bun isolated installs, check whether the installed Bun supports a global virtual store and whether a warm test install actually links into it. Prefer the project's configured browser cache and pinned browser revisions. When a heavy fresh install is still needed, explain what is missing and whether future runs can reuse the result.

## During tests

Keep temporary work in one task directory and separate inputs from generated output. Reuse the project's documented fixture directory or the configured shared test-source path. For Nous local tests, check `NOUS_TEST_SOURCES_DIR` and use the manifest to pass the preserved file path to the test runner. Keep private fixtures and credentials outside Git. Use a fresh output directory for each run that needs independent results.

## Close out

Before publication and again after verification, account for what the task created. Keep the evidence needed for an open review or for a reproducible test. Remove task-owned outputs, scratch dependencies and temporary worktrees as soon as their purpose ends. Verify the intended publication payload and the cleanup.

When you find older leftovers, establish ownership and check for running consumers, Git changes and unique commits, open reviews, and test inputs or evidence that still matter. Remove confirmed disposable material within the user's authorization. Preserve recoverable local work before removing a checkout, and verify the resolved destination before a recursive operation. Keep shared caches and reusable test data under their existing owner.

### Worktrees whose work is already published

Harness-created worktrees outlive their task. The [worktree pruner](scripts/prune-worktrees.mjs) removes only linked worktrees under one root that are idle, clean, unlocked, unused by any process, and whose `HEAD` is on a remote or equals a merged pull request's head; everything else is kept with its reason. It is a dry run unless `--execute` is passed and appends one JSON line per worktree to `~/.look-after-the-environment/prune-worktrees.log`:

```sh
node <skill>/scripts/prune-worktrees.mjs --repo <main checkout> --root <worktrees dir> [--min-idle-days 3] [--execute]
```

For the weekly Windows inventory, run the same entry point with `--config <json>`. The JSON next to the launcher defines `repositoryRoots`, `worktreeRoots`, `leftoverRoots`, optional `containerDepth` by root, and `minIdleDays` (at least 1.5). The task writes `worktree-inventory.json` next to the configuration unless `output` selects another destination. Repository discovery includes nested repositories and linked worktrees. Discovery skips dependency directories and does not follow directory links.

Review missing paths, unreadable directories, ignored files and possible process references before proposing an exact deletion list. File sizes are logical bytes. A hard-linked file may occupy space shared with another checkout. Process command lines and executable paths can reveal active consumers, but do not expose every current directory or open handle. Residual directories are inventoried for manual review because their Git, data and reference checks differ from registered worktrees. Configuration mode never deletes. The weekly task runs it first, then runs the strict `--repo/--root --execute` mode for each repository and root pair listed in its launcher: the maintainer authorized unattended removal of worktrees that meet those strict criteria (2026-11-21). Residual directories and anything the strict mode keeps go to the maintainer as an exact list.

### Windows worktrees and residual directories

For a clean, authorized worktree, enable long paths on the first removal command: `git -c core.longpaths=true -C <repository> worktree remove -- <absolute-worktree-path>`. A failed removal can unregister the worktree while leaving its directory. Check both Git's worktree list and the filesystem before deciding what remains.

Keep the requested outcome explicit: deleting a directory, reclaiming disk space and archiving a checkout are different results. A directory moved elsewhere still occupies disk space. If execution policy refuses an authorized deletion, report deletion as blocked; neither a move nor a user-run script completes it. A skill or script location cannot change the execution policy.

When recoverable archiving is itself authorized, a confirmed task-owned residual directory whose Git registration is absent can use the bundled [recoverable retirement helper](scripts/retire-directory.ps1). Recheck ownership and running consumers before execution. Choose recovery storage on the same volume, outside the target, and preview with PowerShell 7:

```powershell
& <skill>/scripts/retire-directory.ps1 -Path <absolute-target> -ApprovedParent <absolute-immediate-parent> -RecoveryRoot <absolute-recovery-directory>
```

Inspect the resolved target, then run the same command with `-Execute` within the existing cleanup authorization. The helper accepts only a real directory directly inside the approved parent and renames it into recovery storage on the same volume. It rejects parent-root targets, link ancestors and recovery paths inside the target. Record the returned recovery path. Retirement removes the active checkout location and preserves its complete tree; it does not reclaim disk space. Permanent disposal remains a separate authorized operation through a permitted tool.

The agent executes the authorized operation and verifies its actual result. Keep execution in the normal tool approval channel: a script location or launch queue does not grant permission to run rejected operations. If the requested operation is refused, preserve the data and report that specific operation as pending, without substituting an archive or assigning the maintainer a one-off script as a completed cleanup.

Recoverable archiving is complete only after the active target directory and its Git worktree registration are absent, recovery storage contains the tree, and preserved neighbors remain intact. Deletion or space-reclamation requests retain their own completion criteria. When changing the helper, run [its Windows behavior tests](scripts/test-retire-directory.ps1) with `-TestRoot <external-test-directory>`; they exercise preview, invalid scope, junctions, long paths, actual restoration and repeat execution using disposable fixtures.

### Desktop approval for permanent disposal

When the maintainer requests interactive disposal, use the [desktop approval window](scripts/request-deletion.py) to show one or more explicitly named Windows directories. Recheck ownership, running consumers, and whether the contents are still needed. Pass each absolute directory path as a separate argument in the maintainer's graphical session, using Python 3.11 or later with Tk.

```powershell
python <skill>/scripts/request-deletion.py "C:\absolute\task\cache" "D:\absolute\task\scratch" --reason "<why these directories can be deleted>"
```

The window lists the exact resolved paths. **Approva** applies to the entire list and shows progress during permanent deletion. **Rifiuta** or closing the window before approval leaves the directories in place. The maintainer presses the approval button for a real request. Report a pending decision while the window is open. After it closes, verify the presence or absence of each path before reporting the outcome. If an error occurs, check what remains and require a fresh request before retrying. Use the applicable tool approval channel for execution. This separate desktop decision cannot override an execution refusal.
