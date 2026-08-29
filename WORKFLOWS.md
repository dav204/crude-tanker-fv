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
dates — update the calendar when it does.

**2026-08-13 — before FREEZING a report-day prereg, sweep the name's full trail
since its last decision-log entry:** `sp_scan --names <TICKER>` over the daily
archive + an archive-GAP check for the window (`ls` the period — a hole in the
PDF archive is silent) + one issuer-newsflow search for names with no filing
channel (Oslo/Euronext names have no EDGAR sentinel). A daily consumed for one
print is NOT a triaged daily. (The BRUT H1 prereg froze 8/12 blind to the
issuer's 7/07 delivery + sale-leaseback + DEMERGER + CEO release: the 7/03→7/14
archive hole is Pareto's Jul/Aug cadence — SOURCE-QUIET, audited 8/13 PM: the RC
history walk found no dailies ever existed to backfill (brut_log) — and the 8/06
daily's BRUT paragraph sat untriaged beside the FFA prints taken from the same
issue. The prereg's band survived on subsequent-events routing — the miss was
recoverable luck, not process.) Cadence quirks worth
remembering: TEN reports Q2 in SEPTEMBER (H1 reporter); FLNG's calendar
slot is Aug-28 but 2025's release came Aug-20; the early cluster
(STNG/ASC/TNK/CCEC) opens Jul-28.

Per name, on report day:

1. Pull the 6-K/10-Q + press release (curl + pypdf for PDFs that fail
   WebFetch; **trust the report counts, not the fleet page**).
2. Update `inputs/balance_sheets/<ticker>_<quarter>.yaml` (with the
   provenance trio `source_url` / `retrieved_at` / `filing_period_end` —
   required from 2026-Q2 sheets on); touch the fleet manifest only for
   entries/exits/deliveries. **A snapshot advance moves BOTH halves in one
   commit: bump the manifest `report_date` to the new quarter WITH the new
   sheet** — the pair guard reds any run whose two halves disagree, and
   `scripts/check_snapshot_advance.py` warns on the one pattern the guard
   can't see (snapshot advanced, label not bumped). Cost structure and
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

- **Tests:** `PYTHONPATH=src .venv/bin/python -m pytest -q` (count grows monotonically; the
  current census lives in README — do not hardcode it here, it rots). Never bare `pytest` —
  the package isn't installed.
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
  **Before promoting an UNNAMED broker print, sweep the class file for same-age/similar-price rows in
  the trailing ~6 weeks — unnamed prints are re-report magnets** (2026-08-09: all 4 queued unnamed
  Pareto prints resolved to already-promoted deals — Jag Lokesh, WF Artemis, Wooyang Belos, Singapore
  Spirit/TNK; marks_trail_triage_2026-08-09.md §B-dedupe).
- **Daily price refresh:** `python -m crude_tanker_fv.price_refresh` — fetches watchlist closes (Yahoo)
  into the automation-writable `prices_daily.yaml`; launchd 18:30 daily. Pipeline values at the live
  close; watchlist statics stay as the consensus_pnav/fwd_pe vintage anchors. Flagged quotes (>15% day
  move, >30% vs static) are written but never applied.
- **Regen sequencing (2026-08-29; bit 2× in one week — FLNG 8/25, TRMD 8/29):** COMMIT the
  pair/inputs FIRST, regen SECOND. A regen over uncommitted inputs stamps `source_commit
  -dirty` and the hygiene guard reds it AFTER the ~8-min run — the guard catches it, but a
  wasted regen each time. Corollary: an uncommitted regen also blocks the price cron's
  dirty-tree stand-down (8/25-8/29: four stale sessions from one uncommitted tree).
- **Flush automation drift:** `./scripts/commit_drift.sh` — stages + commits (one step) the 8
  automation-written files the launchd jobs churn. COMMIT-ONLY (push stays manual). Decision logs +
  per-name pipeline outputs EXCLUDED — commit those deliberately with their annotations.
- **Weekly news pull (mechanical):** `scripts/news_pull_cron.sh` — launchd Sat 08:00, chains RC ingest
  → `sp_scan` → `--links` → `fetch_links` → `pareto_archive --build-manifest` → `ffa_ocr`. The download
  step is its own module `crude_tanker_fv.fetch_links` so every `sp_scan` mode stays local-only.
- **Oslo issuer poller:** `python -m crude_tanker_fv.newsweb_poll [--dry-run] [--all]` — the Oslo/
  Euronext issuer-release channel for BRUT/MPCC/CAPT/BWLP (added 2026-08-16). Staging-only, rides
  the hourly edgar-poll row; mechanics + the two filter traps in §Data-sources below.
- **FFA widget OCR (incremental):** `python -m crude_tanker_fv.ffa_ocr` — parses the daily 3-panel
  Cape/Pmax/Smax screenshot into `state/ffa_ocr_curves.json` + review queue; `--staleness` exits 1 if
  the feed is >7 days quiet. Promotion to `inputs/market_data/ffa_forward_curve.yaml` is HUMAN-ONLY.
  Scratch under `state/ffa_scratch/` — tesseract can't read /tmp in the agent sandbox.
- **Weekly news pull (agent-judgment):** `/news-pull` — web-sweeps watchlist names (weighted to APPROX
  + live-event names) into a dated digest. Review-only; promotion is human-only.
- **PDFs:** the `.venv/` has `pypdf`. `.venv/bin/python scripts/fetch_pdf.py <url>` (WebFetch fails on
  many FlateDecode PDFs). Raw `curl` works but prompts.
- **Two venvs:** the engine + all `crude_tanker_fv` code + the full suite run on `.venv` (Python
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
- **HKEXnews (2343 / any future HKEX name)** — `python -m crude_tanker_fv.hkex_poll` (F-3 light
  adapter, 2026-07-14; rides the hourly edgar-poll launchd row). Per-company JSON index
  `titleSearchServlet.do?stockId=<id>` (stockIds from `hkex_stockid:` keys in data_sources.yaml,
  pinned in `tests/test_hkex_poll.py`); the servlet's `result` field is a JSON-encoded STRING;
  filings are English PDFs under `www1.hkexnews.hk/listedco/...` (fetch_pdf-allowlisted via the
  data_sources URLs). Arrivals land in `state/edgar_manifest.jsonl` with `source: "hkexnews"` —
  sentinel FILING-LANDED + draft queue work unchanged. HK cadence is SEMI-ANNUAL (Annual ~Mar,
  Interim ~Jul/Aug) + Monthly Returns (share count).
- **Oslo/Euronext NewsWeb (BRUT / MPCC / CAPT / BWLP)** — `python -m crude_tanker_fv.newsweb_poll`
  (added 2026-08-16; rides the same hourly edgar-poll row). Closes the LAST venue with no filing
  lane: these names have `sec_edgar: null` and no HKEX id, so before this the only thing that could
  see a demerger or a placement was the weekly agent sweep — and when that lapsed, BRUT's 7/07
  demerger sat unread five weeks, MPCC's 6/25 acquisition seven, MPCC's +10.0% share placement
  (6/30–7/02) and CAPT's 8/06 + 8/13 deliveries likewise. Feed is MFN's JSON Feed 1.1
  (`mfn.se/all/a/<slug>.json`; slugs from `mfn_slug:` keys in data_sources.yaml, pinned in
  `tests/test_newsweb_poll.py`). **Two mechanics worth knowing before you touch the filter:**
  (1) relevance is a DENY-list (only `sub:ci:insider` is dropped), because CAPT's vessel deliveries
  are tagged `ext:ob:non-regulatory` — an allow-list on `:regulatory` would drop the very releases
  the module exists for; (2) each release can arrive TWICE — `source: "ob"` (Oslo Børs mirror,
  `TICKER: ` title prefix, `<pre>` body) and `source: "mfn"` (issuer distribution, richer tags) —
  under different news_id *and* different group_id, so dedup keys on (date, punctuation-stripped
  title) and keeps the richer copy. Release bodies stage as `.txt` + any PDF attachments into
  `inputs/filings/<ticker>/`; arrivals land in `state/edgar_manifest.jsonl` with `source: "newsweb"`.
  **BWLP is dual-lane** (Oslo primary + NYSE FPI) and is polled by BOTH — dedupe at read time.

## Earnings-date sweep — the recurring verification (added 2026-07-21, owner directive)

The calendar's windows are only as good as their last verification — the SBLK case
(2026-07-21): a wrongly-"confirmed" entry looks SAFE to every mechanical check, because
date-setting PRs are newswire releases, mostly NOT EDGAR filings. So the sweep itself is
agent work; the TRIGGER is mechanical (sentinel `EARNINGS-UNCONFIRMED` — a window opening
≤10d with status=expected pages per-name; `EARNINGS-SWEEP-STALE` — any window ≤21d with
`meta.last_date_sweep` >7d old pages for the full sweep).

**The sweep (weekly during earnings season, on the sentinel page or at the Saturday session):**
1. Fan out research agents over: every `expected` name whose window opens within ~21d,
   PLUS re-verification of `confirmed` names inside 14d (the FLNG early-release pattern).
2. Per name, only an ISSUER-GRADE source upgrades to confirmed: the company's own date PR
   (GlobeNewswire/PRNewswire/Business Wire), its financial-calendar page, or an exchange
   calendar (Euronext/Oslo Newspoint, HKEXnews board-meeting notice). Aggregator dates
   (MarketBeat/stockanalysis/Nasdaq) are ESTIMATES — record them labeled, never as status.
3. Update `inputs/earnings_calendar.yaml`: status + window + a basis line carrying the
   citation, the verbatim date sentence's substance, and the sweep date. Windows the
   pattern no longer supports get honestly RE-SHAPED (SB's Q1 slip, GSL's lateness), not
   left to look precise.
4. Stamp `meta.last_date_sweep`, run the calendar guard (`pytest -k calendar`), commit.

The backstop stack, for the record: the sweep verifies dates AHEAD; EARNINGS-DUE pages
14d out; the EDGAR poller polls in-window names every run (and everything at least ~12h)
so a print is never missed outright — what the sweep protects is the PREPARATION: the
report-day refresh queued, FVs current at the event, and no false confidence from a
stale "confirmed".

## Consensus-pair recapture — the quarterly packet (added 2026-07-03, WO2 3.1)

The consensus pair (`current_price` + `consensus_pnav` + `consensus_fwd_pe`) is valid only AS A
PAIR from one vintage — the TEN $44 lesson. Trigger `all_sectors_consensus_pair_recapture`
pages when due; the recapture is ONE sitting, one source:

1. Pick ONE Pareto Shipping Daily (the newest with the full share-price/P/NAV/P/E table);
   note its date — that date becomes every touched name's `as_of`.
2. For every covered name: transcribe price, P/NAV, fwd P/E from THAT daily. Never mix days,
   never keep an old pnav against a new price.
3. APPROX names — DISCOVERED per sitting, never enumerated here (rule reshaped
   2026-08-09, owner ruling: the prose roster went stale when containers onboarded —
   "when a rule can be a test, it becomes a test"): any covered name the chosen daily
   prints NO P/NAV for is handled APPROX for that sitting — price + fwd P/E from the
   daily, pnav stays flagged with its own basis note ("flag, don't fake"). Names absent
   from the table entirely keep their FULL static pair at its current vintage. The
   expected two-sense partition is PINNED in `tests/test_approx_roster.py` (against
   `reconcile.APPROX_PNAV_TICKERS`) — an onboard or Pareto coverage change must move
   the pin deliberately, so divergence is a test failure, not silence. Residual:
   k_broker = price ÷ consensus_pnav, so APPROX names carry a mixed-vintage pair BY
   DESIGN — any k-band test allowance retired at a rebase needs a scoped APPROX-name
   replacement.
4. Rebase `inputs/watchlist.yaml` in one commit; run the gate loop (pytest -> reconcile ->
   drift annotate/ratify). Band flips from the price move follow the isolate-commit
   discipline (memory: isolate commit from price drift).
   **FX rule (codified 2026-08-09):** conversion applies to the PRICE leg only — pnav and
   fwd P/E are unit-free ratios — at the DAILY's date FX, never the promote date (the
   MPCC/CAPT machinery: e.g. "kr 24.0 × 0.101838 Jul-3 FX"). Applies to every non-USD
   quote (NOK: BRUT/CAPT/BWLP/MPCC; HKD: 2343 when sourced).
   **Staging pattern (sanctioned 2026-08-09):** transcription may land first as
   `inputs/watchlist_rebase_<date>.yaml.draft` with a NOT-APPLIED marker — transcription
   and promotion are separate acts; the draft is the sanctioned artifact, and the
   promote consumes + deletes it.
5. Re-arm the trigger to the next quarter boundary; record the sitting in decisions/.

## Ops gotcha — long-running nohup jobs (migrated from CLAUDE.md 2026-07-18)

Long-running nohup jobs die silently (block-buffered stdout; 2026-06-10). Pattern:
`nohup sh -c 'PYTHONUNBUFFERED=1 … ; echo "EXIT $?"' >> log 2>&1 &`; watch log mtime, not contents.

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
