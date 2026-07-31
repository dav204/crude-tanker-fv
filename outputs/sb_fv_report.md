# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.81
- **Model fair value:** $10.35
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 1,080.5 |
| Fleet value — Post-Panamax | 386.2 |
| Fleet value — Cape | 271.5 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 227.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,092.3** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$10.73** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,150 | 18,028 | 0.529 | 0.159 | 0.155 |
| Q2 | 19,100 | 18,008 | 0.528 | 0.159 | 0.150 |
| Q3 | 17,325 | 17,298 | 0.500 | 0.150 | 0.139 |
| Q4 | 16,725 | 17,058 | 0.490 | 0.147 | 0.132 |
| Q5 | 16,125 | 16,818 | 0.480 | 0.144 | 0.126 |
| Q6 | 15,525 | 16,578 | 0.470 | 0.141 | 0.121 |
| Q7 | 15,125 | 16,418 | 0.464 | 0.139 | 0.116 |
| Q8 | 14,825 | 16,298 | 0.459 | 0.138 | 0.112 |
| Σ discounted DPS | | | | | 1.05 |
| Terminal value (NAV, q9) | | | | 10.63 | 8.41 |
| **DivStrip implied price** | | | | | **$9.46** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,075/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,150/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,150 / 10-yr mean $11,900 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.73 (NAV) + 0.30 × $9.46 (strip) = **$10.35**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.95 | 115% |
| Balance-sheet net | -4.44 | -43% |
| Discounted DPS (strip, 8-10q) | 0.32 | 3% |
| Discounted terminal (aged NAV) | 2.52 | 24% |
| **Blend FV** | **10.35** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.89 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.41 |
| 95% | $10.42 |
| 100% | $10.43 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.73** ≥ price **$7.81** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,735 | 0.00× |
| 12-month FFA | 20,366 | 0.00× |
| Current spot | 22,033 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (62% of fleet value) | 0 | 0.00× |
| Post-Panamax (22% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.12 | $8.65 | $10.18 | $11.72 | $13.25 |
| **-15%** | $7.20 | $8.73 | $10.27 | $11.80 | $13.33 |
| **+0%** | $7.28 | $8.81 | $10.35 | $11.88 | $13.41 |
| **+15%** | $7.36 | $8.89 | $10.43 | $11.96 | $13.49 |
| **+30%** | $7.44 | $8.98 | $10.51 | $12.04 | $13.57 |

_Current price $7.81. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.35** is +32.5% vs the current price ($7.81) and +45.7% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.73 ≥ $7.81); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
