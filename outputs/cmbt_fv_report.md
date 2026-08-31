# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.35
- **Model fair value:** $15.83
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 635.5 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,835.6 |
| Fleet value — Pana | 1,048.2 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,789.2** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.50** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 41,313 | 41,313 | 1.402 | 0.701 | 0.683 |
| Q2 | 42,125 | 42,125 | 1.430 | 0.715 | 0.679 |
| Q3 | 28,725 | 28,725 | 0.701 | 0.350 | 0.324 |
| Q4 | 33,625 | 33,625 | 0.815 | 0.408 | 0.367 |
| Q5 | 33,625 | 33,625 | 0.594 | 0.297 | 0.261 |
| Q6 | 33,625 | 33,625 | 0.592 | 0.296 | 0.253 |
| Q7 | 33,125 | 33,125 | 0.575 | 0.288 | 0.240 |
| Q8 | 32,625 | 32,625 | 0.559 | 0.279 | 0.227 |
| Σ discounted DPS | | | | | 3.03 |
| Terminal value (NAV, q9) | | | | 14.21 | 11.23 |
| **DivStrip implied price** | | | | | **$14.27** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$36,447/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,425/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,425 / 10-yr mean $23,650 = **1.70×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.50 (NAV) + 0.30 × $14.27 (strip) = **$15.83**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.44 | 123% |
| Balance-sheet net | -7.89 | -50% |
| Discounted DPS (strip, 8-10q) | 0.91 | 6% |
| Discounted terminal (aged NAV) | 3.37 | 21% |
| **Blend FV** | **15.83** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.79 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.91 |
| 95% | $15.94 |
| 100% | $15.95 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **96,705** | — |
| 10-year mean | 24,617 | 3.93× |
| 12-month FFA | 51,684 | 1.87× |
| Current spot | 80,994 | 1.19× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 68,195 | 2.88× |
| Suezmax (16% of fleet value) | 165,543 | 5.97× |
| Pana (13% of fleet value) | 36,363 | 3.06× |
| VLCC (8% of fleet value) | 266,955 | 6.67× |
| Ctr-Large (3% of fleet value) | 114,837 | 2.80× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.03 | $12.50 | $14.97 | $17.44 | $19.91 |
| **-15%** | $10.46 | $12.93 | $15.40 | $17.87 | $20.34 |
| **+0%** | $10.90 | $13.36 | $15.83 | $18.30 | $20.77 |
| **+15%** | $11.33 | $13.80 | $16.27 | $18.74 | $21.21 |
| **+30%** | $11.76 | $14.23 | $16.70 | $19.17 | $21.64 |

_Current price $18.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.83** is -13.7% vs the current price ($18.35) and -4.6% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$96,705/day** (1.87× the current forward) — 3.9× the value-weighted 10-yr mean ($24,617, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
