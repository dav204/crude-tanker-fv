# BRUT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $5.21
- **Model fair value:** $9.27
- **Analyst target:** $7.13

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,851.9 |
| + Cash & equivalents | 66.0 |
| + Working capital (net) | 0.0 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,373.1 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **544.8** |
| Diluted shares | 61,923,808 |
| **NAV / share** | **$8.80** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 147,500 | 0.141 | 0.000 | 0.000 |
| Q2 | 183,500 | 183,500 | 0.193 | 0.000 | 0.000 |
| Q3 | 165,500 | 165,500 | 0.394 | 0.000 | 0.000 |
| Q4 | 123,500 | 123,500 | 0.273 | 0.000 | 0.000 |
| Q5 | 111,500 | 111,500 | 0.387 | 0.000 | 0.000 |
| Q6 | 135,500 | 135,500 | 0.675 | 0.000 | 0.000 |
| Q7 | 147,500 | 147,500 | 0.744 | 0.000 | 0.000 |
| Q8 | 105,500 | 105,500 | 0.783 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 13.12 | 10.37 |
| **DivStrip implied price** | | | | | **$10.37** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $8.80 (NAV) + 0.30 × $10.37 (strip) = **$9.27**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.33 |
| 95% | $9.35 |
| 100% | $9.35 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$8.80** ≥ price **$5.21** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 40,000 | 0.00× |
| 12-month FFA | 155,000 | 0.00× |
| Current spot | 388,300 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $3.32 | $6.14 | $8.96 | $11.78 | $14.60 |
| **-15%** | $3.48 | $6.30 | $9.12 | $11.94 | $14.76 |
| **+0%** | $3.63 | $6.45 | $9.27 | $12.09 | $14.91 |
| **+15%** | $3.78 | $6.60 | $9.43 | $12.25 | $15.07 |
| **+30%** | $3.94 | $6.76 | $9.58 | $12.40 | $15.22 |

_Current price $5.21. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.27** is +77.9% vs the current price ($5.21) and +30.0% vs the analyst target ($7.13). NAV alone covers the price (NAV/sh $8.80 ≥ $5.21); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
