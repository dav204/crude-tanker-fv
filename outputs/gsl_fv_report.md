# GSL — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $45.30
- **Model fair value:** $44.02
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
| Q1 | 64,000 | 32,571 | 3.429 | 0.625 | 0.609 |
| Q2 | 62,250 | 32,571 | 3.429 | 0.625 | 0.593 |
| Q3 | 60,500 | 32,571 | 3.525 | 0.625 | 0.578 |
| Q4 | 58,750 | 32,571 | 3.700 | 0.625 | 0.563 |
| Q5 | 57,000 | 32,571 | 3.855 | 0.625 | 0.549 |
| Q6 | 55,250 | 32,571 | 3.951 | 0.625 | 0.534 |
| Q7 | 53,500 | 33,597 | 4.135 | 0.625 | 0.521 |
| Q8 | 51,750 | 33,971 | 4.308 | 0.625 | 0.507 |
| Q9 | 50,000 | 35,970 | 4.525 | 0.625 | 0.494 |
| Q10 | 48,000 | 38,218 | 4.785 | 0.625 | 0.481 |
| Σ discounted DPS | | | | | 5.43 |
| Terminal value (NAV, q9) | | | | 60.16 | 45.15 |
| **DivStrip implied price** | | | | | **$50.58** |

_FFA spot is the Ctr-Large forward curve that drives the strip cash flows; its 12-month average is **$61,375/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$64,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $64,000 / 10-yr mean $41,000 = **1.51×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $41.20 (NAV) + 0.30 × $50.58 (strip) = **$44.02**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 33.25 | 76% |
| Balance-sheet net | -4.41 | -10% |
| Discounted DPS (strip, 8-10q) | 1.63 | 4% |
| Discounted terminal (aged NAV) | 13.54 | 31% |
| **Blend FV** | **44.02** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.89 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $43.62 |
| 95% | $43.75 |
| 100% | $43.79 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.33× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **131,422** | — |
| 10-year mean | 38,802 | 3.39× |
| 12-month FFA | 56,392 | 2.33× |
| Current spot | 58,686 | 2.24× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Large (70% of fleet value) | 143,036 | 3.49× |
| Ctr-Intermediate (30% of fleet value) | 104,466 | 3.10× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $34.09 | $38.24 | $42.38 | $46.53 | $50.68 |
| **-15%** | $34.36 | $38.51 | $42.65 | $46.80 | $50.95 |
| **+0%** | $34.63 | $38.77 | $42.92 | $47.07 | $51.22 |
| **+15%** | $34.89 | $39.04 | $43.19 | $47.34 | $51.48 |
| **+30%** | $35.16 | $39.31 | $43.46 | $47.61 | $51.75 |

_Current price $45.30. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$44.02** is -2.8% vs the current price ($45.30) and -15.4% vs the analyst target ($52.04). The current price implies the fleet earning a value-weighted blended **$131,422/day** (2.33× the current forward) — 3.4× the value-weighted 10-yr mean ($38,802, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
