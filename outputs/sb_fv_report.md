# SB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $8.52
- **Model fair value:** $10.42
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
| Q1 | 21,900 | 19,128 | 0.574 | 0.172 | 0.168 |
| Q2 | 22,900 | 19,528 | 0.590 | 0.177 | 0.168 |
| Q3 | 18,200 | 17,648 | 0.514 | 0.154 | 0.143 |
| Q4 | 18,167 | 17,635 | 0.513 | 0.154 | 0.139 |
| Q5 | 18,167 | 17,635 | 0.513 | 0.154 | 0.135 |
| Q6 | 18,166 | 17,634 | 0.513 | 0.154 | 0.132 |
| Q7 | 17,766 | 17,474 | 0.507 | 0.152 | 0.127 |
| Q8 | 17,466 | 17,354 | 0.502 | 0.151 | 0.122 |
| Σ discounted DPS | | | | | 1.13 |
| Terminal value (NAV, q9) | | | | 10.86 | 8.59 |
| **DivStrip implied price** | | | | | **$9.72** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$20,292/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$20,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $20,550 / 10-yr mean $11,900 = **1.71×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.72 (NAV) + 0.30 × $9.72 (strip) = **$10.42**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.43 | 119% |
| Balance-sheet net | -4.92 | -47% |
| Discounted DPS (strip, 8-10q) | 0.34 | 3% |
| Discounted terminal (aged NAV) | 2.58 | 25% |
| **Blend FV** | **10.42** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.49 |
| 95% | $10.50 |
| 100% | $10.51 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.72** ≥ price **$8.52** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,676 | 0.00× |
| 12-month FFA | 23,052 | 0.00× |
| Current spot | 23,774 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (62% of fleet value) | 0 | 0.00× |
| Post-Panamax (23% of fleet value) | 0 | 0.00× |
| Cape (15% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.04 | $8.64 | $10.24 | $11.83 | $13.43 |
| **-15%** | $7.13 | $8.73 | $10.33 | $11.93 | $13.52 |
| **+0%** | $7.23 | $8.82 | $10.42 | $12.02 | $13.61 |
| **+15%** | $7.32 | $8.91 | $10.51 | $12.11 | $13.71 |
| **+30%** | $7.41 | $9.01 | $10.60 | $12.20 | $13.80 |

_Current price $8.52. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.42** is +22.3% vs the current price ($8.52) and +46.8% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.72 ≥ $8.52); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
