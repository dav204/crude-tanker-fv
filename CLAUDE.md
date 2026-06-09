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
- **Transaction-anchored recalibration** is populated for VLCC, Suezmax,
  Aframax, MR (with own fits) + LR2 (data file but proxies to Aframax
  until ≥2 prints). DO NOT add other classes (LR1, Handysize, LNGC, MGC,
  bulk classes) to this pipeline without an analogous transaction sample
  of comparable quality (§9.9 scope discipline).
- **Two structural framework limitations are now codified**: §12 (high-payout
  pure-plays at peak — tool UNDERvalues because dividends are the thesis;
  NAT archetype) and **§15 (governance/value-trap discount — tool OVERvalues
  because asset NAV won't be realised; TEN archetype, schema knob
  `governance_discount_pct` on BalanceSheet, default 0.0, applied at blend
  layer + strip terminal but NOT to `compute_nav`)**. They are inverse
  cases of the same NAV-vs-realisation gap. The haircut is judgmental,
  not parametric — store it auditably per-name with a rationale.

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
