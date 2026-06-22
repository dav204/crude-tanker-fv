# CLAUDE.md — agent operating rules for the Tanker FV tool

**Read this first, every session.** Mistakes that show up here are mistakes
that have already happened once. Each rule has a date so you can see how
old/proven it is. When you correct a recurring mistake, append a dated rule.

## Project stance — a forward-looking valuation aid (2026-06-21)

This is a **forward-looking, fundamentals tool for valuing individual shipping
equities** — independent NAV (per-vessel age-curve marks) + a forward dividend
strip, blended by cycle position. Judge it by whether its per-name reads are
sound, auditable, and useful for a position call — **not** by a cross-sectional
information coefficient. It is not, and is not trying to be, a rigorously
backtested cross-sectional quant portfolio. Development proceeds normally:
new sectors, methodology refinements, features, and the Q2/event-window work
are all in scope (see PLAN.md).

A crude-subsector "edge" backtest was run earlier and lives in `backtest/`
(`backtest/REPORT.md`). Its finding — no *statistically demonstrated*
cross-sectional edge on the ~1.5 years of published P/NAV that exist — is
**expected** for a 4-name universe over ~6 quarters and is a known limitation
of cross-sectional testing at that scale, **not** a refutation of the per-name
valuation work. It is kept as a recorded diagnostic, **not** a development gate.

(History: a 2026-06-14 "development freeze" paused feature work pending that
verdict; it was **LIFTED 2026-06-21 by owner decision** for the reasons above.
The backtest artefacts are retained as reference.)

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
  chains RC ingest → `sp_scan` → `--links` → `fetch_links` →
  `pareto_archive --build-manifest` → `ffa_ocr` (+ staleness alarm);
  log at `state/news_pull.log`. (The download step moved from
  `sp_scan --fetch-links` to its own module
  `python -m crude_tanker_fv.fetch_links` on 2026-06-12 so every
  `sp_scan` mode is local-only — see the permissions note in
  "What NOT to do".)
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
  render to text. Pattern (2026-06-12): `.venv/bin/python
  scripts/fetch_pdf.py <url>` (downloads to /tmp, validates the host
  against `inputs/data_sources.yaml` — add new sources THERE, not to the
  script) then `.venv/bin/python -c "from pypdf import PdfReader; ..."`.
  Raw `curl` still works but prompts in agent sessions; the wrapper is
  permission-allowlisted. (Caught on DHT, ECO, multiple times.)
- **ECO's domain TLS chain fails WebFetch entirely** — use fetch_pdf.py,
  which carries the one audited TLS-verification exception for that host.
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
  resolved report_ids baked in) then `python -m crude_tanker_fv.fetch_links`
  (downloads new report IDs to `inputs/research_pareto_other/linked/`) then
  `pareto_archive --build-manifest`. Retro-harvested 2026-06-10: 220
  reports (217 company_report) incl. ~70 directly on watchlist names —
  full NAV breakdowns and estimates, far richer than the daily prose.
  Run the harvest as part of the weekly/quarterly ingest.
- **MB Shipbrokers weeklies (direct subscription since 2026-06-12):**
  Container / Dry Bulk / Tanker (LNG pending) arrive Fridays by email;
  the email tables are IMAGES — the PDF behind the "Download report"
  flexmail link is the artifact. Harvest the links from Gmail (read-only
  API), fetch with `scripts/fetch_pdf.py` (cdn.flxml.eu allowlisted via
  `data_sources.yaml` `mb_shipbrokers_weeklies`), archive at
  `inputs/research_mb/<feed>/YYYY/` (container CONTINUES the frozen
  `research_pareto_other/container_weekly` archive — extraction passes
  read both roots). Independent cross-check, not a calibration input —
  same discipline as VIE.
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
  fits as of 2026-06-12: VLCC (10 in-window), Suezmax (19),
  Aframax (13 — incl. the premium-channel-noted Seamusic print, see
  aframax.yaml), **LR2 (11 — own-fit; the Aframax-proxy alias is retired)**,
  MR (21), Cape (26), Pana (5 — thinnest fit; Vulcania is TC-attached),
  Supra-Ultra (22). Primarily mined from
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
- **Don't widen `.claude/settings.json` permission rules casually
  (2026-06-12).** The tracked allowlist (see
  `PERMISSIONS_PROPOSAL.md` for the full rationale) encodes policy:
  every `sp_scan` mode is local-only BY CONSTRUCTION (network download
  lives in `crude_tanker_fv.fetch_links`, which asks); the watchlist /
  transactions / FFA-curve edits ask because promotion is human-only;
  `git push` asks because pushing is a deliberate event. Two caveats to
  remember: Bash permission rules are PREFIX matchers (a network flag
  on an allowed module leaks through when flags are reordered — that's
  why fetch_links is a separate module, keep it that way), and
  file-rules only govern the agent's file tools, not `cat`/`sed` via
  Bash — they're drift guardrails, not security walls. Per-machine
  "don't ask again" accumulation goes in `.claude/settings.local.json`
  (gitignored), never the tracked file.
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

(One-liners; full notes live in METHODOLOGY §6. Prices/EVs quoted here
are the vintage at which the note was written — read the latest
`outputs/delta_report.md` for live position + FV; don't "fix" a
quick-ref price unless the note itself is being updated.)

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
  employment table lives in the 10-Q MD&A. **LIVE DEAL (updated 2026-06-21):
  Diana LOST the Jun-18 proxy fight — all 6 Genco nominees re-elected, pill
  ratified, hostile path now structurally blocked. Diana did NOT withdraw:
  $24.80 all-cash tender still live to Jun-26 + non-binding $27.34 cash+stock
  under board review. Price de-rating below the cash leg (~$23.66). Framing
  migrating deal-arb → NAV-discount but still event-contingent until Jun-26;
  hold BUY as event-contingent, not a clean NAV-discount signal. On a tender
  lapse with no deal, drop the overlay and expect reversion toward the pre-bid
  0.66-0.75× Pareto-NAV regime. See gnk_log 2026-06-21.**
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

- **MPCC** — 1st containerships validator (Oslo/NOK; `yahoo_symbol:
  MPCC.OL`). 51 on-water (21 feeder / 30 intermediate, ~129k TEU) + 15
  OWNED NB rows at the CAPT §3.1 net-of-commitment convention ($633.7M
  commitments; Uthalden JV pair excluded both sides). Coverage 99/69/41%
  of 2026/27/28 days fixed → coverage_schedule; ~50%-of-adj-profit
  dividend (policy_type variable). NAV $2.27, TRIM EV −29.6% at NOK
  26.42 (= USD $2.78 carried in the watchlist, CAPT NOK machinery).
  APPROX anchor = company-implied NAV NOK ~25.5 (Jul-25, stale);
  Pareto covers on EV/EBITDA only (HOLD TP NOK 25). §15.7 DECLINED
  (fees 0.6%/yr GAV, payout channel wide open). KNOWN SOFT: cohort age
  ESTIMATES (deck has no built years) + NB delivery quarters — refine at
  Q2 (reports 2026-08-26). §11.8.5(b) marks-tilt ledger row ACTIVE; its
  3 disclosed sale prints show tool old-age marks 0-33% BELOW realized
  (deliberate, conservative). Onboarded 2026-06-12.
- **GSL** — 2nd containerships validator, the charter-book stress test.
  71 vessels (0 feeder / 30 intermediate / 41 large; 18.2-yr
  TEU-weighted), full per-vessel charter table from the 6-K PR;
  coverage_schedule computed at mid-redelivery cross-foots disclosed
  100%/86%. Coverage dampening visible: scenario FV spread only ±10%.
  NAV $38.59 (prefs $109M subtracted), TRIM EV −18.5% at $38.99; tool
  fleet 22% BELOW cost book (§11.8.5(b) row). APPROX = P/B proxy, WEAK.
  §15.7 dimension-6 charter-affiliation pass DECLINED: CMA CGM equity
  ZERO since 2022-08-05, 13/71 vessels (#2 behind Maersk 24) — tripwires
  incl. the Jun-26 $917M NB order's undisclosed charterers (Q2 check).
  NB order is POST-snapshot — Q2 item. Onboarded 2026-06-12.

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

- **2026-06-21 — B6 §9.2 terminal-value multiple LOCKED at 1.0× (owner decision).**
  Closes the last open Week-5 item. Owner ratified the memo recommendation
  (`outputs/terminal_value_options_memo.md`): keep the q9 terminal at 1.0× ×
  aged-NAV — `w_earn` + the conservative transaction-anchored marks already carry
  the cycle view, the sweep flips are immaterial band-edge wiggles, and the
  alternatives are flawed (uniform 0.9× wrong at troughs; 1.1× = forbidden
  calibrate-to-broker). Cycle-conditional recorded as the designated successor,
  revisited only on an adoption trigger. No engine change (1.0× was production);
  now PINNED by `tests/test_dividend_strip.py::test_terminal_nav_multiple_locked_at_1x`
  (locked-weights idiom — changing it needs a deliberate memo + test edit).
  §9.2 item 2 marked *resolved*; memo DECISION block filled; dividend_strip.py
  constant comment updated. tests: +1 (the pin); full suite 283 passed (the two
  reconcile state-tests un-skip now that `state/last_run.json` is fresh).
- **2026-06-21 — DEVELOPMENT FREEZE LIFTED (owner decision).** The 2026-06-14
  freeze (which gated all feature/sector/methodology work on a crude-backtest
  "edge" verdict) is removed. Rationale: this is a forward-looking valuation aid
  for picking/valuing individual shipping names, not a cross-sectional quant
  portfolio, so a cross-sectional IC backtest is not the right gate — and the
  backtest's null is an expected small-sample result, not a refutation of the
  per-name work. The freeze DECISION RECORD at the top of CLAUDE.md was replaced
  with a forward-looking project-stance note; PLAN.md was rewritten from a
  backtest-gate plan into the live forward plan (Week-5 hardening status + active
  backlog), with the backtest demoted to a reference section. The `backtest/`
  artefacts (PRE_REGISTRATION.md, REPORT.md) are retained as a recorded
  diagnostic — accurate history, no longer a gate. (Unrelated uses of "frozen"
  for stale data archives/vintages — container feed, MB anchor — are untouched;
  they mean a stale feed, not the dev freeze.)
- **2026-06-21 (Week 5) — B6 §9.2 terminal-value options memo WRITTEN (owner
  decision pending).** Re-ran the terminal-NAV-multiple sweep over the full
  19-name watchlist (`scripts/terminal_value_sensitivity.py`; was 12 names at
  the Jun-5 first run) → 7 band-edge flippers (0.9× turns peak names DHT/ECO
  more bearish; 1.1× turns ASC/SBLK→HOLD + GNK→BUY [deal-pinned, discount];
  12/19 never flip; CCEC most sensitive but holds BUY). Wrote
  `outputs/terminal_value_options_memo.md`: four options (1.0× / 0.9× / 1.1× /
  cycle-conditional), each steelmanned by an independent agent panel, with an
  empty owner DECISION block. **Recommendation: ratify 1.0× now** (auditable;
  marks already conservative; `w_earn` already down-weights the strip at peak —
  the at-stake flips are immaterial band-edge wiggles), **cycle-conditional as
  the designated successor** pending two adoption triggers (empirically-sized
  embedded-mark error, or the book gaining trough-band names); **reject uniform
  0.9×** (wrong sign at troughs — dominated by cycle-conditional) **and 1.1×**
  (its broker-gap justification is the forbidden "calibrate to broker" move,
  §6/§9). Key mechanism point: the terminal = current marks aged forward (never
  re-priced), so the multiple sets the *embedded asset-price level* — orthogonal
  to `w_earn`, which only weights the leg; §15's `governance_discount_pct` is the
  architectural precedent for a multiplier at this layer. No engine change (rec
  is status-quo); `TERMINAL_NAV_MULTIPLE` stays 1.0. §9.2 item 2 + PLAN.md B6
  updated to point at the memo. Was a parked Week-5 item; resumed at owner
  direction.
- **2026-06-21 (Week 5) — B5 anchor-basis commensurability SHIPPED** (commit
  5fc3b7d). Cycle-position anchors carry three non-composable bases (a cycle
  ratio is forward-12M-TC / anchor): `tc_10yr_mean` (crude/product/lng),
  `archive_22mo_median` (dry_bulk), `fy_calendar_avg` (containerships). Every
  `cycle_anchors` block in `scenario_inputs.yaml` now declares an `anchor_basis`
  enum (12 added; containerships' 3 prose tags normalized). Shared helpers in
  `scenarios.py` (`all_sector_anchor_bases` / `detect_mixed_anchor_basis` /
  `format_mixed_anchor_basis` / `ANCHOR_BASIS_LABELS`) drive a **MIXED-ANCHOR-
  BASIS** flag on the two cross-sector surfaces: the delta-report table
  footnote and the `reconcile --all` footer (per-name basis shown in
  `--verbose`); `--sector` / single-name runs use one basis so never flag.
  METHODOLOGY §10 gains the three-basis subsection. Metadata + diagnostics
  ONLY — the engine reads just `ten_year_mean`, ignores the new key, so the
  valuation core is untouched (FV-band + cycle/blend pins unchanged). Tests
  +5 (3 scenarios, 2 delta) → 280 passed, 2 skipped. The B5 commit was kept
  to the 7 source/doc/yaml/test files; the verification pipeline run's
  regenerated outputs + routine decision-log stubs were reverted (they
  regenerate on the next real refresh). Was a parked Week-5 item; resumed at
  owner direction with the freeze set aside.
- **2026-06-12 (Week 5) — MB Weekly 24 prints PROMOTED (owner decision,
  7 prints recategorized per owner review) + drift loop run.** Fit
  inputs: **Seamusic** (Aframax age-17 $52.5M, in-window WITH
  premium-channel note — buyer screen: undisclosed buyer + immediate
  rename to VIRTUS MARIS + no ice notation = NOT confirmed-clean;
  single-print drift GATE passed: 5yr −3.6%/10yr +0.1%/slope negative,
  no flip on the print alone; REVISIT if no second clean corroborating
  print by Q3), Vulcania (Pana n=4→5, TC-ATTACHED caveat — residual
  could be entirely the charter), Ausone + Santa Rita (Supra-Ultra,
  curve-bracketing pair). Documentation-only (owner recategorization —
  original note overstated): Proteas (age 21 — old-age-leg validation
  DEAD-ON, the Picardy/Predator pattern; NOT fit thickening), White Bay
  (age 22), Shanhaiguan (age 0 NB; Dalian print on a Korean-spec anchor
  = conservative-to-fair, not validated-exactly). Drift loop: ONE flip
  — SBLK TRIM/SHORT→HOLD (+1.1% NAV; Pana fit +6.9/+3.0 → +11.5/+7.5;
  band-edge third oscillation, leans on the TC-attached print — sblk_log
  annotated, no size action). Ethanol/corn driver re-routed from
  demand-destruction overlay to dry-bulk scenario tree
  (framework_breakers entry — sector-structural ≠ macro recession).
  Tests 277 green, no re-pins. Fit counts: Aframax 13 / Pana 5 /
  Supra-Ultra 22.
- **2026-06-12 (Week 5) — MB weeklies first direct delivery: ingest route
  built + three-sector once-over run (review-only, nothing promoted).**
  Container/Dry Bulk/Tanker Weekly 24 archived to `inputs/research_mb/`
  (LNG not delivered — verify subscription); route = Gmail link harvest →
  fetch_pdf.py (cdn.flxml.eu added to data_sources.yaml
  `mb_shipbrokers_weeklies`). Findings in
  `outputs/mb_weekly_check_2026-06-12.md`: (1) container — frozen 10
  weeks hid a feeder rally (+13.4%, position 0.98x→1.12x; MBCI +13.9%;
  intermediate/large drift normal; marks layer current; MPCC most
  exposed) → owner-gated `twelve_month_tc.yaml` container refresh queued;
  (2) tanker — MB 5yr assessments land 5/6 classes inside
  TXN_PURE_PLAY_K_BAND over our txn marks (first INDEPENDENT
  confirmation of the B4 band semantics), but crude NB anchors read
  14-35% above MB Korea NB with a 5yr>NB prompt inversion (review item);
  Hormuz trigger NOT met (draft memo, 30-day window, conditions — the
  closest signal yet); (3) dry bulk — txn marks validated by MB's own
  prints (Proteas $12.10M dead-on the age-21 Pana curve), Supra
  assessment gap = basis not error, **Pana anchor flagged structurally
  LOW** (MB 5yr tenor never below ~16k vs anchor 11.9k — Q3 refinement +
  B5 xref). 7 promotable print candidates queued (Seamusic Aframax
  $52.5M ~65% above fit; Shanhaiguan NB resale $90M; Vulcania/Proteas
  Pana; 3 Supra-Ultra) — promotion human-only, each triggers the
  prints→rerun→drift loop.
- **2026-06-12 (Week 5, Session A) — B4 shipped: mark-driven classification
  restated to post-flip k_broker semantics + fetch_links argparse fix.**
  Two-regime definition landed in METHODOLOGY §9 item 9: txn-anchored
  sectors (crude/product/dry bulk) — mark-validated = k_broker inside the
  uniform pure-play band `TXN_PURE_PLAY_K_BAND = (1.05, 1.25)` (constants
  in `marks.py`, uniformity < 0.05; DHT/ECO/FRO 1.12-1.14 at the Jun-2026
  fit, ~+13-17pp spread EXPECTED); mark-driven = outside the band either
  side. Un-anchored sectors (LNG/containerships) keep the original ≈1.0
  reading. Broker-sweep Read column relabeled MECHANICAL
  (`wide-spread`/`narrow-spread`, owner decision) — it had been printing
  the canonical validators DHT/ECO/FRO as "mark-driven" at their expected
  band premium; §6 prose is the canonical classification. Dated
  restatements appended to §6 INSW/TNK/ASC/STNG/HAFN/SBLK, §7.5, §9
  item 10, §15.2; LIMITATIONS §1 definition updated. No mark changes —
  pipeline re-run diff was text-only, delta 0 material, reconcile 19/19.
  fetch_links: zero-option argparse front door (`--help` exits 0
  pre-network, unknown flags exit 2 — closes the Week-4 §5 observation);
  no-arg cron path unchanged. tests: 274 → 277.
- **2026-06-12 (post-Week-4-close) — brokerage MCP decision REVISED:
  keep the IBKR connector attached, DENY it in Claude Code.** The
  Week 4 owner action ("detach entirely") is superseded: the connector
  feeds a weekly Cowork portfolio routine + ad-hoc Chat discussion, and
  claude.ai connectors are account-level all-or-nothing (no per-surface
  Chat/Cowork/Code scoping exists; Code's `deniedMcpServers` doesn't
  match cloud-synced connectors). DENY rules on the synced server id
  (`mcp__8de167eb-dbd9-4178-b52a-a756c1f27b24`) added to
  `~/.claude/settings.json` (machine-wide) AND the tracked
  `.claude/settings.json`. Deny, not ask — the §5 red-team proved
  autonomous sessions auto-approve ask-tier. Verified live same
  session: read-only `get_account_summary` probe refused at the
  permission layer (deny rules hot-reload mid-session). CAVEAT: if
  IBKR is disconnected/reconnected at claude.ai, the UUID may change
  and the deny goes silently stale — re-check the id in a fresh
  session's tool list. Full rationale: PERMISSIONS_PROPOSAL.md §6.4
  revision note. Same session: `settings.local.json` pruned 262 → 38
  allow entries (arbitrary-write/interpreter/credential-exposing
  allows, ffmpeg-era strays, ask-tier-bypassing curl/launchctl
  carve-outs, tracked-allowlist duplicates, stale one-offs).
- **2026-06-12 (Week 4, Step 3 — WEEK 4 CLOSED)** — Week-close checklist
  run. **§5 red-team pass (first session with the allowlist active):
  DENY rules ENFORCE** (env-file Read refused, `rm -rf` refused);
  allow-tier friction-free (pytest, reordered-flag sp_scan, outputs
  edit, sec.gov WebFetch — probes 7-10 clean); **ASK tier NOT testable
  in an autonomous session** — the autonomous permission mode
  auto-approves ask-class calls (curl with no matching rule executed;
  watchlist Edit applied + immediately reverted; fetch_links ran), so
  the prompt half of §5 carries to Week 5 as an INTERACTIVE-session
  item. Real finding, fixed: `Bash(git push *)` had accumulated in
  `.claude/settings.local.json` as a blanket allow — it defeated the
  tracked ask-on-push policy in EVERY session, not just this one —
  pruned. Two new leak observations recorded: `git -C <path> push`
  dodges the `git push` prefix matcher (the -C variant of the
  flag-reorder leak), and fetch_links ignores unknown flags (`--help`
  ran a real pass; dedupe held, 0 downloads — argparse fix queued
  Week 5). **Verification gate: 274 passed; pipeline clean (0 material,
  0 input changes); `/reconcile --all` 19/19, 0 SANITY FAIL, 0 drift
  alerts.** Documentation audit (two read-only agents, fixes applied in
  main session): README 17→19 names / 4→5 sectors / 243→274 tests +
  containerships watchlist table + METHODOLOGY line count ~720→~2,900;
  METHODOLOGY §1 coverage header 19/5, stale "Week 4 candidate" lines
  closed, **§11.8.6.4 horizon header corrected "12 quarters"→"10 strip
  quarters"** (body and Appendix A already said 10; owner ratification
  of the A1 interpretation still pending); LIMITATIONS gains the
  containerships-CLOSED sector entry, the §11.8.5 stale-vintage +
  old-age-tilt OPEN limitation, the APPROX consensus_pnav list
  completed to all SEVEN names with actual bases (audit agent's
  suggested values were wrong — re-verified against watchlist.yaml
  before applying), §15 declined list completed
  (TNK/CCEC/CAPT/MPCC/GSL), validator list extended to all 5 sectors.
  Quick-ref preamble gains the vintage-prices note (quick-ref prices
  are note-vintage, not live — stop "fixing" them). PLAN.md rewritten
  for Week 5 (B4/B5/B6 + Q2 carry-forwards per owner direction).
  OWNER ACTIONS re-flagged: brokerage MCP connector was STILL attached
  in this session (order-writing surfaces reachable); A1 horizon
  ratification.
- **2026-06-12 (Week 4, Step 2 + maintenance)** — **CONTAINERSHIPS SHIPPED:
  engine (per-sector `strip_horizon` + `coverage_schedule`, zero-drift
  verified on all 17 prior names), Container Set A wiring (A2 class
  signatures, A3 TEU-weighted intermediate $43,400/$33,700 applied at
  onboarding), MPCC + GSL onboarded (19 names, SANITY 0 FAIL, both
  n/a-APPROX), §15.7 screens both DECLINED (GSL = the dimension-6
  charter-affiliation founding pass: CMA CGM equity zero since 2022,
  13/71 vessels), calibration lock recorded N/A-by-construction
  (machine-confirmed; primary substitute = MPCC's 3 disclosed sale
  prints — tool old-age marks 0-33% BELOW realized, conservative by
  design).** Maintenance landed: B1 overlay ledger (§16, 11 active
  rows), B2 §14.4 double-count warning, B3 all 10 weight-skips
  re-pinned (DHT wnav-vs-base direction REVERSED under Jun-9 weights).
  SESSION-LOG NOTES: (a) A1 horizon — owner brief said "~12q from
  report date"; under the repo's q3_2026 strip-start convention,
  end-2028 = **10 strip quarters** — wired as 10, flagged for owner
  review; (b) MPCC cohort AGES and NB delivery quarters are ESTIMATES
  (deck discloses no built years) — refine at Q2 (2026-08-26); (c) GSL
  analyst_target/consensus_pnav are book-based placeholders (CMDB
  convention) — replace if VIE coverage surfaces; (d) PR #2 reviewed +
  worktree-verified, MERGED by owner same day (entry below); changelog
  conflict resolved additively at integration. Tests 243 → 274. Full
  detail: METHODOLOGY Appendix A 2026-06-12.
- **2026-06-11 (Week 4, Step 1)** — **§11.8 containerships methodology
  decision doc LOCKED** (time-boxed one session, doc before code, dry-bulk
  §11.7 as template). Decisions: 3-class collapse (ctr_feeder ≤2,000 /
  ctr_intermediate 2,000-5,500 / ctr_large >5,500, WB variants excluded
  from class averages); **charter-book convention = coverage-schedule
  generalization of the §3.2 blend** (strip earns disclosed contracted
  rates through expiry via per-quarter cov_q, re-fixes at scenario rates;
  NAV stays on-curve at bare marks; charter premium/discount = v1
  limitation), NOT §11.6 off-curve; Container Set A scenarios
  0.25/0.40/0.20/0.15 (disruption_persists / gradual_normalization /
  normalization_plus_overhang / demand_recession); cycle anchors from the
  weekly's FY21-25 table NOT the boom-only 19-month archive median
  (feeder $20,850 / intermediate $32,300 / large $41,000 → positions
  0.98x/1.30x/1.53x at the Apr-01 vintage); **external anchor: NONE —
  all-APPROX sector** (verified: Pareto's own liner table dashes MPCC's
  P/NAV; they value the space on EV/EBITDA) → v1 calibration lock
  recorded N/A-by-construction with VIE + marks-consistency substitutes;
  validators MPCC + **GSL** (DAC deferred — Capesize hybrid, same logic
  as CMRE). Empirical basis: mechanical extraction of all four data
  tables across the 42-issue MB archive (40-42/42 parse rate). Key
  fresh source found on disk: Pareto MPCC quarterly review 2026-05-28
  (HOLD, TP NOK 25, 99/69/41% of 26/27/28 days fixed, $2bn backlog).
- **2026-06-12 — Permission allowlist shipped (`.claude/settings.json`,
  tracked) + fetch_links module split + fetch_pdf.py wrapper.** Full
  rationale in `PERMISSIONS_PROPOSAL.md` (decision record). Narrow
  allows for the constant loop (pytest/reconcile/pipeline/refresh/
  sp_scan/price_refresh, git add/commit, WebFetch to the
  data_sources.yaml host set); ask on git push, fetch_links,
  ingest_rocketchat, curl, launchctl, and the three human-only
  promotion surfaces (watchlist vintage / transactions / FFA curve —
  the TEN-$44 and promotion rules turned mechanical); deny on
  credential-shaped reads. Two structural changes: `--fetch-links`
  moved out of sp_scan into `crude_tanker_fv.fetch_links` (Bash rules
  are prefix matchers — a network flag on an allowed module leaks when
  flags are reordered, so the boundary is now a module boundary;
  news_pull_cron.sh updated), and `scripts/fetch_pdf.py` replaces the
  ad-hoc curl pattern (host-validated against data_sources.yaml in
  code; carries the single audited Okeanis TLS exception). Brokerage
  MCP decision: detach from Claude Code entirely (owner action),
  not deny-rules. New "What NOT to do" rule on widening the allowlist.
  *(Ordering note: this entry lands between Step 1 and Step 2 of Week 4
  chronologically; merged after Step 2 completed — see the entry above.)*
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
