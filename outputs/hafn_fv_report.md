# HAFN — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $10.12
- **Model fair value:** $4.92
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
| Q1 | 29,600 | 29,600 | 0.571 | 0.457 | 0.445 |
| Q2 | 29,600 | 29,600 | 0.571 | 0.457 | 0.434 |
| Q3 | 30,000 | 30,000 | 0.448 | 0.359 | 0.332 |
| Q4 | 30,000 | 30,000 | 0.448 | 0.359 | 0.323 |
| Q5 | 25,250 | 25,250 | 0.312 | 0.250 | 0.219 |
| Q6 | 25,250 | 25,250 | 0.312 | 0.250 | 0.214 |
| Q7 | 25,250 | 25,250 | 0.312 | 0.250 | 0.208 |
| Q8 | 25,250 | 25,250 | 0.312 | 0.250 | 0.203 |
| Σ discounted DPS | | | | | 2.38 |
| Terminal value (NAV, q9) | | | | 4.06 | 3.21 |
| **DivStrip implied price** | | | | | **$5.59** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,800/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$30,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $30,000 / 10-yr mean $16,000 = **1.89×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $4.64 (NAV) + 0.30 × $5.59 (strip) = **$4.92**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 4.53 | 92% |
| Balance-sheet net | -1.28 | -26% |
| Discounted DPS (strip, 8-10q) | 0.71 | 14% |
| Discounted terminal (aged NAV) | 0.96 | 20% |
| **Blend FV** | **4.92** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.57 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $4.92 |
| 95% | $4.94 |
| 100% | $4.94 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.16× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **225,137** | — |
| 10-year mean | 20,356 | 11.06× |
| 12-month FFA | 43,623 | 5.16× |
| Current spot | 44,763 | 5.03× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (54% of fleet value) | 153,796 | 9.61× |
| LR1 (23% of fleet value) | 353,525 | 12.81× |
| LR2 (14% of fleet value) | 353,525 | 12.81× |
| Handysize (8% of fleet value) | 108,122 | 6.76× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $3.39 | $3.97 | $4.55 | $5.12 | $5.70 |
| **-15%** | $3.58 | $4.16 | $4.73 | $5.31 | $5.89 |
| **+0%** | $3.77 | $4.34 | $4.92 | $5.50 | $6.08 |
| **+15%** | $3.95 | $4.53 | $5.11 | $5.69 | $6.26 |
| **+30%** | $4.14 | $4.72 | $5.30 | $5.87 | $6.45 |

_Current price $10.12. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$4.92** is -51.4% vs the current price ($10.12) and -50.8% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$225,137/day** (5.16× the current forward) — 11.1× the value-weighted 10-yr mean ($20,356, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
