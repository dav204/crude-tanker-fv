# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.36
- **Model fair value:** $10.17
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 1,026.7 |
| Fleet value — Post-Panamax | 416.4 |
| Fleet value — Cape | 268.8 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 227.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,066.0** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$10.47** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 20,775 | 18,678 | 0.568 | 0.171 | 0.166 |
| Q2 | 19,500 | 18,168 | 0.551 | 0.165 | 0.157 |
| Q3 | 17,000 | 17,168 | 0.495 | 0.148 | 0.137 |
| Q4 | 16,500 | 16,968 | 0.478 | 0.143 | 0.129 |
| Q5 | 15,800 | 16,688 | 0.458 | 0.137 | 0.121 |
| Q6 | 15,400 | 16,528 | 0.449 | 0.135 | 0.115 |
| Q7 | 14,800 | 16,288 | 0.437 | 0.131 | 0.109 |
| Q8 | 14,500 | 16,168 | 0.429 | 0.129 | 0.104 |
| Σ discounted DPS | | | | | 1.04 |
| Terminal value (NAV, q9) | | | | 10.98 | 8.68 |
| **DivStrip implied price** | | | | | **$9.72** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,444/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$17,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $17,500 / 10-yr mean $11,900 = **1.42×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $10.47 (NAV) + 0.40 × $9.72 (strip) = **$10.17**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $10.25 |
| 95% | $10.27 |
| 100% | $10.28 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.47** ≥ price **$6.36** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,745 | 0.00× |
| 12-month FFA | 20,186 | 0.00× |
| Current spot | 23,248 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (60% of fleet value) | 0 | 0.00× |
| Post-Panamax (24% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.89 | $8.36 | $9.84 | $11.31 | $12.78 |
| **-15%** | $7.06 | $8.53 | $10.00 | $11.47 | $12.94 |
| **+0%** | $7.23 | $8.70 | $10.17 | $11.64 | $13.11 |
| **+15%** | $7.39 | $8.86 | $10.33 | $11.81 | $13.28 |
| **+30%** | $7.56 | $9.03 | $10.50 | $11.97 | $13.44 |

_Current price $6.36. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$10.17** is +59.9% vs the current price ($6.36) and +43.2% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.47 ≥ $6.36); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
