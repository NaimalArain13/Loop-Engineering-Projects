# Session 1 Summary — Projects 1, 2, 3

**Date:** 2026-08-14
**Repo:** github.com/NaimalArain13/Loop-Engineering-Projects (single repo, no submodules)
**Last commit pushed:** `708bf60` (working tree clean, everything up to date)

Paste this whole file into a new session as context, then say "start project 4."

---

## What this is

Working through the [Loop Engineering Crash Course](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course#practice-projects)'s
8 hands-on practice projects, one at a time, each in its own subfolder of
this parent directory. Building with **Claude Code** (not OpenCode) — `/loop`,
`/goal`, Routines, worktrees, skills.

Before starting any project, the assistant explains it contextually first
(which heartbeat/concept it teaches, the scenario, the "done when" criteria)
— this is a standing request, not a one-off.

## Standing rules (also in `CLAUDE.md` at repo root — read that file first)

1. **Never `git push`.** Commit locally when asked; the user pushes manually.
2. **One repo, not many.** Don't `git init` inside a `project-N-...` folder —
   this parent folder is the one repo. Plain folders only.
3. **Dependencies stay project-local.** A project's venv/`requirements.txt`/
   `package.json` etc. lives inside that project's own folder, not the
   parent root.
4. **User runs the actual loop-triggering command themselves.** When a step
   calls for starting a real heartbeat (`/loop`, `/goal`, a scheduled prompt),
   give the exact command/prompt text for the user to paste — don't invoke
   it directly via the Skill/Agent tool. Scaffolding, file edits, git
   commands (except push), and running checkers (e.g. `pytest`) are fine to
   run directly.

## All 8 projects (for reference)

| # | Project | Concept | Status |
|---|---------|---------|--------|
| 1 | A watch loop (in-session) | 4 | ✅ done, pushed |
| 2 | Make the tests pass, then stop (conditional + maker-checker) | 5, 11 | ✅ done, pushed |
| 3 | The morning brief with a memory (scheduled + spine) | 6, 12 | ✅ done, pushed |
| 4 | A fix loop with a real checker (worktree, skill, maker-checker) | 8, 9, 11 | ⬜ next |
| 5 | Codify the body (dynamic workflows) | interlude, 8, 11 | ⬜ |
| 6 | The doorbell loop (event-driven, connectors) | 7, 10 | ⬜ |
| 7 | Break it on purpose (observability, cost) | obs, 13, 14 | ⬜ |
| 8 | Your own daily loop (capstone) | all six parts | ⬜ |

## Project 1 — A watch loop (done)

Folder: `project-1-watch-loop/`. Simulated a long task (`long_task.sh`,
sleeps then writes `task_done.txt`), started it as a harness-tracked
background job (plain `nohup ... &` does NOT reliably survive between
separate Bash tool calls in this environment — use the Bash tool's own
`run_in_background: true` instead), then used `/loop` (via `CronCreate`,
1-minute cadence) to poll for the marker file. It reported completion once
and stopped cleanly (`CronDelete`).

## Project 2 — Make the tests pass, then stop (done)

Folder: `project-2-tests-pass/`. Python + pytest, scoped in a project-local
`.venv/` (gitignored). `utils.py` had 3 deliberate one-line bugs (`add`
subtracted instead of added, `is_palindrome` didn't normalize case,
`factorial(0)` returned 0 instead of 1); `test_utils.py` exercised them.
User ran `/goal` themselves with a capped-at-6-attempts prompt; the checker
was `.venv/bin/pytest -q`'s exit code, not the agent's own judgment. Fixed
and passed on attempt 1/6.

## Project 3 — The morning brief with a memory (done)

Folder: `project-3-morning-brief/`. `progress.md` is the spine: a
`last_seen_commit` pointer plus a dated `## Entries` log. The loop body
(a plain prompt, not a slash command, run manually 3 times) reads the
pointer, lists only commits since then (`git log --oneline <ptr>..HEAD`),
summarizes, appends an entry, and advances the pointer.

Verified across 3 runs: run 1 summarized full history (3 commits), run 2
correctly found nothing new (no repeat of run 1), run 3 picked up exactly
the 2 commits made in between. That's the proof the spine works — later
runs build on earlier ones instead of restarting from scratch.

## Environment notes worth remembering

- Python: `python3` is 3.14, but `python3-venv`/`pip` were not installed by
  default — user installed `python3.14-venv` via `sudo apt` themselves.
- Bash tool: **shell state (background jobs, `cd`) does not persist between
  separate tool calls** — only cwd persists, and even that gets reset in
  some cases. Detached processes (`nohup`/`disown`) are not reliable for
  anything that needs to survive across calls; use `run_in_background: true`
  on the Bash tool itself.
- User's email: naimalarain13@gmail.com. Today's date at time of writing:
  2026-08-14.

## Next up: Project 4

**"A fix loop with a real checker"** — Concept 8 (worktree), 9 (skill), 11
(maker-checker). 1-2 hrs, medium-hard.

> A smaller version of the Part 5 loop. Write a short skill with fix steps,
> and a reviewer agent that replies PASS or FAIL. Take one real bug, have
> the implementer draft a fix in its own checkout (worktree or branch), and
> let the reviewer grade it. Open a PR only on PASS.
>
> Done when: a good fix gets a PASS and a PR, AND a deliberately bad fix
> (planted on purpose) gets a FAIL with reasons. If the reviewer passes the
> bad fix, the checker is too soft.

This one is a step up: it needs an isolated checkout (git worktree or
branch) for the implementer to work in, a written skill file describing the
fix steps, a separate reviewer role that grades PASS/FAIL, and — since it
opens a PR on PASS — will likely need its own throwaway *remote* repo,
which is the first project where deviating from "one repo, no git init"
might genuinely be warranted. Confirm with the user before creating a
second repo/remote for this.
