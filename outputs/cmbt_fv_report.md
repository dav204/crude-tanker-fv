# CMBT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $19.33
- **Model fair value:** $15.86
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
| Q1 | 48,500 | 48,500 | 1.515 | 0.758 | 0.738 |
| Q2 | 43,666 | 43,666 | 1.405 | 0.703 | 0.667 |
| Q3 | 29,875 | 29,875 | 0.797 | 0.398 | 0.368 |
| Q4 | 33,509 | 33,509 | 0.880 | 0.440 | 0.396 |
| Q5 | 33,508 | 33,508 | 0.617 | 0.308 | 0.271 |
| Q6 | 33,508 | 33,508 | 0.615 | 0.307 | 0.263 |
| Q7 | 33,008 | 33,008 | 0.597 | 0.299 | 0.249 |
| Q8 | 32,508 | 32,508 | 0.581 | 0.291 | 0.236 |
| Σ discounted DPS | | | | | 3.19 |
| Terminal value (NAV, q9) | | | | 14.24 | 11.26 |
| **DivStrip implied price** | | | | | **$14.45** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,888/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$36,771/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $36,771 / 10-yr mean $23,650 = **1.83×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $14.45 (strip) = **$15.86**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.74 | 124% |
| Balance-sheet net | -8.22 | -52% |
| Discounted DPS (strip, 8-10q) | 0.96 | 6% |
| Discounted terminal (aged NAV) | 3.38 | 21% |
| **Blend FV** | **15.86** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.93 |
| 95% | $15.97 |
| 100% | $15.98 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.17× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **116,320** | — |
| 10-year mean | 24,718 | 4.71× |
| 12-month FFA | 53,676 | 2.17× |
| Current spot | 83,846 | 1.39× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 84,272 | 3.56× |
| Suezmax (15% of fleet value) | 208,148 | 7.50× |
| Pana (13% of fleet value) | 42,565 | 3.58× |
| VLCC (9% of fleet value) | 282,262 | 7.06× |
| Ctr-Large (3% of fleet value) | 133,004 | 3.24× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.95 | $12.46 | $14.97 | $17.47 | $19.98 |
| **-15%** | $10.40 | $12.91 | $15.41 | $17.92 | $20.43 |
| **+0%** | $10.84 | $13.35 | $15.86 | $18.37 | $20.87 |
| **+15%** | $11.29 | $13.80 | $16.31 | $18.81 | $21.32 |
| **+30%** | $11.74 | $14.24 | $16.75 | $19.26 | $21.77 |

_Current price $19.33. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.86** is -18.0% vs the current price ($19.33) and -4.4% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$116,320/day** (2.17× the current forward) — 4.7× the value-weighted 10-yr mean ($24,718, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
