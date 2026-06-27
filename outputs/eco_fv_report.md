# ECO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $49.88
- **Model fair value:** $36.78
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 949.0 |
| Fleet value — Suezmax | 952.4 |
| + Cash & equivalents | 176.5 |
| + Working capital (net) | 86.9 |
| − Total debt | 683.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 158.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,322.9** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$33.88** |

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
| Terminal value (NAV, q9) | | | | 28.81 | 22.78 |
| **DivStrip implied price** | | | | | **$43.54** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.50×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.88 (NAV) + 0.30 × $43.54 (strip) = **$36.78**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $36.73 |
| 95% | $36.87 |
| 100% | $36.91 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.54× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **304,990** | — |
| 10-year mean | 33,862 | 9.01× |
| 12-month FFA | 119,937 | 2.54× |
| Current spot | 228,213 | 1.34× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (50% of fleet value) | 216,148 | 7.79× |
| VLCC (50% of fleet value) | 394,152 | 9.85× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $25.54 | $29.88 | $34.23 | $38.58 | $42.92 |
| **-15%** | $26.81 | $31.16 | $35.50 | $39.85 | $44.20 |
| **+0%** | $28.08 | $32.43 | $36.78 | $41.12 | $45.47 |
| **+15%** | $29.36 | $33.70 | $38.05 | $42.40 | $46.75 |
| **+30%** | $30.63 | $34.98 | $39.33 | $43.67 | $48.02 |

_Current price $49.88. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$36.78** is -26.3% vs the current price ($49.88) and -18.3% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$304,990/day** (2.54× the current forward) — 9.0× the value-weighted 10-yr mean ($33,862, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
