# Project 10 — The Secrets Drill

*Difficulty: easy to medium · Uses: A4 (secrets), A2 (the environment).*

Fail the `.env` way once, on purpose, so you never do it by accident.

## Repo

The routine, its throwaway repo, and both run transcripts live in their
own repo, not this folder:

**https://github.com/NaimalArain13/project-10-secrets-drill**

## Build

A Claude Code Routine reads a dummy secret (`DEMO_API_TOKEN`) and writes
proof of what it found to a branch. First fired with the token in a
gitignored `.env` file — expected to fail, because the fresh cloud clone
never contains it. Then re-fired with the token moved to the Routine's
environment-variables panel and one line added to the prompt:
*"credentials are available as environment variables; do not look for a
`.env` file."*

## Done when

The second run reads the token from the environment, and the mechanical
reason the first run could not — gitignored files never reach GitHub, so
the fresh cloud clone never contains them — is stated in the repo's own
README, in the user's own words.
