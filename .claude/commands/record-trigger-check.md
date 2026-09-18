---
description: Record an agent-drafted trigger check (decisions/trigger_check_<card>_<due>.draft.md) as the owner's word — onto the card and into the decisions record — then commit and push
argument-hint: <card> <due> [hold | fired | reweight]
allowed-tools: Bash(git mv *), Bash(git add *), Bash(git commit *), Bash(git status*), Bash(git log*), Bash(git push origin main), Bash(PYTHONPATH=src .venv/bin/python -m pytest *)
---

Record the Thursday task's draft for `$1` (due `$2`). The draft is agent-assembled and unverified;
this command is where the owner's word enters. The owner is in the chat: the disposition is theirs
(the optional third argument, else the draft's proposal, confirmed in one line).

1. Read `decisions/trigger_check_$1_$2.draft.md` in full. Refuse to record a draft with no
   `## Verification` section, or whose data-gaps list carries a "correction MAY be owed" line the
   owner has not ruled on (rule on it first: annotate the prior record with a dated supersession
   note, never a silent edit).
2. `git mv` the draft to the record name the card's comments use — for `crude_geopolitics_weekly`
   that is `decisions/geopolitics_weekly_check_$2.md`; otherwise `decisions/$1_check_$2.md`.
   Replace the `**DRAFT — …**` banner with `**Recorded <today> by the owner — disposition:
   <hold | fired | reweight>.**` and delete the `## Ready to paste` section once its text is on the
   card. Everything else stays as drafted; owner overrides are appended, dated, not edited in.
3. The card (`inputs/reweight_triggers.yaml`), per the disposition:
   - hold: paste the draft's `due:` re-arm comment (due + 7 days, same weekday) and status-line note.
   - fired: `status: fired`, add `fired: <today>` (the page identity; test-enforced), keep `due:`.
   - reweight: as for hold, plus the pre-registered proposal per the card's `action` and a fork in
     `inputs/forks.yaml` (kind per the 2026-09-10 policy); the reweight itself never lands here.
4. `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_refresh.py tests/test_notify.py tests/test_sentinel.py`
   must be green (the register guards: a fired card carries `fired:`, a re-armed one does not).
5. `git add` the record, the card (and the fork file if any); `git commit` with the subject
   `trigger-check record: $1 $2 - <disposition>`; then `git push origin main` (the merge-your-own
   rule, 2026-09-18). Report the commit hash and the next due date.
