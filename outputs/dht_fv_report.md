# DHT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $18.76
- **Model fair value:** $15.98
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,633.4 |
| + Cash & equivalents | 161.7 |
| + Working capital (net) | 137.6 |
| − Total debt | 434.8 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,419.4** |
| Diluted shares | 161,235,573 |
| **NAV / share** | **$15.01** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 118,981 | 1.324 | 1.324 | 1.290 |
| Q2 | 183,500 | 138,781 | 1.577 | 1.577 | 1.496 |
| Q3 | 165,500 | 128,881 | 1.450 | 1.450 | 1.341 |
| Q4 | 123,500 | 105,781 | 1.156 | 1.156 | 1.042 |
| Q5 | 111,500 | 99,181 | 1.072 | 1.072 | 0.941 |
| Q6 | 135,500 | 112,381 | 1.240 | 1.240 | 1.060 |
| Q7 | 147,500 | 118,981 | 1.324 | 1.324 | 1.103 |
| Q8 | 105,500 | 95,881 | 1.030 | 1.030 | 0.836 |
| Σ discounted DPS | | | | | 9.11 |
| Terminal value (NAV, q9) | | | | 11.58 | 9.16 |
| **DivStrip implied price** | | | | | **$18.27** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.01 (NAV) + 0.30 × $18.27 (strip) = **$15.98**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.43 | 72% |
| Balance-sheet net | -0.93 | -6% |
| Discounted DPS (strip, 8-10q) | 2.73 | 17% |
| Discounted terminal (aged NAV) | 2.75 | 17% |
| **Blend FV** | **15.98** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.50 = **85%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.92 |
| 95% | $15.97 |
| 100% | $15.98 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.31× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **358,707** | — |
| 10-year mean | 40,000 | 8.97× |
| 12-month FFA | 155,000 | 2.31× |
| Current spot | 285,500 | 1.26× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $12.45 | $13.90 | $15.35 | $16.80 | $18.25 |
| **-15%** | $12.77 | $14.22 | $15.67 | $17.12 | $18.57 |
| **+0%** | $13.09 | $14.53 | $15.98 | $17.43 | $18.88 |
| **+15%** | $13.40 | $14.85 | $16.30 | $17.75 | $19.20 |
| **+30%** | $13.72 | $15.17 | $16.62 | $18.07 | $19.52 |

_Current price $18.76. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.98** is -14.8% vs the current price ($18.76) and -0.1% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$358,707/day** (2.31× the current forward) — 9.0× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
