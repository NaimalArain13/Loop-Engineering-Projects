# Project 4 — A Fix Loop With a Real Checker

*Difficulty: medium to hard · Uses: Concept 8 (worktree), Concept 9 (skill),
Concept 11 (maker-checker).*

An implementer drafts a fix in its own checkout, a separate reviewer grades
it, and only a `PASS` opens a PR.

## Repo

The working loop — code, skill, and history — lives in its own repo, not
this folder:

**https://github.com/NaimalArain13/project-4-fix-loop**

## Build

A smaller version of the full end-to-end loop. A short skill holds the fix
steps; a reviewer agent replies `PASS` or `FAIL`. The implementer drafts a
fix for one real bug in its own checkout (worktree or branch), and the
reviewer grades it. A PR opens only on `PASS`.

## Done when

Two things are both true: a good fix gets a `PASS` and a PR, *and* a
deliberately bad fix planted on purpose gets a `FAIL` with reasons. A
checker that approves everything is no checker.
