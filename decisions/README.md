# Decision logs

This directory holds one log file per ticker (`{ticker}_log.md`, lowercase) —
the **user-curated** counterpart to the auto-generated delta report.

## How they're populated

Every pipeline run **prepends** a structured "model state" entry to the top of
each ticker's log file (METHODOLOGY §7.8). Existing content below the new
entry is preserved verbatim — the tool never edits or deletes prior content.

The auto-prepended entry captures the model state at the moment of the run:
price, single-point FV, scenario PW FV, NAV/share, position, broker spread,
and (after the first run) deltas vs the previous run with material flags.
Each entry ends with a placeholder:

```
**Decision:** _[pending annotation]_
```

This is your prompt to **annotate**, replacing the placeholder with what you
actually did and why. Most runs will result in "no action" — that's fine,
the log still captures the steady-state context that surrounds your real
decisions.

## How to use them

- After a pipeline run, scan `outputs/delta_report.md` for material moves.
- For each material move (and any non-material name where you took or
  considered action), open the relevant `{ticker}_log.md` and replace the
  pending-annotation line with your decision.
- Keep it terse: "Held — Phase 1 MoU thesis intact, will reassess Q2"
  is enough. The structured model-state context is already captured above
  for free.

## Why this matters

Over a year of entries, the log becomes the feedback loop on your own
decision-making: was the model's TRIM signal predictive? Did the names where
you overrode the model do better or worse? Are there patterns in when you
agree vs disagree with the framework?

The model outputs without this log are scoreless. The log makes them
scoreable.

## File format

Plain markdown. The tool only touches the area between the file header (the
first `---` separator after the intro) and the next existing content. You can
write below entries in any markdown structure — sections, bullet points,
prose — and it will be preserved across all future runs.

## Tracked in git

These files ARE git-tracked (unlike `state/last_run.json`, which is machine-
local). The decision history is durable: each commit captures a moment in
your decision-making record. Treat them as a research journal.
