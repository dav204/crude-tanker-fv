#!/bin/zsh
# Daily watchlist price refresh (Yahoo chart API -> prices_daily.yaml).
# Invoked by launchd via ~/Library/LaunchAgents/com.crude-tanker-fv.price-refresh.plist
# (18:30 local, after the NYSE close). Writes ONLY the automation-writable
# inputs/market_data/prices_daily.yaml — never watchlist.yaml.

set -eu

PROJECT="${HOME}/Projects/crude-tanker-fv"

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

echo "=== [price-refresh] $(date '+%Y-%m-%d %H:%M:%S')"
./.venv/bin/python -m crude_tanker_fv.price_refresh
echo "=== [price-refresh] EXIT CODE $?"
