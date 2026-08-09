# SB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $7.60
- **Model fair value:** $10.24
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 1,111.1 |
| Fleet value — Post-Panamax | 409.3 |
| Fleet value — Cape | 273.3 |
| + Cash & equivalents | 134.5 |
| + Working capital (net) | 37.7 |
| − Total debt | 511.4 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 277.2 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,077.3** |
| Diluted shares | 101,833,473 |
| **NAV / share** | **$10.58** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 20,500 | 18,568 | 0.551 | 0.165 | 0.161 |
| Q2 | 20,325 | 18,498 | 0.548 | 0.165 | 0.156 |
| Q3 | 16,250 | 16,868 | 0.482 | 0.145 | 0.134 |
| Q4 | 17,200 | 17,248 | 0.497 | 0.149 | 0.134 |
| Q5 | 17,225 | 17,258 | 0.498 | 0.149 | 0.131 |
| Q6 | 17,225 | 17,258 | 0.498 | 0.149 | 0.128 |
| Q7 | 16,825 | 17,098 | 0.491 | 0.147 | 0.123 |
| Q8 | 16,525 | 16,978 | 0.486 | 0.146 | 0.118 |
| Σ discounted DPS | | | | | 1.09 |
| Terminal value (NAV, q9) | | | | 10.57 | 8.36 |
| **DivStrip implied price** | | | | | **$9.45** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,569/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,300 / 10-yr mean $11,900 = **1.51×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.58 (NAV) + 0.30 × $9.45 (strip) = **$10.24**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.33 | 120% |
| Balance-sheet net | -4.92 | -48% |
| Discounted DPS (strip, 8-10q) | 0.33 | 3% |
| Discounted terminal (aged NAV) | 2.51 | 24% |
| **Blend FV** | **10.24** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.89 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.30 |
| 95% | $10.32 |
| 100% | $10.33 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.58** ≥ price **$7.60** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,690 | 0.00× |
| 12-month FFA | 20,811 | 0.00× |
| Current spot | 23,304 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (62% of fleet value) | 0 | 0.00× |
| Post-Panamax (23% of fleet value) | 0 | 0.00× |
| Cape (15% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.90 | $8.48 | $10.07 | $11.65 | $13.24 |
| **-15%** | $6.99 | $8.57 | $10.15 | $11.74 | $13.32 |
| **+0%** | $7.07 | $8.66 | $10.24 | $11.82 | $13.41 |
| **+15%** | $7.16 | $8.74 | $10.33 | $11.91 | $13.49 |
| **+30%** | $7.24 | $8.83 | $10.41 | $11.99 | $13.58 |

_Current price $7.60. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.24** is +34.7% vs the current price ($7.60) and +44.2% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.58 ≥ $7.60); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
