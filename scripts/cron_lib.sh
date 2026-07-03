#!/bin/sh
# Shared cron heartbeat + run ledger (WO2 0.2; design invariants 1 & 7).
# Source AFTER JOB and PROJECT are set, from the wrapper's own directory
# (the tmp-repo test harness points PROJECT elsewhere):
#     JOB=price-refresh
#     . "$(dirname "$0")/cron_lib.sh"
#
# The EXIT trap writes state/heartbeat/$JOB (one overwritten line — including
# on SKIP: a skip is a live job standing down, not a dead one) and appends an
# initiator-stamped line to state/automation_runs.log: launchd runs carry
# XPC_SERVICE_NAME; anything else records manual:<user>@<tty> — the
# no-human-fetches instrument the WO2 acceptance compiles. A wrapper may
# pre-set CRON_INITIATOR (the Saturday MB Gmail step uses session:mb-batch,
# R-7). Sentinel job-health reads ONLY heartbeats, never these wrappers' logs.
#
# Wrappers set CRON_OUTCOME before exiting: ok | flags | skipped-paused |
# skipped-dirty. The default is error — an unmanaged exit IS an error.

CRON_START_TS=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
if [ -z "${CRON_INITIATOR:-}" ]; then
  # Only OUR labels count as launchd: interactive macOS shells carry
  # XPC_SERVICE_NAME=0 (Terminal sets application.* / 0) — caught live 2026-07-03
  # by the ctxprobe; a bare $XPC_SERVICE_NAME test would stamp manual runs "0".
  case "${XPC_SERVICE_NAME:-}" in
    com.crude-tanker-fv.*)
      CRON_INITIATOR="$XPC_SERVICE_NAME" ;;
    *)
      cron_tty=$(tty 2>/dev/null || echo notty)
      case "$cron_tty" in /dev/*) cron_tty=${cron_tty#/dev/} ;; *) cron_tty=notty ;; esac
      CRON_INITIATOR="manual:$(id -un)@${cron_tty}" ;;
  esac
fi
CRON_OUTCOME="error"
CRON_NOTE=""

cron_exit() {
  cron_rc=${1:-$?}
  mkdir -p "$PROJECT/state/heartbeat"
  printf 'ts=%s job=%s outcome=%s rc=%s note=%s\n' \
    "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$JOB" "$CRON_OUTCOME" "$cron_rc" "$CRON_NOTE" \
    > "$PROJECT/state/heartbeat/$JOB"
  printf '%s job=%s initiator=%s outcome=%s rc=%s\n' \
    "$CRON_START_TS" "$JOB" "$CRON_INITIATOR" "$CRON_OUTCOME" "$cron_rc" \
    >> "$PROJECT/state/automation_runs.log"
}
trap 'cron_exit $?' EXIT
