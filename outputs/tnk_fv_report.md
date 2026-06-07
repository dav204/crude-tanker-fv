# TNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $70.80
- **Model fair value:** $79.13
- **Analyst target:** $75.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 822.3 |
| Fleet value — Aframax | 882.2 |
| Fleet value — VLCC | 88.5 |
| + Cash & equivalents | 996.2 |
| + Working capital (net) | 97.3 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,886.5** |
| Diluted shares | 34,643,858 |
| **NAV / share** | **$83.32** |
| NAV / share (ex yard discount) | $84.84 |
| Yard-discount impact / share | $-1.52 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 68,400 | 5.086 | 1.521 | 1.482 |
| Q2 | 88,000 | 78,540 | 6.123 | 1.781 | 1.690 |
| Q3 | 82,000 | 73,860 | 5.671 | 1.668 | 1.542 |
| Q4 | 64,000 | 59,820 | 4.247 | 1.312 | 1.182 |
| Q5 | 59,000 | 55,920 | 3.832 | 1.208 | 1.060 |
| Q6 | 70,000 | 64,500 | 4.782 | 1.445 | 1.236 |
| Q7 | 74,000 | 67,620 | 5.051 | 1.513 | 1.260 |
| Q8 | 56,000 | 53,580 | 3.613 | 1.153 | 0.936 |
| Σ discounted DPS | | | | | 10.39 |
| Terminal value (NAV, q9) | | | | 74.57 | 58.96 |
| **DivStrip implied price** | | | | | **$69.35** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **2.15×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $83.32 (NAV) + 0.30 × $69.35 (strip) = **$79.13**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $84.81 |
| 95% | $86.36 |
| 100% | $86.88 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$83.32** ≥ price **$70.80** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 28,280 | 0.00× |
| 12-month FFA | 84,644 | 0.00× |
| Current spot | 75,527 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (49% of fleet value) | 0 | 0.00× |
| Suezmax (46% of fleet value) | 0 | 0.00× |
| VLCC (5% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $69.03 | $73.68 | $78.32 | $82.96 | $87.61 |
| **-15%** | $69.44 | $74.08 | $78.72 | $83.37 | $88.01 |
| **+0%** | $69.84 | $74.49 | $79.13 | $83.77 | $88.41 |
| **+15%** | $70.25 | $74.89 | $79.53 | $84.18 | $88.82 |
| **+30%** | $70.65 | $75.29 | $79.94 | $84.58 | $89.22 |

_Current price $70.80. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$79.13** is +11.8% vs the current price ($70.80) and +5.5% vs the analyst target ($75.00). NAV alone covers the price (NAV/sh $83.32 ≥ $70.80); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
