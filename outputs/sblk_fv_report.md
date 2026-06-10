# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $27.20
- **Model fair value:** $25.66
- **Analyst target:** $34.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,567.7 |
| Fleet value — Pana | 957.0 |
| Fleet value — Supra-Ultra | 1,300.5 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 100.0 |
| **= NAV total** | **3,075.2** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$26.19** |

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
| Terminal value (NAV, q9) | | | | 22.12 | 17.49 |
| **DivStrip implied price** | | | | | **$24.87** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.23×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $26.19 (NAV) + 0.40 × $24.87 (strip) = **$25.66**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.19 |
| 95% | $25.66 |
| 100% | $25.82 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.30× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **28,969** | — |
| 10-year mean | 17,406 | 1.66× |
| 12-month FFA | 22,298 | 1.30× |
| Current spot | 27,332 | 1.06× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (41% of fleet value) | 38,375 | 1.62× |
| Supra-Ultra (34% of fleet value) | 21,315 | 1.53× |
| Pana (25% of fleet value) | 23,962 | 2.01× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.41 | $21.26 | $24.12 | $26.97 | $29.83 |
| **-15%** | $19.18 | $22.03 | $24.89 | $27.75 | $30.60 |
| **+0%** | $19.95 | $22.80 | $25.66 | $28.52 | $31.37 |
| **+15%** | $20.72 | $23.58 | $26.43 | $29.29 | $32.15 |
| **+30%** | $21.49 | $24.35 | $27.20 | $30.06 | $32.92 |

_Current price $27.20. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.66** is -5.7% vs the current price ($27.20) and -25.6% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$28,969/day** (1.30× the current forward) — 1.7× the value-weighted 10-yr mean ($17,406, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $73.3M (+18%) / 10yr $50.5M (+12%) [n=21], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $85.9M (-7%) / 10yr $69.7M (-13%) [n=18], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
