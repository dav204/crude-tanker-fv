#!/usr/bin/env bash
# Deliberate, cause-required re-ratification of the committed drift-gate baseline.
#
# Reads state/last_run.json (authored by the latest pipeline run) and rewrites
# baselines/reconcile_baseline.yaml with the current EV% / tool NAV / position
# band / k_broker per name, plus meta (ratified_at, ratified_commit=HEAD, cause).
#
# This is the ONLY sanctioned way to move the baseline — never hand-edit the
# numbers. Re-ratify when a drift is real and accepted (Q-refresh, methodology
# change, market move): the cause is recorded in the YAML meta and should head
# the commit message. The script does NOT commit — review the diff first, the
# same human-only discipline as watchlist / FFA-curve promotion.
#
# Usage: scripts/ratify_baseline.sh "<cause>"
set -euo pipefail

cause="${1:-}"
if [[ -z "${cause// }" ]]; then
  echo "usage: scripts/ratify_baseline.sh \"<cause>\"  (cause is mandatory)" >&2
  exit 2
fi

cd "$(dirname "$0")/.."
# drift_gate --ratify also appends the RATIFY_LOG.md row (WO1 Task 4 — the
# producer's page to the governance repo's weekly monitor; kept in Python so
# the row cannot diverge from the ratify that actually happened).
PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.drift_gate --ratify --cause "$cause"

echo
echo "Baseline rewritten (+ RATIFY_LOG.md row). Review the diff, then commit deliberately:"
echo "  git add baselines/reconcile_baseline.yaml RATIFY_LOG.md"
echo "  git commit -m \"baseline: re-ratify drift gate — ${cause}\""
