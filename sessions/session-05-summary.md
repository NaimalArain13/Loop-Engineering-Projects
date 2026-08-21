# Session 5 Summary — Project 10 ("The secrets drill") built and completed

**Date:** 2026-08-21
**Repo:** github.com/NaimalArain13/Loop-Engineering-Projects (parent — `.gitignore`,
root `README.md`, and `project-10-secrets-drill-docs/` updated locally, **not
pushed**, per standing rule)
**New repo this session:** github.com/NaimalArain13/project-10-secrets-drill
(public, separate throwaway repo — same "own repo" pattern as projects 4, 5,
6, 8, 9)

Paste this whole file (plus `session-01` through `-04` summaries for full
prior context) into a new session as context.

---

## What happened this session

1. Continuing directly from Project 9 in the same conversation. User asked
   to plan Project 10 ("The secrets drill," course text just after Project
   9's section). Noted in passing: the parent repo's latest commit at the
   time (`1246dce`, a different git identity `NaimalInspect13
   <n.salahuddin@scopeinspectapp.com>` — the same "concurrent session/tool"
   pattern already documented in session-03) was titled "Add session
   summary for session 5" but its actual diff only added
   `.claude/settings.local.json` (a benign MCP permission entry) — no
   session-05 file existed. Flagged as odd but not blocking; this file is
   the real session-05.
2. **Plan mode.** Asked the user one clarifying question: since the course's
   drill-section intro says the three drills (9, 10, 11) run "in a
   throwaway repository" (singular — possibly meant to be shared), should
   Project 10 reuse `project-9-rehearse-routine` or get its own repo? User
   chose a new dedicated repo, `project-10-secrets-drill`, matching the
   per-project convention.
3. Ran a Plan subagent to work out exact file contents (dummy secret
   format, prompts, README/CLAUDE.md templates), reviewed the result, and
   caught/fixed a design flaw before finalizing: the agent's draft had
   both runs push to the same branch name (`claude/secret-check`), which
   would let run 2 silently overwrite run 1's evidence unless the user
   paused mid-drill to report back before touching the dashboard. Fixed by
   giving each run its own branch (`claude/secret-check-1` /
   `claude/secret-check-2`), so both runs can be fired back-to-back like
   Project 9, and evidence persists independently either way. Wrote and
   got approval on the final plan (overwriting the prior Project-9 plan
   file at `~/.claude/plans/now-we-need-to-golden-wall.md`).
4. **Implementation** (assistant did this directly):
   - Scaffolded `project-10-secrets-drill/`: `.gitignore` (excludes
     `.env`), `.env.example`, `CLAUDE.md` (push-override, matching
     projects 5/6/9's pattern), `README.md`, then
     `routine-prompt-run-1.md` (reads `DEMO_API_TOKEN` from a `.env` file,
     expected to fail) and `routine-prompt-run-2.md` (surgical diff:
     reads it from the environment instead, with the appendix's exact
     recommended line) — confirmed via `diff` that only the sourcing
     clause and branch number changed between the two. Created a local,
     untracked `.env` with the real dummy value
     (`DEMO_API_TOKEN=demo-token-abc123`); confirmed with `git status`
     that it never shows as trackable.
   - `gh repo create project-10-secrets-drill --public --source=.
     --remote=origin`, pushed `main`, verified with `git ls-remote`.
   - Updated the parent repo: `.gitignore`, new pointer stub
     `project-10-secrets-drill-docs/README.md`, root `README.md` (row 10,
     renamed/extended "own repo" section). Committed locally, **not
     pushed**.
   - Handed the user the literal firing instructions and stopped, per the
     established rule that the user fires both Routine runs themselves.
5. **User fired run 1**, which succeeded exactly as designed — confirmed
   independently (before the user even reported back) by fetching
   `origin/claude/secret-check-1` directly: `secret-check-result.txt`
   read `DEMO_API_TOKEN NOT FOUND`.
6. **Run 2 hit a real bug the assistant introduced.** The Routine found
   `DEMO_API_TOKEN` in the environment (proving the fix itself worked) but
   *refused* to write/push the result, because `CLAUDE.md`'s wording —
   "never paste its value into any file, commit message, or PR" — directly
   contradicted `routine-prompt-run-2.md`'s explicit instruction to write
   the dummy token into `secret-check-result.txt` and push it. The Routine
   correctly treated the checked-in repo policy as authoritative over the
   scheduled task's instructions (the right instinct for an unattended run
   facing a policy conflict) and declined rather than silently overriding
   it — it created no branch and pushed nothing, then reported the
   conflict back to the user.
7. **Root-caused and fixed**: the `CLAUDE.md` rule had been written too
   broadly — intended to stop a *real* credential from ever being
   committed (already fully handled by `.gitignore` alone), but it didn't
   distinguish that from the drill's own designed mechanism of writing a
   fully fake, zero-sensitivity dummy value into a throwaway result file
   as proof. Rewrote `CLAUDE.md` to separate the two clearly: never commit
   the actual `.env` file, but writing `DEMO_API_TOKEN`'s value into
   `secret-check-result.txt` is explicitly sanctioned, expected evidence.
   Committed and pushed the fix directly (push allowed in this repo per
   its own `CLAUDE.md`).
8. **User re-fired run 2** against the corrected repo; it succeeded.
   Independently verified by fetching `origin/claude/secret-check-2`
   directly: `secret-check-result.txt` read
   `DEMO_API_TOKEN=demo-token-abc123`, matching the known dummy value
   exactly.
9. User filled in the repo's `README.md` `## Proof` section themselves
   (both transcript links, both results, and their own one-sentence A2/A4
   lesson) and the assistant diffed (only `## Proof` touched), committed,
   and pushed.

## Status

- **Project 10 is done**, per the course's own done-when criteria: run 1
  failed to find the token (independently verified: `NOT FOUND` on
  `claude/secret-check-1`), run 2 found it via the environment
  (independently verified: correct dummy value on `claude/secret-check-2`),
  and the user has stated the mechanical A2/A4 lesson in their own words
  in the repo's README.
- Notable process finding, worth carrying forward: **an assistant-authored
  `CLAUDE.md` policy can silently conflict with an assistant-authored
  routine prompt** if the policy is worded more broadly than intended.
  When scaffolding future drills that both (a) write project-level policy
  files and (b) write task prompts for an unattended agent to follow,
  cross-check the two against each other before handoff — don't just
  proofread each in isolation.
- Parent repo (`Loop-Engineering-Projects`) has local, unpushed commits
  for Project 10 (`.gitignore`, `README.md`,
  `project-10-secrets-drill-docs/`) — same unpushed state as Project 9's
  parent-repo commit from session 4. User needs to `git push` the parent
  repo when ready.
- `project-10-secrets-drill` is fully pushed and up to date, including
  the `CLAUDE.md` fix and the completed `## Proof` section.

## Next up (resume here)

1. **Push the parent repo.** Two rounds of local-only commits are now
   stacked up (Project 9's and Project 10's `.gitignore`/README/
   pointer-stub changes) — user needs to run `git push` themselves.
2. **Project 11 — Build the two-routine gate** (1-2 hrs, medium-hard, uses
   A3 API trigger / A4 the gate / A6 checklist): Routine A drafts
   something reviewable on a one-off schedule; Routine B has an API
   trigger and does one small follow-up action, fired only by the user's
   own `curl` call after reviewing A's draft. Not yet scoped/planned —
   next logical project in sequence.
3. **Project 12 — Build a dreaming loop** (capstone): still blocked on
   Project 8 (or Project 3) accumulating enough real, dated log history
   for a genuine repeated failure to exist for the dreaming loop to catch.
   Not yet scoped/planned.
4. Carried over, unresolved since session 3 (not touched this session):
   - Project 4's `demo-bad-fix` half still not run/confirmed.
   - Project 8 (`Morning-Maintenance-Loop`) still has only one day of
     runs; done-when needs a full unattended week.
   - Projects 1, 2, 6, 7 still need live re-verification against the
     top-level README's "done" claims (Project 6's PR review-comment
     authorship in particular).

## Environment notes worth remembering

- Confirmed again this session: the parent repo has a second active git
  identity (`NaimalInspect13 <n.salahuddin@scopeinspectapp.com>`) making
  commits concurrently with this session's own work — same pattern
  documented in session 3. This time it produced a commit with a
  misleading message ("session 5 summary") whose actual diff was
  unrelated (`.claude/settings.local.json`). Not harmful, but worth a
  quick `git log --format='%an <%ae> %s'` scan at the start of a session
  to catch mismatched messages/diffs before trusting recent history at
  face value.
- The `claude.ai/code/session_...` transcript-URL-403-on-WebFetch and
  "verify Routine behavior via `git fetch` + reading the pushed branch
  directly" techniques from session 4 both held up again this session,
  including for catching the run-2 CLAUDE.md conflict before the user
  even had to explain what went wrong in detail.
