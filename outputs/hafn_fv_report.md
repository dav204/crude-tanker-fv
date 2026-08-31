# HAFN — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $8.47
- **Model fair value:** $4.83
- **Analyst target:** $10.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 467.7 |
| Fleet value — LR1 | 762.0 |
| Fleet value — MR | 1,782.5 |
| Fleet value — Handysize | 262.5 |
| + Cash & equivalents | 271.0 |
| + Working capital (net) | 189.2 |
| − Total debt | 808.3 |
| − Lease liabilities | 77.1 |
| − Newbuild commitments | 503.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,345.9** |
| Diluted shares | 506,029,778 |
| **NAV / share** | **$4.64** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 29,300 | 29,300 | 0.461 | 0.369 | 0.359 |
| Q2 | 29,300 | 29,300 | 0.461 | 0.369 | 0.350 |
| Q3 | 29,250 | 29,250 | 0.417 | 0.334 | 0.309 |
| Q4 | 29,250 | 29,250 | 0.417 | 0.334 | 0.301 |
| Q5 | 25,000 | 25,000 | 0.300 | 0.240 | 0.210 |
| Q6 | 25,000 | 25,000 | 0.300 | 0.240 | 0.205 |
| Q7 | 25,000 | 25,000 | 0.300 | 0.240 | 0.200 |
| Q8 | 25,000 | 25,000 | 0.300 | 0.240 | 0.195 |
| Σ discounted DPS | | | | | 2.13 |
| Terminal value (NAV, q9) | | | | 3.99 | 3.16 |
| **DivStrip implied price** | | | | | **$5.28** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,275/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$29,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $29,250 / 10-yr mean $16,000 = **1.80×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $4.64 (NAV) + 0.30 × $5.28 (strip) = **$4.83**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 4.53 | 94% |
| Balance-sheet net | -1.28 | -27% |
| Discounted DPS (strip, 8-10q) | 0.64 | 13% |
| Discounted terminal (aged NAV) | 0.95 | 20% |
| **Blend FV** | **4.83** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.60 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $4.83 |
| 95% | $4.85 |
| 100% | $4.85 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.14× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **159,436** | — |
| 10-year mean | 20,356 | 7.83× |
| 12-month FFA | 38,507 | 4.14× |
| Current spot | 30,439 | 5.24× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (54% of fleet value) | 121,210 | 7.58× |
| LR1 (23% of fleet value) | 230,517 | 8.35× |
| LR2 (14% of fleet value) | 230,517 | 8.35× |
| Handysize (8% of fleet value) | 86,017 | 5.38× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $3.33 | $3.91 | $4.48 | $5.06 | $5.64 |
| **-15%** | $3.50 | $4.08 | $4.66 | $5.23 | $5.81 |
| **+0%** | $3.68 | $4.25 | $4.83 | $5.41 | $5.98 |
| **+15%** | $3.85 | $4.43 | $5.00 | $5.58 | $6.16 |
| **+30%** | $4.02 | $4.60 | $5.18 | $5.76 | $6.33 |

_Current price $8.47. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$4.83** is -43.0% vs the current price ($8.47) and -51.7% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$159,436/day** (4.14× the current forward) — 7.8× the value-weighted 10-yr mean ($20,356, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
