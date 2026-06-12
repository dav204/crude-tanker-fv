#!/bin/zsh
# Weekly news-pull runner — chains the existing scanners over whatever the
# week's Rocket.Chat ingest delivered. Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.news-pull.plist (Saturday 08:00,
# after Friday's Shipping Daily has arrived via the 07:00 daily RC ingest).
#
# Chain: RC incremental ingest -> sp_scan (prints) -> sp_scan --links
#        -> fetch_links -> pareto_archive --build-manifest
#
# Writes ONLY automation-writable trees (raw archives under inputs/, scan
# cursors, outputs/ review queues) — never a pipeline-loaded YAML. Promotion
# of anything it surfaces is human-only.
#
# Secrets live in ~/.config/crude-tanker-fv.env (chmod 600).

set -eu

PROJECT="${HOME}/Projects/crude-tanker-fv"
SECRETS="${HOME}/.config/crude-tanker-fv.env"
PY="${PROJECT}/.venv/bin/python"

if [[ -f "$SECRETS" ]]; then
  # shellcheck disable=SC1090
  source "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

step() {
  echo "=== [news-pull] $(date '+%Y-%m-%d %H:%M:%S') $1"
}

trap 'rc=$?; echo "=== [news-pull] EXIT CODE ${rc} at step: ${CURRENT_STEP:-unknown}"; exit $rc' EXIT

CURRENT_STEP="rocketchat ingest"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.ingest_rocketchat

CURRENT_STEP="sp_scan (S&P print scan, incremental)"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.sp_scan

CURRENT_STEP="sp_scan --links (link inventory)"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.sp_scan --links

CURRENT_STEP="fetch_links (download new linked reports)"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.fetch_links

CURRENT_STEP="pareto_archive --build-manifest"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.pareto_archive --build-manifest

CURRENT_STEP="ffa_ocr (FFA widget scan, incremental)"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.ffa_ocr

CURRENT_STEP="ffa_ocr --staleness (single-source feed alarm)"
step "$CURRENT_STEP"
if ! "$PY" -m crude_tanker_fv.ffa_ocr --staleness; then
  echo "!!! [news-pull] FFA FEED STALE — no parsed widget in >7 days."
  echo "!!! The FFA curve rides ONE poster's screenshot habit; check the"
  echo "!!! Rocket.Chat channel before trusting any FFA-derived input."
fi

CURRENT_STEP="done"
step "chain complete — review queues: outputs/sp_print_candidates.md, outputs/ffa_ocr_queue.md, outputs/pareto_daily_links.json"
