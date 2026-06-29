# ECO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $49.88
- **Model fair value:** $35.41
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 936.4 |
| Fleet value — Suezmax | 897.8 |
| + Cash & equivalents | 176.5 |
| + Working capital (net) | 86.9 |
| − Total debt | 683.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 158.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,255.7** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$32.16** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 140,737 | 3.623 | 3.080 | 3.001 |
| Q2 | 183,500 | 172,417 | 4.604 | 3.913 | 3.714 |
| Q3 | 165,500 | 156,577 | 4.154 | 3.531 | 3.265 |
| Q4 | 123,500 | 119,617 | 2.917 | 2.479 | 2.233 |
| Q5 | 111,500 | 109,057 | 2.552 | 2.169 | 1.904 |
| Q6 | 135,500 | 130,177 | 3.350 | 2.848 | 2.435 |
| Q7 | 147,500 | 140,737 | 3.623 | 3.080 | 2.566 |
| Q8 | 105,500 | 103,777 | 2.375 | 2.019 | 1.638 |
| Σ discounted DPS | | | | | 20.76 |
| Terminal value (NAV, q9) | | | | 28.12 | 22.23 |
| **DivStrip implied price** | | | | | **$42.99** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.50×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $32.16 (NAV) + 0.30 × $42.99 (strip) = **$35.41**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $35.37 |
| 95% | $35.50 |
| 100% | $35.54 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.70× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **326,486** | — |
| 10-year mean | 34,002 | 9.60× |
| 12-month FFA | 120,736 | 2.70× |
| Current spot | 231,861 | 1.41× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (51% of fleet value) | 419,140 | 10.48× |
| Suezmax (49% of fleet value) | 229,851 | 8.28× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.44 | $28.65 | $32.86 | $37.07 | $41.28 |
| **-15%** | $25.71 | $29.93 | $34.14 | $38.35 | $42.56 |
| **+0%** | $26.99 | $31.20 | $35.41 | $39.62 | $43.83 |
| **+15%** | $28.26 | $32.47 | $36.68 | $40.89 | $45.10 |
| **+30%** | $29.54 | $33.75 | $37.96 | $42.17 | $46.38 |

_Current price $49.88. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$35.41** is -29.0% vs the current price ($49.88) and -21.3% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$326,486/day** (2.70× the current forward) — 9.6× the value-weighted 10-yr mean ($34,002, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
