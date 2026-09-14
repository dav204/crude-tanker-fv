# CMBT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $19.48
- **Model fair value:** $15.94
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 701.3 |
| Fleet value — Suezmax | 1,247.9 |
| Fleet value — Cape | 4,933.2 |
| Fleet value — Pana | 1,045.9 |
| Fleet value — Ctr-Large | 256.5 |
| + Cash & equivalents | 159.8 |
| + Working capital (net) | 1,252.7 |
| − Total debt | 5,447.1 |
| − Lease liabilities | 5.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 532.7 |
| **= NAV total** | **4,777.3** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.46** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 51,100 | 51,100 | 1.582 | 0.791 | 0.771 |
| Q2 | 45,375 | 45,375 | 1.455 | 0.727 | 0.690 |
| Q3 | 30,975 | 30,975 | 0.828 | 0.414 | 0.383 |
| Q4 | 34,842 | 34,842 | 0.917 | 0.459 | 0.413 |
| Q5 | 34,842 | 34,842 | 0.654 | 0.327 | 0.287 |
| Q6 | 34,841 | 34,841 | 0.652 | 0.326 | 0.279 |
| Q7 | 34,341 | 34,341 | 0.635 | 0.317 | 0.264 |
| Q8 | 33,841 | 33,841 | 0.618 | 0.309 | 0.251 |
| Σ discounted DPS | | | | | 3.34 |
| Terminal value (NAV, q9) | | | | 14.41 | 11.39 |
| **DivStrip implied price** | | | | | **$14.73** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$40,573/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$38,175/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $38,175 / 10-yr mean $23,650 = **1.88×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $14.73 (strip) = **$15.94**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.74 | 124% |
| Balance-sheet net | -8.22 | -52% |
| Discounted DPS (strip, 8-10q) | 1.00 | 6% |
| Discounted terminal (aged NAV) | 3.42 | 21% |
| **Blend FV** | **15.94** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.77 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.02 |
| 95% | $16.06 |
| 100% | $16.07 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.16× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **118,156** | — |
| 10-year mean | 24,718 | 4.78× |
| 12-month FFA | 54,797 | 2.16× |
| Current spot | 83,846 | 1.41× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 87,485 | 3.70× |
| Suezmax (15% of fleet value) | 207,107 | 7.46× |
| Pana (13% of fleet value) | 44,126 | 3.71× |
| VLCC (9% of fleet value) | 280,850 | 7.02× |
| Ctr-Large (3% of fleet value) | 132,339 | 3.23× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.01 | $12.52 | $15.03 | $17.53 | $20.04 |
| **-15%** | $10.47 | $12.98 | $15.49 | $17.99 | $20.50 |
| **+0%** | $10.93 | $13.44 | $15.94 | $18.45 | $20.96 |
| **+15%** | $11.39 | $13.89 | $16.40 | $18.91 | $21.42 |
| **+30%** | $11.85 | $14.35 | $16.86 | $19.37 | $21.88 |

_Current price $19.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.94** is -18.2% vs the current price ($19.48) and -3.9% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$118,156/day** (2.16× the current forward) — 4.8× the value-weighted 10-yr mean ($24,718, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
