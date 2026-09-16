# CMBT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $19.33
- **Model fair value:** $12.95
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
| − Newbuild commitments | 900.8 |
| + Newbuild advances | 532.7 |
| **= NAV total** | **3,876.4** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$13.36** |

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
| Terminal value (NAV, q9) | | | | 11.14 | 8.81 |
| **DivStrip implied price** | | | | | **$11.99** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,888/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$36,771/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $36,771 / 10-yr mean $23,650 = **1.83×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $13.36 (NAV) + 0.30 × $11.99 (strip) = **$12.95**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.74 | 152% |
| Balance-sheet net | -10.39 | -80% |
| Discounted DPS (strip, 8-10q) | 0.96 | 7% |
| Discounted terminal (aged NAV) | 2.64 | 20% |
| **Blend FV** | **12.95** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.73 = **92%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $13.02 |
| 95% | $13.06 |
| 100% | $13.07 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.15× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **168,836** | — |
| 10-year mean | 24,718 | 6.83× |
| 12-month FFA | 53,676 | 3.15× |
| Current spot | 83,846 | 2.01× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 122,319 | 5.17× |
| Suezmax (15% of fleet value) | 302,122 | 10.89× |
| Pana (13% of fleet value) | 61,782 | 5.19× |
| VLCC (9% of fleet value) | 409,697 | 10.24× |
| Ctr-Large (3% of fleet value) | 193,053 | 4.71× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.04 | $9.55 | $12.06 | $14.57 | $17.07 |
| **-15%** | $7.49 | $10.00 | $12.50 | $15.01 | $17.52 |
| **+0%** | $7.93 | $10.44 | $12.95 | $15.46 | $17.97 |
| **+15%** | $8.38 | $10.89 | $13.40 | $15.90 | $18.41 |
| **+30%** | $8.83 | $11.33 | $13.84 | $16.35 | $18.86 |

_Current price $19.33. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$12.95** is -33.0% vs the current price ($19.33) and -21.9% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$168,836/day** (3.15× the current forward) — 6.8× the value-weighted 10-yr mean ($24,718, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
