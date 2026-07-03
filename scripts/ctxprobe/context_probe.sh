#!/bin/sh
# Execution-context probe (WO2 0.5) — THROWAWAY 7-day harness, not part of the
# standing automation. One line per firing to ~/ctxprobe.log answering: does
# launchd run our jobs when the lid is closed / another family profile is
# switched in / nobody is logged in / just after wake — and can those runs see
# the network and the secrets file? The owner checklist + expected semantics
# live in decisions/ctxprobe_checklist_2026-07-03.md. Uninstall after the
# window; the measured-semantics note is committed BEFORE schedules freeze.
# Every probe degrades gracefully off-macOS so the smoke test runs in CI.

LOG="${CTXPROBE_LOG:-$HOME/ctxprobe.log}"
ts=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
case "${XPC_SERVICE_NAME:-}" in
  com.crude-tanker-fv.*) initiator="$XPC_SERVICE_NAME" ;;
  *) initiator=manual ;;   # interactive shells carry XPC_SERVICE_NAME=0
esac
console_user=$(stat -f%Su /dev/console 2>/dev/null || echo unknown)
me=$(id -un)
if [ "$console_user" = "$me" ]; then switched_in=yes; else switched_in=no; fi
wake=$(sysctl -n kern.waketime 2>/dev/null | sed 's/.*sec = \([0-9]*\),.*/\1/')
now_epoch=$(date +%s)
secs_since_wake=$(( now_epoch - ${wake:-$now_epoch} ))
if route -n get default >/dev/null 2>&1; then default_route=yes; else default_route=no; fi
if curl -m 3 -sI https://github.com -o /dev/null 2>/dev/null; then http_ok=yes; else http_ok=no; fi
if [ -r "$HOME/.config/crude-tanker-fv.env" ]; then secrets_readable=yes; else secrets_readable=no; fi
power=$(pmset -g ps 2>/dev/null | head -1 | sed "s/Now drawing from '\(.*\)'/\1/")

printf '%s initiator=%s console_user=%s me=%s switched_in=%s secs_since_wake=%s default_route=%s http_ok=%s secrets_readable=%s power="%s"\n' \
  "$ts" "$initiator" "$console_user" "$me" "$switched_in" "$secs_since_wake" \
  "$default_route" "$http_ok" "$secrets_readable" "$power" >> "$LOG"
