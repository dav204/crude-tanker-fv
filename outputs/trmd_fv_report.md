# TRMD — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $28.20
- **Model fair value:** $27.27
- **Analyst target:** $25.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,496.9 |
| Fleet value — LR1 | 342.3 |
| Fleet value — MR | 2,021.2 |
| + Cash & equivalents | 196.0 |
| + Working capital (net) | 110.0 |
| − Total debt | 1,089.6 |
| − Lease liabilities | 5.0 |
| − Newbuild commitments | 360.0 |
| + Newbuild advances | 50.0 |
| **= NAV total** | **2,761.8** |
| Diluted shares | 103,300,000 |
| **NAV / share** | **$26.74** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 2.165 | 1.624 | 1.582 |
| Q2 | 30,000 | 30,000 | 2.949 | 2.212 | 2.099 |
| Q3 | 28,000 | 28,000 | 2.678 | 2.008 | 1.857 |
| Q4 | 19,000 | 19,000 | 1.703 | 1.278 | 1.151 |
| Q5 | 18,000 | 18,000 | 1.513 | 1.135 | 0.996 |
| Q6 | 23,000 | 23,000 | 2.082 | 1.561 | 1.335 |
| Q7 | 26,000 | 26,000 | 2.352 | 1.764 | 1.470 |
| Q8 | 18,000 | 18,000 | 1.431 | 1.074 | 0.871 |
| Σ discounted DPS | | | | | 11.36 |
| Terminal value (NAV, q9) | | | | 21.70 | 17.16 |
| **DivStrip implied price** | | | | | **$28.52** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.69×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $26.74 (NAV) + 0.30 × $28.52 (strip) = **$27.27**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $27.50 |
| 95% | $28.18 |
| 100% | $28.41 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.18× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **58,812** | — |
| 10-year mean | 21,527 | 2.73× |
| 12-month FFA | 49,762 | 1.18× |
| Current spot | 30,054 | 1.96× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (52% of fleet value) | 29,251 | 1.83× |
| LR2 (39% of fleet value) | 91,298 | 3.31× |
| LR1 (9% of fleet value) | 91,298 | 3.31× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.97 | $22.35 | $25.74 | $29.12 | $32.50 |
| **-15%** | $19.74 | $23.12 | $26.50 | $29.89 | $33.27 |
| **+0%** | $20.50 | $23.89 | $27.27 | $30.65 | $34.04 |
| **+15%** | $21.27 | $24.65 | $28.04 | $31.42 | $34.80 |
| **+30%** | $22.04 | $25.42 | $28.80 | $32.19 | $35.57 |

_Current price $28.20. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$27.27** is -3.3% vs the current price ($28.20) and +9.1% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$58,812/day** (1.18× the current forward) — 2.7× the value-weighted 10-yr mean ($21,527, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
