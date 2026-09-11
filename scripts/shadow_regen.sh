#!/bin/bash
# SHADOW regen (2026-09-11, the results-landed shadow build): value a name on its DRAFT pair
# without touching the live tree. The owner's 2026-07-03 rule keeps unattended agents at
# drafts only; this script is how a draft gets a number anyway — in a throwaway git worktree
# of HEAD where the drafts are copied over the live files, the pipeline runs, the pair guards
# run, and the name's scorecard row is diffed against the committed surface. Nothing here
# writes to the repo tree or to git.
#
#   scripts/shadow_regen.sh <TICKER> <QUARTER>
#
# Drafts it looks for (committed, tracked — an untracked draft would block auto-land):
#   inputs/balance_sheets/<ticker>_<QUARTER>.yaml.draft   (required)
#   inputs/fleet_manifests/<ticker>.yaml.draft            (optional; else the live manifest)
# Output: a JSON block on stdout (shadow row, committed row, deltas, guard verdicts) between
# SHADOW-JSON-BEGIN / SHADOW-JSON-END lines, plus the guard tails. Exit 0 = ran; 2 = no draft;
# 3 = pipeline failed.
set -u
cd "$(dirname "$0")/.." || exit 1
main="$(pwd)"
ticker="${1:?usage: scripts/shadow_regen.sh <TICKER> <QUARTER>}"
quarter="${2:?usage: scripts/shadow_regen.sh <TICKER> <QUARTER>}"
lc="$(echo "$ticker" | tr '[:upper:]' '[:lower:]')"
bs_draft="inputs/balance_sheets/${lc}_${quarter}.yaml.draft"
fm_draft="inputs/fleet_manifests/${lc}.yaml.draft"
[ -f "$bs_draft" ] || { echo "[shadow] NO DRAFT: $bs_draft"; exit 2; }
head_sha="$(git rev-parse --short HEAD)"
wt="$(mktemp -d /tmp/crude-fv-shadow.XXXXXX)"
cleanup() { git worktree remove --force "$wt" >/dev/null 2>&1; rm -rf "$wt"; }
trap cleanup EXIT
git worktree add --detach "$wt" HEAD >/dev/null 2>&1 || { echo "[shadow] worktree add failed"; exit 1; }
cp "$bs_draft" "$wt/inputs/balance_sheets/${lc}_${quarter}.yaml"
fm_used="live"
if [ -f "$fm_draft" ]; then cp "$fm_draft" "$wt/inputs/fleet_manifests/${lc}.yaml"; fm_used="draft"; fi
echo "[shadow] HEAD $head_sha | sheet draft: $bs_draft | manifest: $fm_used | worktree $wt"
( cd "$wt" && PYTHONPATH="$wt/src" "$main/.venv/bin/python" -m crude_tanker_fv.pipeline "$quarter" ) >"$wt/shadow_pipeline.log" 2>&1 \
  || { echo "[shadow] PIPELINE FAILED — tail:"; tail -20 "$wt/shadow_pipeline.log"; exit 3; }
grep -E "STALE-PRICE|STROBE|Traceback|Error" "$wt/shadow_pipeline.log" | sort -u | cut -c1-140 | sed 's/^/[shadow] pipeline: /'
guards="$wt/shadow_guards.log"
( cd "$wt" && PYTHONPATH="$wt/src" "$main/.venv/bin/python" -m pytest -q -p no:cacheprovider \
    tests/test_quarter_coherence.py tests/test_manifest_provenance.py tests/test_scrubber_provenance.py \
    -k "$ticker or $lc or coherence or provenance" ) >"$guards" 2>&1
echo "[shadow] guards: $(tail -1 "$guards")"
grep -E "^FAILED" "$guards" | cut -c1-160 | sed 's/^/[shadow] /'
PYTHONPATH="$main/src" "$main/.venv/bin/python" - "$ticker" "$main/outputs/book_scorecard.json" "$wt/outputs/book_scorecard.json" "$guards" "$head_sha" "$fm_used" <<'EOF'
import json, sys
ticker, live_p, shadow_p, guards_p, head, fm_used = sys.argv[1:7]

def row(path):
    d = json.load(open(path))
    rows = d.get("names") or d.get("rows") or d.get("book") or d
    if isinstance(rows, dict):
        return rows.get(ticker) or {}
    return next((x for x in rows if isinstance(x, dict) and x.get("ticker") == ticker), {})

live, shadow = row(live_p), row(shadow_p)
deltas = {}
for k in sorted(set(live) | set(shadow)):
    a, b = live.get(k), shadow.get(k)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool):
        if a != b:
            deltas[k] = {"live": a, "shadow": b, "delta": b - a}
    elif a != b:
        deltas[k] = {"live": a, "shadow": b}
guards = open(guards_p).read().splitlines()
out = {"ticker": ticker, "head": head, "manifest_used": fm_used,
       "guards_tail": guards[-1] if guards else "", "guard_failures": [g for g in guards if g.startswith("FAILED")],
       "live": live, "shadow": shadow, "deltas": deltas}
print("SHADOW-JSON-BEGIN"); print(json.dumps(out, indent=1, default=str)); print("SHADOW-JSON-END")
EOF
