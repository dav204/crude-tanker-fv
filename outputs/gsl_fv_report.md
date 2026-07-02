# GSL — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $37.78
- **Model fair value:** $43.00
- **Analyst target:** $52.04

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Large | 1,222.9 |
| Fleet value — Ctr-Intermediate | 529.4 |
| + Cash & equivalents | 404.9 |
| + Working capital (net) | 0.0 |
| − Total debt | 657.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,390.5** |
| Diluted shares | 36,035,434 |
| **NAV / share** | **$38.59** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Large, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 62,500 | 32,571 | 3.429 | 0.625 | 0.609 |
| Q2 | 61,500 | 32,571 | 3.429 | 0.625 | 0.593 |
| Q3 | 60,000 | 32,571 | 3.515 | 0.625 | 0.578 |
| Q4 | 58,500 | 32,571 | 3.671 | 0.625 | 0.563 |
| Q5 | 57,000 | 32,571 | 3.819 | 0.625 | 0.549 |
| Q6 | 55,500 | 32,571 | 3.902 | 0.625 | 0.534 |
| Q7 | 54,000 | 33,621 | 4.098 | 0.625 | 0.521 |
| Q8 | 52,000 | 33,990 | 4.285 | 0.625 | 0.507 |
| Q9 | 50,000 | 35,970 | 4.495 | 0.625 | 0.494 |
| Q10 | 48,000 | 38,218 | 4.785 | 0.625 | 0.481 |
| Σ discounted DPS | | | | | 5.43 |
| Terminal value (NAV, q9) | | | | 58.89 | 44.20 |
| **DivStrip implied price** | | | | | **$49.63** |

_FFA spot is the Ctr-Large forward curve that drives the strip cash flows; its 12-month average is **$60,625/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$62,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $62,500 / 10-yr mean $41,000 = **1.45×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $38.59 (NAV) + 0.40 × $49.63 (strip) = **$43.00**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $42.49 |
| 95% | $42.66 |
| 100% | $42.72 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$38.59** ≥ price **$37.78** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,795 | 0.00× |
| 12-month FFA | 55,143 | 0.00× |
| Current spot | 56,730 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Large (70% of fleet value) | 0 | 0.00× |
| Ctr-Intermediate (30% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $32.66 | $36.76 | $40.86 | $44.96 | $49.07 |
| **-15%** | $33.01 | $37.11 | $41.21 | $45.31 | $49.42 |
| **+0%** | $33.35 | $37.46 | $41.56 | $45.66 | $49.76 |
| **+15%** | $33.70 | $37.81 | $41.91 | $46.01 | $50.11 |
| **+30%** | $34.05 | $38.15 | $42.26 | $46.36 | $50.46 |

_Current price $37.78. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$43.00** is +13.8% vs the current price ($37.78) and -17.4% vs the analyst target ($52.04). NAV alone covers the price (NAV/sh $38.59 ≥ $37.78); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
