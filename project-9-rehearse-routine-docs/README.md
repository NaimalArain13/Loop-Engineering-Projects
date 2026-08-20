# Project 9 — Rehearse a Routine for Free

*Difficulty: easy · Uses: A1, A3 (one-off schedules), A5 (reading runs).*

Prove a prompt with one-off runs before committing it to a repeating
schedule.

## Repo

The routine, its throwaway repo, and both run transcripts live in their
own repo, not this folder:

**https://github.com/NaimalArain13/project-9-rehearse-routine**

## Build

A Claude Code Routine, fired only with one-off runs (never a repeating
schedule), summarizes the repo's last 24 hours of commits onto a
`claude/summary` branch. The same routine is then re-fired with two
sentences added to its prompt — forcing it to read a file that does not
exist — to produce a second, failing run.

## Done when

Two green runs exist: one transcript showing the summary actually
happened, one showing the missing-file read failing. Read side by side,
the status column cannot tell them apart — both show green — which is
the A5 lesson: green means the session ended without an infrastructure
error, nothing about whether the task itself succeeded.
