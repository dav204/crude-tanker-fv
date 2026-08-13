# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (65.0% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $60.01 (= whole-company $92.38 × crude_share). Product sleeve (~35%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q2
- **Current price (crude-allocated):** $60.01
- **Model fair value:** $37.59
- **Analyst target (crude-allocated):** $51.64

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 689.9 |
| Fleet value — Suezmax | 776.3 |
| Fleet value — Aframax | 175.5 |
| Fleet value — LR1 | 102.2 |
| + Cash & equivalents | 265.9 |
| + Working capital (net) | 183.6 |
| − Total debt | 365.4 |
| − Lease liabilities | 4.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,823.5** |
| Diluted shares | 49,857,565 |
| **NAV / share** | **$36.57** |
| NAV / share (ex yard discount) | $37.44 |
| Yard-discount impact / share | $-0.86 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 118,900 | 118,900 | 5.002 | 3.621 | 3.528 |
| Q2 | 118,900 | 118,900 | 5.002 | 3.621 | 3.437 |
| Q3 | 58,050 | 58,050 | 2.582 | 1.927 | 1.782 |
| Q4 | 58,050 | 58,050 | 2.582 | 1.927 | 1.736 |
| Q5 | 26,950 | 26,950 | 1.005 | 0.823 | 0.723 |
| Q6 | 26,950 | 26,950 | 1.005 | 0.823 | 0.704 |
| Q7 | 26,950 | 26,950 | 1.005 | 0.823 | 0.686 |
| Q8 | 26,950 | 26,950 | 1.005 | 0.823 | 0.668 |
| Σ discounted DPS | | | | | 13.26 |
| Terminal value (NAV, q9) | | | | 33.78 | 26.71 |
| **DivStrip implied price** | | | | | **$39.97** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$88,475/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$58,050/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $58,050 / 10-yr mean $27,747 = **2.23×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $36.57 (NAV) + 0.30 × $39.97 (strip) = **$37.59**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 24.49 | 65% |
| Balance-sheet net | 1.12 | 3% |
| Discounted DPS (strip, 8-10q) | 3.98 | 11% |
| Discounted terminal (aged NAV) | 8.01 | 21% |
| **Blend FV** | **37.59** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.67 = **90%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $37.67 |
| 95% | $37.79 |
| 100% | $37.82 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.48× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **468,801** | — |
| 10-year mean | 33,465 | 14.01× |
| 12-month FFA | 104,693 | 4.48× |
| Current spot | 235,542 | 1.99× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (45% of fleet value) | 396,180 | 14.28× |
| VLCC (40% of fleet value) | 638,880 | 15.97× |
| Aframax (10% of fleet value) | 249,305 | 6.83× |
| LR1 (6% of fleet value) | 249,305 | 9.03× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.46 | $32.56 | $35.66 | $38.76 | $41.86 |
| **-15%** | $30.43 | $33.53 | $36.63 | $39.73 | $42.82 |
| **+0%** | $31.40 | $34.50 | $37.59 | $40.69 | $43.79 |
| **+15%** | $32.36 | $35.46 | $38.56 | $41.66 | $44.76 |
| **+30%** | $33.33 | $36.43 | $39.53 | $42.63 | $45.72 |

_Current price $60.01. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$37.59** is -37.4% vs the current price ($60.01) and -27.2% vs the analyst target ($51.64). The current price implies the fleet earning a value-weighted blended **$468,801/day** (4.48× the current forward) — 14.0× the value-weighted 10-yr mean ($33,465, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 65.0% of vessel value ($1,744M crude vs $941M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -37% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~35% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
