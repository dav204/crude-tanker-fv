# DHT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.40
- **Model fair value:** $16.49
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,729.9 |
| + Cash & equivalents | 126.2 |
| + Working capital (net) | 134.1 |
| − Total debt | 505.3 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 55.7 |
| **= NAV total** | **2,462.2** |
| Diluted shares | 161,041,637 |
| **NAV / share** | **$15.29** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 118,981 | 1.265 | 1.265 | 1.233 |
| Q2 | 183,500 | 138,781 | 1.507 | 1.507 | 1.430 |
| Q3 | 165,500 | 128,881 | 1.386 | 1.386 | 1.282 |
| Q4 | 123,500 | 105,781 | 1.104 | 1.104 | 0.995 |
| Q5 | 111,500 | 99,181 | 1.024 | 1.024 | 0.898 |
| Q6 | 135,500 | 112,381 | 1.185 | 1.185 | 1.013 |
| Q7 | 147,500 | 118,981 | 1.265 | 1.265 | 1.054 |
| Q8 | 105,500 | 95,881 | 0.983 | 0.983 | 0.798 |
| Σ discounted DPS | | | | | 8.70 |
| Terminal value (NAV, q9) | | | | 13.38 | 10.58 |
| **DivStrip implied price** | | | | | **$19.28** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.29 (NAV) + 0.30 × $19.28 (strip) = **$16.49**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.96 |
| 95% | $16.36 |
| 100% | $16.49 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.96× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **148,415** | — |
| 10-year mean | 40,000 | 3.71× |
| 12-month FFA | 155,000 | 0.96× |
| Current spot | 388,300 | 0.38× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $12.79 | $14.34 | $15.88 | $17.42 | $18.97 |
| **-15%** | $13.10 | $14.64 | $16.18 | $17.73 | $19.27 |
| **+0%** | $13.40 | $14.94 | $16.49 | $18.03 | $19.57 |
| **+15%** | $13.70 | $15.25 | $16.79 | $18.33 | $19.88 |
| **+30%** | $14.01 | $15.55 | $17.09 | $18.64 | $20.18 |

_Current price $16.40. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$16.49** is +0.5% vs the current price ($16.40) and +3.0% vs the analyst target ($16.00). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$148,415/day** (0.96× the current forward) — 3.7× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is below the forward curve.
