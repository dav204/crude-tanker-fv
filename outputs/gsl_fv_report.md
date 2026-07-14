# GSL — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $40.81
- **Model fair value:** $43.06
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
| Terminal value (NAV, q9) | | | | 59.09 | 44.35 |
| **DivStrip implied price** | | | | | **$49.78** |

_FFA spot is the Ctr-Large forward curve that drives the strip cash flows; its 12-month average is **$60,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$63,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $63,000 / 10-yr mean $41,000 = **1.49×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $38.59 (NAV) + 0.40 × $49.78 (strip) = **$43.06**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 29.18 | 68% |
| Balance-sheet net | -6.03 | -14% |
| Discounted DPS (strip, 8-10q) | 2.17 | 5% |
| Discounted terminal (aged NAV) | 17.74 | 41% |
| **Blend FV** | **43.06** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.89 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $42.55 |
| 95% | $42.72 |
| 100% | $42.78 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.66× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **36,896** | — |
| 10-year mean | 38,795 | 0.95× |
| 12-month FFA | 55,764 | 0.66× |
| Current spot | 57,970 | 0.64× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Large (70% of fleet value) | 40,029 | 0.98× |
| Ctr-Intermediate (30% of fleet value) | 29,658 | 0.88× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $32.70 | $36.80 | $40.90 | $45.00 | $49.11 |
| **-15%** | $33.05 | $37.16 | $41.26 | $45.36 | $49.46 |
| **+0%** | $33.41 | $37.51 | $41.62 | $45.72 | $49.82 |
| **+15%** | $33.77 | $37.87 | $41.97 | $46.08 | $50.18 |
| **+30%** | $34.13 | $38.23 | $42.33 | $46.43 | $50.54 |

_Current price $40.81. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$43.06** is +5.5% vs the current price ($40.81) and -17.3% vs the analyst target ($52.04). The current price implies the fleet earning a value-weighted blended **$36,896/day** (0.66× the current forward) — 1.0× the value-weighted 10-yr mean ($38,795, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
