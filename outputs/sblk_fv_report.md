# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $25.81
- **Model fair value:** $26.00
- **Analyst target:** $34.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,563.3 |
| Fleet value — Pana | 988.6 |
| Fleet value — Supra-Ultra | 1,318.8 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 100.0 |
| **= NAV total** | **3,120.6** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$26.57** |

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
| Terminal value (NAV, q9) | | | | 22.47 | 17.77 |
| **DivStrip implied price** | | | | | **$25.15** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.23×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $26.57 (NAV) + 0.40 × $25.15 (strip) = **$26.00**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.54 |
| 95% | $26.00 |
| 100% | $26.16 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.96× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **21,396** | — |
| 10-year mean | 17,337 | 1.23× |
| 12-month FFA | 22,230 | 0.96× |
| Current spot | 27,227 | 0.79× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (40% of fleet value) | 28,429 | 1.20× |
| Supra-Ultra (34% of fleet value) | 15,791 | 1.13× |
| Pana (26% of fleet value) | 17,752 | 1.49× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.68 | $21.57 | $24.46 | $27.35 | $30.24 |
| **-15%** | $19.45 | $22.34 | $25.23 | $28.12 | $31.01 |
| **+0%** | $20.22 | $23.11 | $26.00 | $28.89 | $31.78 |
| **+15%** | $20.99 | $23.88 | $26.77 | $29.66 | $32.56 |
| **+30%** | $21.77 | $24.66 | $27.55 | $30.44 | $33.33 |

_Current price $25.81. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.00** is +0.7% vs the current price ($25.81) and -24.6% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$21,396/day** (0.96× the current forward) — 1.2× the value-weighted 10-yr mean ($17,337, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
