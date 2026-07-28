# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.67
- **Model fair value:** $9.75
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 988.8 |
| Fleet value — Post-Panamax | 407.1 |
| Fleet value — Cape | 275.5 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 227.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,025.6** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$10.07** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,150 | 18,007 | 0.578 | 0.173 | 0.169 |
| Q2 | 19,100 | 17,987 | 0.582 | 0.175 | 0.166 |
| Q3 | 17,325 | 17,277 | 0.523 | 0.157 | 0.145 |
| Q4 | 16,725 | 17,037 | 0.507 | 0.152 | 0.137 |
| Q5 | 16,125 | 16,797 | 0.491 | 0.147 | 0.129 |
| Q6 | 15,525 | 16,557 | 0.476 | 0.143 | 0.122 |
| Q7 | 15,125 | 16,397 | 0.466 | 0.140 | 0.116 |
| Q8 | 14,825 | 16,277 | 0.458 | 0.137 | 0.112 |
| Σ discounted DPS | | | | | 1.10 |
| Terminal value (NAV, q9) | | | | 10.00 | 7.91 |
| **DivStrip implied price** | | | | | **$9.00** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,075/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,150/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,150 / 10-yr mean $11,900 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.07 (NAV) + 0.30 × $9.00 (strip) = **$9.75**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.49 | 118% |
| Balance-sheet net | -4.44 | -46% |
| Discounted DPS (strip, 8-10q) | 0.33 | 3% |
| Discounted terminal (aged NAV) | 2.37 | 24% |
| **Blend FV** | **9.75** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.81 |
| 95% | $9.83 |
| 100% | $9.84 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.07** ≥ price **$7.67** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,837 | 0.00× |
| 12-month FFA | 20,493 | 0.00× |
| Current spot | 22,167 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (59% of fleet value) | 0 | 0.00× |
| Post-Panamax (24% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.54 | $8.01 | $9.48 | $10.95 | $12.42 |
| **-15%** | $6.68 | $8.15 | $9.62 | $11.09 | $12.55 |
| **+0%** | $6.81 | $8.28 | $9.75 | $11.22 | $12.69 |
| **+15%** | $6.95 | $8.42 | $9.88 | $11.35 | $12.82 |
| **+30%** | $7.08 | $8.55 | $10.02 | $11.49 | $12.96 |

_Current price $7.67. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.75** is +27.1% vs the current price ($7.67) and +37.3% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.07 ≥ $7.67); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
