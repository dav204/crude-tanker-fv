# CMBT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $19.38
- **Model fair value:** $15.87
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
| Q1 | 45,125 | 45,125 | 1.446 | 0.723 | 0.704 |
| Q2 | 44,125 | 44,125 | 1.429 | 0.714 | 0.678 |
| Q3 | 29,925 | 29,925 | 0.801 | 0.401 | 0.370 |
| Q4 | 34,292 | 34,292 | 0.901 | 0.450 | 0.406 |
| Q5 | 34,292 | 34,292 | 0.638 | 0.319 | 0.280 |
| Q6 | 34,291 | 34,291 | 0.636 | 0.318 | 0.272 |
| Q7 | 33,791 | 33,791 | 0.618 | 0.309 | 0.258 |
| Q8 | 33,291 | 33,291 | 0.602 | 0.301 | 0.244 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 14.27 | 11.29 |
| **DivStrip implied price** | | | | | **$14.50** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,367/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,025/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,025 / 10-yr mean $23,650 = **1.85×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $14.50 (strip) = **$15.87**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.74 | 124% |
| Balance-sheet net | -8.22 | -52% |
| Discounted DPS (strip, 8-10q) | 0.96 | 6% |
| Discounted terminal (aged NAV) | 3.39 | 21% |
| **Blend FV** | **15.87** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.95 |
| 95% | $15.99 |
| 100% | $16.00 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.17× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **116,170** | — |
| 10-year mean | 24,718 | 4.70× |
| 12-month FFA | 53,461 | 2.17× |
| Current spot | 83,846 | 1.39× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 83,371 | 3.53× |
| Suezmax (15% of fleet value) | 208,716 | 7.52× |
| Pana (13% of fleet value) | 44,356 | 3.73× |
| VLCC (9% of fleet value) | 283,032 | 7.08× |
| Ctr-Large (3% of fleet value) | 133,367 | 3.25× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.96 | $12.47 | $14.98 | $17.49 | $19.99 |
| **-15%** | $10.41 | $12.92 | $15.43 | $17.93 | $20.44 |
| **+0%** | $10.86 | $13.37 | $15.87 | $18.38 | $20.89 |
| **+15%** | $11.31 | $13.81 | $16.32 | $18.83 | $21.34 |
| **+30%** | $11.76 | $14.26 | $16.77 | $19.28 | $21.79 |

_Current price $19.38. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.87** is -18.1% vs the current price ($19.38) and -4.3% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$116,170/day** (2.17× the current forward) — 4.7× the value-weighted 10-yr mean ($24,718, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
