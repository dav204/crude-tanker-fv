# STNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $75.60
- **Model fair value:** $77.29
- **Analyst target:** $94.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 2,273.4 |
| Fleet value — MR | 1,402.0 |
| Fleet value — Handymax | 205.3 |
| + Cash & equivalents | 984.3 |
| + Working capital (net) | 602.8 |
| − Total debt | 789.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 572.8 |
| + Newbuild advances | 90.0 |
| **= NAV total** | **4,196.0** |
| Diluted shares | 50,030,000 |
| **NAV / share** | **$83.87** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 69,375 | 3.958 | 0.450 | 0.438 |
| Q2 | 88,000 | 80,750 | 5.395 | 0.450 | 0.427 |
| Q3 | 82,000 | 75,500 | 4.898 | 0.450 | 0.416 |
| Q4 | 64,000 | 59,750 | 3.112 | 0.450 | 0.405 |
| Q5 | 59,000 | 55,375 | 2.764 | 0.450 | 0.395 |
| Q6 | 70,000 | 65,000 | 3.806 | 0.450 | 0.385 |
| Q7 | 74,000 | 68,500 | 4.301 | 0.450 | 0.375 |
| Q8 | 56,000 | 52,750 | 2.614 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 74.30 | 58.75 |
| **DivStrip implied price** | | | | | **$61.96** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.76×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $83.87 (NAV) + 0.30 × $61.96 (strip) = **$77.29**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $83.94 |
| 95% | $85.19 |
| 100% | $85.60 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$83.87** ≥ price **$75.60** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 22,796 | 0.00× |
| 12-month FFA | 55,506 | 0.00× |
| Current spot | 37,868 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (59% of fleet value) | 0 | 0.00× |
| MR (36% of fleet value) | 0 | 0.00× |
| Handymax (5% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $63.21 | $70.25 | $77.29 | $84.34 | $91.38 |
| **-15%** | $63.21 | $70.25 | $77.29 | $84.34 | $91.38 |
| **+0%** | $63.21 | $70.25 | $77.29 | $84.34 | $91.38 |
| **+15%** | $63.21 | $70.25 | $77.29 | $84.34 | $91.38 |
| **+30%** | $63.21 | $70.25 | $77.29 | $84.34 | $91.38 |

_Current price $75.60. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$77.29** is +2.2% vs the current price ($75.60) and -17.8% vs the analyst target ($94.00). NAV alone covers the price (NAV/sh $83.87 ≥ $75.60); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
