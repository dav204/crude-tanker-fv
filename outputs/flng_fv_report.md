# FLNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $30.67
- **Model fair value:** $28.16
- **Analyst target:** $25.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 2,915.0 |
| + Cash & equivalents | 389.1 |
| + Working capital (net) | 56.0 |
| − Total debt | 1,821.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,539.1** |
| Diluted shares | 54,092,376 |
| **NAV / share** | **$28.45** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 76,873 | 0.871 | 0.750 | 0.731 |
| Q2 | 80,000 | 83,773 | 1.016 | 0.750 | 0.712 |
| Q3 | 75,000 | 82,623 | 0.992 | 0.750 | 0.694 |
| Q4 | 48,000 | 76,413 | 0.861 | 0.750 | 0.676 |
| Q5 | 52,000 | 77,333 | 0.881 | 0.750 | 0.658 |
| Q6 | 80,000 | 83,773 | 1.016 | 0.750 | 0.641 |
| Q7 | 75,000 | 82,623 | 0.992 | 0.750 | 0.625 |
| Q8 | 50,000 | 76,873 | 0.871 | 0.750 | 0.609 |
| Σ discounted DPS | | | | | 5.34 |
| Terminal value (NAV, q9) | | | | 28.61 | 22.63 |
| **DivStrip implied price** | | | | | **$27.97** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.71×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $28.45 (NAV) + 0.60 × $27.97 (strip) = **$28.16**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 21.56 | 77% |
| Balance-sheet net | -10.17 | -36% |
| Discounted DPS (strip, 8-10q) | 3.21 | 11% |
| Discounted terminal (aged NAV) | 13.58 | 48% |
| **Blend FV** | **28.16** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.40 + 0.60 × 0.81 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $28.52 |
| 95% | $28.59 |
| 100% | $28.61 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.14× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **198,475** | — |
| 10-year mean | 85,000 | 2.33× |
| 12-month FFA | 63,250 | 3.14× |
| Current spot | 40,000 | 4.96× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.51 | $23.16 | $27.81 | $32.46 | $37.11 |
| **-15%** | $18.69 | $23.34 | $27.99 | $32.64 | $37.29 |
| **+0%** | $18.87 | $23.52 | $28.16 | $32.81 | $37.46 |
| **+15%** | $19.04 | $23.69 | $28.34 | $32.99 | $37.64 |
| **+30%** | $19.22 | $23.87 | $28.52 | $33.16 | $37.81 |

_Current price $30.67. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$28.16** is -8.2% vs the current price ($30.67) and +12.7% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$198,475/day** (3.14× the current forward) — 2.3× the value-weighted 10-yr mean ($85,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
