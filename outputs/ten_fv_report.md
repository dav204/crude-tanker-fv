# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $37.99
- **Model fair value:** $58.09
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 310.3 |
| Fleet value — Suezmax | 1,060.1 |
| Fleet value — Aframax | 1,467.2 |
| Fleet value — LR2 | 231.1 |
| Fleet value — LR1 | 250.6 |
| Fleet value — MR | 98.8 |
| Fleet value — Handysize | 26.9 |
| Fleet value — LNGC | 443.2 |
| + Cash & equivalents | 321.4 |
| + Working capital (net) | 28.0 |
| − Total debt | 2,148.2 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 400.0 |
| **= NAV total** | **2,655.2** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$88.13** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 36,629 | 5.042 | 1.333 | 1.299 |
| Q2 | 88,000 | 38,995 | 5.502 | 1.420 | 1.348 |
| Q3 | 82,000 | 37,903 | 5.306 | 1.383 | 1.279 |
| Q4 | 64,000 | 34,627 | 4.679 | 1.264 | 1.139 |
| Q5 | 59,000 | 33,717 | 4.510 | 1.232 | 1.081 |
| Q6 | 70,000 | 35,719 | 4.908 | 1.308 | 1.118 |
| Q7 | 74,000 | 36,447 | 5.042 | 1.333 | 1.110 |
| Q8 | 56,000 | 33,171 | 4.418 | 1.214 | 0.986 |
| Σ discounted DPS | | | | | 9.36 |
| Terminal value (NAV, q9) | | | | 50.98 | 40.31 |
| **DivStrip implied price** | | | | | **$49.67** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.97×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $88.13 (NAV) + 0.30 × $49.67 (strip) = **$58.09**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $64.53 |
| 95% | $66.11 |
| 100% | $66.64 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$88.13** ≥ price **$37.99** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 34,797 | 0.00× |
| 12-month FFA | 82,275 | 0.00× |
| Current spot | 76,983 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (38% of fleet value) | 0 | 0.00× |
| Suezmax (27% of fleet value) | 0 | 0.00× |
| LNGC (11% of fleet value) | 0 | 0.00× |
| VLCC (8% of fleet value) | 0 | 0.00× |
| LR1 (6% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $41.38 | $49.59 | $57.81 | $66.02 | $74.23 |
| **-15%** | $41.52 | $49.73 | $57.95 | $66.16 | $74.37 |
| **+0%** | $41.66 | $49.87 | $58.09 | $66.30 | $74.51 |
| **+15%** | $41.80 | $50.01 | $58.23 | $66.44 | $74.65 |
| **+30%** | $41.94 | $50.15 | $58.37 | $66.58 | $74.79 |

_Current price $37.99. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$58.09** is +52.9% vs the current price ($37.99) and +12.8% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $88.13 ≥ $37.99); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
