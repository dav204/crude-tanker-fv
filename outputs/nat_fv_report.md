# NAT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $5.20
- **Model fair value:** $3.09
- **Analyst target:** $6.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 993.3 |
| + Cash & equivalents | 75.0 |
| + Working capital (net) | 25.0 |
| − Total debt | 395.0 |
| − Lease liabilities | 5.0 |
| − Newbuild commitments | 153.0 |
| + Newbuild advances | 17.0 |
| **= NAV total** | **557.3** |
| Diluted shares | 211,750,663 |
| **NAV / share** | **$2.63** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 71,000 | 0.406 | 0.406 | 0.395 |
| Q2 | 99,000 | 83,600 | 0.500 | 0.500 | 0.474 |
| Q3 | 92,000 | 78,560 | 0.462 | 0.462 | 0.427 |
| Q4 | 67,500 | 60,920 | 0.331 | 0.331 | 0.298 |
| Q5 | 60,000 | 55,520 | 0.290 | 0.290 | 0.255 |
| Q6 | 78,000 | 68,480 | 0.387 | 0.387 | 0.331 |
| Q7 | 81,500 | 71,000 | 0.406 | 0.406 | 0.338 |
| Q8 | 56,500 | 53,000 | 0.272 | 0.272 | 0.221 |
| Σ discounted DPS | | | | | 2.74 |
| Terminal value (NAV, q9) | | | | 1.78 | 1.41 |
| **DivStrip implied price** | | | | | **$4.15** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.21×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.63 (NAV) + 0.30 × $4.15 (strip) = **$3.09**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.92 |
| 95% | $3.04 |
| 100% | $3.09 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.38× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **287,175** | — |
| 10-year mean | 27,747 | 10.35× |
| 12-month FFA | 85,000 | 3.38× |
| Current spot | 68,700 | 4.18× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.98 | $2.40 | $2.82 | $3.24 | $3.66 |
| **-15%** | $2.11 | $2.53 | $2.95 | $3.37 | $3.79 |
| **+0%** | $2.25 | $2.67 | $3.09 | $3.51 | $3.92 |
| **+15%** | $2.38 | $2.80 | $3.22 | $3.64 | $4.06 |
| **+30%** | $2.51 | $2.93 | $3.35 | $3.77 | $4.19 |

_Current price $5.20. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$3.09** is -40.7% vs the current price ($5.20) and -48.6% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$287,175/day** (3.38× the current forward) — 10.3× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.
