---
name: look-after-the-environment
description: Reuse compatible tools, dependencies, browsers and test data before installing them, and clean up temporary test artifacts and worktrees after verification or before publishing. Use when preparing a test environment, installing a dependency, or closing out work that created temporary files.
---

## Before installing

Identify the exact version, platform and entry point the project expects from its lockfile, tool configuration or existing scripts. Check the project, PATH and the package manager's shared cache or store. Reuse a compatible installation through its supported entry point. A tool on PATH does not satisfy a project-local import unless the project supports that resolution.

Use the configured package manager and its shared store for missing packages. Keep each project's own lockfile and dependency resolution. On Windows, hard links require the same volume. For Bun isolated installs, check whether the installed Bun supports a global virtual store and whether a warm test install actually links into it. Prefer the project's configured browser cache and pinned browser revisions. When a heavy fresh install is still needed, explain what is missing and whether future runs can reuse the result.

## During tests

Keep temporary work in one task directory and separate inputs from generated output. Reuse the project's documented fixture directory or the configured shared test-source path. For Nous local tests, check `NOUS_TEST_SOURCES_DIR` and use the manifest to pass the preserved file path to the test runner. Keep private fixtures and credentials outside Git. Use a fresh output directory for each run that needs independent results.

## Close out

Before publication and again after verification, account for what the task created. Keep the evidence needed for an open review or for a reproducible test. Remove task-owned outputs, scratch dependencies and temporary worktrees as soon as their purpose ends. Verify the intended publication payload and the cleanup.

When you find older leftovers, establish ownership and check for running consumers, Git changes and unique commits, open reviews, and test inputs or evidence that still matter. Remove confirmed disposable material within the user's authorization. Preserve recoverable local work before removing a checkout, and verify the resolved destination before a recursive operation. Keep shared caches and reusable test data under their existing owner.

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

