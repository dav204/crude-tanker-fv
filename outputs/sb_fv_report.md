# SB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $8.27
- **Model fair value:** $10.41
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 1,125.3 |
| Fleet value — Post-Panamax | 409.3 |
| Fleet value — Cape | 273.3 |
| + Cash & equivalents | 134.5 |
| + Working capital (net) | 37.7 |
| − Total debt | 511.4 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 277.2 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,091.5** |
| Diluted shares | 101,833,473 |
| **NAV / share** | **$10.72** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 21,300 | 18,888 | 0.564 | 0.169 | 0.165 |
| Q2 | 21,600 | 19,008 | 0.569 | 0.171 | 0.162 |
| Q3 | 17,725 | 17,458 | 0.506 | 0.152 | 0.140 |
| Q4 | 17,941 | 17,544 | 0.510 | 0.153 | 0.138 |
| Q5 | 17,941 | 17,544 | 0.510 | 0.153 | 0.134 |
| Q6 | 17,941 | 17,544 | 0.510 | 0.153 | 0.131 |
| Q7 | 17,541 | 17,384 | 0.503 | 0.151 | 0.126 |
| Q8 | 17,241 | 17,264 | 0.498 | 0.149 | 0.121 |
| Σ discounted DPS | | | | | 1.12 |
| Terminal value (NAV, q9) | | | | 10.82 | 8.56 |
| **DivStrip implied price** | | | | | **$9.68** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$19,642/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,663/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,663 / 10-yr mean $11,900 = **1.64×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.72 (NAV) + 0.30 × $9.68 (strip) = **$10.41**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.43 | 119% |
| Balance-sheet net | -4.92 | -47% |
| Discounted DPS (strip, 8-10q) | 0.34 | 3% |
| Discounted terminal (aged NAV) | 2.57 | 25% |
| **Blend FV** | **10.41** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.47 |
| 95% | $10.49 |
| 100% | $10.50 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.72** ≥ price **$8.27** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,676 | 0.00× |
| 12-month FFA | 22,551 | 0.00× |
| Current spot | 23,774 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (62% of fleet value) | 0 | 0.00× |
| Post-Panamax (23% of fleet value) | 0 | 0.00× |
| Cape (15% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.03 | $8.63 | $10.23 | $11.82 | $13.42 |
| **-15%** | $7.12 | $8.72 | $10.32 | $11.91 | $13.51 |
| **+0%** | $7.21 | $8.81 | $10.41 | $12.00 | $13.60 |
| **+15%** | $7.30 | $8.90 | $10.50 | $12.09 | $13.69 |
| **+30%** | $7.39 | $8.99 | $10.59 | $12.18 | $13.78 |

_Current price $8.27. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.41** is +25.8% vs the current price ($8.27) and +46.6% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.72 ≥ $8.27); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
