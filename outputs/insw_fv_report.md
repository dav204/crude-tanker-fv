# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (68.4% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $53.32 (= whole-company $78.00 × crude_share). Product sleeve (~32%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q1
- **Current price (crude-allocated):** $53.32
- **Model fair value:** $42.18
- **Analyst target (crude-allocated):** $54.35

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 783.8 |
| Fleet value — Suezmax | 899.9 |
| Fleet value — Aframax | 200.2 |
| Fleet value — LR1 | 86.4 |
| + Cash & equivalents | 257.6 |
| + Working capital (net) | 156.7 |
| − Total debt | 382.2 |
| − Lease liabilities | 5.5 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,996.9** |
| Diluted shares | 49,700,000 |
| **NAV / share** | **$40.18** |
| NAV / share (ex yard discount) | $41.17 |
| Yard-discount impact / share | $-0.99 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.875 | 2.832 | 2.759 |
| Q2 | 99,000 | 99,000 | 4.870 | 3.529 | 3.350 |
| Q3 | 92,000 | 92,000 | 4.418 | 3.213 | 2.971 |
| Q4 | 67,500 | 67,500 | 3.132 | 2.312 | 2.083 |
| Q5 | 60,000 | 60,000 | 2.754 | 2.048 | 1.797 |
| Q6 | 78,000 | 78,000 | 3.590 | 2.633 | 2.251 |
| Q7 | 81,500 | 81,500 | 3.864 | 2.825 | 2.353 |
| Q8 | 56,500 | 56,500 | 2.566 | 1.916 | 1.555 |
| Σ discounted DPS | | | | | 19.12 |
| Terminal value (NAV, q9) | | | | 35.06 | 27.72 |
| **DivStrip implied price** | | | | | **$46.84** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.41×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $40.18 (NAV) + 0.30 × $46.84 (strip) = **$42.18**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $42.96 |
| 95% | $44.13 |
| 100% | $44.53 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.72× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **303,978** | — |
| 10-year mean | 32,600 | 9.32× |
| 12-month FFA | 111,719 | 2.72× |
| Current spot | 190,978 | 1.59× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (46% of fleet value) | 231,277 | 8.34× |
| VLCC (40% of fleet value) | 421,741 | 10.54× |
| Aframax (10% of fleet value) | 210,190 | 7.62× |
| LR1 (4% of fleet value) | 210,190 | 7.62× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $33.05 | $36.64 | $40.23 | $43.83 | $47.42 |
| **-15%** | $34.02 | $37.61 | $41.21 | $44.80 | $48.39 |
| **+0%** | $34.99 | $38.58 | $42.18 | $45.77 | $49.37 |
| **+15%** | $35.96 | $39.56 | $43.15 | $46.74 | $50.34 |
| **+30%** | $36.93 | $40.53 | $44.12 | $47.71 | $51.31 |

_Current price $53.32. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$42.18** is -20.9% vs the current price ($53.32) and -22.4% vs the analyst target ($54.35). The current price implies the fleet earning a value-weighted blended **$303,978/day** (2.72× the current forward) — 9.3× the value-weighted 10-yr mean ($32,600, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 68.4% of vessel value ($1,970M crude vs $912M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -21% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~32% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
