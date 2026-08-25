### Opening a PR

Invoked at the end of every other playbook.

**Worktree.** Use a separate Git worktree for each writing subagent when the repository and user authorize branch changes. Preserve dirty user work. Move authorized work to a fresh worktree when changes overlap. Never use `git reset --hard` as a cleanup shortcut.

**Commits.** Commit liberally; rebase into small, ordered commits before opening PRs. Each commit is a future PR: landable, ordered to tell the story. Amend when the fix belongs in a just-made commit; new commit when separable.

**PRs.** Run `$unslop` over prose and comments before commit. Apply the root Comments rules before review. Write every pull-request title, description, and commit body with `$docs-doc`, then apply `$unslop`. Use one word for each action, keep articles, and avoid `-ing` when a plain verb works.

**Titles.** Use Conventional Commits only when the repository follows that convention. Keep the subject short and imperative. Apply the same `$docs-doc` and `$unslop` pass as the body. Name a real symbol when one carries the change. Do not add a trailing period.

**Descriptions.** Use these sections in order. Drop a section when it is empty.

- `## Why`. State the intent and why this approach fits.
- `## Scope`. State facts from the diff. Name real symbols and paths. Name both sides of a rename or retarget. State what is in and out when the boundary matters.
- `## Tradeoffs`. State real choices only. Skip this section when there are none.
- `## Blast Radius`. State who and what the change touches. Explain why the change is safe or risky. If main is red without the fix, name the continuing cost.
- `## Verification`. State how you ran each check and its rigor. Name the real path, such as the terminal and the project verification skill, `$agent-browser`, or the targeted tests. State the outcome of each check, not only the command name.

After these sections, attach videos or screenshots when they prove a claim. Do not use `## Summary` or `## Test plan` boilerplate. A commit body does not restate its subject.

**Size and stacks.** Prefer five narrow PRs to one large PR. Stack follow-ups with Graphite (`gt`), and keep the ordered stack visible to reviewers. Branch from main only for independent work. Rebase on `main` before substantial stack work.

**Readiness.** Open every PR ready, never as a draft. Cloud-agent PR tools default to draft, so set `draft: false` on every PR creation call. If a PR still opens as a draft, run the host's ready command, such as `gh pr ready <number>`. Run `gh pr view <number>` before you refer to PR status.

**Babysit.** Opening a PR does not start a babysit. Post the URL and keep building. Finish the phase or stack first. Run a separate babysit pass only when the user asks for one after the whole stack exists. A babysit for each new PR stalls the build and spends checks on commits that later waves restart. Push back when feedback drifts from intent.

A subagent that opens an authorized pull request runs `$interrogate`, `$unslop`, and the root Comments rules. It returns the URL and does not babysit.
