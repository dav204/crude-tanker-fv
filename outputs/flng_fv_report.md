# FLNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $30.50
- **Model fair value:** $26.27
- **Analyst target:** $25.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 2,915.0 |
| + Cash & equivalents | 389.1 |
| + Working capital (net) | 56.0 |
| − Total debt | 1,821.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,539.1** |
| Diluted shares | 54,092,376 |
| **NAV / share** | **$28.45** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 76,873 | 0.871 | 0.750 | 0.731 |
| Q2 | 80,000 | 83,773 | 1.016 | 0.750 | 0.712 |
| Q3 | 75,000 | 82,623 | 0.992 | 0.750 | 0.694 |
| Q4 | 48,000 | 76,413 | 0.861 | 0.750 | 0.676 |
| Q5 | 52,000 | 77,333 | 0.881 | 0.750 | 0.658 |
| Q6 | 80,000 | 83,773 | 1.016 | 0.750 | 0.641 |
| Q7 | 75,000 | 82,623 | 0.992 | 0.750 | 0.625 |
| Q8 | 50,000 | 76,873 | 0.871 | 0.750 | 0.609 |
| Σ discounted DPS | | | | | 5.34 |
| Terminal value (NAV, q9) | | | | 24.61 | 19.46 |
| **DivStrip implied price** | | | | | **$24.81** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.71×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $28.45 (NAV) + 0.60 × $24.81 (strip) = **$26.27**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $29.47 |
| 95% | $30.07 |
| 100% | $30.27 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **50.00× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **3,162,500** | — |
| 10-year mean | 85,000 | 37.21× |
| 12-month FFA | 63,250 | 50.00× |
| Current spot | 40,000 | 79.06× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.21 | $21.74 | $26.27 | $30.80 | $35.33 |
| **-15%** | $17.21 | $21.74 | $26.27 | $30.80 | $35.33 |
| **+0%** | $17.21 | $21.74 | $26.27 | $30.80 | $35.33 |
| **+15%** | $17.21 | $21.74 | $26.27 | $30.80 | $35.33 |
| **+30%** | $17.21 | $21.74 | $26.27 | $30.80 | $35.33 |

_Current price $30.50. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.27** is -13.9% vs the current price ($30.50) and +5.1% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$3,162,500/day** (50.00× the current forward) — 37.2× the value-weighted 10-yr mean ($85,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
