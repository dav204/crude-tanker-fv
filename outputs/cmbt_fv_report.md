# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.29
- **Model fair value:** $15.57
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 621.3 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,821.8 |
| Fleet value — Pana | 985.0 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,698.1** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.19** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 34,900 | 34,900 | 1.024 | 0.512 | 0.499 |
| Q2 | 35,725 | 35,725 | 1.168 | 0.584 | 0.554 |
| Q3 | 30,675 | 30,675 | 0.980 | 0.490 | 0.453 |
| Q4 | 29,675 | 29,675 | 0.781 | 0.390 | 0.352 |
| Q5 | 28,675 | 28,675 | 0.700 | 0.350 | 0.307 |
| Q6 | 27,675 | 27,675 | 0.785 | 0.393 | 0.336 |
| Q7 | 27,175 | 27,175 | 0.800 | 0.400 | 0.333 |
| Q8 | 26,675 | 26,675 | 0.613 | 0.306 | 0.249 |
| Σ discounted DPS | | | | | 3.08 |
| Terminal value (NAV, q9) | | | | 13.96 | 11.04 |
| **DivStrip implied price** | | | | | **$14.12** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.72×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.19 (NAV) + 0.30 × $14.12 (strip) = **$15.57**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.22 | 123% |
| Balance-sheet net | -7.89 | -51% |
| Discounted DPS (strip, 8-10q) | 0.92 | 6% |
| Discounted terminal (aged NAV) | 3.31 | 21% |
| **Blend FV** | **15.57** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.64 |
| 95% | $15.67 |
| 100% | $15.68 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.25× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **62,034** | — |
| 10-year mean | 24,692 | 2.51× |
| 12-month FFA | 49,770 | 1.25× |
| Current spot | 68,092 | 0.91× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (61% of fleet value) | 40,812 | 1.73× |
| Suezmax (16% of fleet value) | 105,945 | 3.82× |
| Pana (12% of fleet value) | 22,529 | 1.89× |
| VLCC (8% of fleet value) | 193,194 | 4.83× |
| Ctr-Large (3% of fleet value) | 75,408 | 1.84× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.81 | $12.25 | $14.69 | $17.13 | $19.57 |
| **-15%** | $10.25 | $12.69 | $15.13 | $17.57 | $20.01 |
| **+0%** | $10.69 | $13.13 | $15.57 | $18.01 | $20.45 |
| **+15%** | $11.13 | $13.57 | $16.01 | $18.45 | $20.89 |
| **+30%** | $11.57 | $14.01 | $16.45 | $18.89 | $21.33 |

_Current price $16.29. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.57** is -4.4% vs the current price ($16.29) and -6.2% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$62,034/day** (1.25× the current forward) — 2.5× the value-weighted 10-yr mean ($24,692, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
