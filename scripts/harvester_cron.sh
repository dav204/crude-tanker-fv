#!/bin/sh
# Weekly broker-marks harvester (WO2 1.3) — crawls the free mirrors
# (hellenicshippingnews + capitallink) for the current quarter's broker
# weeklies via the vendored shipping_harvester. Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.harvester.plist (Saturday 09:00,
# after the 08:00 news-pull).
#
# Runs ONLY on .venv310 (the harvester needs 3.10+; never the engine venv) and
# ONLY inside shipping_harvester/ (its DATA_ROOT is cwd-relative). Staging-only
# writer (invariant 3): everything lands in gitignored data/ — PAUSE applies,
# no dirty-tree guard. Politeness is the package's own policy (2s/host,
# robots.txt respected); a weekly top-up crawls a few listing pages only.

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"

cd "$PROJECT"

JOB=harvester
. "$(dirname "$0")/cron_lib.sh"

if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

year=$(date +%Y)
month=$(date +%m)
case "$month" in
  01|02|03) q=1 ;;
  04|05|06) q=2 ;;
  07|08|09) q=3 ;;
  *)        q=4 ;;
esac
since="${year}Q${q}"
if [ "$q" -eq 4 ]; then
  until="$((year + 1))Q1"
else
  until="${year}Q$((q + 1))"
fi

echo "=== [harvester] $(date '+%Y-%m-%d %H:%M:%S') crawl ${since}..${until}"
cd "$PROJECT/shipping_harvester"
PYTHONPATH=. PYTHONUNBUFFERED=1 "$PROJECT/.venv310/bin/python" \
  -m shipping_harvester.cli run --since "$since" --until "$until" \
  --max-pages 4 --capitallink
CRON_OUTCOME=ok
echo "=== [harvester] done"
