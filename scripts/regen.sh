#!/bin/bash
# The ONE way to regenerate the decision surface (2026-09-10). Three times this quarter a
# surface shipped with a stale weight-family sidecar (9/02, 9/07, 9/10) because the five
# sidecar scripts are a separate step from the pipeline and were skipped after an input
# change. This script makes the sequence a single command:
#   1. refuse a dirty determinant tree (src/ + inputs/) — the stamp would read -dirty;
#   2. re-run the five weight-family sidecars if scenario_inputs.yaml is newer than the
#      family sidecar (or always, with --sidecars);
#   3. run the pipeline for the quarter;
#   4. run the outputs-hygiene guard and print the stamp + family status.
# It writes nothing to git. Usage: scripts/regen.sh <QUARTER> [--sidecars]
set -euo pipefail
cd "$(dirname "$0")/.." || exit 1
quarter="${1:?usage: scripts/regen.sh <QUARTER> [--sidecars]}"
force="${2:-}"
if git status --porcelain | grep -qE "^( M|\?\?) (src|inputs)/"; then
  echo "[regen] REFUSED: determinants dirty — commit or stash src/ and inputs/ first:"
  git status --porcelain | grep -E "^( M|\?\?) (src|inputs)/"
  exit 3
fi
need=0
[ "$force" = "--sidecars" ] && need=1
family=outputs/crude_weight_robustness.md
if [ ! -f "$family" ] || [ inputs/scenario_inputs.yaml -nt "$family" ]; then need=1; fi
if ! PYTHONPATH=src ./.venv/bin/python -c 'from crude_tanker_fv.scorecard import weight_family_basis; import sys; sys.exit(0 if weight_family_basis()["status"] == "current" else 1)'; then need=1; fi
if [ "$need" -eq 1 ]; then
  for s in crude_weight_robustness dry_bulk_weight_comparison lng_weight_comparison lpg_weight_comparison product_weight_comparison; do
    PYTHONPATH=src ./.venv/bin/python "scripts/$s.py" >/dev/null 2>&1 && echo "[regen] sidecar ok: $s" || { echo "[regen] SIDECAR FAILED: $s"; exit 4; }
  done
else
  echo "[regen] sidecars current (scenario_inputs.yaml not newer than $family)"
fi
PYTHONPATH=src ./.venv/bin/python -m crude_tanker_fv.pipeline "$quarter"
PYTHONPATH=src ./.venv/bin/python - <<'EOF'
import json
d = json.load(open("outputs/book_scorecard.json"))
print("[regen] stamp:", d.get("source_commit"), "| weight-family:", (d.get("weight_family_basis") or {}).get("status"))
EOF
PYTHONPATH=src ./.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_outputs_hygiene.py 2>&1 | tail -1 | sed 's/^/[regen] hygiene: /'
