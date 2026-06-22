# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.90
- **Model fair value:** $21.12
- **Analyst target:** $27.98

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 237.8 |
| Fleet value — Pana | 140.3 |
| Fleet value — Supra-Ultra | 307.2 |
| + Cash & equivalents | 258.5 |
| + Working capital (net) | 3.8 |
| − Total debt | 141.4 |
| − Lease liabilities | 20.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **785.5** |
| Diluted shares | 24,180,472 |
| **NAV / share** | **$32.49** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,075 | 19,075 | 1.228 | 0.000 | 0.000 |
| Q2 | 17,550 | 17,550 | 1.110 | 0.000 | 0.000 |
| Q3 | 14,800 | 14,800 | 0.817 | 0.000 | 0.000 |
| Q4 | 14,200 | 14,200 | 0.736 | 0.000 | 0.000 |
| Q5 | 13,800 | 13,800 | 0.661 | 0.000 | 0.000 |
| Q6 | 13,500 | 13,500 | 0.621 | 0.000 | 0.000 |
| Q7 | 13,200 | 13,200 | 0.577 | 0.000 | 0.000 |
| Q8 | 13,000 | 13,000 | 0.546 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 23.64 | 18.69 |
| **DivStrip implied price** | | | | | **$18.69** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,406/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$16,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $16,000 / 10-yr mean $13,930 = **1.21×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $32.49 (NAV) + 0.40 × $18.69 (strip) = **$21.12**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.83 |
| 95% | $21.96 |
| 100% | $22.01 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$32.49** ≥ price **$16.90** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 16,887 | 0.00× |
| 12-month FFA | 21,380 | 0.00× |
| Current spot | 26,124 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (45% of fleet value) | 0 | 0.00× |
| Cape (35% of fleet value) | 0 | 0.00× |
| Pana (20% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.69 | $18.39 | $20.10 | $21.81 | $23.51 |
| **-15%** | $17.20 | $18.90 | $20.61 | $22.32 | $24.02 |
| **+0%** | $17.71 | $19.41 | $21.12 | $22.83 | $24.53 |
| **+15%** | $18.22 | $19.92 | $21.63 | $23.34 | $25.04 |
| **+30%** | $18.73 | $20.43 | $22.14 | $23.85 | $25.55 |

_Current price $16.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.12** is +25.0% vs the current price ($16.90) and -24.5% vs the analyst target ($27.98). NAV alone covers the price (NAV/sh $32.49 ≥ $16.90); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
