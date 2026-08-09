# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $17.80
- **Model fair value:** $21.30
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.6 |
| Fleet value — Pana | 147.9 |
| Fleet value — Supra-Ultra | 330.4 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **786.0** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$32.43** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,200 | 19,200 | 1.393 | 0.000 | 0.000 |
| Q2 | 19,158 | 19,158 | 1.352 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.754 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.862 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.827 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.792 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.753 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.716 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 24.27 | 19.19 |
| **DivStrip implied price** | | | | | **$19.19** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,977/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$16,750/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $16,750 / 10-yr mean $13,930 = **1.31×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.70 (NAV) + 0.40 × $19.19 (strip) = **$21.30**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 17.17 | 81% |
| Balance-sheet net | 2.28 | 11% |
| §15 governance haircut | -5.84 | -27% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.68 | 36% |
| **Blend FV** | **21.30** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.13 |
| 95% | $22.29 |
| 100% | $22.34 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$32.43** ≥ price **$17.80** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **930** | — |
| 10-year mean | 16,517 | 0.06× |
| 12-month FFA | 22,383 | 0.04× |
| Current spot | 25,553 | 0.04× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (48% of fleet value) | 705 | 0.05× |
| Cape (31% of fleet value) | 1,383 | 0.06× |
| Pana (21% of fleet value) | 771 | 0.06× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.76 | $18.48 | $20.20 | $21.92 | $23.64 |
| **-15%** | $17.31 | $19.03 | $20.75 | $22.47 | $24.19 |
| **+0%** | $17.85 | $19.57 | $21.30 | $23.02 | $24.74 |
| **+15%** | $18.40 | $20.12 | $21.84 | $23.56 | $25.28 |
| **+30%** | $18.95 | $20.67 | $22.39 | $24.11 | $25.83 |

_Current price $17.80. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.30** is +19.6% vs the current price ($17.80) and -23.9% vs the analyst target ($27.98). NAV alone covers the price (NAV/sh $32.43 ≥ $17.80); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
