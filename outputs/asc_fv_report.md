# ASC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.00
- **Model fair value:** $14.90
- **Analyst target:** $17.95

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 618.4 |
| Fleet value — Handysize | 49.1 |
| + Cash & equivalents | 47.2 |
| + Working capital (net) | 131.0 |
| − Total debt | 103.4 |
| − Lease liabilities | 1.8 |
| − Newbuild commitments | 88.8 |
| + Newbuild advances | 1.0 |
| **= NAV total** | **652.7** |
| Diluted shares | 40,900,000 |
| **NAV / share** | **$15.96** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.465 | 0.310 | 0.302 |
| Q2 | 30,000 | 30,000 | 0.831 | 0.555 | 0.526 |
| Q3 | 28,000 | 28,000 | 0.740 | 0.493 | 0.456 |
| Q4 | 19,000 | 19,000 | 0.328 | 0.219 | 0.197 |
| Q5 | 18,000 | 18,000 | 0.282 | 0.188 | 0.165 |
| Q6 | 23,000 | 23,000 | 0.511 | 0.341 | 0.291 |
| Q7 | 26,000 | 26,000 | 0.648 | 0.432 | 0.360 |
| Q8 | 18,000 | 18,000 | 0.282 | 0.188 | 0.153 |
| Σ discounted DPS | | | | | 2.45 |
| Terminal value (NAV, q9) | | | | 13.74 | 10.87 |
| **DivStrip implied price** | | | | | **$13.32** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.38×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $15.96 (NAV) + 0.40 × $13.32 (strip) = **$14.90**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.10 |
| 95% | $15.32 |
| 100% | $15.39 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.55× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **38,252** | — |
| 10-year mean | 16,000 | 2.39× |
| 12-month FFA | 24,750 | 1.55× |
| Current spot | 20,000 | 1.91× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (93% of fleet value) | 38,252 | 2.39× |
| Handysize (7% of fleet value) | 38,252 | 2.39× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.45 | $12.87 | $14.30 | $15.73 | $17.15 |
| **-15%** | $11.75 | $13.18 | $14.60 | $16.03 | $17.45 |
| **+0%** | $12.05 | $13.48 | $14.90 | $16.33 | $17.75 |
| **+15%** | $12.35 | $13.78 | $15.20 | $16.63 | $18.06 |
| **+30%** | $12.66 | $14.08 | $15.51 | $16.93 | $18.36 |

_Current price $16.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.90** is -6.9% vs the current price ($16.00) and -17.0% vs the analyst target ($17.95). The current price implies the fleet earning a value-weighted blended **$38,252/day** (1.55× the current forward) — 2.4× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.
