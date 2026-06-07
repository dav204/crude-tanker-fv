# HAFN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.70
- **Model fair value:** $5.70
- **Analyst target:** $10.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 634.1 |
| Fleet value — LR1 | 848.8 |
| Fleet value — MR | 1,588.8 |
| Fleet value — Handysize | 319.7 |
| + Cash & equivalents | 146.5 |
| + Working capital (net) | 475.0 |
| − Total debt | 943.5 |
| − Lease liabilities | 35.9 |
| − Newbuild commitments | 405.0 |
| + Newbuild advances | 40.0 |
| **= NAV total** | **2,668.5** |
| Diluted shares | 500,000,000 |
| **NAV / share** | **$5.34** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.556 | 0.445 | 0.434 |
| Q2 | 30,000 | 30,000 | 0.738 | 0.591 | 0.561 |
| Q3 | 28,000 | 28,000 | 0.676 | 0.541 | 0.500 |
| Q4 | 19,000 | 19,000 | 0.450 | 0.360 | 0.324 |
| Q5 | 18,000 | 18,000 | 0.406 | 0.325 | 0.285 |
| Q6 | 23,000 | 23,000 | 0.538 | 0.430 | 0.368 |
| Q7 | 26,000 | 26,000 | 0.601 | 0.480 | 0.400 |
| Q8 | 18,000 | 18,000 | 0.387 | 0.310 | 0.252 |
| Σ discounted DPS | | | | | 3.12 |
| Terminal value (NAV, q9) | | | | 4.32 | 3.42 |
| **DivStrip implied price** | | | | | **$6.54** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $5.34 (NAV) + 0.30 × $6.54 (strip) = **$5.70**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.70 |
| 95% | $5.87 |
| 100% | $5.93 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.59× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **123,511** | — |
| 10-year mean | 21,072 | 5.86× |
| 12-month FFA | 47,706 | 2.59× |
| Current spot | 20,697 | 5.97× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (47% of fleet value) | 64,079 | 4.00× |
| LR1 (25% of fleet value) | 200,003 | 7.25× |
| LR2 (19% of fleet value) | 200,003 | 7.25× |
| Handysize (9% of fleet value) | 64,079 | 4.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $4.10 | $4.71 | $5.32 | $5.93 | $6.54 |
| **-15%** | $4.29 | $4.90 | $5.51 | $6.12 | $6.73 |
| **+0%** | $4.47 | $5.09 | $5.70 | $6.31 | $6.92 |
| **+15%** | $4.66 | $5.28 | $5.89 | $6.50 | $7.11 |
| **+30%** | $4.85 | $5.46 | $6.08 | $6.69 | $7.30 |

_Current price $7.70. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.70** is -26.0% vs the current price ($7.70) and -43.0% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$123,511/day** (2.59× the current forward) — 5.9× the value-weighted 10-yr mean ($21,072, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
