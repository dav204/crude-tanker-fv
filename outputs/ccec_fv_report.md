# CCEC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $21.90
- **Model fair value:** $22.88
- **Analyst target:** $25.17

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 5,399.5 |
| Fleet value — MGC | 585.0 |
| + Cash & equivalents | 546.4 |
| + Working capital (net) | 12.9 |
| − Total debt | 2,602.9 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 2,251.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,689.3** |
| Diluted shares | 60,121,845 |
| **NAV / share** | **$28.10** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 80,557 | 1.938 | 0.150 | 0.146 |
| Q2 | 80,000 | 83,557 | 2.041 | 0.150 | 0.142 |
| Q3 | 75,000 | 83,057 | 2.023 | 0.150 | 0.139 |
| Q4 | 48,000 | 80,357 | 1.932 | 0.150 | 0.135 |
| Q5 | 52,000 | 80,757 | 1.946 | 0.150 | 0.132 |
| Q6 | 80,000 | 83,557 | 2.041 | 0.150 | 0.128 |
| Q7 | 75,000 | 83,057 | 2.023 | 0.150 | 0.125 |
| Q8 | 50,000 | 80,557 | 1.938 | 0.150 | 0.122 |
| Σ discounted DPS | | | | | 1.07 |
| Terminal value (NAV, q9) | | | | 23.18 | 18.33 |
| **DivStrip implied price** | | | | | **$19.39** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.77×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $28.10 (NAV) + 0.60 × $19.39 (strip) = **$22.88**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $29.67 |
| 95% | $30.94 |
| 100% | $31.36 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$28.10** ≥ price **$21.90** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 78,646 | 0.00× |
| 12-month FFA | 59,560 | 0.00× |
| Current spot | 38,534 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LNGC (90% of fleet value) | 0 | 0.00× |
| MGC (10% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $5.93 | $14.40 | $22.88 | $31.35 | $39.82 |
| **-15%** | $5.93 | $14.40 | $22.88 | $31.35 | $39.82 |
| **+0%** | $5.93 | $14.40 | $22.88 | $31.35 | $39.82 |
| **+15%** | $5.93 | $14.40 | $22.88 | $31.35 | $39.82 |
| **+30%** | $5.93 | $14.40 | $22.88 | $31.35 | $39.82 |

_Current price $21.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$22.88** is +4.5% vs the current price ($21.90) and -9.1% vs the analyst target ($25.17). NAV alone covers the price (NAV/sh $28.10 ≥ $21.90); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Additional diagnostics

- [`ccec_buy_diagnostic.md`](ccec_buy_diagnostic.md) — CCEC — buy-actionability diagnostic
