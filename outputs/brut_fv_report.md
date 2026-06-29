# BRUT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $5.34
- **Model fair value:** $5.16
- **Analyst target:** $7.13

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,538.7 |
| + Cash & equivalents | 100.0 |
| + Working capital (net) | 0.0 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,370.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **268.7** |
| Diluted shares | 61,900,000 |
| **NAV / share** | **$4.34** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 147,500 | 0.141 | 0.000 | 0.000 |
| Q2 | 183,500 | 183,500 | 0.193 | 0.000 | 0.000 |
| Q3 | 165,500 | 165,500 | 0.394 | 0.000 | 0.000 |
| Q4 | 123,500 | 123,500 | 0.273 | 0.000 | 0.000 |
| Q5 | 111,500 | 111,500 | 0.387 | 0.000 | 0.000 |
| Q6 | 135,500 | 135,500 | 0.675 | 0.000 | 0.000 |
| Q7 | 147,500 | 147,500 | 0.745 | 0.000 | 0.000 |
| Q8 | 105,500 | 105,500 | 0.783 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 8.95 | 7.08 |
| **DivStrip implied price** | | | | | **$7.08** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $4.34 (NAV) + 0.30 × $7.08 (strip) = **$5.16**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.23 |
| 95% | $5.24 |
| 100% | $5.24 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.17× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **181,776** | — |
| 10-year mean | 40,000 | 4.54× |
| 12-month FFA | 155,000 | 1.17× |
| Current spot | 388,300 | 0.47× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $0.14 | $2.50 | $4.85 | $7.21 | $9.56 |
| **-15%** | $0.30 | $2.65 | $5.01 | $7.36 | $9.72 |
| **+0%** | $0.45 | $2.81 | $5.16 | $7.52 | $9.87 |
| **+15%** | $0.61 | $2.96 | $5.32 | $7.67 | $10.02 |
| **+30%** | $0.76 | $3.12 | $5.47 | $7.83 | $10.18 |

_Current price $5.34. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.16** is -3.3% vs the current price ($5.34) and -27.6% vs the analyst target ($7.13). The current price implies the fleet earning a value-weighted blended **$181,776/day** (1.17× the current forward) — 4.5× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
