# Project 3 — The Morning Brief With a Memory

**Concept:** 6, scheduled heartbeat + Concept 12, the spine
**Difficulty:** medium · 45-60 min

## Goal
A loop that runs once, reads `progress.md`, gathers something simple from
the repo (here: the last day's/last unrecorded commits), writes a short
summary, and updates `progress.md` with what it found and the date — such
that a second run clearly builds on the first instead of repeating it.

## The spine
`progress.md` is the memory. It tracks:
- `last_seen_commit` — the commit SHA the loop had already summarized as of
  its last run. On the next run, only commits *after* this one are new.
- `## Entries` — a dated log of what each run found.

Without this file, every run would be identical: "summarize all commits,"
forever, with no sense of what's already been reported. That's the trap
this project is built to make you feel.

## The loop body (run this prompt, twice, minutes/runs apart)

```
Read project-3-morning-brief/progress.md and find the last_seen_commit value.
- If it is "none", list all commits in this repo: git log --oneline
- Otherwise, list only commits since then: git log --oneline <last_seen_commit>..HEAD
Summarize what happened in 2-3 sentences.
Then update progress.md:
- Append a new entry under "## Entries" with today's date and the summary.
- Update last_seen_commit to the current HEAD commit SHA (git rev-parse HEAD).
Do not repeat anything already listed in a previous entry.
```

Run 1 will summarize everything up to that point (Projects 1 and 2's
commits). Between run 1 and run 2, make at least one new commit
(e.g. committing this project's own scaffold) so run 2 has something new
and different to report — otherwise run 2 will correctly report "nothing
new," which also proves the spine works, just less visibly.

## Done when
- [ ] Run 1 produces an entry and advances `last_seen_commit`.
- [ ] Run 2 produces a *different* entry — new commits only, not a repeat
      of run 1's summary.
- [ ] If run 2 starts from nothing (re-summarizes everything from scratch),
      the spine isn't working yet.

## Path to the real heartbeat
This project proves the spine manually. The actual Concept 6 version wires
the same prompt to a Routine (GitHub-hosted, cloud) or a cron trigger with
a daily cadence, so it fires unattended every morning — no one pasting the
prompt in by hand.
