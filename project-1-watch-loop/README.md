# Project 1 — A Watch Loop

**Concept:** 4, in-session heartbeat
**Difficulty:** easy · 15-30 min

## Goal
Start a long task, then set up an in-session loop that checks every minute
whether it has finished, and tells you the moment it has — without you
sitting and watching the terminal.

## Files
- `long_task.sh` — simulates a long-running task. Sleeps for N seconds
  (default 180), then writes `task_done.txt`.

## How this run works
1. `long_task.sh` is launched detached (`nohup ... &`), so it is a real OS
   process independent of any single tool call — closer to a real build
   than something the assistant is directly babysitting.
2. `/loop` is started with a 1-minute interval. Each wake-up checks for
   `task_done.txt`. On the first wake-up where it exists, the loop reports
   the result once and stops itself.

## Done when
- [x] The loop notices the task finished and says so exactly once.
- [x] The loop can be / was stopped cleanly (no orphaned watcher).
- [x] Nobody sat staring at the terminal waiting.

## The concept this proves
An in-session loop only exists inside the session that started it. If the
terminal/session had been closed before `task_done.txt` appeared, the
watching would have died with it — that's not a limitation to work around,
it *is* what "in-session" means. (Project 3 later swaps this for a
scheduled loop with memory, which survives across sessions.)
