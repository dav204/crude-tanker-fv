# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (65.4% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $55.28 (= whole-company $84.49 × crude_share). Product sleeve (~35%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q1
- **Current price (crude-allocated):** $55.28
- **Model fair value:** $38.63
- **Analyst target (crude-allocated):** $52.01

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 654.8 |
| Fleet value — Suezmax | 789.3 |
| Fleet value — Aframax | 182.2 |
| Fleet value — LR1 | 86.4 |
| + Cash & equivalents | 246.6 |
| + Working capital (net) | 150.0 |
| − Total debt | 365.8 |
| − Lease liabilities | 5.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,738.2** |
| Diluted shares | 49,700,000 |
| **NAV / share** | **$34.97** |
| NAV / share (ex yard discount) | $35.81 |
| Yard-discount impact / share | $-0.84 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.885 | 2.840 | 2.767 |
| Q2 | 99,000 | 99,000 | 4.881 | 3.537 | 3.357 |
| Q3 | 92,000 | 92,000 | 4.429 | 3.220 | 2.978 |
| Q4 | 67,500 | 67,500 | 3.142 | 2.320 | 2.090 |
| Q5 | 60,000 | 60,000 | 2.765 | 2.055 | 1.804 |
| Q6 | 78,000 | 78,000 | 3.600 | 2.640 | 2.258 |
| Q7 | 81,500 | 81,500 | 3.875 | 2.832 | 2.359 |
| Q8 | 56,500 | 56,500 | 2.576 | 1.923 | 1.561 |
| Σ discounted DPS | | | | | 19.17 |
| Terminal value (NAV, q9) | | | | 35.39 | 27.98 |
| **DivStrip implied price** | | | | | **$47.16** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.35×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $34.97 (NAV) + 0.30 × $47.16 (strip) = **$38.63**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $38.72 |
| 95% | $38.86 |
| 100% | $38.91 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **316,781** | — |
| 10-year mean | 33,353 | 9.50× |
| 12-month FFA | 110,547 | 2.87× |
| Current spot | 185,488 | 1.71× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (46% of fleet value) | 243,574 | 8.78× |
| VLCC (38% of fleet value) | 444,164 | 11.10× |
| Aframax (11% of fleet value) | 221,366 | 6.07× |
| LR1 (5% of fleet value) | 221,366 | 8.02× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.84 | $32.90 | $35.95 | $39.01 | $42.06 |
| **-15%** | $31.18 | $34.23 | $37.29 | $40.34 | $43.40 |
| **+0%** | $32.52 | $35.57 | $38.63 | $41.68 | $44.74 |
| **+15%** | $33.86 | $36.91 | $39.97 | $43.02 | $46.08 |
| **+30%** | $35.20 | $38.25 | $41.31 | $44.36 | $47.42 |

_Current price $55.28. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$38.63** is -30.1% vs the current price ($55.28) and -25.7% vs the analyst target ($52.01). The current price implies the fleet earning a value-weighted blended **$316,781/day** (2.87× the current forward) — 9.5× the value-weighted 10-yr mean ($33,353, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 65.4% of vessel value ($1,713M crude vs $905M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -30% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~35% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
