# Project 2 — Make the Tests Pass, Then Stop

**Concept:** 5, conditional heartbeat (run-until-done) + Concept 11, maker-checker
**Difficulty:** easy to medium · 30-45 min

## Goal
Keep working until the tests pass — but let a *command* (the test runner),
not the agent, decide when the work is done. Cap it at a small number of
tries so a broken loop can't run forever.

## Files
- `utils.py` — three tiny functions (`add`, `is_palindrome`, `factorial`),
  each with one deliberate bug.
- `test_utils.py` — pytest tests that currently fail against those bugs.
- `.venv/` — project-local virtualenv with pytest installed (gitignored).

## The bugs (don't peek if you want the loop to find them itself)
- `add`: subtracts instead of adding.
- `is_palindrome`: doesn't normalize case, so `"RaceCar"` fails.
- `factorial`: returns 0 for `factorial(0)` instead of 1.

## Checker command
```
.venv/bin/pytest -q
```
Exit code 0 = pass. Non-zero = fail. This exit code is the maker-checker
split in action: the agent doesn't get to decide "looks good to me," the
test runner does.

## Done when
- [ ] The loop stops because `pytest` actually exits 0 — not because it hit
      the try cap.
- [ ] If it keeps hitting the cap instead, that's the lesson: the stop
      condition or the prompt needs work, not a higher cap.
