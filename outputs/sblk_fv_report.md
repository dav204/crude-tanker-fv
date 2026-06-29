# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.64
- **Model fair value:** $26.00
- **Analyst target:** $34.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.5 |
| Fleet value — Pana | 1,022.2 |
| Fleet value — Supra-Ultra | 1,330.4 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 100.0 |
| **= NAV total** | **3,160.0** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$26.91** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 31,200 | 31,200 | 1.498 | 1.423 | 1.386 |
| Q2 | 31,450 | 31,450 | 1.391 | 1.322 | 1.255 |
| Q3 | 28,500 | 28,500 | 1.113 | 1.057 | 0.978 |
| Q4 | 27,000 | 27,000 | 1.033 | 0.982 | 0.884 |
| Q5 | 25,500 | 25,500 | 0.956 | 0.908 | 0.797 |
| Q6 | 25,000 | 25,000 | 0.917 | 0.871 | 0.745 |
| Q7 | 24,500 | 24,500 | 0.871 | 0.827 | 0.689 |
| Q8 | 24,000 | 24,000 | 0.839 | 0.797 | 0.647 |
| Σ discounted DPS | | | | | 7.38 |
| Terminal value (NAV, q9) | | | | 21.82 | 17.25 |
| **DivStrip implied price** | | | | | **$24.63** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.23×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $26.91 (NAV) + 0.40 × $24.63 (strip) = **$26.00**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.94 |
| 95% | $26.00 |
| 100% | $26.02 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.75× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **16,572** | — |
| 10-year mean | 17,271 | 0.96× |
| 12-month FFA | 22,169 | 0.75× |
| Current spot | 27,130 | 0.61× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (40% of fleet value) | 22,080 | 0.93× |
| Supra-Ultra (34% of fleet value) | 12,264 | 0.88× |
| Pana (26% of fleet value) | 13,787 | 1.16× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.63 | $21.51 | $24.38 | $27.26 | $30.14 |
| **-15%** | $19.44 | $22.32 | $25.19 | $28.07 | $30.94 |
| **+0%** | $20.25 | $23.12 | $26.00 | $28.88 | $31.75 |
| **+15%** | $21.05 | $23.93 | $26.81 | $29.68 | $32.56 |
| **+30%** | $21.86 | $24.74 | $27.61 | $30.49 | $33.37 |

_Current price $24.64. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.00** is +5.5% vs the current price ($24.64) and -24.6% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$16,572/day** (0.75× the current forward) — 1.0× the value-weighted 10-yr mean ($17,271, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
