#!/bin/sh
# Daily watchlist price refresh (Yahoo chart API -> prices_daily.yaml).
# Invoked by launchd via ~/Library/LaunchAgents/com.crude-tanker-fv.price-refresh.plist
# (18:30 local, after the NYSE close). Writes ONLY the automation-writable
# inputs/market_data/prices_daily.yaml — never watchlist.yaml.

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=price-refresh
. "$(dirname "$0")/cron_lib.sh"

# Collision guard (WO1 Task 3, 2026-07-02): no automation through live surgery.
# The 18:52 Jul-2 fetch landed mid-F-13-fix and had to be hand-separated into
# its own commit. Re-scoped 2026-07-06 (owner-approved): dirt confined to the
# automation-drift list (scripts/drift_files.txt — the daily RC ingest writes
# tracked files every morning) is ROUTINE, not surgery; the guard starved the
# price fetch two nights running behind it. Skip only on non-drift dirt.
if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi
non_drift=""
while IFS= read -r line; do
  [ -z "$line" ] && continue
  p=${line#???}
  if ! grep -qxF "$p" "$(dirname "$0")/drift_files.txt" 2>/dev/null; then
    non_drift="$p"
    break
  fi
done <<PORCELAIN
$(git status --porcelain 2>/dev/null)
PORCELAIN
if [ -n "$non_drift" ]; then
  CRON_OUTCOME=skipped-dirty
  CRON_NOTE="non_drift=$non_drift"
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: dirty-tree ($non_drift)"
  exit 0
fi

echo "=== [price-refresh] $(date '+%Y-%m-%d %H:%M:%S')"
./.venv/bin/python -m crude_tanker_fv.price_refresh
CRON_OUTCOME=ok
echo "=== [price-refresh] EXIT CODE $?"
