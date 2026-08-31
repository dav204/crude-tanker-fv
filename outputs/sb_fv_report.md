# SB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $8.52
- **Model fair value:** $10.34
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 1,118.8 |
| Fleet value — Post-Panamax | 409.3 |
| Fleet value — Cape | 273.3 |
| + Cash & equivalents | 134.5 |
| + Working capital (net) | 37.7 |
| − Total debt | 511.4 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 277.2 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,085.0** |
| Diluted shares | 101,833,473 |
| **NAV / share** | **$10.65** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 20,563 | 18,593 | 0.552 | 0.166 | 0.161 |
| Q2 | 21,791 | 19,084 | 0.572 | 0.172 | 0.163 |
| Q3 | 17,375 | 17,318 | 0.500 | 0.150 | 0.139 |
| Q4 | 18,009 | 17,572 | 0.511 | 0.153 | 0.138 |
| Q5 | 18,008 | 17,571 | 0.511 | 0.153 | 0.134 |
| Q6 | 18,008 | 17,571 | 0.511 | 0.153 | 0.131 |
| Q7 | 17,608 | 17,411 | 0.504 | 0.151 | 0.126 |
| Q8 | 17,308 | 17,291 | 0.499 | 0.150 | 0.122 |
| Σ discounted DPS | | | | | 1.11 |
| Terminal value (NAV, q9) | | | | 10.75 | 8.50 |
| **DivStrip implied price** | | | | | **$9.61** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$19,434/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,583/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,583 / 10-yr mean $11,900 = **1.62×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.65 (NAV) + 0.30 × $9.61 (strip) = **$10.34**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.38 | 120% |
| Balance-sheet net | -4.92 | -48% |
| Discounted DPS (strip, 8-10q) | 0.33 | 3% |
| Discounted terminal (aged NAV) | 2.55 | 25% |
| **Blend FV** | **10.34** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.41 |
| 95% | $10.42 |
| 100% | $10.43 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.65** ≥ price **$8.52** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,683 | 0.00× |
| 12-month FFA | 22,016 | 0.00× |
| Current spot | 23,786 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (62% of fleet value) | 0 | 0.00× |
| Post-Panamax (23% of fleet value) | 0 | 0.00× |
| Cape (15% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.98 | $8.57 | $10.16 | $11.75 | $13.34 |
| **-15%** | $7.07 | $8.66 | $10.25 | $11.84 | $13.43 |
| **+0%** | $7.16 | $8.75 | $10.34 | $11.93 | $13.52 |
| **+15%** | $7.25 | $8.84 | $10.43 | $12.02 | $13.61 |
| **+30%** | $7.34 | $8.93 | $10.52 | $12.11 | $13.70 |

_Current price $8.52. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.34** is +21.4% vs the current price ($8.52) and +45.7% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.65 ≥ $8.52); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
