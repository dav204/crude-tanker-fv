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

# launchd PATH is bare (/usr/bin:/bin:...) — Homebrew tools are invisible to
# cron jobs. Caught live 2026-07-04: the Saturday news-pull died at ffa_ocr
# on FileNotFoundError('tesseract') while every interactive run worked. One
# fix here covers every wrapper.
PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
export PATH

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

# Wake-time DNS race (observed 9x in edgar_poll.err through 2026-07-21, plus
# price-refresh 7/17+7/21 and rocketchat-ingest 7/17: launchd fires the first
# post-wake run before name resolution is up -> URLError Errno 8, rc=1, a
# FETCH-FAILED page for a self-healing transient). Fetch wrappers call this
# BEFORE their python: waits up to ~30s for DNS; on persistent failure stands
# down as skipped-no-network rc=0 (the next scheduled run covers it) — the
# same live-job-standing-down semantics as skipped-paused.
cron_require_network() {
  crn_host="${1:-sec.gov}"
  crn_tries=0
  # write-nothing resolvers only: python3 would create $HOME/Library caches
  # (dirties the tmp-repo test harness whose HOME is the repo).
  while [ $crn_tries -lt 6 ]; do
    if command -v dscacheutil >/dev/null 2>&1; then
      dscacheutil -q host -a name "$crn_host" 2>/dev/null | grep -q ip_address && return 0
    elif command -v getent >/dev/null 2>&1; then
      getent hosts "$crn_host" >/dev/null 2>&1 && return 0
    fi
    crn_tries=$((crn_tries + 1))
    sleep 5
  done
  CRON_OUTCOME=skipped-no-network
  CRON_NOTE="dns-unresolvable:${crn_host}-after-30s"
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: network not up (${crn_host} unresolvable after ~30s)"
  exit 0
}

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
