# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.29
- **Model fair value:** $15.83
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 635.5 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,835.6 |
| Fleet value — Pana | 1,034.4 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,775.4** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.46** |

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
| Terminal value (NAV, q9) | | | | 14.25 | 11.27 |
| **DivStrip implied price** | | | | | **$14.35** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.73×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $14.35 (strip) = **$15.83**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.41 | 123% |
| Balance-sheet net | -7.89 | -50% |
| Discounted DPS (strip, 8-10q) | 0.92 | 6% |
| Discounted terminal (aged NAV) | 3.38 | 21% |
| **Blend FV** | **15.83** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.79 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.89 |
| 95% | $15.93 |
| 100% | $15.94 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.16× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **57,624** | — |
| 10-year mean | 24,638 | 2.34× |
| 12-month FFA | 49,731 | 1.16× |
| Current spot | 68,120 | 0.85× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 37,941 | 1.60× |
| Suezmax (16% of fleet value) | 98,491 | 3.55× |
| Pana (13% of fleet value) | 20,944 | 1.76× |
| VLCC (8% of fleet value) | 179,601 | 4.49× |
| Ctr-Large (3% of fleet value) | 70,102 | 1.71× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.02 | $12.48 | $14.95 | $17.41 | $19.88 |
| **-15%** | $10.46 | $12.92 | $15.39 | $17.85 | $20.32 |
| **+0%** | $10.90 | $13.36 | $15.83 | $18.29 | $20.76 |
| **+15%** | $11.33 | $13.80 | $16.26 | $18.73 | $21.19 |
| **+30%** | $11.77 | $14.24 | $16.70 | $19.17 | $21.63 |

_Current price $16.29. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.83** is -2.8% vs the current price ($16.29) and -4.6% vs the analyst target ($16.59). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$57,624/day** (1.16× the current forward) — 2.3× the value-weighted 10-yr mean ($24,638, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
