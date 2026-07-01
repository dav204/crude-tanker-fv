# ECO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $50.12
- **Model fair value:** $37.33
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 949.0 |
| Fleet value — Suezmax | 978.9 |
| + Cash & equivalents | 176.5 |
| + Working capital (net) | 86.9 |
| − Total debt | 683.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 158.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,349.3** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$34.56** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.623 | 3.080 | 3.001 |
| Q2 | 99,000 | 99,000 | 4.604 | 3.913 | 3.714 |
| Q3 | 92,000 | 92,000 | 4.154 | 3.531 | 3.265 |
| Q4 | 67,500 | 67,500 | 2.917 | 2.479 | 2.233 |
| Q5 | 60,000 | 60,000 | 2.552 | 2.169 | 1.904 |
| Q6 | 78,000 | 78,000 | 3.350 | 2.848 | 2.435 |
| Q7 | 81,500 | 81,500 | 3.623 | 3.080 | 2.566 |
| Q8 | 56,500 | 56,500 | 2.375 | 2.019 | 1.638 |
| Σ discounted DPS | | | | | 20.76 |
| Terminal value (NAV, q9) | | | | 29.14 | 23.05 |
| **DivStrip implied price** | | | | | **$43.80** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.49×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $34.56 (NAV) + 0.30 × $43.80 (strip) = **$37.33**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $37.29 |
| 95% | $37.42 |
| 100% | $37.46 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.51× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **299,354** | — |
| 10-year mean | 33,779 | 8.86× |
| 12-month FFA | 119,458 | 2.51× |
| Current spot | 226,023 | 1.32× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (51% of fleet value) | 213,005 | 7.68× |
| VLCC (49% of fleet value) | 388,422 | 9.71× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $25.98 | $30.38 | $34.78 | $39.19 | $43.59 |
| **-15%** | $27.25 | $31.66 | $36.06 | $40.46 | $44.86 |
| **+0%** | $28.53 | $32.93 | $37.33 | $41.73 | $46.14 |
| **+15%** | $29.80 | $34.20 | $38.61 | $43.01 | $47.41 |
| **+30%** | $31.07 | $35.48 | $39.88 | $44.28 | $48.68 |

_Current price $50.12. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$37.33** is -25.5% vs the current price ($50.12) and -17.0% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$299,354/day** (2.51× the current forward) — 8.9× the value-weighted 10-yr mean ($33,779, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
