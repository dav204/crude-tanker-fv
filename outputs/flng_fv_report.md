# FLNG — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $31.48
- **Model fair value:** $27.01
- **Analyst target:** $25.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 2,869.5 |
| + Cash & equivalents | 397.4 |
| + Working capital (net) | -0.7 |
| − Total debt | 1,793.7 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,472.5** |
| Diluted shares | 54,092,376 |
| **NAV / share** | **$27.22** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 76,873 | 0.871 | 0.750 | 0.731 |
| Q2 | 80,000 | 83,773 | 1.016 | 0.750 | 0.712 |
| Q3 | 75,000 | 82,623 | 0.992 | 0.750 | 0.694 |
| Q4 | 48,000 | 76,413 | 0.861 | 0.750 | 0.676 |
| Q5 | 52,000 | 77,333 | 0.881 | 0.750 | 0.658 |
| Q6 | 80,000 | 83,773 | 1.016 | 0.750 | 0.641 |
| Q7 | 75,000 | 82,623 | 0.992 | 0.750 | 0.625 |
| Q8 | 50,000 | 76,873 | 0.871 | 0.750 | 0.609 |
| Σ discounted DPS | | | | | 5.34 |
| Terminal value (NAV, q9) | | | | 27.22 | 21.53 |
| **DivStrip implied price** | | | | | **$26.87** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.71×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $27.22 (NAV) + 0.60 × $26.87 (strip) = **$27.01**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 21.22 | 79% |
| Balance-sheet net | -10.33 | -38% |
| Discounted DPS (strip, 8-10q) | 3.21 | 12% |
| Discounted terminal (aged NAV) | 12.92 | 48% |
| **Blend FV** | **27.01** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.40 + 0.60 × 0.80 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $27.37 |
| 95% | $27.44 |
| 100% | $27.46 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.81× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **304,350** | — |
| 10-year mean | 85,000 | 3.58× |
| 12-month FFA | 63,250 | 4.81× |
| Current spot | 65,000 | 4.68× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.53 | $22.09 | $26.66 | $31.23 | $35.80 |
| **-15%** | $17.70 | $22.27 | $26.84 | $31.40 | $35.97 |
| **+0%** | $17.88 | $22.44 | $27.01 | $31.58 | $36.15 |
| **+15%** | $18.05 | $22.62 | $27.19 | $31.76 | $36.32 |
| **+30%** | $18.23 | $22.80 | $27.36 | $31.93 | $36.50 |

_Current price $31.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$27.01** is -14.2% vs the current price ($31.48) and +8.0% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$304,350/day** (4.81× the current forward) — 3.6× the value-weighted 10-yr mean ($85,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
