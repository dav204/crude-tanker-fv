# GSL — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $42.44
- **Model fair value:** $45.50
- **Analyst target:** $52.04

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Large | 1,196.3 |
| Fleet value — Ctr-Intermediate | 515.4 |
| + Cash & equivalents | 499.0 |
| + Working capital (net) | -64.8 |
| − Total debt | 676.4 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 124.3 |
| **= NAV total** | **1,484.8** |
| Diluted shares | 36,035,434 |
| **NAV / share** | **$41.20** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Large, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 63,000 | 32,571 | 3.429 | 0.625 | 0.609 |
| Q2 | 61,500 | 32,571 | 3.429 | 0.625 | 0.593 |
| Q3 | 59,500 | 32,571 | 3.525 | 0.625 | 0.578 |
| Q4 | 58,000 | 32,571 | 3.700 | 0.625 | 0.563 |
| Q5 | 56,500 | 32,571 | 3.855 | 0.625 | 0.549 |
| Q6 | 54,500 | 32,571 | 3.951 | 0.625 | 0.534 |
| Q7 | 53,000 | 33,572 | 4.132 | 0.625 | 0.521 |
| Q8 | 51,500 | 33,953 | 4.306 | 0.625 | 0.507 |
| Q9 | 49,500 | 35,872 | 4.515 | 0.625 | 0.494 |
| Q10 | 48,000 | 38,218 | 4.785 | 0.625 | 0.481 |
| Σ discounted DPS | | | | | 5.43 |
| Terminal value (NAV, q9) | | | | 61.98 | 46.52 |
| **DivStrip implied price** | | | | | **$51.95** |

_FFA spot is the Ctr-Large forward curve that drives the strip cash flows; its 12-month average is **$60,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$63,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $63,000 / 10-yr mean $41,000 = **1.49×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $41.20 (NAV) + 0.40 × $51.95 (strip) = **$45.50**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 28.50 | 63% |
| Balance-sheet net | -3.78 | -8% |
| Discounted DPS (strip, 8-10q) | 2.17 | 5% |
| Discounted terminal (aged NAV) | 18.61 | 41% |
| **Blend FV** | **45.50** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.90 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $45.03 |
| 95% | $45.21 |
| 100% | $45.26 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.30× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **16,874** | — |
| 10-year mean | 38,802 | 0.43× |
| 12-month FFA | 55,780 | 0.30× |
| Current spot | 57,987 | 0.29× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Large (70% of fleet value) | 18,302 | 0.45× |
| Ctr-Intermediate (30% of fleet value) | 13,560 | 0.40× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $35.37 | $39.38 | $43.39 | $47.39 | $51.40 |
| **-15%** | $35.73 | $39.74 | $43.74 | $47.75 | $51.76 |
| **+0%** | $36.09 | $40.09 | $44.10 | $48.11 | $52.12 |
| **+15%** | $36.44 | $40.45 | $44.46 | $48.47 | $52.47 |
| **+30%** | $36.80 | $40.81 | $44.82 | $48.82 | $52.83 |

_Current price $42.44. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$45.50** is +7.2% vs the current price ($42.44) and -12.6% vs the analyst target ($52.04). The current price implies the fleet earning a value-weighted blended **$16,874/day** (0.30× the current forward) — 0.4× the value-weighted 10-yr mean ($38,802, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
