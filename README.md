# Loop Engineering Projects

Hands-on practice projects from the Loop Engineering Crash Course
(https://agentfactory.panaversity.org/docs/loop-engineering-crash-course#practice-projects).
Eight projects, easy to hard, covering all six parts of a loop across all
four heartbeats: in-session, conditional, scheduled, and event-driven.

## Projects

| # | Project | Heartbeat / Concept | Where it lives |
|---|---------|----------------------|-----------------|
| 1 | [Watch loop](./project-1-watch-loop) — notice a long task finish without watching the terminal | In-session (Concept 4) | This repo |
| 2 | [Make the tests pass, then stop](./project-2-tests-pass) — a conditional loop that stops when a test runner says so, not when the agent decides | Conditional, maker-checker | This repo |
| 3 | [Morning brief with a memory](./project-3-morning-brief) — a scheduled loop whose second run visibly builds on the first | Scheduled, the spine | This repo |
| 4 | [A fix loop with a real checker](./project-4-fix-loop-docs) — implementer drafts, reviewer grades, only `PASS` opens a PR | Worktree, skill, maker-checker | [Own repo](https://github.com/NaimalArain13/project-4-fix-loop) |
| 5 | [Codify the body](./project-5-codify-body-docs) — Project 4's orchestration turned into one re-runnable command, proven to have no memory of its own | Dynamic workflow, worktree, maker-checker | [Own repo](https://github.com/NaimalArain13/project-5-codify-body) |
| 6 | [The doorbell loop](./project-6-doorbell-loop-docs) — the repo reviews its own pull requests, unprompted | Event-driven, connectors | [Own repo](https://github.com/NaimalArain13/project-6-doorbell-loop) |
| 7 | [Break it on purpose](./project-7-break-it-on-purpose) — sabotage the Project 3 loop, then diagnose the failure from the spine alone | Observability, cost | This repo |
| 8 | [Your own daily loop](./project-8-your-own-daily-loop) — the full six-part loop on a real chore, run unattended for a week (capstone) | All six parts | [Own repo](https://github.com/NaimalArain13/Morning-Maintenance-Loop) |

## Why Projects 4, 5, and 6 live in their own repos

Projects 1, 2, 3, 7, and 8's docs are plain exercises that read and write
files inside this repo — a normal subfolder is enough. Projects 4, 5, and 6
are different: their whole point is a loop that **acts on GitHub**, not
just on the local filesystem —

- **Project 4** and **Project 5** open real pull requests as part of their
  own done-when criteria. A PR needs a real `origin` remote to open
  against; a shared monorepo remote would mean every practice fix landing
  as a PR against `Loop-Engineering-Projects` itself, mixed in with
  unrelated commit history from every other project.
- **Project 6** specifically needs the **Claude GitHub App** installed on
  the repo and a Routine wired to that repo's pull-request events. Both are
  repo-level configuration — they can't be scoped to "just this
  subfolder" of a bigger repo, so the doorbell loop needs a repo of its
  own to fire on.

So each of the three got its own **throwaway GitHub repo** (see the
`.gitignore` at this level, which excludes their local folders from this
parent repo's tracking), and a small pointer README — `project-4-fix-loop-docs/`,
`project-5-codify-body-docs/`, `project-6-doorbell-loop-docs/` — was added
here so they're still discoverable from this index without pulling their
full history and PR churn into the parent repo.
