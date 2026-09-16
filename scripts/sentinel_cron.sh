#!/bin/sh
# Daily read-only sentinel (WO1 V-2/V-3, 2026-07-02): trigger due/overdue,
# input staleness, committed-surface coherence, price basis. Exit 0 = quiet.
# Invoked by launchd via ~/Library/LaunchAgents/com.crude-tanker-fv.sentinel.plist
# (installation is human-only — see the plist in this directory). Changes
# NOTHING beyond one dated line in state/sentinel.log.

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"
SECRETS="${HOME}/.config/crude-tanker-fv.env"

# SMTP creds + healthchecks ping URL (WO2 0.2) — env-only, never in the repo.
if [ -f "$SECRETS" ]; then
  # shellcheck disable=SC1090
  . "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=sentinel
. "$(dirname "$0")/cron_lib.sh"

# PAUSE guard (WO1 Task 3). The dirty-tree case is NOT a skip here (WO2 0.3,
# invariant 3): the sentinel itself detects a dirty tree and runs in META-MODE
# — content checks suspended, heartbeat/digest/ping still fire, DIRTY-TOO-LONG
# pages at 36h (12h in an open earnings window). A dirty reconciliation week
# must not look like death to the dead-man.
if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

echo "=== [sentinel] $(date '+%Y-%m-%d %H:%M:%S')"
rc=0
./.venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log \
  --notify --ping || rc=$?
# rc mapping (2026-09-02, Stage 0): 0 quiet · 2 flags · anything else — including
# 1, python's uncaught-traceback exit — stays the default `error`. Before this,
# rc=1 read as a normal flag day: the 2026-09-01 run died on a YAML ParserError
# in inputs/archive_gaps.yaml and the heartbeat said `outcome=flags`.
case $rc in
  0) CRON_OUTCOME=ok ;;
  2) CRON_OUTCOME=flags ;;
esac
echo "=== [sentinel] EXIT CODE $rc"

# WEEKLY REPORT (2026-09-02) — Saturday only, on the back of the run that already has the
# env sourced and the channel proven. Deliberately NOT a new launchd job: a new plist is an
# owner install, and this needs none. The report is the owner-facing surface that replaces
# reading a 30-flag daily digest; its failure must never fail the sentinel, so it is
# non-fatal and its rc rides the note.
# Called EVERY run, not gated on the weekday: the module decides (weekly_report.is_due).
# A shell `date +%u -eq 6` test was the first cut and it failed on its first real Saturday —
# the Mac was dark 9/05-9/06, launchd coalesced the missed firings into one run on Monday
# 9/07, and the weekday test was false there, so the report skipped and could never catch up.
echo "=== [weekly-report] $(date '+%Y-%m-%d %H:%M:%S')"
report_rc=0
./.venv/bin/python -m crude_tanker_fv.weekly_report --if-due --send || report_rc=$?
[ "$report_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}weekly_report=rc${report_rc}"
echo "=== [weekly-report] EXIT CODE $report_rc"

# Commit the run's own outputs that are NOT on the drift list (2026-09-12): the Saturday weekly
# report and the news digest are written by these jobs, yet every Saturday they sat untracked and
# auto-land refused ("non-drift dirt") until someone committed them by hand — the lane froze on
# 9/12 exactly so. Automation products get committed by the automation; a commit is skipped when
# nothing changed. Never touches inputs/ or decisions/.
echo "=== [commit-outputs] $(date '+%Y-%m-%d %H:%M:%S')"
if git status --porcelain -- outputs/weekly_report_*.md outputs/news_digest_*.md | grep -q .; then
  git add outputs/weekly_report_*.md outputs/news_digest_*.md \
    && git commit -q -m "outputs: weekly report / news digest $(date '+%Y-%m-%d') (cron products, auto-committed)" \
    && echo "[commit-outputs] committed" || { echo "[commit-outputs] FAILED"; CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}commit_outputs=failed"; }
else
  echo "[commit-outputs] nothing to commit"
fi

# Price-leg regen (2026-09-15). The nightly price refresh writes a DETERMINANT
# (inputs/market_data/prices_daily.yaml) and NOTHING regenerated the surface behind it, so
# auto-land's (e) — "determinants changed since the surface <stamp>" — could never pass and the
# committed baseline anchor sat frozen 9/12 through 9/15. Auto-land landed on 9/10 and 9/11 only
# because a chat session happened to regenerate those mornings. This lane runs, unattended, the
# exact 2026-09-11 chain that DID land: price vintage ALONE (df80814) -> residual drift (b357696)
# -> regen (stamp b357696) -> surface + annotations (33aafbf, 1988a4d). The order is load-bearing:
# scripts/regen.sh refuses ANY modified path under src/ or inputs/ (regen.sh:16 — drift-list paths
# included) and scorecard._vintage_stamp ALSO sees staged changes, so the determinants must be
# COMMITTED, never merely staged, or the surface stamps -dirty and the hygiene guard reds. Runs
# BEFORE auto-land so that lane sees a clean tree and a current surface. Nothing here ever
# ratifies — that stays auto-land's, composed from the annotations.
echo "=== [price-leg] $(date '+%Y-%m-%d %H:%M:%S')"
mkdir -p "$PROJECT/state"
leg_rc=0
det=""
head_now=""
leg_quarter=$(./.venv/bin/python -c 'from crude_tanker_fv.loaders import current_book_quarter; print(current_book_quarter() or "")' 2>/dev/null || echo "")
leg_stamp=$(./.venv/bin/python -c 'import json; print(json.load(open("outputs/book_scorecard.json")).get("source_commit") or "")' 2>/dev/null || echo "")
[ -n "$leg_quarter" ] || { echo "[price-leg] SKIPPED: no book quarter in state/last_run.json"; leg_rc=9; }

# 1. The price vintage in its OWN commit — the CLAUDE.md price-basis rule. A dirty tree launders
# the tape into whatever else is landing, so it is never bundled with anything.
if [ "$leg_rc" -eq 0 ] && ! git diff --quiet -- inputs/market_data/prices_daily.yaml; then
  if git add -- inputs/market_data/prices_daily.yaml && git commit -q -m "Price vintage $(date '+%Y-%m-%d') — absorbed as its own commit (daily refresher output)"; then
    echo "[price-leg] price vintage committed alone: $(git rev-parse --short HEAD)"
  else
    echo "[price-leg] FAILED to commit the price vintage"; leg_rc=1
  fi
fi

# 2. The REST of the drift list, separately. commit_drift.sh is #!/bin/zsh and uses the zsh-only
# ${(@f)...} at line 40 — it MUST run through its shebang; `bash scripts/commit_drift.sh` dies
# with "bad substitution", commits nothing, and every later regen then refuses.
if [ "$leg_rc" -eq 0 ]; then
  if ./scripts/commit_drift.sh > "$PROJECT/state/commit_drift.out" 2>&1; then
    sed 's/^/[price-leg] /' "$PROJECT/state/commit_drift.out"
  else
    echo "[price-leg] commit_drift FAILED:"; sed 's/^/[price-leg] /' "$PROJECT/state/commit_drift.out"; leg_rc=2
  fi
fi

# 3. Regen — only when a determinant actually moved since the stamp (the same history diff
# promote._surface_matches_head does, archives and process files excluded). A bogus or empty stamp
# reads as "moved". There is no timeout(1)/gtimeout on this Mac and the healthchecks ping already
# fired in the [sentinel] lane above, so a hang here would be INVISIBLE to the external dead-man
# for ~24h and launchd will not start a second instance of the label: the 900s watchdog is this
# lane's dead-man, not a nicety.
if [ "$leg_rc" -eq 0 ]; then
  det=$(git diff --name-only "$leg_stamp" HEAD -- src inputs ":(exclude)inputs/filings" ":(exclude)inputs/research_issuer" ":(exclude)inputs/research_pareto" ":(exclude)inputs/research_pareto_other" ":(exclude)inputs/research_mb" ":(exclude)inputs/ffa_drybulk" ":(exclude)inputs/forks.yaml" ":(exclude)inputs/notify.yaml" ":(exclude)inputs/reweight_triggers.yaml" ":(exclude)inputs/data_sources.yaml" ":(exclude)inputs/rocketchat_sources.yaml" ":(exclude)inputs/archive_gaps.yaml" ":(exclude)inputs/earnings_calendar.yaml" ":(exclude)inputs/agent_duties.yaml" 2>/dev/null || echo "?")
  if [ -z "$det" ]; then
    echo "[price-leg] surface $leg_stamp already current for HEAD — no regen needed"
  else
    echo "[price-leg] determinants moved since $leg_stamp: $(echo "$det" | tr '\n' ' ')"
    bash scripts/regen.sh "$leg_quarter" > "$PROJECT/state/regen.out" 2>&1 &
    leg_pid=$!
    ( sleep 900; kill -9 "$leg_pid" 2>/dev/null ) &
    leg_watch=$!
    wait "$leg_pid" || { echo "[price-leg] regen.sh rc != 0 (refusal, sidecar failure, or the 900s watchdog)"; leg_rc=3; }
    kill "$leg_watch" 2>/dev/null || true
    sed 's/^/[price-leg] /' "$PROJECT/state/regen.out"
  fi
fi

# 4. VERIFY BEFORE COMMITTING. regen.sh sets neither -e nor pipefail and both its pipeline stage
# and its hygiene stage end in a pipe, so it exits 0 on a DEAD pipeline and on a RED guard alike —
# its exit code cannot gate this commit. The wrapper checks the two things that matter: the
# surface must be stamped with THIS HEAD (a pipeline that died mid-run leaves yesterday's stamp),
# and the outputs-hygiene guard must be green. A rejected surface is left dirty and uncommitted,
# never reverted (CLAUDE.md: no unilateral revert on a gate fail) — the owner decides.
if [ "$leg_rc" -eq 0 ] && [ -n "$det" ]; then
  head_now=$(git rev-parse --short HEAD)
  new_stamp=$(./.venv/bin/python -c 'import json; print(json.load(open("outputs/book_scorecard.json")).get("source_commit") or "")' 2>/dev/null || echo "")
  if [ "$new_stamp" != "$head_now" ]; then
    echo "[price-leg] SURFACE REJECTED: stamp $new_stamp != HEAD $head_now — the pipeline did not finish this run; nothing committed"
    leg_rc=4
  elif ! ./.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_outputs_hygiene.py > "$PROJECT/state/regen_hygiene.out" 2>&1; then
    echo "[price-leg] SURFACE REJECTED: outputs-hygiene guard RED; nothing committed"
    tail -5 "$PROJECT/state/regen_hygiene.out" | sed 's/^/[price-leg] /'
    leg_rc=5
  fi
fi

# 5. Annotate the PURE-PRICE gate rows, so auto-land's (a) can read 0 UNEXPLAINED. The annotator
# measures the gate's own window — the baseline anchor commit's committed surface against the
# working-tree one — so it is order-insensitive and may run either side of the commit below; it
# runs here because the annotations belong IN that commit. It refuses anything whose fair value
# moved, and that refusal is a correct outcome: the row stays UNEXPLAINED, auto-land freezes on
# (a) with the reason named, and a human writes the cause. It never ratifies and never touches
# inputs/ or outputs/.
if [ "$leg_rc" -eq 0 ] && [ -n "$det" ]; then
  ann_rc=0
  ./.venv/bin/python -m crude_tanker_fv.annotate --apply > "$PROJECT/state/annotate.out" 2>&1 || ann_rc=$?
  sed 's/^/[price-leg] /' "$PROJECT/state/annotate.out"
  [ "$ann_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}annotate=rc${ann_rc}"
fi

# 6. Commit the surface and the logs. Gated on SURFACE VALIDITY, not on the annotator: an
# unannotated auto entry that IS committed freezes auto-land on (a) — loud, attributable, clean
# tree — while leaving it uncommitted freezes on (c), holds auto-push AND starves tonight's price
# refresh (price_refresh_cron.sh skips on non-drift dirt), then pages DIRTY-TOO-LONG at 36h.
# `git add -u` stages tracked modifications only, so an untracked draft a chat left under
# decisions/ or outputs/ is never swept into an automation commit. The subject prefix is
# "Regen (price leg) — ", declared on the price-leg node in graph.yaml and enforced by R6: it is
# deliberately NOT the chat-era "Regen — ", whose historical commits carried PLAN.md edits too.
if [ "$leg_rc" -eq 0 ] && [ -n "$det" ]; then
  if git status --porcelain -- outputs decisions | grep -q .; then
    if git add -u -- outputs decisions && git commit -q -m "Regen (price leg) — $(date '+%Y-%m-%d') via scripts/regen.sh (stamp $head_now): surface + gate annotations"; then
      echo "[price-leg] surface committed: $(git rev-parse --short HEAD)"
    else
      echo "[price-leg] FAILED to commit the regenerated surface"; leg_rc=6
    fi
  else
    echo "[price-leg] regen reproduced the committed surface byte-for-byte — nothing to commit"
  fi
fi
[ "$leg_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}price_leg=rc${leg_rc}"
echo "=== [price-leg] EXIT CODE $leg_rc"

# Auto-land (owner's word 2026-09-10, "wire it in now"): the promoter's landing lane
# re-ratifies the drift-gate baseline ONLY when every precondition holds — 0 UNEXPLAINED,
# every moved row annotated since the last ratify, drift-only tree, no flip toward BUY, the
# committed surface current for HEAD and fresh. A quiet gate lands nothing; a FREEZE (rc 1)
# is the normal state while a move awaits its annotation and rides the ledger note. Runs
# BEFORE auto-push so the baseline commit goes out in the same morning.
echo "=== [auto-land] $(date '+%Y-%m-%d %H:%M:%S')"
land_rc=0
PYTHONPATH=src ./.venv/bin/python -m crude_tanker_fv.promote land || land_rc=$?
[ "$land_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}auto_land=rc${land_rc}"
echo "=== [auto-land] EXIT CODE $land_rc"

# Auto-push (owner ruling 2026-09-10): push main when the tree is drift-only and the drift
# gate reads 0 UNEXPLAINED. Held states ride the ledger note; a push is never a way past a
# red gate. Runs here because launchd already has the shell, the env, and the keychain.
echo "=== [auto-push] $(date '+%Y-%m-%d %H:%M:%S')"
push_rc=0
bash scripts/auto_push.sh || push_rc=$?
[ "$push_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}auto_push=rc${push_rc}"
echo "=== [auto-push] EXIT CODE $push_rc"

exit $rc
