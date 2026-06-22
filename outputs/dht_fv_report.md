# DHT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.89
- **Model fair value:** $14.00
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,350.5 |
| + Cash & equivalents | 126.2 |
| + Working capital (net) | 134.1 |
| − Total debt | 505.3 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 55.7 |
| **= NAV total** | **2,082.7** |
| Diluted shares | 161,041,637 |
| **NAV / share** | **$12.93** |

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
| Terminal value (NAV, q9) | | | | 9.86 | 7.80 |
| **DivStrip implied price** | | | | | **$16.50** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $12.93 (NAV) + 0.30 × $16.50 (strip) = **$14.00**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $13.94 |
| 95% | $13.99 |
| 100% | $14.00 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.42× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **529,540** | — |
| 10-year mean | 40,000 | 13.24× |
| 12-month FFA | 155,000 | 3.42× |
| Current spot | 388,300 | 1.36× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.81 | $12.10 | $13.40 | $14.69 | $15.99 |
| **-15%** | $11.11 | $12.40 | $13.70 | $14.99 | $16.29 |
| **+0%** | $11.41 | $12.71 | $14.00 | $15.30 | $16.59 |
| **+15%** | $11.72 | $13.01 | $14.31 | $15.60 | $16.90 |
| **+30%** | $12.02 | $13.31 | $14.61 | $15.90 | $17.20 |

_Current price $18.89. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.00** is -25.9% vs the current price ($18.89) and -12.5% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$529,540/day** (3.42× the current forward) — 13.2× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
