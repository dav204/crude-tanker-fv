#!/bin/sh
# Hourly EDGAR filings poller (WO2 2.2). Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.edgar-poll.plist.
#
# The poller itself enforces cadence (invariant 5): names inside an open
# earnings window poll every run; off-season names only when their last poll
# is >12h old — so the hourly schedule costs ~2 polls/day/name off-season.
# Staging-only writer (invariant 3): PAUSE applies, NO dirty-tree guard —
# filing detection must not blind during a dirty reconciliation week.
# Politeness lives in the module (spacing, conditional GETs, backoff, cap).

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=edgar-poll
. "$(dirname "$0")/cron_lib.sh"

cron_require_network sec.gov

if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

echo "=== [edgar-poll] $(date '+%Y-%m-%d %H:%M:%S')"
./.venv/bin/python -m crude_tanker_fv.edgar_poll
# HKEX light adapter (F-3, 2026-07-14) rides the same hourly row — its own
# 12h off-season cadence + politeness live in the module; same PAUSE gate.
./.venv/bin/python -m crude_tanker_fv.hkex_poll
# Oslo/Euronext issuer channel (2026-08-16) rides the same row for the same
# reasons — and closes the last venue with no filing lane at all. Its absence
# is what hid the BRUT 7/07 demerger, the MPCC 6/25 acquisition + 7/01
# placement, and the CAPT 8/06+8/13 deliveries. Network guard above tests
# sec.gov; mfn.se resolving is not separately gated (one DNS failure mode).
./.venv/bin/python -m crude_tanker_fv.newsweb_poll
CRON_OUTCOME=ok
echo "=== [edgar-poll] done"
