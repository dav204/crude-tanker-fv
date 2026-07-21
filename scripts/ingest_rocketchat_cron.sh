#!/bin/sh
# Wrapper for the daily Rocket.Chat ingest (Pareto PDFs + FFA screenshots +
# Baltic-indexes time-series). Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.rocketchat-ingest.plist.
#
# /bin/sh + PAUSE-guarded + root-override (WO2 1.1). Guard re-scope
# (invariant 3): this is a STAGING-ONLY writer (gitignored archives, cursors,
# outputs/ queues) — PAUSE applies, the dirty-tree guard does NOT (fetching
# must not stop during a dirty reconciliation week; nothing here touches the
# tracked tree).
#
# Secrets live in ~/.config/crude-tanker-fv.env (chmod 600), expected to set:
#   export ROCKETCHAT_USER_ID=...
#   export ROCKETCHAT_TOKEN=...

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"
SECRETS="${HOME}/.config/crude-tanker-fv.env"

if [ -f "$SECRETS" ]; then
  # shellcheck disable=SC1090
  . "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=rocketchat-ingest
. "$(dirname "$0")/cron_lib.sh"

cron_require_network rc.seekingalpha.com

if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

# Daily Rocket.Chat ingest (Pareto PDFs + FFA screenshots + Baltic indexes).
# Tolerate a non-fatal ingest hiccup (e.g. a transient TLS read) so the scan
# below still runs over whatever dailies did land.
ingest_rc=0
./.venv/bin/python -m crude_tanker_fv.ingest_rocketchat "$@" || ingest_rc=$?

# Incremental S&P print scan over the freshly-ingested dailies — local-only,
# cursor-based. Surfaces prints same-day instead of waiting for the Saturday
# news-pull cron (added 2026-06-21; closes the up-to-a-week scan lag the Jun-20
# run exposed). The linked-report harvest + manifest stay weekly in
# news_pull_cron.sh.
./.venv/bin/python -m crude_tanker_fv.sp_scan

# Daily incremental FFA-widget OCR (WO2 1.1) — same-day curve prints instead
# of Saturday-latency; cursor-based, tolerant like the ingest above.
ocr_rc=0
./.venv/bin/python -m crude_tanker_fv.ffa_ocr || ocr_rc=$?

if [ "$ingest_rc" -eq 0 ]; then
  CRON_OUTCOME=ok
else
  CRON_NOTE="ingest_rc=$ingest_rc ocr_rc=$ocr_rc"
fi
exit "$ingest_rc"
