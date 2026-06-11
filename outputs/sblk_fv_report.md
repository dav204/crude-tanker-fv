# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $27.06
- **Model fair value:** $25.74
- **Analyst target:** $34.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,563.3 |
| Fleet value — Pana | 957.0 |
| Fleet value — Supra-Ultra | 1,314.2 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 100.0 |
| **= NAV total** | **3,084.4** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$26.27** |

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
| Terminal value (NAV, q9) | | | | 22.23 | 17.57 |
| **DivStrip implied price** | | | | | **$24.95** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.23×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $26.27 (NAV) + 0.40 × $24.95 (strip) = **$25.74**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.28 |
| 95% | $25.74 |
| 100% | $25.90 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.26× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **27,977** | — |
| 10-year mean | 17,386 | 1.61× |
| 12-month FFA | 22,268 | 1.26× |
| Current spot | 27,292 | 1.03× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (41% of fleet value) | 37,110 | 1.57× |
| Supra-Ultra (34% of fleet value) | 20,612 | 1.48× |
| Pana (25% of fleet value) | 23,172 | 1.95× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.47 | $21.33 | $24.20 | $27.06 | $29.93 |
| **-15%** | $19.24 | $22.11 | $24.97 | $27.83 | $30.70 |
| **+0%** | $20.01 | $22.88 | $25.74 | $28.61 | $31.47 |
| **+15%** | $20.78 | $23.65 | $26.51 | $29.38 | $32.24 |
| **+30%** | $21.56 | $24.42 | $27.28 | $30.15 | $33.01 |

_Current price $27.06. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.74** is -4.9% vs the current price ($27.06) and -25.4% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$27,977/day** (1.26× the current forward) — 1.6× the value-weighted 10-yr mean ($17,386, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
