# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (65.3% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $60.28 (= whole-company $92.28 × crude_share). Product sleeve (~35%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q1
- **Current price (crude-allocated):** $60.28
- **Model fair value:** $38.50
- **Analyst target (crude-allocated):** $51.93

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 636.9 |
| Fleet value — Suezmax | 800.7 |
| Fleet value — Aframax | 182.2 |
| Fleet value — LR1 | 86.4 |
| + Cash & equivalents | 246.1 |
| + Working capital (net) | 149.7 |
| − Total debt | 365.2 |
| − Lease liabilities | 5.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,731.6** |
| Diluted shares | 49,700,000 |
| **NAV / share** | **$34.84** |
| NAV / share (ex yard discount) | $35.67 |
| Yard-discount impact / share | $-0.82 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.886 | 2.840 | 2.767 |
| Q2 | 99,000 | 99,000 | 4.881 | 3.537 | 3.357 |
| Q3 | 92,000 | 92,000 | 4.429 | 3.221 | 2.978 |
| Q4 | 67,500 | 67,500 | 3.143 | 2.320 | 2.090 |
| Q5 | 60,000 | 60,000 | 2.765 | 2.056 | 1.804 |
| Q6 | 78,000 | 78,000 | 3.601 | 2.641 | 2.258 |
| Q7 | 81,500 | 81,500 | 3.875 | 2.832 | 2.360 |
| Q8 | 56,500 | 56,500 | 2.577 | 1.924 | 1.561 |
| Σ discounted DPS | | | | | 19.18 |
| Terminal value (NAV, q9) | | | | 35.25 | 27.87 |
| **DivStrip implied price** | | | | | **$47.05** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.34×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $34.84 (NAV) + 0.30 × $47.05 (strip) = **$38.50**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 24.03 | 62% |
| Balance-sheet net | 0.36 | 1% |
| Discounted DPS (strip, 8-10q) | 5.75 | 15% |
| Discounted terminal (aged NAV) | 8.36 | 22% |
| **Blend FV** | **38.50** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.59 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $38.60 |
| 95% | $38.74 |
| 100% | $38.78 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.44× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **378,011** | — |
| 10-year mean | 33,246 | 11.37× |
| 12-month FFA | 109,911 | 3.44× |
| Current spot | 169,673 | 2.23× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (47% of fleet value) | 292,335 | 10.54× |
| VLCC (37% of fleet value) | 533,082 | 13.33× |
| Aframax (11% of fleet value) | 265,681 | 7.28× |
| LR1 (5% of fleet value) | 265,681 | 9.63× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.74 | $32.78 | $35.83 | $38.87 | $41.91 |
| **-15%** | $31.08 | $34.12 | $37.17 | $40.21 | $43.25 |
| **+0%** | $32.42 | $35.46 | $38.50 | $41.55 | $44.59 |
| **+15%** | $33.76 | $36.80 | $39.84 | $42.89 | $45.93 |
| **+30%** | $35.10 | $38.14 | $41.18 | $44.22 | $47.27 |

_Current price $60.28. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$38.50** is -36.1% vs the current price ($60.28) and -25.9% vs the analyst target ($51.93). The current price implies the fleet earning a value-weighted blended **$378,011/day** (3.44× the current forward) — 11.4× the value-weighted 10-yr mean ($33,246, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 65.3% of vessel value ($1,706M crude vs $906M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -36% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~35% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
