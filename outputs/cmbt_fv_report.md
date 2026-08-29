# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.35
- **Model fair value:** $15.65
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

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
| Q1 | 38,800 | 38,800 | 1.345 | 0.672 | 0.655 |
| Q2 | 37,250 | 37,250 | 1.306 | 0.653 | 0.620 |
| Q3 | 25,875 | 25,875 | 0.626 | 0.313 | 0.289 |
| Q4 | 31,225 | 31,225 | 0.754 | 0.377 | 0.339 |
| Q5 | 31,250 | 31,250 | 0.533 | 0.267 | 0.234 |
| Q6 | 31,250 | 31,250 | 0.531 | 0.266 | 0.227 |
| Q7 | 30,750 | 30,750 | 0.514 | 0.257 | 0.214 |
| Q8 | 30,250 | 30,250 | 0.498 | 0.249 | 0.202 |
| Σ discounted DPS | | | | | 2.78 |
| Terminal value (NAV, q9) | | | | 13.88 | 10.98 |
| **DivStrip implied price** | | | | | **$13.76** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$33,288/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$31,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $31,550 / 10-yr mean $23,650 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $13.76 (strip) = **$15.65**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.41 | 124% |
| Balance-sheet net | -7.89 | -50% |
| Discounted DPS (strip, 8-10q) | 0.83 | 5% |
| Discounted terminal (aged NAV) | 3.29 | 21% |
| **Blend FV** | **15.65** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.80 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.71 |
| 95% | $15.75 |
| 100% | $15.76 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.98× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **98,659** | — |
| 10-year mean | 24,638 | 4.00× |
| 12-month FFA | 49,729 | 1.98× |
| Current spot | 81,098 | 1.22× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 66,040 | 2.79× |
| Suezmax (16% of fleet value) | 175,527 | 6.33× |
| Pana (13% of fleet value) | 36,839 | 3.10× |
| VLCC (8% of fleet value) | 283,056 | 7.08× |
| Ctr-Large (3% of fleet value) | 121,763 | 2.97× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.89 | $12.36 | $14.82 | $17.29 | $19.75 |
| **-15%** | $10.31 | $12.77 | $15.24 | $17.70 | $20.17 |
| **+0%** | $10.72 | $13.18 | $15.65 | $18.11 | $20.58 |
| **+15%** | $11.13 | $13.59 | $16.06 | $18.52 | $20.99 |
| **+30%** | $11.54 | $14.01 | $16.47 | $18.94 | $21.40 |

_Current price $18.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.65** is -14.7% vs the current price ($18.35) and -5.7% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$98,659/day** (1.98× the current forward) — 4.0× the value-weighted 10-yr mean ($24,638, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
