# Tanker & Gas-Carrier Fair Value Tool

Independent fair-value estimate per share for tanker and gas-carrier equities,
built to validate and stress-test sell-side analyst targets across the
**crude / LNG / product** segments. Blends two lenses — net asset value (NAV)
and a forward dividend strip — with the blend weight set by cycle position,
then runs five-scenario sensitivities, a broker-NAV sweep, and a
transaction-anchored curve diagnostic. **Not investment advice.**

See [METHODOLOGY.md](METHODOLOGY.md) for the full framework (~2,900 lines);
this README is orientation for someone landing on the repo cold.

## Status (2026-06-12)

- **19 tickers** across 5 sectors: crude (8, incl. **TEN** the 3-sleeve hybrid and
  **CAPT** the first Oslo/NOK listing), LNG (2), product (4), dry bulk (3),
  containerships (2)
- **274 tests passing** end-to-end
- **7 output families** regenerated per pipeline run + 5 standalone diagnostics
  (LNG weight robustness, crude weight robustness, VIE coverage universe xref,
  VIE market rates xref, terminal-value sensitivity)
- **Onboarded sector validators:** DHT (crude) / FLNG (LNG) / ASC (product) /
  SBLK + GNK + CMDB (dry bulk, 2026-06-09/10) / MPCC + GSL (containerships,
  2026-06-12 — first charter-coverage sector); TRMD added 2026-06-03 (first
  full-3-class product), HAFN 2026-06-04 (first IFRS + pool operator), CAPT
  2026-06-11 (17th name, newbuild-heavy crude, tightest first reconcile on record)
- **Locked weight families:** crude Set A (current); LNG Set B-revised v3
  (2026-06-01, §11.3); product Set B v2 (2026-06-03, §11.5)
- **Framework limitations now documented:** §12 (high-payout pure-plays at
  peak), §13 (scenario-weight stability), §14 (MEG export infrastructure
  + cargo switching + sanction waiver + stockpile replenishment dynamics),
  §10 (TC-vs-spot baseline methodology + VIE within-window structural
  adjustment refinement), §11.6 (DP2 shuttle off-curve-at-contracted-book
  convention — closes the TEN architectural blocker), §15 (governance /
  structural-NAV-trap discount — the inverse of §12; first applied to TEN
  at 30% haircut for controlled-FPI + related-party + low-payout drivers)
- **External counter-signals tracked:** VIE Coverage Universe cross-reference
  (Catlin / Mintzmyer) — full 10-of-10 overlap; CCEC / ASC / TRMD / HAFN
  direct opposite-direction signals documented in §6 footnotes

## What this tool does

1. **Per-name fair value.** For each ticker on the watchlist, compute a tool
   fair value per share by blending NAV (per-vessel age-curve marks, balance
   sheet adjustments, newbuild orderbook valued at delivered-market-less-
   remaining-commitments) and a forward dividend strip (8 quarters of EPS →
   DPS → discounted DPS, with a terminal NAV). Cycle-position weighting shifts
   the blend toward NAV at peak and toward earnings at trough.

2. **Scenario sensitivity.** Each sector has 4-5 macro scenarios with their
   own probability weights, vessel-value multipliers, and forward curves. The
   crude sector uses a three-phase MoU framework (escalation / pre-MoU
   baseline / MoU base / MoU bear); LNG runs glut-cycle scenarios with a
   `vessel_scale_multiplier`-driven structural-reset tail; product runs
   refinery-margin / glut scenarios.

3. **Decision-relevant diagnostics.** The pipeline surfaces (a) the implied
   breakeven TCE that justifies the current price (and how far above the
   forward curve it sits), (b) a 5×5 sensitivity heatmap (rate shock × vessel-
   value shock), (c) a broker-NAV sweep showing how mark-driven each call is
   (the `k_broker` premium that lifts tool NAV to consensus NAV — wide spreads
   signal mark-uncertain names; tight spreads signal mark-validated ones),
   and (d) a transaction-anchored curve recalibration toggle that re-fits
   mid-age curve anchors against disclosed second-hand transactions.

4. **Pre-flight + post-flight workflow.** A `refresh` command emits a
   pre-flight checklist of what's stale or missing for the target quarter
   (with IR URLs to pull from); the pipeline emits a post-flight delta
   report (what changed since last run) and prepends a structured
   model-state entry to a per-ticker decision log where you annotate what
   you actually did and why.

## What this tool is NOT

Pre-empting the "where does this go wrong?" question — see
[LIMITATIONS.md](LIMITATIONS.md) for the full set with detail. Headlines:

- **Not investment advice.** The tool produces a fair-value estimate; the
  decision is yours. Documented framework limitations (§12) exist for
  high-payout cyclicals at peak — see NAT and STNG entries in METHODOLOGY §6.
- **Not real-time.** Inputs are point-in-time per quarter. The tool is for
  decision support around Q-end earnings, not intraday rate moves.
- **Not API-stable.** The Python modules are private surface; treat them
  as research scaffolding, not a contract. Input YAML schemas are
  documented (METHODOLOGY §4) but may evolve.
- **Not multi-user.** No auth, no permissioning, no API endpoint. This is
  single-user research infrastructure.
- **Not a Bloomberg / Clarksons / VesselsValue replacement.** The tool
  consumes data from those sources (vessel value curves, broker NAVs); it
  doesn't substitute for them.
- **Coverage scope: Handysize-and-above clean product + Chemical Handymax.**
  Clean-product Handysize (~37-40k) and Chemical Handymax (38k IMO-II coated)
  are now ON-curve as of 2026-06-05 — HAFN's 22, ASC's 2, and STNG's 14 hulls
  migrated from `working_capital_net`. Residual gaps: ASC's 4 × 25k stainless
  chemical hulls (sub-25k specialty pool, off-curve) and pure-chemical parcel
  operators above Handysize (Stolt-Nielsen / Odfjell — un-onboardable until a
  stainless-Handymax curve at the Odfjell-NB $72.5M anchor lands). DP2 shuttle
  tankers were RESOLVED via the §11.6 off-curve-at-contracted-book convention
  (TEN onboarded 2026-06-06); dry bulk is IN-scope as of 2026-06-09 (§11.7,
  SBLK/GNK/CMDB); containerships are IN-scope as of 2026-06-12 (§11.8,
  MPCC/GSL — coverage-schedule charter framework, all-APPROX external
  anchors). Offshore remains out of scope.

## Current watchlist

**Crude sector (`sectors.crude` — three-phase MoU framework):**

| Ticker | Company | Fleet shape |
|---|---|---|
| DHT  | DHT Holdings | Pure VLCC (22 vessels) — crude methodology validator |
| ECO  | Okeanis Eco Tankers | Modern VLCC + Suezmax, all-spot, eco design |
| FRO  | Frontline | VLCC + Suezmax + LR2; 9 Hemen VLCC NBs newbuild-at-market |
| INSW | International Seaways | Hybrid crude + product (whole-company v2 carve-out) |
| TNK  | Teekay Tankers | Atlantic-skewed: Suezmax + Aframax/LR2 + 1 VLCC |
| NAT  | Nordic American Tankers | Pure Suezmax (18 vessels) — §12 framework-limitation case |
| TEN  | Tsakos Energy Navigation | 3-sleeve hybrid: crude + product + LNG (60 in-water + 19 NBs); 4 DP2 shuttle off-curve via §11.6 convention; §15 case (30% haircut) |
| CAPT | Capital Tankers | 12 VLCC + 10 Suezmax + 4 Aframax + 4 LR2; 21 NBs at delivered-market-less-commitment; Oslo/NOK (added 2026-06-11) |

**LNG sector (`sectors.lng` — glut-cycle framework):**

| Ticker | Company | Fleet shape |
|---|---|---|
| FLNG | Flex LNG | 13 modern 174k cbm LNGCs (MEGI / X-DF) — LNG methodology validator |
| CCEC | Capital Clean Energy Carriers | 12 LNGCs + 9 LNG NBs + 1 MGC + 8 gas NBs |

**Product sector (`sectors.product` — refining-margin / glut framework, unlocked 2026-06-01):**

| Ticker | Company | Fleet shape |
|---|---|---|
| ASC  | Ardmore Shipping | 19 active MRs + 6 off-curve Handysize/chem — product validator |
| STNG | Scorpio Tankers | 32 LR2 + 41 MR on-curve + 14 Handymax off-curve + 10 NBs (incl. 2 VLCC) |
| HAFN | Hafnia | Largest product fleet (~120 incl. pools); IFRS reporter |
| TRMD | Torm | First full 3-class product (LR2 + LR1 + MR) |

**Dry bulk sector (`sectors.dry_bulk` — Bulk Set A, unlocked 2026-06-09):**

| Ticker | Company | Fleet shape |
|---|---|---|
| SBLK | Star Bulk Carriers | 135 bulkers (Cape 31 / Pana 46 / Supra-Ultra 58) — first dry-bulk validator; §6 mark-driven |
| GNK  | Genco Shipping | 44 bulkers (Cape 19 / Supra-Ultra 25, no Pana) — VALIDATES the txn-anchored curves (k 1.04) |
| CMDB | Costamare Bulkers | 30 owned older bulkers + P&L-only chartered-in platform; §15 case (30% haircut), APPROX anchor |

**Containerships sector (`sectors.containerships` — Container Set A,
coverage-schedule charter framework, unlocked 2026-06-12):**

| Ticker | Company | Fleet shape |
|---|---|---|
| MPCC | MPC Container Ships | 51 on-water (21 feeder / 30 intermediate) + 15 owned NBs net-of-commitment; Oslo/NOK; first containerships validator |
| GSL  | Global Ship Lease | 71 vessels (30 intermediate / 41 large, 18.2-yr TEU-weighted); full charter table — the coverage-convention stress test; APPROX P/B anchor |

## Sample output: broker-NAV sweep

_Illustrative snapshot from the 2026-06-04 vintage (13 names); the live
19-name table regenerates every run at `outputs/broker_nav_sweep.md`._

The diagnostic that distinguishes mark-validated calls from mark-driven ones.
Per name: `k_broker` is the uniform vessel-mark premium that lifts tool NAV
to the consensus broker NAV (= price ÷ consensus P/NAV). The EV%-spread is
how much of the call is value vs mark choice.

| Ticker | Cons. P/NAV | k_broker | EV @ tool | EV @ broker | Spread | Read |
|---|---:|---:|---:|---:|---:|---|
| DHT  | 1.09 | 0.99 | -18.7% | -19.8% | -1pp  | mark-validated |
| ECO  | 1.22 | 0.99 | -32.4% | -33.2% | -1pp  | mark-validated |
| FRO  | 1.21 | 0.99 | -30.8% | -31.4% | -1pp  | mark-validated |
| STNG | 0.87 | 1.10 | -13.0% | -5.9%  | +7pp  | mostly mark-validated |
| CCEC | 0.90 | 0.98 | +14.1% | +5.0%  | -9pp  | mark-validated, weight-driven BUY |
| TNK  | 0.76 | 1.18 | -1.7%  | +8.0%  | +10pp | mark-driven |
| FLNG | 1.42 | 0.87 | -7.2%  | -28.3% | -21pp | tool above broker |
| INSW | 0.97 | 1.37 | -32.2% | -10.1% | +22pp | mark-driven |
| ASC  | 0.75 | 1.59 | -26.5% | +13.1% | +40pp | mark-driven |
| NAT  | 0.85 | 1.79 | -57.8% | -5.2%  | +53pp | mark-driven + §12 case |

A 0pp spread means the call is the same at tool marks and broker marks; a
wide spread means the call would flip under reasonable mark choices.
Mark-validated bucket = the tool's NAV machinery agrees with broker
consensus on the assets it covers. Mark-driven bucket = the call is
dominantly a question of which vessel marks you believe.

## The two-command workflow

```sh
# Start of quarter (or whenever something feels stale):
python -m crude_tanker_fv.refresh           # → outputs/refresh_checklist.md
#   Scan the checklist; pull missing balance sheets via the IR URLs it lists;
#   update stale market data files; refresh APPROX consensus_pnav entries.

# After data assembly:
python -m crude_tanker_fv.pipeline 2026-Q1  # → 7 output families
#   Then open outputs/delta_report.md for the "what changed" summary,
#   and annotate decisions/{ticker}_log.md with your calls.
```

The 7 output families per pipeline run:

| Output | What it answers |
|---|---|
| `{ticker}_fv_report.md` + `.xlsx` | Single-point FV with full NAV breakdown, dividend strip, breakeven, 5×5 sensitivity (per name) |
| `{ticker}_scenarios.md` | Probability-weighted FV across the sector's scenarios, with EV% and position recommendation (per name) |
| `fair_value_summary.xlsx` | Watchlist roll-up: tool FV vs current vs analyst target, all names in one table |
| `scenario_summary.xlsx` | Per-sector scenario sheets + cross-name pair-trade implied returns |
| `broker_nav_sweep.md` + `.xlsx` | The mark-validated vs mark-driven discrimination diagnostic (shown above) |
| `transaction_anchor_comparison.md` + `.xlsx` | NAV / EV impact of applying transaction-anchored mid-age curves (Aframax + Suezmax) |
| `delta_report.md` + `decisions/{ticker}_log.md` | What changed since last run + per-ticker decision log with structured model-state entries |

## Architecture at a glance

```
src/crude_tanker_fv/
  schemas.py         input data structures               (METHODOLOGY §4)
  loaders.py         YAML input loaders                  (§4)
  vessel_values.py   per-class age-curve marks           (§3.1)
  nav.py             NAV per share                       (§3.1)
  dividend_strip.py  forward dividend strip              (§3.2)
  cycle.py           cycle-position weighting            (§2.3)
  blend.py           blended fair value                  (§2.1-2.2)
  breakeven.py       implied breakeven TCE               (§3.3)
  sensitivity.py     5×5 sensitivity grid                (§3.4)
  scenarios.py       scenario engine + sector class maps (§11)
  carveout.py        hybrid crude+product carve-out      (§6)
  marks.py           broker-NAV sweep + k_broker solve   (§9.9)
  transactions.py    transaction-anchored curve recalibration (§9.9)
  validate.py        input validation + warnings         (§4.6)
  report.py          per-name + watchlist output         (§7)
  pipeline.py        orchestration / CLI entry           (§8)
  delta.py           snapshot + delta report + decision-log prepend (§7.7, §7.8)
  refresh.py         pre-flight quarterly refresh checklist (§8.3)
inputs/
  fleet_manifests/      {ticker}.yaml
  balance_sheets/       {ticker}_{quarter}.yaml
  cost_structures/      {ticker}.yaml
  dividend_policies/    {ticker}.yaml
  market_data/          vessel_value_curves, spot_tce, twelve_month_tc,
                        ffa_forward_curve, historical_tce_means
                        + transactions/{class}.yaml
  scenario_inputs.yaml  per-sector scenarios + forward curves
  watchlist.yaml        current prices + analyst targets + consensus_pnav
  data_sources.yaml     per-ticker IR URLs for the refresh checklist
outputs/                generated reports (md + xlsx), regenerated each run
decisions/              per-ticker decision logs (user-curated, git-tracked)
state/                  pipeline state snapshot (machine-local, gitignored)
tests/                  177 tests, all green
```

## Install

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q                                    # 243 passing (2026-06-11)
python -m crude_tanker_fv.refresh             # smoke-test refresh
python -m crude_tanker_fv.pipeline 2026-Q1   # smoke-test full pipeline
```

To regenerate the methodology PDF (requires Pandoc + LaTeX):

```sh
# macOS:  brew install pandoc basictex
# Linux:  apt install pandoc texlive-xetex
bash scripts/build_methodology_pdf.sh        # → METHODOLOGY.pdf
```

## Validation status

- **Per-sector methodology validators:** DHT (pure VLCC, single-class, full-
  payout) for crude; FLNG (pure modern LNGCs, fixed dividend, no NBs) for
  LNG; ASC (pure MR, single-class, variable payout) for product. Each
  validator's fair value is band-locked in tests so structural regressions
  surface immediately.
- **Mark discrimination:** the broker-NAV sweep classifies every name as
  mark-validated (DHT / ECO / FRO / STNG with ≤10pp spread) or mark-driven
  (TNK / INSW / NAT / ASC with >10pp spread). Critical for sizing — wide
  spreads mean the call is sensitive to vessel-mark choice.
- **Transaction anchoring:** Aframax and Suezmax curves were recalibrated
  against disclosed second-hand transactions (TNK Aframax sale-leasebacks,
  NAT Suezmax disposals). The recalibration is opt-in (default off in
  production) to preserve the broker-marked baseline as the primary lens.
- **Hybrid carve-out preservation invariant:** INSW's whole-company FV is
  pinned to within $0.20/sh across the v2 product-sector refactor — the
  refactor swapped the v1 shortcut (MR forwards under `sectors.crude`)
  for the clean `sectors.product` routing without disturbing the answer.

## Documentation

- **[METHODOLOGY.md](METHODOLOGY.md)** — full framework (~720 lines, 12
  sections + 11.5 product-sector subsection + per-ticker §6 notes)
- **[LIMITATIONS.md](LIMITATIONS.md)** — known framework limitations and
  validation status (the "where does this go wrong?" doc)
- **[decisions/README.md](decisions/README.md)** — decision-log format and
  workflow guidance
- Per-name reports include a Modeling Notes section + data-validation
  warnings at the top

## Repo layout cheatsheet

```
README.md           ← you are here
METHODOLOGY.md      ← the framework (canonical)
LIMITATIONS.md      ← the credibility doc
src/                ← code (16 modules, ~3500 lines)
inputs/             ← per-ticker YAMLs + market data + scenarios
outputs/            ← generated each run
decisions/          ← user-curated per-ticker logs
state/              ← machine-local snapshot (gitignored)
tests/              ← 177 tests
scripts/            ← PDF build script
notebooks/          ← exploratory / hand-check work
```
