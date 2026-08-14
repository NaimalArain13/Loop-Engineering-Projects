# Project 6 — The Doorbell Loop

*Difficulty: medium · Uses: Concept 7 (event-driven), Concept 10
(connectors).*

A loop that reacts to a pull request, with no prompt typed.

## Repo

The working loop — code, skill, and history — lives in its own repo, not
this folder:

**https://github.com/NaimalArain13/project-6-doorbell-loop**

## Build

The repo reviews its own pull requests: a Claude Code Routine with a
GitHub pull-request trigger fires on every PR, unprompted. A PR containing
one deliberately planted bug (an off-by-one / missing null check) is opened
against the repo to test it.

## Done when

The PR gets a review nobody asked for, and the review flags the planted
bug. Pushing a follow-up commit re-fires the loop through the `synchronize`
event — the event heartbeat working a second time. Together with Projects
1–3, this completes all four heartbeats: in-session, conditional,
scheduled, and event-driven.
