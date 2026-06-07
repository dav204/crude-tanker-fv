---
description: Tool↔broker NAV reconciliation (sanity / calibration-lock / drift) for one or many tickers
argument-hint: <TICKER> | --all | --sector <s> | --calibration-lock <s> [--verbose]
allowed-tools: Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.reconcile *)
---

Run the reconcile diagnostic — surfaces tool↔broker NAV gap per ticker,
flags SANITY failures (gap >±50% = bug, not a call), reports drift since
the last reconcile, and offers a calibration-lock mode for new sectors.

Background (full detail in CLAUDE.md "Reconciliation has three jobs"):

- **SANITY** — gap within ±50%; fails are bugs.
- **CALIBRATION** — `--calibration-lock <sector>` reports the v1 lock hit
  rate (≥70%/±10% for new sectors, ≥80%/±5% for existing).
- **DRIFT** — every reconcile compares against `state/last_reconcile.json`
  and alerts on >2pp moves.

The tool produces independent NAV; wide spreads documented in METHODOLOGY
§6 are calls, not failures. Do not "fix" them by tweaking marks.

!`PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.reconcile $ARGUMENTS`
