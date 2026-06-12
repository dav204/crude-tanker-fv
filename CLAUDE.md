# CLAUDE.md — agent operating rules for the Tanker FV tool

**Read this first, every session.** Mistakes that show up here are mistakes
that have already happened once. Each rule has a date so you can see how
old/proven it is. When you correct a recurring mistake, append a dated rule.

## What this repo is

Per-share fair value tool for shipping equities. NAV (per-vessel age-curve
marks) + forward dividend strip, blended by cycle position. Sectors live
in `inputs/scenario_inputs.yaml` under `sectors.<name>`. Per-ticker
artefacts: `inputs/{fleet_manifests,balance_sheets,cost_structures,dividend_policies}/`,
plus a row in `inputs/watchlist.yaml`. See `METHODOLOGY.md` (~1450 lines)
for the full framework; this file is the operational rulebook.

## How to run things

- Tests: `PYTHONPATH=src .venv/bin/python -m pytest -q` (174 baseline at
  2026-06-05; should only ever grow). Never use `pytest` without
  `PYTHONPATH=src` — the package isn't installed.
- Pipeline: `python -m crude_tanker_fv.pipeline <QUARTER>` (e.g. `2026-Q1`).
- Pre-flight (what's stale / missing): `python -m crude_tanker_fv.refresh`.
- Reconcile a name: `python -m crude_tanker_fv.reconcile <TICKER>`
  (or `/reconcile <TICKER>` — see `.claude/commands/reconcile.md`).
- S&P print scan (incremental): `python -m crude_tanker_fv.sp_scan` —
  scans only Pareto dailies newer than the cursor in
  `inputs/market_data/transactions/_scan_state.json`, writes the review
  queue to `outputs/sp_print_candidates.md`. Candidates are
  human-classified into `transactions/<class>.yaml`; never auto-promote.
- Daily price refresh: `python -m crude_tanker_fv.price_refresh` —
  fetches all watchlist closes (Yahoo) into the automation-writable
  `inputs/market_data/prices_daily.yaml`; launchd-scheduled 18:30 daily
  (`com.crude-tanker-fv.price-refresh`). The pipeline CLI values at the
  live close; watchlist statics stay as the consensus_pnav/fwd_pe
  vintage anchors (broker NAV + consensus EPS use them). Flagged quotes
  (>15% day move, >30% vs static) are written but never applied.
- Earnings calendar: `inputs/earnings_calendar.yaml` — hand-maintained
  (the weekly digest flags newly-announced dates; update on sight). The
  preflight's §0 section consumes it; report-day workflow below.
- Weekly news pull (mechanical half): `scripts/news_pull_cron.sh` —
  launchd-scheduled Saturdays 08:00 (`com.crude-tanker-fv.news-pull`),
  chains RC ingest → `sp_scan` → `--links` → `--fetch-links` →
  `pareto_archive --build-manifest` → `ffa_ocr` (+ staleness alarm);
  log at `state/news_pull.log`.
- FFA widget OCR (incremental): `python -m crude_tanker_fv.ffa_ocr` —
  classifies + parses the daily 3-panel Cape/Pmax/Smax FFA screenshot
  from `inputs/ffa_drybulk/` into `state/ffa_ocr_curves.json` + review
  queue `outputs/ffa_ocr_queue.md` (cursor in `state/ffa_ocr_state.json`;
  `--staleness` exits 1 if the single-source feed is >7 days quiet).
  Promotion to `inputs/market_data/ffa_forward_curve.yaml` is HUMAN-ONLY.
  OCR scratch under `state/ffa_scratch/` — tesseract can't read /tmp in
  the agent sandbox.
  Agent-judgment half: `/news-pull` — web-sweeps watchlist names
  (weighted to APPROX + live-event names) into a dated review digest at
  `outputs/news_digest_YYYY-MM-DD.md`. Digest is review-only; promotion
  is human-only.
- The venv at `.venv/` has `pypdf` installed. **Use it for PDFs that fail
  WebFetch** (see below).

## What this tool is, philosophically (locked 2026-06-06)

**The tool produces independent NAV from transaction-validated marks.** Broker
consensus (Pareto P/NAV) and VIE Coverage Universe are *discrimination
diagnostics*, not calibration targets. Wide tool↔broker spreads are
**features** — the divergence is the call (METHODOLOGY §6 INSW, FLNG,
ASC, NAT, TNK; §9.9). Names whose spreads have already been documented
in §6 with a thesis (mark-driven, weight-driven, §12 high-payout pure-play)
are intentional, not failures.

This means: **do not "fix" wide spreads by tweaking marks toward Pareto.**
If a name's spread changes, the question is whether the methodology
drifted or the market moved — not whether to recalibrate the curve.

## Verification loop — every change runs the gate

After any change to inputs, schemas, marks, scenarios, or pipeline code:

1. `pytest -q` — must stay at 174+ passing.
2. `/reconcile <affected ticker>` — must report **SANITY = OK** (tool NAV
   within ±50% of broker NAV — anything wider is a bug, not a call).
3. If the **drift column** moved >2pp since the previous quarterly run,
   update the ticker's `decisions/<ticker>_log.md` with the why (market
   move? methodology change? data refresh?).

The sanity check is a **bug gate**, not a consensus-matching gate. INSW at
−36% to broker NAV is OK (mark-driven, §6 documented); INSW at −95%
would be SANITY=FAIL (you broke something).

## Reconciliation has three jobs, do not conflate them

| Job | What it checks | When it runs | Gate? |
|---|---|---|---|
| **A. Sanity** | Tool NAV within ±50% of broker NAV (no unit error, mis-routed sector, miscount). | Every run, every name. | Yes — pytest fails. |
| **B. v1 calibration lock** | When a new sector ships, ≥70% of validator names land within ±10% of broker NAV at lock-time. | Once per new sector. | Yes, one-time. |
| **C. Drift detection** | Has any name's spread moved >2pp since the previous run without an explainable cause? | Each quarterly refresh. | No — alert. |

Existing sectors (crude / product / LNG) were locked at the tighter
≥80%/±5% bar; new sectors (dry bulk, containers, LPG, offshore drilling)
ship at ≥70%/±10% v1 and tighten to existing-tier in Q3 with one more
quarter of data. **The bars apply at lock-time, not per-run.**

## Data sources — what to trust and how to fetch

- **Quarterly reports (IR PDFs)** are the source of record for fleet counts
  and balance sheets at quarter-end. The live IR fleet *page* is a
  point-in-time snapshot that disagrees with the report at quarter-end —
  **trust the report.** (Caught on FRO 2026-05.)
- **WebFetch fails on many IR PDFs** — FlateDecode binary content doesn't
  render to text. Pattern: `curl -sSL <url> -o /tmp/<file>.pdf` then
  `.venv/bin/python -c "from pypdf import PdfReader; ..."`. (Caught on
  DHT, ECO, multiple times.)
- **ECO's domain TLS chain fails WebFetch entirely** — always curl + pypdf.
- **Compass Maritime weekly URL changes every week** — pattern is
  `compassmar.com/wp-content/uploads/YYYY/MM/Compass-Weekly-Report-MMM-DD-YY.pdf`.
- **Pareto Shipping Daily** is the source for `consensus_pnav` and
  `consensus_fwd_pe` in `watchlist.yaml`. Howe Robinson tanker rates.
  Pareto does NOT publish P/NAV for NAT, ASC, CCEC — those carry APPROX
  values flagged in the YAML comments; `/reconcile` reports them as
  APPROX and downweights the gap accordingly.
- **The dailies carry hyperlinks to Pareto's detailed research** (company
  quarterly reviews/previews, newsflashes) as PDF link annotations —
  `extract_text()` NEVER sees them (they live in /Annots). They resolve to
  publicly-hosted FactSet/BlueMatrix tracked downloads, no auth, tokens
  long-lived; some arrive Proofpoint-wrapped (decoded offline). Harvest:
  `sp_scan --links` (inventory at `outputs/pareto_daily_links.json`, with
  resolved report_ids baked in) then `sp_scan --fetch-links` (downloads
  new report IDs to `inputs/research_pareto_other/linked/`) then
  `pareto_archive --build-manifest`. Retro-harvested 2026-06-10: 220
  reports (217 company_report) incl. ~70 directly on watchlist names —
  full NAV breakdowns and estimates, far richer than the daily prose.
  Run the harvest as part of the weekly/quarterly ingest.
- **VIE Coverage Universe** (Catlin / Mintzmyer) is an independent
  external check, not a calibration input. Track stance disagreements in
  §6 footnotes; do NOT bulk-update from VIE without an explicit
  methodology decision per class.

## Recurring gotchas to NOT relearn

- **Never type a market price from filing/report prose (2026-06-10).**
  TEN was carried at $44.00 for five days because Q1 6-K text "~$44" was
  read as a live quote; the market was at ~$37 all week and every TEN
  signal ran against the wrong denominator. Prices come from
  `prices_daily.yaml` (auto-fetched) or a dated quote source — and a
  watchlist `current_price` NEVER moves without rebasing
  `consensus_pnav` / `consensus_fwd_pe` from the same vintage (broker
  NAV = price/pnav drifts silently otherwise). See ten_log 2026-06-10.

- **Cross-foot the manifest against the source table before shipping
  (2026-06-11).** TEN shipped with 58 vessel rows under a `fleet_summary`
  claiming 60 on-curve: the onboarding plan's "14 conventional Suezmax"
  was an arithmetic slip (the kit listed 16 = 20 − 4 shuttles) and the
  manifest was built to the PLAN, not re-checked against the SOURCE —
  two 2025-built Suezmaxes (≈ +9% NAV) sat omitted for five days. When
  building or editing a manifest, sum the rows and check them against
  the issuer table AND the summary block. Machine-enforced since
  2026-06-11: `test_fleet_summary_totals_cross_foot_against_vessel_rows`
  (test_validate.py) fails on any `on_curve_total` / `total_operating`
  that doesn't equal the vessel-row sum.

- **Long-running background jobs die silently under nohup (2026-06-10).**
  Python block-buffers stdout when not a TTY, so a crashing job's traceback
  sits in an unflushed buffer and is lost — the log just goes quiet (looks
  like a hang, is actually a death). The Rocket.Chat backfill "died" twice
  this way before we instrumented it. Pattern for any multi-hour job:
  `nohup sh -c 'PYTHONUNBUFFERED=1 ... ; echo "EXIT CODE $?"' >> log 2>&1 &`
  — unbuffered output + explicit exit-code echo, detached so session
  events can't kill it. Watch the log mtime, not just its contents.

- **Newbuilds valued at delivered market less remaining commitment** —
  NOT at sunk cost (METHODOLOGY §3.1, §9.6). Decisive for FRO ~$5.7/sh.
- **ECO sale-leaseback is in "borrowings"** on the balance sheet — no
  separate operating-lease line. Don't double-count.
- **Frontline's SWS yard is Chinese**, not Korean. (Mislabeled at least twice.)
- **TC anchors, not spot anchors.** `historical_tce_means.yaml` is
  TC-anchored; VIE multipliers are spot-anchored. They don't numerically
  compose. (METHODOLOGY §10, VIE methodology section.)
- **Weight-set names are sector-namespaced.** "Crude Set A/B/C/D" and "LNG
  Set B / Set B-revised" are not interchangeable. Cross-sector "Set B"
  without a prefix is a methodology error.
- **Transaction-anchored recalibration** covers eight classes with own
  fits as of 2026-06-10: VLCC (10 in-window), Suezmax (19),
  Aframax (12), **LR2 (11 — own-fit; the Aframax-proxy alias is retired)**,
  MR (21), Cape (26), Pana (4), Supra-Ultra (20). Primarily mined from
  the Pareto Shipping Daily archive via `sp_scan.py`; GNK's 10-Q added 4
  issuer-confirmed Cape prints at onboarding. The Pana 2016-kamsarmax
  pair (Sep/Oct-2025) is disambiguated as DISTINCT vessels — see
  pana.yaml notes. DO NOT add other
  classes (LR1, Handysize, LNGC, MGC) without an analogous sample —
  the 2026-06-09 LNGC scan found only demolition prints, so LNG stays
  out (§9.9 scope discipline). **`use_transaction_anchored` is DEFAULT-ON
  since 2026-06-09 (owner decision, METHODOLOGY Appendix A Part 4)** —
  transaction-validated marks ARE the headline marks; pass `False` for
  the un-anchored diagnostic baseline. k_broker now reads as the broker
  premium over transaction levels (uniform ~1.12-1.14 on validated crude
  pure-plays at the Jun-2026 fit). Sinokor-scale buyers are the market,
  not a distortion — exclude aggregate prints only when no per-vessel
  split is disclosed (no-back-solve rule).
- **When new transaction prints land, the comparison is the drift gate
  (2026-06-09).** Adding prints to any `transactions/<class>.yaml` can move
  every name holding that class. After promoting prints: re-run the
  pipeline, read `outputs/transaction_anchor_comparison.md`, and annotate
  the decision log of every name whose txn-anchored EV moved >2pp or whose
  position band flipped — same discipline as the quarterly drift gate,
  applied to the marks layer. Onboarding a new ticker often surfaces new
  prints from its filings (e.g. GNK will), so expect this loop on every
  onboarding.
- **Two structural framework limitations are now codified**: §12 (high-payout
  pure-plays at peak — tool UNDERvalues because dividends are the thesis;
  NAT archetype) and **§15 (governance/value-trap discount — tool OVERvalues
  because asset NAV won't be realised; TEN archetype, schema knob
  `governance_discount_pct` on BalanceSheet, default 0.0, applied at blend
  layer + strip terminal but NOT to `compute_nav`)**. They are inverse
  cases of the same NAV-vs-realisation gap. The haircut is judgmental,
  not parametric — store it auditably per-name with a rationale.
- **Don't back-solve validator marks to broker NAV (2026-06-09).** Caught
  ratcheting Cape vessel-value curves upward in two passes ($65M → $78M →
  $88M NB) during SBLK onboarding to shrink the −22% gap toward the v1
  calibration-lock ±10% bar. The first lift was independent reasoning
  (anchored to publicly-observable Chinese yard NB cost); the second was
  back-solving to the target. The methodology forbids this — see "What this
  tool is, philosophically" above. The v1 calibration-lock test REPORTS a
  hit rate; failing it surfaces a methodology question (transaction-anchor
  the classes per §9.9? accept as documented mark-driven?), NOT a license
  to tune marks. If a validator gap is wide, do the §9.9 transaction-anchored
  work (build `inputs/market_data/transactions/<class>.yaml` from disclosed
  prints, refit) — that's the methodologically-honest fix. See
  `decisions/sblk_log.md` for the full incident.

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

## What NOT to do

- Don't change locked weights (Crude Set A, LNG Set B-revised, Product
  Set B v2) without a §11.x revision and a new lock test.
- Don't add classes to the transaction-anchored pipeline without a
  comparable sample (§9.9 scope discipline).
- Don't bulk-update market data from VIE — directional cross-check only.
- Don't fix a wide tool↔broker spread by tweaking marks. Document the
  divergence in §6 if it's a real call.
- Don't run pipeline against state you didn't author. `state/last_run.json`
  is gitignored and quarter-specific.
- Don't add error handling for cases that can't happen, or comments
  explaining what the code does. METHODOLOGY.md carries the why.
- **Don't drop credential files in the repo.** Secrets (Rocket.Chat PATs,
  API tokens, broker creds, anything that grants access) live in
  `~/.config/crude-tanker-fv.env` — the launchd wrapper sources it.
  `.gitignore` blocks `*_token*`, `*_credentials*`, `*_secret*`, `*.rtf`,
  `.env*` defensively, but the gate is discipline. (Caught 2026-06-09:
  stray `rocketchat_token.rtf` landed at repo root, untracked but one
  `git add -A` away from being public history.)

## Per-ticker quick-refs

(One-liners; full notes live in METHODOLOGY §6.)

- **DHT** — pure VLCC, single-class methodology validator. If DHT is weird,
  the methodology has a bug.
- **FRO** — LR2 classification choice (crude vs product) is open (§9.3).
  Trust the report counts, not the fleet page.
- **ECO** — all-spot, modern fleet; sale-leaseback in borrowings; TLS chain
  fails WebFetch.
- **NAT** — §12 archetype: high-payout pure-play; tool reads as "rich" at
  peak. Treat tool FV as NAV floor. APPROX consensus_pnav.
- **INSW** — mark-driven (k_broker 1.52 post txn-anchor flip, ~1.6 at live
  prices; was 1.37 pre-flip); hybrid crude+product carve-out. Pareto
  BUY→HOLD 2026-05-18 (valuation-driven, TP raised).
- **TNK** — Atlantic-skewed; Aframax transaction anchor; both mark-driven
  AND weight-driven.
- **FLNG** — tool above broker (k_broker 0.87); mature TC-heavy book.
- **CCEC** — weight-driven BUY; large NB orderbook; high scenario torque.
  APPROX consensus_pnav.
- **ASC** — first product validator; off-curve chemical-Handy residual.
  APPROX consensus_pnav.
- **STNG** — multi-class product; buyback channel invisible to strip.
- **HAFN** — IFRS reporting + pool operator; largest product fleet.
- **TRMD** — first full 3-class product.
- **TEN** — three-sleeve crude+product+LNG (`THREE_SLEEVE_TICKERS`); DP2
  shuttle off-curve at contracted book (§11.6); **first §15 case**
  (governance/value-trap haircut at 30%). Txn-anchored NAV $88.13 (asset
  NAV $95.95 un-anchored), post-haircut PW FV $62.56 vs price $37.99 →
  BUY (EV +64.7%). APPROX consensus_pnav (no Pareto coverage; VIE-stale
  anchor). Onboarded 2026-06-06; June-5 data-kit reconcile 2026-06-11
  added two Suezmaxes the build omitted (Dr Irene Tsakos, Silia T) —
  NAV +9.1%, see ten_log. H1 reporter: Q2 events (Ulysses sale, charter
  rolls) land at the SEPTEMBER refresh.
- **SBLK** — first dry-bulk validator (Cape 31 / Pana 46 / Supra-Ultra 58
  post-Eagle-Bulk fleet, §11.7.1 class collapse); mark-driven (k_broker
  1.27 at v1, 1.27 post-transaction-anchor — the recalibration shifted
  the gap by 0.6pp, confirming the −21% spread is methodological, not a
  curve artefact). Cape was understated (+18%/+12% at 5/10yr), Supra-Ultra
  overstated (−10%/−13%), Pana roughly calibrated. Transaction sample:
  Pareto Shipping Daily archive + SBLK Q1 2026 6-K Star Stonington
  ($19.6M). Tool HOLD at live prices (band-edge; was TRIM/SHORT at the
  Jun-5 static — see sblk_log 2026-06-11), broker BUY. §15.7-screened
  OUT (self-managed, ~100% payout). Onboarded + transaction-anchored
  2026-06-09. GNK (k 1.04 on identical curves) isolates SBLK's gap as
  name-specific — likely the 46-vessel Pana book on the thinnest fit.
- **GNK** — second dry-bulk validator; VALIDATES the transaction-anchored
  dry-bulk curves (k_broker 1.04, gap −5.2% — within the v1 ±10% bar on
  the same marks where SBLK reads −21%). No Pana exposure (19 Cape /
  25 Supra-Ultra at Mar-31). US domestic issuer — 10-Q not 6-K; per-vessel
  employment table lives in the 10-Q MD&A. **LIVE DEAL: Diana hostile cash
  tender $24.80, deadline Jun-26-2026; price is tender-pinned, so EV/position
  signals are deal-arb readings, not NAV-discount signals, until resolution.**
  No §15 haircut (event risk ≠ realisation impairment). v1 lock outcome:
  1/2 (50%) FAIL-with-explanation — the miss is the documented SBLK case;
  no curve tuning per the back-solve rule. Onboarded 2026-06-09/10.
- **CMDB** — third dry-bulk validator, APPROX-anchored (zero Pareto/VIE
  coverage; consensus_pnav 0.62 is a P/BV proxy — spinoff book ≈ recent
  fair value). 29 owned old bulkers at Mar-31 (6 Cape / 7 Pana / 16
  Supra-Ultra); the ~20-vessel CBI chartered-in trading platform is
  P&L-ONLY, never in the manifest. Tool asset NAV $32.23 = book +15.8%.
  **Second §15 case — 30% governance haircut (owner decision 2026-06-10,
  TEN-equivalent: related-party fees $21.6M/yr, no payout, family
  control, 0.6× P/BV).** Post-haircut PW FV $19.82 vs price $17.25 →
  mild BUY (+14.9% EV); pre-haircut read +64%. No external anchor to
  triangulate the 30% (unlike TEN's VIE check) — revisit on any payout
  initiation. Consolidated EPS includes the trading platform → §9.11
  xref reads structurally hot. Watch Q2 for the Astros price (clean
  age-8 Ultramax print). Onboarded 2026-06-10; Week 2 closed.

- **CAPT** — 17th name, first Oslo/NOK listing (watchlist carries USD;
  `yahoo_symbol: CAPT.OL` — bare CAPT on Yahoo is the wrong issuer).
  Marinakis ~75%; 30 firm vessels, 21 NB through mid-28 (heaviest §3.1/
  §9.6 delivered-market-less-commitment user); 13 options at cost
  EXCLUDED from NAV. Tightest first reconcile on record: −2.6% vs real
  Pareto pnav (k_broker 1.04) — validates NB convention + txn-anchored
  crude curves. BUY, EV +38.8% — deepest-discount crude name. §15
  deep-dived vs the full Euronext admission doc (archived
  `inputs/research_issuer/`) and NOT applied: single share class, fees
  ~0.4% of GAV/yr (vs CMDB ~4%), transfers at broker marks, pays ~50%
  from quarter one; BUT blank-check preferreds + written-consent
  control + no board committees + Crude Carriers fold-in precedent =
  SIX named tripwires in capt_log (option-funding dilution, preferred
  issuance, payout walk-back, sponsor merger proposal, fee escalation,
  Q1-27 NB-debt landing). Breakeven solve reads $0/day (net-cash
  + NB-heavy; cosmetic). Onboarded 2026-06-11 from archived Pareto
  initiation + Q1 review — pull issuer Q1 report at Q2 refresh.

## Week-close checklist (codified 2026-06-11, owner decision)

Work is organised in discrete sprints called "Weeks". At the END of each
Week, before handoff, run this checklist — documentation accretes play-
dough seams during a sprint and this is where they get smoothed:

1. **Documentation audit.** METHODOLOGY.md: relocate content that
   accreted into the wrong section (shipped things out of "NOT in v1"
   lists; status updates out of bullet asides), split run-on NOTE
   paragraphs, fix stale counts/k_brokers/positions/statuses, verify
   cross-references resolve, and write the Week's Appendix A entry.
   CLAUDE.md: quick-refs reconciled against the latest delta report;
   stale workflow notes removed. README.md + LIMITATIONS.md: refresh
   against current state (limitations that closed get marked closed,
   not deleted). Fan out read-only audit agents for the inventory; apply
   fixes in the main session.
2. **Verification gate.** Full pytest green; pipeline runs clean;
   `/reconcile --all` SANITY column all OK/n-a-APPROX.
3. **PLAN.md rewritten** for the next Week (theme, steps, standing
   threads, definition of done). PLAN.md is the sprint handoff document
   — a new agent reads CLAUDE.md, then PLAN.md, then starts.
4. **Clean git state** — everything committed with the Week-close
   changelog entry; no untracked strays (check for credential-shaped
   files per the secrets rule).
5. **Push to GitHub** (`git push origin main`) — added 2026-06-11,
   owner request. Push at Week close at minimum; mid-week pushes after
   significant commits are fine too.

## The compounding-knowledge habit

Anytime the agent makes a mistake that wasn't caught by these rules,
append a dated rule to the relevant section. Ruthlessly edit until the
mistake rate visibly drops. This file is checked into git; rules survive
sessions.

## Changelog

- **2026-06-11 (post-close) — TEN June-5 data-kit reconcile (user-supplied
  PDF; tenn.gr blocks agent fetching).** Found + fixed a Q1 manifest
  omission: Dr Irene Tsakos + Silia T (2025-built conventional Suezmaxes)
  were never entered — the onboarding plan's "14 conventional Suezmax"
  slip; fleet_summary claimed 60 on-curve over 58 rows. NAV/sh $80.79 →
  $88.13 (+9.1%), gap to APPROX broker −26.0% → −19.3%, BUY unchanged.
  Q2-vintage kit deltas (Ulysses sale confirmed — no gross price, not
  promotable; Sola TS step-up; Dimitris P spot→TC $40k; Alaska/Archangel
  to spot-indexed TC) documented in ten_log for the September H1 refresh,
  NOT applied to the Mar-31 snapshot. New cross-foot guard test
  (test_validate.py) + gotcha rule. tests: 244 passed.
- **2026-06-11 (WEEK 3 CLOSED)** — **first Week-close checklist run
  (checklist itself codified this session, owner decision).**
  Documentation audit via two read-only agents, fixes applied:
  METHODOLOGY line-46 monster paragraph → dated scope-change log;
  coverage header 8→17 names/4 sectors; preferred_equity comment
  (TEN is the user, not "none"); STNG §6 mark-validated→mark-driven
  with date-stamps; INSW version-label footnote; §6 entries ADDED for
  CMDB + CAPT; FFA-OCR saga moved OUT of §11.7.7 "NOT in v1" into new
  §11.7.8 (onboarding table → §11.7.9); Appendix A entries added for
  2026-06-10 + 2026-06-11 (closing the §15.7 dangling promise).
  README: status 2026-06-11, 17 names/4 sectors/243 tests, dry-bulk +
  CAPT/HAFN/TRMD watchlist tables, DP2/dry-bulk scope line corrected.
  LIMITATIONS: dry-bulk greenfield marked CLOSED, §15 names updated
  (TEN+CMDB cases; TNK/CCEC screened-declined), mark-driven snapshot
  marked as vintage with pointer to the live sweep. CLAUDE.md
  quick-refs reconciled (INSW k 1.52+, SBLK HOLD); earnings-calendar
  maintenance line added; stale "(Coming end of Week 0)" removed.
  Verification gate: 243 passed/10 skipped; `/reconcile --all` 17/17
  SANITY OK, 0 drift alerts; refresh checklist regenerated 17/17.
  **PLAN.md created** (the rolling sprint-plan/handoff doc — Week 4 =
  containers; Step 0 flags the Container Weekly feed stale since
  Apr-01). Week 3 final tally: news-pull v1, daily price refresh +
  TEN fix, FFA-OCR Stage 1 + market-consistency diagnostic, earnings
  readiness, CAPT (17th name), §15.7 + full-book retro screen,
  Week-close checklist.
- **2026-06-11 (Week 3, day 2, Part 4)** — **§15.7 screening procedure
  FORMALISED + full-book retro screen run (owner-approved).** New
  METHODOLOGY §15.7: cheap gate (multi-year median P/NAV ≥0.85 → N/A),
  structured screen below it (control/share structure, related-party
  fee load %GAV/yr, distribution behaviour, natural-experiment comp,
  external anchor), the evidence-vs-mechanism doctrine (haircuts price
  EVIDENCE; mechanism → tripwires), two quantitative calibration
  anchors (capitalized fee drag; external-anchor implied discount),
  mandatory recording per name + onboarding step 4. Retro outcomes,
  all 17: 9 gated N/A (DHT ECO FRO FLNG INSW HAFN NAT-§12 ASC GNK);
  3 Step-1 declines (STNG TRMD SBLK — open payout/buyback channels, §6
  mark-driven discounts); 2 full-screen declines with tripwires —
  **TNK 0%** (dual-class 54.9%-votes-on-30.8%-economics BUT fee leakage
  internalized Dec-24, $6.00/sh specials since mid-23; TK-combination
  tripwire) and **CCEC 0%, closest call** (float ~13%, sponsor-paid
  exec comp, fiduciary waiver, ~24% payout vs CAPT-like 0.4%-of-GAV
  fees, real conflicts committee, 76-quarter dividend record;
  payout-path + CAPT↔CCEC cross-dealing tripwires; 10% alternative
  documented — owner call). **Haircut recalibrations: TEN HOLD 30%**
  (band 30-36; VIE-implied drifted to 36.3% but the payout raise argues
  down; TCM fee anchor due at Q2) and **CMDB HOLD 30%, RE-GROUNDED** —
  capitalized fee drag ($28M/yr ÷ 10-12%) = 30-36% of the $779M equity
  NAV, landing on the haircut independently of TEN-equivalence.
- **2026-06-11 (Week 3, day 2, Part 3)** — **CAPT onboarded (17th name,
  Week 3 stretch goal) — first Oslo/NOK listing.** Assembled entirely
  from the linked-report harvest (Pareto initiation Apr-19 + Q1 review
  May-27, both already on disk) — zero new fetching for data assembly;
  issuer-report confirmation deferred to the Q2 refresh. 30 firm
  vessels (12 VLCC / 10 Suez / 4 Afra / 4 LR2-crude-routed), 9 on-water
  at Mar-31, 21 NBs at delivered-market-less-$1,880M-commitment with a
  Pareto-waypoint fleet_schedule ramp (11 Apr-26 → 17 Nov-26 → 24 YE-27
  → 30 mid-28); 13 options at cost excluded. NOK handling: watchlist in
  USD (NOK 116.2 / 9.5221 = $12.20, Jun-10 vintage incl. pnav 0.67 +
  P/E 11.1 from the same daily); price_refresh gains `yahoo_symbol` +
  `quote_currency` fields (CAPT.OL + NOK=X conversion — bare "CAPT" is
  Captivision). NAME_ALIASES + data_sources + earnings calendar
  entries added; 23-mention Pareto sweep distilled. **First reconcile:
  −2.6% gap on a real Pareto print, SANITY OK, k_broker 1.04 — the
  tightest onboarding baseline on record; BUY EV +38.8%.** §15
  considered + declined (documented in the balance sheet + log).
  tests: 243 passed, 10 skipped.
- **2026-06-11 (Week 3, day 2, Part 2)** — **Q2 earnings-readiness pass.**
  `inputs/earnings_calendar.yaml` built for all 16 names (web-swept +
  cadence-verified: 5 calendar-confirmed — ECO Aug-4, SBLK Aug-5,
  TRMD Aug-26, HAFN+FLNG Aug-28; 11 expected windows; TEN is a
  SEPTEMBER H1 reporter). Preflight gains §0 earnings check
  (`refresh.check_earnings_calendar`): 🔴 REFRESH DUE when a report
  window opens with no target-quarter balance sheet, 🟡 within 14 days.
  Report-day refresh runbook added to CLAUDE.md (7 steps incl. the
  issuer-report S&P sweep — Appendix A backlog CLOSED — and the
  vintage-rebase rule). Season shape: early cluster Jul-28→Aug-6
  (STNG/ASC/TNK/CCEC/ECO/GNK/INSW/DHT/SBLK/CMDB), late cluster
  Aug-20→31 (FLNG/FRO/NAT/TRMD/HAFN), TEN mid-Sep. tests: 238 passed.
- **2026-06-11 (Week 3, day 2)** — **FFA-OCR Stage 1 SHIPPED** (the
  Week 3 centerpiece; owner-approved re-scope, no longer trigger-gated).
  `ffa_ocr.py`: classifier (Cape + Cal2\d + "Produc* Price Change"
  signature) + TSV-positional parser (x-band panel assignment, per-row
  tenor majority vote, conf≥60 gate, trailing-only punct strip) +
  sanity model + review queue (`outputs/ffa_ocr_queue.md`) + incremental
  cursor + `--staleness` alarm, wired as the new tail of the weekly
  news-pull chain. Key empirics: the widget posts EVERY business day
  (45/46 days Apr-1→Jun-11; the ~7% archive-wide rate was format-era
  dilution); recipe = grayscale → 4× LANCZOS → psm 6 (color drops the
  headers; tesseract can't read /tmp in the sandbox — scratch lives in
  `state/ffa_scratch/`); DISCOVERED tick model — months/Cal tick $12.5
  truncated, Q tenors display the unrounded 3-month average (31766 =
  95300/3 is real, not noise). 29/45 days fully clean, 16 flagged
  (incomplete grids only; the parser refuses to guess on mangled
  tokens like "(3800"). Promotion to `ffa_forward_curve.yaml` is
  human-only; strip integration is diagnostic-first pending one review
  cycle. Stage 2 (2020-2026 backfill) open. tests: 233 passed.
- **2026-06-10 (night, Week 3 opener, Part 2)** — **first `/news-pull` run
  + TEN price-input error fixed + daily price refresh BUILT.** The
  inaugural digest (`outputs/news_digest_2026-06-10.md`, 4 agents / 16
  names) caught: TEN watchlist price $44.00 was an input ERROR (6-K prose
  "~$44" typed as a live price; actual $36-37.5 all week) — fixed to
  $37.14 with `consensus_pnav` REBASED 0.40→0.34 to preserve the implied
  broker NAV anchor (~$110) and `consensus_fwd_pe` 5.5→4.6 (drift +0.5pp,
  stable; BUY strengthens, EV +30.9%→+55.1%); an unrecorded Pareto stance
  change INSW BUY→HOLD 2026-05-18 (TP raised $84→$88, valuation-driven —
  confirmed verbatim in the archived daily, annotated); GNK deal risk
  front-loaded to the Jun-18 AGM (all 3 proxy advisors back Genco, Diana
  withdrew 4/6 nominees + floated dropping the tender, 38 shares
  tendered); STNG 4×LR2 $285.8M EN-BLOC (documented-not-promoted, watch
  Q2 6-K for splits); CMDB Astros bounded ~$22.8M (inference — NOT
  promotable). **Process fix shipped same session: daily price refresh**
  — `price_refresh.py` fetches all watchlist closes (Yahoo chart API)
  into automation-writable `prices_daily.yaml` with sanity flags (>15%
  day move / >30% vs static, flagged = never applied); launchd
  `com.crude-tanker-fv.price-refresh` daily 18:30; pipeline CLI passes
  `live_prices=True` (tests keep deterministic statics by default).
  VINTAGE RULE: broker NAV (reconcile) + consensus EPS keep the
  watchlist-static `as_of_price` — Pareto ratios pair with Pareto-vintage
  prices; only EV/position reads live. SBLK TRIM/SHORT→HOLD on the
  live-price introduction (band-edge wiggle, annotated). tests: 220
  passed, 10 skipped.
- **2026-06-10 (night, Week 3 opener)** — **periodic news pull v1 BUILT**
  (registered backlog, owner spec + 4 vetting amendments, one session as
  time-boxed). Mechanical half: `scripts/news_pull_cron.sh` + launchd
  plist `com.crude-tanker-fv.news-pull` (Saturdays 08:00, after the
  07:00 daily RC ingest per amendment 2), chaining RC ingest → `sp_scan`
  → `--links` → `--fetch-links` → `pareto_archive --build-manifest`,
  PYTHONUNBUFFERED + per-step banners + exit-code echo per the silent-
  death gotcha. Agent half: `/news-pull` command — web-sweep weighted to
  APPROX (read from `reconcile.APPROX_PNAV_TICKERS`, not hardcoded) +
  live-event names (detected from decision logs), digest at
  `outputs/news_digest_YYYY-MM-DD.md` with promotable-candidate (built-
  year + en-bloc-split fields, amendment 4) / stance-change / live-deal /
  stale-price (APPROX fresher-price-only, amendment 3) / no-action
  sections + drift-loop reminder. Never writes pipeline-loaded YAMLs
  (amendment 1). Dry-run clean end-to-end (cursor Jun-08 → Jun-10).
- **2026-06-06** — file created. Verification-loop, three-jobs
  reconciliation framework, "what this tool is, philosophically" section,
  gotcha list, per-ticker quick-refs all promoted from session memory +
  decision logs.
- **2026-06-09** — added secrets-discipline rule to "What NOT to do" after
  a `rocketchat_token.rtf` was dropped at repo root during Rocket.Chat
  ingest setup. Caught untracked but not gitignored. Defensive `.gitignore`
  patterns added (`*_token*`, `*_credentials*`, `*_secret*`, `*.rtf`, `.env*`).
- **2026-06-09 (evening Part 2)** — dry-bulk classes added to the
  transaction-anchored pipeline. Cape (24 prints) / Pana (6) / Supra-Ultra
  (18) YAMLs landed at `inputs/market_data/transactions/`. Sources are
  the Pareto Shipping Daily archive 2025-01→2026-06 plus the SBLK Q1 2026
  6-K Stonington print. SBLK gap moved −21.7% → −21.1% post-fit, locking
  it in the §6 mark-driven taxonomy (k_broker 1.27). Per-ticker quick-ref
  for SBLK + the §9.9 scope-discipline line updated. tests: 192 passed.
- **2026-06-09 (late evening Part 3)** — tanker classes swept from the same
  Pareto archive: VLCC/Suezmax/Aframax/MR samples expanded, LR2 graduates
  to own-fit (proxy retired). Tanker 10yr anchors were running HOT — VLCC
  fit −18% at both legs; 5 names flip under txn-anchored marks
  (DHT/ECO/FRO→TRIM-or-HOLD-down, TNK BUY→HOLD, TRMD HOLD→TRIM). Toggle
  still opt-in; default-on is an OPEN owner decision. `sp_scan.py` +
  `_scan_state.json` added for incremental future scans (191-candidate
  review queue archived at `outputs/sp_print_candidates.md`). One locked
  test expectation reversed with rationale (Suezmax fit direction — thin-
  sample artifact). Affected decision logs annotated (9 names). tests:
  198 passed. Backlogs registered in METHODOLOGY Appendix A: exogenous
  demand-destruction overlay, issuer-report S&P sweep at refresh, GNK
  onboarding, §6 SBLK promotion, Pana print disambiguation.
- **2026-06-09 (late evening Part 4)** — **txn-anchored marks made the
  pipeline DEFAULT** (owner decision; Sinokor's bid IS the VLCC market).
  Defaults flipped in `value_company` / `run_scenarios_watchlist` /
  `run_broker_sweep` (sweep now recalibrates its "tool" endpoint too).
  Headline re-base: DHT BUY→TRIM/SHORT $14.31, ECO/FRO →TRIM/SHORT,
  TNK BUY→HOLD, TRMD →TRIM/SHORT; FLNG/CCEC untouched. k_broker semantics
  now "broker premium over transaction levels" — uniform 1.12-1.14 on
  crude pure-plays. vlcc.yaml Sinokor exclusion re-grounded on
  data-quality only (no per-vessel split). FV-band + sweep tests re-based.
  Drift flags on this run are the re-base, not market moves — 9 logs
  annotated. tests: 198 passed.
- **2026-06-10 (later still)** — **Pareto linked-report harvest: 220
  detail reports pulled from the dailies' hyperlink annotations.** User
  tip: the dailies embed links to Pareto's full research. pypdf
  `extract_text()` is blind to /Annots — every prior sweep missed them.
  240 of 351 dailies carry links → 267 unique tracked-download URLs
  (FactSet/BlueMatrix, public, long-lived tokens; 100 arrived
  Proofpoint-wrapped and are unwrapped offline). Downloaded 220 new
  reports (47 already archived), 0 failures; 217 classify as
  company_report incl. ~70 on watchlist names (full NAV breakdowns /
  estimates). `sp_scan --links` + `--fetch-links` codified with
  inventory + report_id dedupe (no re-fetching on re-runs);
  `outputs/pareto_daily_links.json` committed. The "Capital Tankers"
  reports in the set are CAPT (Oslo-listed crude newbuild player,
  initiated by Pareto Apr-2026, BUY TP NOK 180 at 0.75-0.84x NAV) — a
  DIFFERENT entity from CCEC, whose no-coverage APPROX status stands.
  CAPT noted as a future onboarding candidate (Pareto-covered pure
  crude, deepest crude NAV discount). tests: 207 passed.
- **2026-06-10 (later)** — **Pareto free-text name-sweep added to the
  process + run retroactively for all 15 names.** `sp_scan.py --names`
  mode (alias-aware: OET=ECO, HAFNI=HAFN, TORM=TRMD, Tsakos=TEN;
  share-price-table noise filtered). 15 review files at
  `outputs/pareto_mentions_<ticker>.md`; distilled entries in every
  decision log. Findings: inputs validated (NAT NB commitments + ASC
  payout-doubling already captured); 1 missed print promoted (TEN Mar-25
  Suezmax $40M — fit moved <0.5pp, under drift gate); Pareto stance
  changes recorded (FLNG→SELL 2026-05-27, OET+FRO→HOLD 2026-05-26,
  INSW→BUY 2026-01-21); consensus_pnav plumbing confirmed by exact
  matches (TRMD stated $34 vs implied $33.98; INSW $80 vs $79.59; SBLK
  $33 vs $33.17). Mention-count distribution empirically confirms the
  APPROX taxonomy (CCEC 0, NAT 4, TEN 5, ASC 6 — "We don't cover ASC"
  verbatim — vs covered names 34-96). Onboarding workflow updated with
  the sweep as step 3; quarterly-refresh habit noted. tests: 205 passed.
- **2026-06-10 (evening)** — **CMDB onboarded (16th name, third dry-bulk
  validator) — Week 2 dry-bulk sequence CLOSED.** APPROX-anchored (zero
  Pareto/VIE coverage; P/BV 0.62 proxies P/NAV on spinoff fair-value
  book). 29 owned at Mar-31 (Clara/Miracle sold Q1; Astros closed Q2);
  CBI chartered-in platform excluded as P&L-only. Tool NAV $32.23 =
  +15.8% over book; 0.54× price/NAV, EV +64% — **flagged §15 candidate
  (related-party fees / no payout / family control), haircut decision
  with owner before the signal is actionable.** CMDB added to
  `APPROX_PNAV_TICKERS` (was missing — briefly mis-entered the lock
  denominator as 1/3; corrected to 1/2 excluded-APPROX same session).
  No promotable prints (Clara+Miracle aggregate gain only — no per-vessel
  prices; no-back-solve). §11.7.8 table marked DONE throughout.
  tests: 210 passed. **Same evening: §15 haircut set at 30% (owner
  decision, TEN-equivalent) — PW FV $28.32 → $19.82, EV +64% → +14.9%
  mild BUY; asset NAV untouched; §15.3 second-case entry added.**
- **2026-06-10** — **GNK onboarded** (15th name, second dry-bulk validator)
  from the Q1 2026 10-Q. k_broker 1.04 / gap −5.2% — VALIDATES the
  transaction-anchored dry-bulk curves on a no-Pana fleet; isolates SBLK's
  −21% as name-specific. v1 dry-bulk calibration lock recorded as 1/2
  (50%) FAIL-with-explanation (SBLK = documented §6 mark-driven miss; no
  tuning per the back-solve rule); revisit at Q3 with the ≥80%/±5% bar.
  6 prints harvested at onboarding (2× GNK nmax $72.75M + Courageous
  $63.55M + Maran SWS cape $30M in-window; Picardy/Predator $10.6M
  documentation) — Cape fit n 21→25, +16.0%/+12.7%; SBLK moved −0.1%
  (under drift gate). Diana tender deal overlay documented in
  decisions/gnk_log.md + watchlist comment — GNK price is tender-pinned
  until Jun-26. tests: 201 passed.
