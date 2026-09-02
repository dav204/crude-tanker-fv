#!/bin/sh
# Weekly news-pull runner — chains the existing scanners over whatever the
# week's Rocket.Chat ingest delivered. Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.news-pull.plist (Saturday 08:00,
# after Friday's Shipping Daily has arrived via the 07:00 daily RC ingest).
#
# Chain: RC incremental ingest -> pareto_archive --build-manifest -> sp_scan (prints)
#        -> ffa_ocr (+ --staleness)
#
# /bin/sh + PAUSE-guarded + root-override (WO2 1.1). Staging-only writer
# (invariant 3): PAUSE applies, the dirty-tree guard does NOT — the weekly
# harvest must not silently vanish because a reconciliation left the tree
# dirty overnight.
#
# Writes ONLY automation-writable trees (raw archives under inputs/, scan
# cursors, outputs/ review queues) — never a pipeline-loaded YAML. Promotion
# of anything it surfaces is human-only.
#
# Secrets live in ~/.config/crude-tanker-fv.env (chmod 600).

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"
SECRETS="${HOME}/.config/crude-tanker-fv.env"
PY="${PROJECT}/.venv/bin/python"

if [ -f "$SECRETS" ]; then
  # shellcheck disable=SC1090
  . "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=news-pull
. "$(dirname "$0")/cron_lib.sh"

cron_require_network sec.gov

if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

step() {
  echo "=== [news-pull] $(date '+%Y-%m-%d %H:%M:%S') $1"
}

# Composes with cron_lib's heartbeat (traps don't stack — one trap, two duties).
trap 'rc=$?; echo "=== [news-pull] EXIT CODE ${rc} at step: ${CURRENT_STEP:-unknown}"; CRON_NOTE="step=${CURRENT_STEP:-unknown}"; cron_exit $rc' EXIT

CURRENT_STEP="rocketchat ingest"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.ingest_rocketchat

# Full manifest rebuild BEFORE the scan (reordered 2026-09-02 — it ran after).
CURRENT_STEP="pareto_archive --build-manifest"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.pareto_archive --build-manifest

CURRENT_STEP="sp_scan (S&P print scan, incremental)"
step "$CURRENT_STEP"
"$PY" -m crude_tanker_fv.sp_scan

# The linked-report harvest (sp_scan --links -> fetch_links) was REMOVED from the
# weekly chain 2026-09-02 (prune ledger row 6): one citation ever, 192 MB of unread
# PDFs. Both modules stay for on-demand onboarding use (fetch_links is ask-tier).

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
CRON_OUTCOME=ok
step "chain complete — review queues: outputs/sp_print_candidates.md, outputs/ffa_ocr_queue.md"
