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

# THREE venue adapters ride this one row, so ONE outcome word has to describe
# three lanes. Each runs non-fatally and its rc lands in CRON_NOTE; the outcome
# is still `error` if any lane failed (a poller that is down must stay loud),
# but the note now says WHICH — so a flag can never again leave you unable to
# tell whether the 19-name EDGAR lane actually polled.
#
# Caught live 2026-08-16: mfn.se threw `URLError: Connection reset by peer`,
# `set -e` killed the wrapper before CRON_OUTCOME was set, and the job reported
# a bare `outcome=error rc=1 note=` — EDGAR and HKEX had both already succeeded
# and nothing said so. Red-on-a-sibling masking a healthy lane is the inverse of
# the 2026-07-18 camouflage rule, and it trains you to ignore the one flag that
# means a filing channel is blind.
#
# NOT swallowed, deliberately: `|| true` here would make a PERSISTENT outage
# indistinguishable from a quiet week — the silent-watchdog failure this repo
# has already been bitten by. Note also that neither `_fetch` catches URLError
# (only HTTPError), so hkex carries the same exposure; it has simply been lucky.
cron_lane() {
  cron_lane_name=$1
  shift
  # `cmd || var=$?` is the only form that both survives `set -e` AND leaves the
  # real status readable — after a failed `if cmd; then`, `$?` is the IF's
  # status (0), not the command's, which would record every failure as rc0.
  cron_lane_rc=0
  "$@" || cron_lane_rc=$?
  if [ "$cron_lane_rc" -eq 0 ]; then
    CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}${cron_lane_name}=ok"
  else
    CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}${cron_lane_name}=rc${cron_lane_rc}"
    CRON_LANE_FAILED=$((CRON_LANE_FAILED + 1))
    echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') LANE FAILED: ${cron_lane_name} rc=${cron_lane_rc}" >&2
  fi
  return 0
}

CRON_LANE_FAILED=0
cron_lane edgar ./.venv/bin/python -m crude_tanker_fv.edgar_poll
# HKEX light adapter (F-3, 2026-07-14) rides the same hourly row — its own
# 12h off-season cadence + politeness live in the module; same PAUSE gate.
cron_lane hkex ./.venv/bin/python -m crude_tanker_fv.hkex_poll
# Oslo/Euronext issuer channel (2026-08-16) rides the same row for the same
# reasons — and closes the last venue with no filing lane at all. Its absence
# is what hid the BRUT 7/07 demerger, the MPCC 6/25 acquisition + 7/01
# placement, and the CAPT 8/06+8/13 deliveries. Network guard above tests
# sec.gov; mfn.se resolving is not separately gated (one DNS failure mode).
cron_lane newsweb ./.venv/bin/python -m crude_tanker_fv.newsweb_poll

if [ "$CRON_LANE_FAILED" -eq 0 ]; then
  CRON_OUTCOME=ok
else
  CRON_OUTCOME=error
  echo "=== [edgar-poll] ${CRON_LANE_FAILED} lane(s) failed: ${CRON_NOTE}" >&2
fi
echo "=== [edgar-poll] done"
[ "$CRON_LANE_FAILED" -eq 0 ] || exit 1
