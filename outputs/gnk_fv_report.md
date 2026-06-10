# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.00
- **Model fair value:** $25.28
- **Analyst target:** $24.80

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 924.0 |
| Fleet value — Supra-Ultra | 505.6 |
| + Cash & equivalents | 54.8 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,165.6** |
| Diluted shares | 44,411,222 |
| **NAV / share** | **$26.24** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 31,200 | 31,465 | 1.198 | 1.198 | 1.167 |
| Q2 | 31,450 | 31,702 | 1.170 | 1.170 | 1.111 |
| Q3 | 28,500 | 28,900 | 0.997 | 0.997 | 0.922 |
| Q4 | 27,000 | 27,475 | 0.928 | 0.928 | 0.836 |
| Q5 | 25,500 | 26,050 | 0.863 | 0.863 | 0.758 |
| Q6 | 25,000 | 25,575 | 0.838 | 0.838 | 0.717 |
| Q7 | 24,500 | 25,100 | 0.813 | 0.813 | 0.677 |
| Q8 | 24,000 | 24,625 | 0.790 | 0.790 | 0.641 |
| Σ discounted DPS | | | | | 6.83 |
| Terminal value (NAV, q9) | | | | 22.11 | 17.48 |
| **DivStrip implied price** | | | | | **$24.31** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.14×** → **mid-cycle**
- Weights: w_nav = 0.50, w_earn = 0.50

## Blended fair value

0.50 × $26.24 (NAV) + 0.50 × $24.31 (strip) = **$25.28**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.59 |
| 95% | $25.11 |
| 100% | $25.28 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.74× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,314** | — |
| 10-year mean | 20,212 | 0.91× |
| 12-month FFA | 24,893 | 0.74× |
| Current spot | 31,457 | 0.58× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (65% of fleet value) | 21,731 | 0.92× |
| Supra-Ultra (35% of fleet value) | 12,070 | 0.87× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.39 | $21.11 | $23.83 | $26.55 | $29.26 |
| **-15%** | $19.11 | $21.83 | $24.55 | $27.27 | $29.99 |
| **+0%** | $19.84 | $22.56 | $25.28 | $27.99 | $30.71 |
| **+15%** | $20.56 | $23.28 | $26.00 | $28.72 | $31.44 |
| **+30%** | $21.29 | $24.01 | $26.72 | $29.44 | $32.16 |

_Current price $24.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.28** is +5.3% vs the current price ($24.00) and +1.9% vs the analyst target ($24.80). The current price implies the fleet earning a value-weighted blended **$18,314/day** (0.74× the current forward) — 0.9× the value-weighted 10-yr mean ($20,212, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
