# Session 4 Summary — Project 9 ("Rehearse a routine for free") built and completed

**Date:** 2026-08-21
**Repo:** github.com/NaimalArain13/Loop-Engineering-Projects (parent — `.gitignore`,
root `README.md`, and `project-9-rehearse-routine-docs/` updated locally, **not
pushed**, per standing rule)
**New repo this session:** github.com/NaimalArain13/project-9-rehearse-routine
(public, separate throwaway repo — same "own repo" pattern as projects 4, 5, 6, 8)

Paste this whole file (plus `session-01`, `-02`, `-03` summaries for full prior
context) into a new session as context.

---

## What happened this session

1. User asked to move on to the remaining crash-course projects tied to
   "Routine practice drills" (line 1836 of `Loop Engineering A Crash
   Course.md`): Project 9 (Rehearse a routine for free), Project 10 (The
   secrets drill), Project 11 (Build the two-routine gate), Project 12
   (Build a dreaming loop) — and to start planning Project 9 specifically.
2. **Plan mode.** Explored in parallel: (a) located the crash-course
   markdown locally at the repo root and pulled the exact text for
   Projects 9-12's builds/done-when criteria; (b) surveyed the established
   conventions from projects 1-8 (own-repo + pointer-stub pattern for
   GitHub-acting projects, `CLAUDE.md` push-override pattern, README/
   SKILL.md style, falsifiable "done when" phrasing). Asked the user two
   clarifying questions, both answered with the recommended option:
   - The user creates and fires the Routine themselves (assistant
     scaffolds + hands off exact prompt text, does not use the `schedule`
     skill on the user's behalf) — consistent with the standing "user runs
     slash commands" preference.
   - New throwaway repo `project-9-rehearse-routine`, matching the
     projects 4/5/6/8 own-repo pattern (a Routine needs a real, connected
     GitHub repo to clone on every run).
   Ran a Plan subagent to work out exact file contents, then wrote and got
   approval on the final plan (saved at
   `~/.claude/plans/now-we-need-to-golden-wall.md`).
3. **Implementation** (assistant did this directly):
   - Scaffolded `project-9-rehearse-routine/`: `README.md`, `CLAUDE.md`
     (overrides parent's "never push" rule, matching project-5/6's
     pattern), `routine-prompt-run-1.md` (success prompt — summarize last
     24h of commits onto a `claude/summary` branch), `routine-prompt-run-2.md`
     (surgical one-clause diff — forces reading a deliberately absent
     `docs/summary-instructions.md` and stopping rather than improvising),
     `notes.md` + `scripts/hello.py` (filler content for the routine to
     actually summarize). Three real, naturally-timed commits — no
     backdating; decided "last 24 hours" satisfies the course's
     illustrative "yesterday's commits" example without the complexity/
     honesty cost of `GIT_AUTHOR_DATE` tricks.
   - `gh repo create project-9-rehearse-routine --public --source=.
     --remote=origin`, pushed `main`, verified with `git ls-remote` (per
     session-03's lesson: don't trust a clean `gh repo create` exit code
     alone).
   - Updated the parent repo: `.gitignore` (excludes the new folder),
     new pointer stub `project-9-rehearse-routine-docs/README.md`, root
     `README.md` (added row 9 to the projects table, renamed/extended the
     "own repo" rationale section to cover Project 9, updated the intro's
     project count framing). Committed locally, **not pushed**.
   - Handed the user the literal firing instructions (dashboard "New
     Routine" → paste run-1 prompt → one-off "Run now" → read transcript →
     edit prompt to run-2 text → "Run now" again → read transcript) and
     stopped, per the user's decision that they fire both runs themselves.
4. **User fired both runs** and returned two transcript URLs (Claude Code
   session links, not independently fetchable by the assistant — `WebFetch`
   confirmed 403 on them, as expected for authenticated session URLs).
5. **Independent verification without transcript access:** fetched the
   new repo's remote branches directly. `origin/claude/summary` exists
   with exactly one commit (`Add commit summary`) on top of the three
   scaffold commits, and its `SUMMARY.md` correctly and legibly describes
   the three real scaffold commits — proving run 1 actually did the work,
   not just returned green. No second commit or stray branch appeared
   after run 2, consistent with run 2 having stopped on the missing-file
   check rather than silently succeeding or partially mutating anything.
6. Asked the user to confirm run 2's transcript specifically showed the
   missing-file stop (not some other failure) and for their own one-
   sentence A5 lesson. User updated `project-9-rehearse-routine/README.md`
   directly (`## Proof` section) with both transcript links and their own
   sentence, confirming run 2 read for the missing file and stopped
   instantly without touching `SUMMARY.md`, and asked the assistant to
   push. Assistant diffed the change (only the `## Proof` section touched),
   committed, and pushed to `project-9-rehearse-routine` (push allowed
   there per its own `CLAUDE.md`). Verified landed via `git ls-remote`.

## Status

- **Project 9 is done**, per the course's own done-when criteria: two
  green runs exist, one transcript shows real success (verified
  independently via the pushed `claude/summary` branch content), one shows
  a clean forced failure (verified independently via the *absence* of any
  further commit/branch), and the user has stated the A5 lesson in their
  own words in the repo's README.
- Parent repo (`Loop-Engineering-Projects`) has local, unpushed commits:
  `.gitignore`, `README.md`, `project-9-rehearse-routine-docs/`. Needs a
  `git push` from the user when they're ready (assistant does not push
  the parent repo, per root `CLAUDE.md`).
- `project-9-rehearse-routine` is fully pushed and up to date, including
  the completed `## Proof` section.

## Next up (resume here)

1. **Push the parent repo.** The `.gitignore`/README/pointer-stub commit
   for Project 9 is local-only — user needs to run `git push` themselves.
2. **Project 10 — The secrets drill** (30-45 min, easy-medium, uses A4
   secrets / A2 the environment): write a prompt needing one dummy secret;
   first run puts it in a gitignored `.env` (should fail, transcript shows
   why); second run moves it to the Routine's environment-variables panel
   with the appendix-recommended prompt line ("credentials are available
   as environment variables; do not look for a `.env` file"). Not yet
   scoped/planned.
3. **Project 11 — Build the two-routine gate** (1-2 hrs, medium-hard, uses
   A3 API trigger / A4 the gate / A6 checklist): Routine A drafts
   something reviewable on a one-off schedule; Routine B has an API
   trigger and does one small follow-up action, fired only by the user's
   own `curl` call after reviewing A's draft. Not yet scoped/planned.
4. **Project 12 — Build a dreaming loop** (2-3 hrs, capstone, uses Concept
   12 spine/improvement loop, Concept 11 maker-checker, Concept 6
   schedule, Part 5 human gate): needs a loop that has already run for a
   week with dated `progress.md` entries (Project 3 or Project 8 qualify)
   — build a second weekly loop over it that proposes rule/skill changes
   as a PR, citing evidence, never committing directly. Blocked in part on
   Project 8 actually accumulating a week of runs (see below) — plan this
   one after Project 8's week is real, or after Project 3 accumulates
   enough log volume to have a genuine repeated failure to catch.
5. Carried over, unresolved since session 3 (not touched this session):
   - Project 4's `demo-bad-fix` half still not run/confirmed.
   - Project 8 (`Morning-Maintenance-Loop`) still has only one day of
     runs; done-when needs a full unattended week.
   - Projects 1, 2, 6, 7 still need live re-verification against the
     top-level README's "done" claims (Project 6's PR review-comment
     authorship in particular).

## Environment notes worth remembering

- `WebFetch` returns a 403 on `claude.ai/code/session_...` URLs (Routine
  run transcripts) — these are authenticated to the user's own login and
  not fetchable by the assistant, unlike `claude.ai/code/artifact/{uuid}`
  URLs which WebFetch can reach. When a user hands over a transcript link
  for verification, fall back to checking observable side effects (repo
  branches/commits/file contents) instead of trying to read the
  transcript directly.
- `ListAgents` does not surface Routine runs as peer sessions — they're
  not addressable via `SendMessage`.
- Verifying a Routine's actual behavior from git state alone (branch
  existence + commit count + file content) worked well here as an
  independent cross-check against the user's own transcript reading,
  without needing transcript access at all.
