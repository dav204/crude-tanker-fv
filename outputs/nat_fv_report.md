# NAT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $5.20
- **Model fair value:** $2.59
- **Analyst target:** $6.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 875.0 |
| + Cash & equivalents | 75.0 |
| + Working capital (net) | 25.0 |
| − Total debt | 395.0 |
| − Lease liabilities | 5.0 |
| − Newbuild commitments | 153.0 |
| + Newbuild advances | 17.0 |
| **= NAV total** | **439.0** |
| Diluted shares | 211,750,663 |
| **NAV / share** | **$2.07** |

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
| Terminal value (NAV, q9) | | | | 1.35 | 1.07 |
| **DivStrip implied price** | | | | | **$3.81** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.21×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.07 (NAV) + 0.30 × $3.81 (strip) = **$2.59**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.43 |
| 95% | $2.55 |
| 100% | $2.59 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.93× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **334,239** | — |
| 10-year mean | 27,747 | 12.05× |
| 12-month FFA | 85,000 | 3.93× |
| Current spot | 68,700 | 4.87× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.59 | $1.96 | $2.33 | $2.70 | $3.07 |
| **-15%** | $1.72 | $2.09 | $2.46 | $2.83 | $3.20 |
| **+0%** | $1.85 | $2.22 | $2.59 | $2.96 | $3.33 |
| **+15%** | $1.99 | $2.36 | $2.73 | $3.10 | $3.47 |
| **+30%** | $2.12 | $2.49 | $2.86 | $3.23 | $3.60 |

_Current price $5.20. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.59** is -50.1% vs the current price ($5.20) and -56.8% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$334,239/day** (3.93× the current forward) — 12.0× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.9M (+16%) / 10yr $50.7M (+13%) [n=25], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
