# CAPT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $13.94
- **Model fair value:** $16.05
- **Analyst target:** $18.90

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,922.4 |
| Fleet value — Suezmax | 1,149.0 |
| Fleet value — Aframax | 294.8 |
| Fleet value — LR2 | 382.8 |
| + Cash & equivalents | 405.0 |
| + Working capital (net) | 13.0 |
| − Total debt | 217.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,880.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,070.0** |
| Diluted shares | 133,700,000 |
| **NAV / share** | **$15.48** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 147,500 | 0.547 | 0.246 | 0.240 |
| Q2 | 183,500 | 183,500 | 1.043 | 0.470 | 0.446 |
| Q3 | 165,500 | 165,500 | 1.109 | 0.499 | 0.461 |
| Q4 | 123,500 | 123,500 | 0.903 | 0.406 | 0.366 |
| Q5 | 111,500 | 111,500 | 0.831 | 0.374 | 0.328 |
| Q6 | 135,500 | 135,500 | 1.210 | 0.545 | 0.466 |
| Q7 | 147,500 | 147,500 | 1.489 | 0.670 | 0.558 |
| Q8 | 105,500 | 105,500 | 1.131 | 0.509 | 0.413 |
| Σ discounted DPS | | | | | 3.28 |
| Terminal value (NAV, q9) | | | | 17.81 | 14.08 |
| **DivStrip implied price** | | | | | **$17.36** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.46×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.48 (NAV) + 0.30 × $17.36 (strip) = **$16.05**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.63 | 122% |
| Balance-sheet net | -8.79 | -55% |
| Discounted DPS (strip, 8-10q) | 0.98 | 6% |
| Discounted terminal (aged NAV) | 4.22 | 26% |
| **Blend FV** | **16.05** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.81 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.12 |
| 95% | $16.16 |
| 100% | $16.17 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.15× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,274** | — |
| 10-year mean | 34,702 | 0.53× |
| 12-month FFA | 119,493 | 0.15× |
| Current spot | 192,308 | 0.10× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (51% of fleet value) | 23,704 | 0.59× |
| Suezmax (31% of fleet value) | 12,999 | 0.47× |
| LR2 (10% of fleet value) | 11,814 | 0.43× |
| Aframax (8% of fleet value) | 11,814 | 0.32× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.15 | $12.72 | $15.30 | $17.87 | $20.45 |
| **-15%** | $10.52 | $13.10 | $15.67 | $18.25 | $20.82 |
| **+0%** | $10.89 | $13.47 | $16.05 | $18.62 | $21.20 |
| **+15%** | $11.27 | $13.84 | $16.42 | $18.99 | $21.57 |
| **+30%** | $11.64 | $14.22 | $16.79 | $19.37 | $21.94 |

_Current price $13.94. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$16.05** is +15.1% vs the current price ($13.94) and -15.1% vs the analyst target ($18.90). The current price implies the fleet earning a value-weighted blended **$18,274/day** (0.15× the current forward) — 0.5× the value-weighted 10-yr mean ($34,702, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
