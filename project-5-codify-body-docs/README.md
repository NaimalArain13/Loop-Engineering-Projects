# Project 5 — Codify the Body

*Difficulty: medium to hard · Uses: the dynamic-workflows interlude,
Concepts 8 and 11.*

Turn Project 4's orchestration into one re-runnable unit, then prove it is
not a loop.

## Repo

The working loop — code, skill, and history — lives in its own repo, not
this folder:

**https://github.com/NaimalArain13/project-5-codify-body**

## Build

Take the fix loop from Project 4 and codify its body: one command (the
`codify-body` skill) runs the whole draft-and-review body — several
candidates, isolated worktrees, a reviewer verdict for each — with no
step-by-step prompting.

## Done when

Two things are true. First, one command runs the whole draft-and-review
body end to end. Second, a fresh session invoking it again shows no memory
of the previous run — proving the interlude's warning: this is an engine,
not a loop, because it has neither a heartbeat to fire it on its own nor a
progress file its agents read and write.
