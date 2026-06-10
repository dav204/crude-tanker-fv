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
- **VIE Coverage Universe** (Catlin / Mintzmyer) is an independent
  external check, not a calibration input. Track stance disagreements in
  §6 footnotes; do NOT bulk-update from VIE without an explicit
  methodology decision per class.

## Recurring gotchas to NOT relearn

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
  fits as of 2026-06-10: VLCC (10 in-window), Suezmax (18),
  Aframax (12), **LR2 (11 — own-fit; the Aframax-proxy alias is retired)**,
  MR (21), Cape (25), Pana (4), Supra-Ultra (17). Primarily mined from
  the Pareto Shipping Daily archive via `sp_scan.py`; GNK's 10-Q added 4
  issuer-confirmed Cape prints at onboarding. DO NOT add other
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
   decision log entry. (Coming end of Week 0.)
2. Pull the latest 6-K / 20-F / press release; fill in the fleet manifest,
   balance sheet, cost structure, dividend policy (METHODOLOGY §8.1).
3. Add the watchlist row (current_price, analyst_target, consensus_pnav,
   consensus_fwd_pe, sector, as_of).
4. Run pipeline + tests + `/reconcile <TICKER>`.
5. If SANITY=OK, close the decision log entry with the reconciliation gap
   recorded as the baseline for future drift detection. If SANITY=FAIL,
   **stop and investigate** — don't paper it over.

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
- **INSW** — mark-driven (k_broker 1.37); hybrid crude+product carve-out.
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
  (governance/value-trap haircut at 30%). Asset NAV $88.56, post-haircut
  PW FV $49.37 vs price $44 → mild BUY (matches VIE Bullish $51.50 within
  $2). APPROX consensus_pnav (no Pareto coverage; VIE-stale anchor).
  Onboarded 2026-06-06.
- **SBLK** — first dry-bulk validator (Cape 31 / Pana 46 / Supra-Ultra 58
  post-Eagle-Bulk fleet, §11.7.1 class collapse); mark-driven (k_broker
  1.27 at v1, 1.27 post-transaction-anchor — the recalibration shifted
  the gap by 0.6pp, confirming the −21% spread is methodological, not a
  curve artefact). Cape was understated (+18%/+12% at 5/10yr), Supra-Ultra
  overstated (−10%/−13%), Pana roughly calibrated. Transaction sample:
  Pareto Shipping Daily archive + SBLK Q1 2026 6-K Star Stonington
  ($19.6M). Tool TRIM/SHORT, broker BUY. Onboarded + transaction-anchored
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

## The compounding-knowledge habit

Anytime the agent makes a mistake that wasn't caught by these rules,
append a dated rule to the relevant section. Ruthlessly edit until the
mistake rate visibly drops. This file is checked into git; rules survive
sessions.

## Changelog

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
