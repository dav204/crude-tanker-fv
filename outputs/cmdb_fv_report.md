# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $17.25
- **Model fair value:** $28.35
- **Analyst target:** $27.98

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 237.8 |
| Fleet value — Pana | 135.2 |
| Fleet value — Supra-Ultra | 306.0 |
| + Cash & equivalents | 258.5 |
| + Working capital (net) | 3.8 |
| − Total debt | 141.4 |
| − Lease liabilities | 20.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **779.3** |
| Diluted shares | 24,180,472 |
| **NAV / share** | **$32.23** |

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
| Terminal value (NAV, q9) | | | | 28.49 | 22.53 |
| **DivStrip implied price** | | | | | **$22.53** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,406/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$16,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $16,000 / 10-yr mean $13,930 = **1.21×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $32.23 (NAV) + 0.40 × $22.53 (strip) = **$28.35**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $30.17 |
| 95% | $30.51 |
| 100% | $30.63 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$32.23** ≥ price **$17.25** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 16,930 | 0.00× |
| 12-month FFA | 21,410 | 0.00× |
| Current spot | 26,177 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (45% of fleet value) | 0 | 0.00× |
| Cape (35% of fleet value) | 0 | 0.00× |
| Pana (20% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.44 | $25.89 | $28.35 | $30.80 | $33.26 |
| **-15%** | $23.44 | $25.89 | $28.35 | $30.80 | $33.26 |
| **+0%** | $23.44 | $25.89 | $28.35 | $30.80 | $33.26 |
| **+15%** | $23.44 | $25.89 | $28.35 | $30.80 | $33.26 |
| **+30%** | $23.44 | $25.89 | $28.35 | $30.80 | $33.26 |

_Current price $17.25. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$28.35** is +64.3% vs the current price ($17.25) and +1.3% vs the analyst target ($27.98). NAV alone covers the price (NAV/sh $32.23 ≥ $17.25); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
