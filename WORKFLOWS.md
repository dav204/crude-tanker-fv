# Workflows — Tanker FV tool

Split out of CLAUDE.md (2026-06-22) to keep the operating rulebook short.
The step-by-step procedures for the three recurring multi-step tasks:
onboarding a ticker, the report-day refresh, and onboarding a sector.
CLAUDE.md carries the gates these run against; this file carries the steps.

## Onboarding a new ticker — the workflow

1. `/add-ticker <SYMBOL> <SECTOR>` — scaffolds YAML stubs, test file,
   decision log entry.
2. Pull the latest 6-K / 20-F / press release; fill in the fleet manifest,
   balance sheet, cost structure, dividend policy (METHODOLOGY §8.1).
3. **Sweep the Pareto free text for the name** (added 2026-06-10 after GNK):
   `python -m crude_tanker_fv.sp_scan --names <TICKER>` (add the alias to
   `NAME_ALIASES` first — Pareto uses Oslo tickers / company names). The
   dailies carry name-specific gold the structured columns miss: Pareto's
   own dated NAV statements (cross-check `consensus_pnav` plumbing),
   stance/TP changes, deal overlays, name-attributed S&P prints, dividend
   policy changes, NB orders. Distill into the decision log; promote any
   prints (then run the prints→rerun→drift loop).
4. **§15 governance screen (METHODOLOGY §15.7, mandatory since
   2026-06-11):** gate at multi-year median P/NAV ≥0.85 (recorded N/A);
   below the gate, run the structured screen (control/share structure,
   related-party fee load as % of GAV/yr, distribution behaviour,
   natural-experiment comp, external anchor). Outcome — applied X% /
   declined-with-tripwires / N/A-gated — goes in the decision log.
   Doctrine: haircuts price EVIDENCE of realisation impairment;
   mechanism generates TRIPWIRES.
5. Add the watchlist row (current_price, analyst_target, consensus_pnav,
   consensus_fwd_pe, sector, as_of).
6. Run pipeline + tests + `/reconcile <TICKER>`.
7. If SANITY=OK, close the decision log entry with the reconciliation gap
   recorded as the baseline for future drift detection. If SANITY=FAIL,
   **stop and investigate** — don't paper it over.

The same `--names` sweep is a quarterly-refresh habit: run it incrementally
over the new quarter's dailies for ALL names and skim for stance changes,
NAV statements, and missed prints. The 2026-06-10 retro-sweep (15 names,
280 dailies) found the inputs solid but surfaced one missed print (TEN's
Mar-25 Suezmax disposal), two Pareto stance changes we hadn't recorded
(FLNG→SELL May-26; OET/FRO→HOLD May-26), and exact-match confirmations of
the consensus_pnav plumbing (TRMD $34 stated vs $33.98 implied).

## Report-day refresh — the workflow (added 2026-06-11 for Q2 season)

`inputs/earnings_calendar.yaml` holds each name's next report date
(confirmed/expected + cadence basis); the preflight
(`python -m crude_tanker_fv.refresh`) flags 🔴 REFRESH DUE when a window
opens with no target-quarter balance sheet on file, and 🟡 reports-soon
within 14 days. The weekly `/news-pull` digest catches newly-announced
dates — update the calendar when it does. Cadence quirks worth
remembering: TEN reports Q2 in SEPTEMBER (H1 reporter); FLNG's calendar
slot is Aug-28 but 2025's release came Aug-20; the early cluster
(STNG/ASC/TNK/CCEC) opens Jul-28.

Per name, on report day:

1. Pull the 6-K/10-Q + press release (curl + pypdf for PDFs that fail
   WebFetch; **trust the report counts, not the fleet page**).
2. Update `inputs/balance_sheets/<ticker>_<quarter>.yaml`; touch the
   fleet manifest only for entries/exits/deliveries, cost structure and
   dividend policy only if the policy actually changed.
3. **Issuer-report S&P sweep** (per filing, ~1-3 prints/quarter with
   better vessel detail than Pareto prose): scan the filing + PRs for
   disclosed vessel sales/purchases. Per-vessel price → promote to
   `transactions/<class>.yaml`; en-bloc without split = document, never
   back-solve. Any promotion triggers the prints→rerun→drift loop.
4. Rebase the watchlist vintage TOGETHER: `current_price` +
   `consensus_pnav` + `consensus_fwd_pe` from the same Pareto daily
   (never the price alone — see the TEN gotcha). APPROX names: refresh
   the price leg only, keep the APPROX flags.
5. `python -m crude_tanker_fv.sp_scan --names <TICKER> --since
   <quarter-start>` — skim the name's Pareto mentions for stance/NAV
   statements and missed prints.
6. Run the pipeline + `/reconcile <TICKER>` — SANITY must be OK; stop
   and investigate a FAIL, don't paper it over.
7. Drift gate: >2pp spread move or position flip → annotate
   `decisions/<ticker>_log.md` with the why (market move? new data?
   methodology?).

## Onboarding a new sector — the workflow

METHODOLOGY §11.4 has the engine-side checklist. Before any code:

1. **Methodology decision doc first** (≈§11.x equivalent) — scenarios,
   weight family name (sector-namespaced), cycle anchors, vessel classes,
   external NAV anchor (does Pareto cover this sector? if not, what?).
2. Land the YAML structure, scenario routing, class map.
3. Add the first validator name. Reconcile. Iterate.
4. Add second validator. Pin a `test_<sector>_locked_weights` so weight
   changes are intentional.
5. Run `/reconcile --calibration-lock <sector>` — the v1 lock test
   reports the hit rate against the new-sector bar (≥70%/±10%).

Methodology decisions get time-boxed to one session. v1 ships; refinements
go in Q3.

## Harvest the MB Shipbrokers weeklies — the workflow (added 2026-06-29)

Four feeds, Fridays by email from `*@mbshipbrokers.com` (Container / Tanker / Dry Bulk /
LNG). Email tables are IMAGES; the PDF behind the "Download report" link is the artifact.
MB is a **cross-check, not a calibration input** (VIE discipline) — promotion is human-only.

**Agent half (authed Gmail session — not cron):**
1. Search Gmail (read-only): `from:mbshipbrokers.com newer_than:21d` (or `subject:Weekly`).
2. For each new weekly, `get_thread` and pull the `cdn.flxml.eu/lt-...` URL that the
   "Download report" button points to (the FIRST `lt-` link in the plaintext body — the
   others are sign-up / privacy / social). If a thread body exceeds the tool limit it is
   saved to a tool-results file; extract the link from there with `grep`/`jq`.
3. Write one TSV line per report:  `<YYYY-MM-DD>\t<email subject>\t<download url>`.

**Mechanical half (scriptable):**
4. `python scripts/mb_harvest.py links.tsv` — fetches each via `fetch_pdf.py` (cdn.flxml.eu
   allowlisted), validates `%PDF`, archives under `inputs/research_mb/<feed>/<YYYY>/`
   (gitignored cache). Idempotent: skips files already archived.

**Then (review, human-gated):** read the new issues (`pypdf`); cross-check S&P prints / value
assessments against the curves; a promotable per-vessel print goes through the normal §9.9
drift-gate path; rate/anchor disagreements are logged (§6 footnote), never auto-applied. The
LNG feed feeds the FLNG/CCEC cross-check (`outputs/mb_lng_crosscheck_*.md`).

## Runbook — the command reference (migrated from CLAUDE.md 2026-07-01)

The daily essentials (tests / pipeline / reconcile / drift gate / fetch_pdf / two-venvs) also
sit in CLAUDE.md; the full list lives here.

- **Tests:** `PYTHONPATH=src .venv/bin/python -m pytest -q` (174 baseline 2026-06-05; should only
  ever grow). Never bare `pytest` — the package isn't installed.
- **Pipeline:** `python -m crude_tanker_fv.pipeline <QUARTER>` (e.g. `2026-Q1`).
- **Pre-flight (what's stale / missing):** `python -m crude_tanker_fv.refresh` — its §0 consumes
  `inputs/earnings_calendar.yaml` (hand-maintained; update on sight when the weekly digest flags a
  newly-announced date).
- **Reconcile a name:** `python -m crude_tanker_fv.reconcile <TICKER>` (or `/reconcile <TICKER>`).
- **Drift gate (committed, Pareto-free):** `python -m crude_tanker_fv.drift_gate` — compares current
  pipeline outputs vs the tracked `baselines/reconcile_baseline.yaml` (EV% / tool NAV / position band /
  k_broker on its *second difference*); exit 1 on UNEXPLAINED drift. `tests/test_drift_gate.py` runs it
  as a build gate. Re-anchor ONLY via `./scripts/ratify_baseline.sh "<cause>"` (mandatory cause; human
  commits) — **never hand-edit the numbers.**
- **S&P print scan (incremental):** `python -m crude_tanker_fv.sp_scan` — scans Pareto dailies newer
  than the cursor, writes the review queue to `outputs/sp_print_candidates.md`. Human-classified into
  `transactions/<class>.yaml`; **never auto-promote.** Every `sp_scan` mode is local-only BY
  CONSTRUCTION (network download lives in `fetch_links`).
- **Daily price refresh:** `python -m crude_tanker_fv.price_refresh` — fetches watchlist closes (Yahoo)
  into the automation-writable `prices_daily.yaml`; launchd 18:30 daily. Pipeline values at the live
  close; watchlist statics stay as the consensus_pnav/fwd_pe vintage anchors. Flagged quotes (>15% day
  move, >30% vs static) are written but never applied.
- **Flush automation drift:** `./scripts/commit_drift.sh` — stages + commits (one step) the 8
  automation-written files the launchd jobs churn. COMMIT-ONLY (push stays manual). Decision logs +
  per-name pipeline outputs EXCLUDED — commit those deliberately with their annotations.
- **Weekly news pull (mechanical):** `scripts/news_pull_cron.sh` — launchd Sat 08:00, chains RC ingest
  → `sp_scan` → `--links` → `fetch_links` → `pareto_archive --build-manifest` → `ffa_ocr`. The download
  step is its own module `crude_tanker_fv.fetch_links` so every `sp_scan` mode stays local-only.
- **FFA widget OCR (incremental):** `python -m crude_tanker_fv.ffa_ocr` — parses the daily 3-panel
  Cape/Pmax/Smax screenshot into `state/ffa_ocr_curves.json` + review queue; `--staleness` exits 1 if
  the feed is >7 days quiet. Promotion to `inputs/market_data/ffa_forward_curve.yaml` is HUMAN-ONLY.
  Scratch under `state/ffa_scratch/` — tesseract can't read /tmp in the agent sandbox.
- **Weekly news pull (agent-judgment):** `/news-pull` — web-sweeps watchlist names (weighted to APPROX
  + live-event names) into a dated digest. Review-only; promotion is human-only.
- **PDFs:** the `.venv/` has `pypdf`. `.venv/bin/python scripts/fetch_pdf.py <url>` (WebFetch fails on
  many FlateDecode PDFs). Raw `curl` works but prompts.
- **Two venvs:** the engine + all `crude_tanker_fv` code + the 315-test suite run on `.venv` (Python
  **3.9.6**). The vendored `shipping_harvester` (broker-weekly parser for the Test 1 backfill) requires
  **3.10+**, so a dedicated `.venv310` (Python 3.12, gitignored, provisioned via `uv`) is used ONLY for
  it: `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m pytest -q` (57 tests). Never run
  the engine/tests on `.venv310` or the harvester on `.venv`. Its **source is tracked** (2026-06-23 —
  Test 1 depends on its parsers); only `shipping_harvester/data/` (crawl cache + broker PDFs) is gitignored.
- **Test 1 (engine EV% ex-post) backtest:** harness `backtest/run_engine_test1.py` (runs on `.venv`)
  reads vintages from `backtest/vintages/`. Method + input spec: `backtest/PRE_REGISTRATION_TEST1.md` +
  `backtest/DATA_CONTRACT_TEST1.md`.

## Data sources — per-source fetch mechanics (migrated from CLAUDE.md 2026-07-01)

The *discipline* rules (trust the report not the fleet page; Pareto = the consensus_pnav source with
NAT/ASC/CCEC APPROX; VIE/MB are cross-checks, not calibration) live in CLAUDE.md. The per-source fetch
quirks live here:

- **WebFetch fails on many IR PDFs** (FlateDecode binary). Pattern: `.venv/bin/python scripts/fetch_pdf.py
  <url>` (downloads to /tmp, validates the host against `inputs/data_sources.yaml` — add new sources
  THERE, not to the script), then parse with pypdf.
- **ECO's domain TLS chain fails WebFetch entirely** — use fetch_pdf.py, which carries the one audited
  TLS-verification exception for that host.
- **EDGAR needs a contact User-Agent** — fetch_pdf.py sends an SEC-compliant contact string (was 403 on
  `Mozilla/5.0`); www.sec.gov is allowlisted. (2026-06-26.)
- **Compass Maritime weekly URL changes every week** — pattern
  `compassmar.com/wp-content/uploads/YYYY/MM/Compass-Weekly-Report-MMM-DD-YY.pdf`.
- **The Pareto dailies carry hyperlinks to Pareto's detailed research** as PDF annotations —
  `extract_text()` NEVER sees them (they live in /Annots). Harvest: `sp_scan --links` → `fetch_links`
  → `pareto_archive --build-manifest`. Full NAV breakdowns/estimates, far richer than the daily prose.
  Part of weekly/quarterly ingest.
- **MB Shipbrokers weeklies** — email tables are IMAGES; the PDF behind the "Download report" flexmail
  link is the artifact (harvest from Gmail read-only, fetch with `fetch_pdf.py`, cdn.flxml.eu
  allowlisted; archive `inputs/research_mb/<feed>/YYYY/`). Full steps in the MB workflow above.

## Consensus-pair recapture — the quarterly packet (added 2026-07-03, WO2 3.1)

The consensus pair (`current_price` + `consensus_pnav` + `consensus_fwd_pe`) is valid only AS A
PAIR from one vintage — the TEN $44 lesson. Trigger `all_sectors_consensus_pair_recapture`
pages when due; the recapture is ONE sitting, one source:

1. Pick ONE Pareto Shipping Daily (the newest with the full share-price/P/NAV/P/E table);
   note its date — that date becomes every touched name's `as_of`.
2. For every covered name: transcribe price, P/NAV, fwd P/E from THAT daily. Never mix days,
   never keep an old pnav against a new price.
3. APPROX names (NAT / ASC / CCEC — Pareto publishes no P/NAV): update price + fwd P/E from
   the daily, keep the pnav flagged APPROX with its own basis note — flag, don't fake.
4. Rebase `inputs/watchlist.yaml` in one commit; run the gate loop (pytest -> reconcile ->
   drift annotate/ratify). Band flips from the price move follow the isolate-commit
   discipline (memory: isolate commit from price drift).
5. Re-arm the trigger to the next quarter boundary; record the sitting in decisions/.

## Week-close checklist (migrated from CLAUDE.md 2026-07-01; codified 2026-06-11, owner decision)

Work is organised in sprints ("Weeks"). At the END of each Week, before handoff, run this — docs accrete
seams during a sprint and this is where they get smoothed:

1. **Documentation audit.** METHODOLOGY.md: relocate misfiled content, fix stale counts/k_brokers/
   positions, verify cross-references, write the Week's Appendix A entry. CLAUDE.md: rules current;
   TICKER_NOTES.md reconciled against the latest delta report; README.md + LIMITATIONS.md refreshed
   (closed limitations marked closed, not deleted). Fan out read-only audit agents; apply fixes in the
   main session.
2. **Verification gate.** Full pytest green; pipeline runs clean; `/reconcile --all` SANITY column all
   OK/n-a-APPROX.
3. **PLAN.md rewritten** for the next Week (theme, steps, standing threads, definition of done).
4. **Clean git state** — everything committed with the Week-close CHANGELOG.md entry; no untracked strays
   (check for credential-shaped files).
5. **Push to GitHub** (`git push origin main`) — at Week close at minimum; mid-week pushes after
   significant commits are fine too.
