# ECO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $47.70
- **Model fair value:** $42.56
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,132.4 |
| Fleet value — Suezmax | 1,005.4 |
| + Cash & equivalents | 176.5 |
| + Working capital (net) | 86.9 |
| − Total debt | 683.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 158.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,559.2** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$39.93** |

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
| Terminal value (NAV, q9) | | | | 35.34 | 27.95 |
| **DivStrip implied price** | | | | | **$48.70** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.51×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $39.93 (NAV) + 0.30 × $48.70 (strip) = **$42.56**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $42.20 |
| 95% | $43.30 |
| 100% | $43.66 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.70× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **207,393** | — |
| 10-year mean | 34,237 | 6.06× |
| 12-month FFA | 122,079 | 1.70× |
| Current spot | 237,994 | 0.87× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (53% of fleet value) | 263,319 | 6.58× |
| Suezmax (47% of fleet value) | 144,401 | 5.20× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $30.32 | $35.34 | $40.36 | $45.38 | $50.41 |
| **-15%** | $31.42 | $36.44 | $41.46 | $46.48 | $51.51 |
| **+0%** | $32.52 | $37.54 | $42.56 | $47.59 | $52.61 |
| **+15%** | $33.62 | $38.64 | $43.67 | $48.69 | $53.71 |
| **+30%** | $34.72 | $39.75 | $44.77 | $49.79 | $54.81 |

_Current price $47.70. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$42.56** is -10.8% vs the current price ($47.70) and -5.4% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$207,393/day** (1.70× the current forward) — 6.1× the value-weighted 10-yr mean ($34,237, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
