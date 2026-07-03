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

# Collision guard (WO1 Task 3, 2026-07-02): no automation through live surgery.
# The 18:52 Jul-2 fetch landed mid-F-13-fix and had to be hand-separated into
# its own commit; the cron now stands down when a PAUSE file exists or the
# working tree is dirty (git status --porcelain non-empty), and says so in the
# log. The skipped fetch self-heals the next day.
if [ -f "$PROJECT/PAUSE" ]; then
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: dirty-tree"
  exit 0
fi

echo "=== [price-refresh] $(date '+%Y-%m-%d %H:%M:%S')"
./.venv/bin/python -m crude_tanker_fv.price_refresh
echo "=== [price-refresh] EXIT CODE $?"
