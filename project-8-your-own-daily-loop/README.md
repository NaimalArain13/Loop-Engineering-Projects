# Project 8 — Your Own Daily Loop (Capstone)

*Difficulty: capstone · Uses: all six parts of the loop.*

The full six-part loop, built around one real, boring, recurring chore, run
unattended for a week.

## Repo

The working loop — code, skill, and history — lives in its own repo, not
this folder:

**https://github.com/NaimalArain13/Morning-Maintenance-Loop**

## The six parts

1. **Heartbeat** — what fires the loop on its own (schedule, event, or a
   cron-equivalent), with no prompt typed by hand.
2. **Worktree** — isolated checkouts so the loop's edits never collide with
   manual work or with themselves across parallel runs.
3. **Skill** — the loop's habits and steps written down once, so every run
   reads them instead of re-deriving the setup from scratch.
4. **Maker-checker** — an implementer drafts, a separate reviewer grades;
   only a passing review ships.
5. **Connector** — the loop can act (open a PR, comment, update a file
   others read), not just talk.
6. **The spine** — a committed progress file the loop reads at the start of
   each run and writes at the end, so the second run visibly builds on the
   first.

## Done when

- It has run unattended for a week, and the changes it ships are trusted
  because they were read, not because reading stopped.
- Concept 15 answered honestly: did understanding of the project keep up
  with what the loop changed? If not, the loop needs to slow down until it
  does.
