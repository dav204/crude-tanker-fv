# GSL — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $38.99
- **Model fair value:** $33.61
- **Analyst target:** $52.04

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Large | 1,222.9 |
| Fleet value — Ctr-Intermediate | 529.4 |
| + Cash & equivalents | 404.9 |
| + Working capital (net) | 0.0 |
| − Total debt | 657.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,390.5** |
| Diluted shares | 36,035,434 |
| **NAV / share** | **$38.59** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Large, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 62,500 | 32,571 | 3.429 | 0.625 | 0.609 |
| Q2 | 61,500 | 32,571 | 3.429 | 0.625 | 0.593 |
| Q3 | 60,000 | 32,571 | 3.515 | 0.625 | 0.578 |
| Q4 | 58,500 | 32,571 | 3.671 | 0.625 | 0.563 |
| Q5 | 57,000 | 32,571 | 3.819 | 0.625 | 0.549 |
| Q6 | 55,500 | 32,571 | 3.902 | 0.625 | 0.534 |
| Q7 | 54,000 | 33,621 | 4.098 | 0.625 | 0.521 |
| Q8 | 52,000 | 33,990 | 4.285 | 0.625 | 0.507 |
| Q9 | 50,000 | 35,970 | 4.495 | 0.625 | 0.494 |
| Q10 | 48,000 | 38,218 | 4.785 | 0.625 | 0.481 |
| Σ discounted DPS | | | | | 5.43 |
| Terminal value (NAV, q9) | | | | 27.59 | 20.71 |
| **DivStrip implied price** | | | | | **$26.14** |

_FFA spot is the Ctr-Large forward curve that drives the strip cash flows; its 12-month average is **$60,625/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$62,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $62,500 / 10-yr mean $41,000 = **1.45×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $38.59 (NAV) + 0.40 × $26.14 (strip) = **$33.61**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $42.78 |
| 95% | $44.39 |
| 100% | $44.92 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **50.00× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **2,757,173** | — |
| 10-year mean | 38,795 | 71.07× |
| 12-month FFA | 55,143 | 50.00× |
| Current spot | 56,730 | 48.60× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Large (70% of fleet value) | 3,031,250 | 73.93× |
| Ctr-Intermediate (30% of fleet value) | 2,124,062 | 63.03× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $25.90 | $30.06 | $34.23 | $38.39 | $42.56 |
| **-15%** | $25.90 | $30.06 | $34.23 | $38.39 | $42.56 |
| **+0%** | $25.90 | $30.06 | $34.23 | $38.39 | $42.56 |
| **+15%** | $25.90 | $30.06 | $34.23 | $38.39 | $42.56 |
| **+30%** | $25.90 | $30.06 | $34.23 | $38.39 | $42.56 |

_Current price $38.99. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$33.61** is -13.8% vs the current price ($38.99) and -35.4% vs the analyst target ($52.04). The current price implies the fleet earning a value-weighted blended **$2,757,173/day** (50.00× the current forward) — 71.1× the value-weighted 10-yr mean ($38,795, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
