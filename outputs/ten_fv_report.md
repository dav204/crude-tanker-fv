# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $44.00
- **Model fair value:** $58.42
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 378.8 |
| Fleet value — Suezmax | 927.9 |
| Fleet value — Aframax | 1,537.7 |
| Fleet value — LR2 | 237.0 |
| Fleet value — LR1 | 250.6 |
| Fleet value — MR | 98.8 |
| Fleet value — Handysize | 26.9 |
| Fleet value — LNGC | 443.2 |
| + Cash & equivalents | 321.4 |
| + Working capital (net) | 28.0 |
| − Total debt | 2,148.2 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 400.0 |
| **= NAV total** | **2,668.0** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$88.56** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 36,629 | 4.880 | 1.302 | 1.269 |
| Q2 | 88,000 | 38,995 | 5.340 | 1.390 | 1.319 |
| Q3 | 82,000 | 37,903 | 5.145 | 1.352 | 1.251 |
| Q4 | 64,000 | 34,627 | 4.518 | 1.233 | 1.111 |
| Q5 | 59,000 | 33,717 | 4.349 | 1.201 | 1.054 |
| Q6 | 70,000 | 35,719 | 4.747 | 1.277 | 1.092 |
| Q7 | 74,000 | 36,447 | 4.880 | 1.302 | 1.085 |
| Q8 | 56,000 | 33,171 | 4.257 | 1.184 | 0.961 |
| Σ discounted DPS | | | | | 9.14 |
| Terminal value (NAV, q9) | | | | 51.80 | 40.96 |
| **DivStrip implied price** | | | | | **$50.10** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.98×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $88.56 (NAV) + 0.30 × $50.10 (strip) = **$58.42**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $64.65 |
| 95% | $66.19 |
| 100% | $66.70 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$88.56** ≥ price **$44.00** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 34,987 | 0.00× |
| 12-month FFA | 83,361 | 0.00× |
| Current spot | 82,210 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (39% of fleet value) | 0 | 0.00× |
| Suezmax (24% of fleet value) | 0 | 0.00× |
| LNGC (11% of fleet value) | 0 | 0.00× |
| VLCC (10% of fleet value) | 0 | 0.00× |
| LR1 (6% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $41.64 | $49.89 | $58.14 | $66.40 | $74.65 |
| **-15%** | $41.78 | $50.03 | $58.28 | $66.54 | $74.79 |
| **+0%** | $41.92 | $50.17 | $58.42 | $66.68 | $74.93 |
| **+15%** | $42.06 | $50.31 | $58.56 | $66.82 | $75.07 |
| **+30%** | $42.20 | $50.45 | $58.70 | $66.96 | $75.21 |

_Current price $44.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$58.42** is +32.8% vs the current price ($44.00) and +13.4% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $88.56 ≥ $44.00); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
