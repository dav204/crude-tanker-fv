---
description: Scaffold YAML stubs, test file, and decision log for a new ticker — removes the blank-page problem
argument-hint: <TICKER> --sector <s> [--quarter Y-Qn] [--dry-run]
allowed-tools: Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.add_ticker *)
---

Scaffold a new ticker onto the watchlist (METHODOLOGY §8.1, CLAUDE.md
"Onboarding a new ticker"). Creates four input YAMLs from canonical
`_template.yaml` files, a test stub (skipped until you remove the marker),
and a decision log entry. Appends a watchlist row with FIXME markers.

What this does NOT do:
- Pull real data — that's the user / next-agent step.
- Run the pipeline.
- Land a new sector in `scenario_inputs.yaml` (methodology §11.x must
  come first; the scaffold warns if the sector doesn't exist yet).

Workflow after scaffolding (printed in next-steps banner):
1. Pull the latest 6-K / 20-F / press release.
2. Fill in the four YAMLs + watchlist FIXME values.
3. Remove `pytest.mark.skip` from the new test file.
4. Run the pipeline + `/reconcile <TICKER>`.

!`PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.add_ticker $ARGUMENTS`
