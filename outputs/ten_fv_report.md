# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $44.00
- **Model fair value:** $53.31
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 310.3 |
| Fleet value — Suezmax | 838.5 |
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
| **= NAV total** | **2,433.7** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$80.78** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 36,629 | 4.880 | 1.302 | 1.269 |
| Q2 | 88,000 | 38,995 | 5.340 | 1.390 | 1.319 |
| Q3 | 82,000 | 37,903 | 5.145 | 1.352 | 1.251 |
| Q4 | 64,000 | 34,627 | 4.518 | 1.233 | 1.111 |
| Q5 | 59,000 | 33,717 | 4.349 | 1.201 | 1.054 |
| Q6 | 70,000 | 35,719 | 4.747 | 1.277 | 1.092 |
| Q7 | 74,000 | 36,447 | 4.880 | 1.302 | 1.085 |
| Q8 | 56,000 | 33,171 | 4.257 | 1.184 | 0.961 |
| Σ discounted DPS | | | | | 9.14 |
| Terminal value (NAV, q9) | | | | 46.32 | 36.63 |
| **DivStrip implied price** | | | | | **$45.77** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.96×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $80.78 (NAV) + 0.30 × $45.77 (strip) = **$53.31**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $59.54 |
| 95% | $61.08 |
| 100% | $61.59 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$80.78** ≥ price **$44.00** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 35,223 | 0.00× |
| 12-month FFA | 82,110 | 0.00× |
| Current spot | 77,484 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (40% of fleet value) | 0 | 0.00× |
| Suezmax (23% of fleet value) | 0 | 0.00× |
| LNGC (12% of fleet value) | 0 | 0.00× |
| VLCC (8% of fleet value) | 0 | 0.00× |
| LR1 (7% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $37.55 | $45.29 | $53.03 | $60.78 | $68.52 |
| **-15%** | $37.69 | $45.43 | $53.17 | $60.92 | $68.66 |
| **+0%** | $37.83 | $45.57 | $53.31 | $61.05 | $68.80 |
| **+15%** | $37.97 | $45.71 | $53.45 | $61.19 | $68.94 |
| **+30%** | $38.11 | $45.85 | $53.59 | $61.33 | $69.08 |

_Current price $44.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$53.31** is +21.2% vs the current price ($44.00) and +3.5% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $80.78 ≥ $44.00); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $73.3M (+18%) / 10yr $50.5M (+12%) [n=21], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $85.9M (-7%) / 10yr $69.7M (-13%) [n=18], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
