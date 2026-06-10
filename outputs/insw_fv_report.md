# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (65.3% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $50.95 (= whole-company $78.00 × crude_share). Product sleeve (~35%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q1
- **Current price (crude-allocated):** $50.95
- **Model fair value:** $37.34
- **Analyst target (crude-allocated):** $51.93

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 645.0 |
| Fleet value — Suezmax | 790.6 |
| Fleet value — Aframax | 182.6 |
| Fleet value — LR1 | 86.4 |
| + Cash & equivalents | 246.2 |
| + Working capital (net) | 149.7 |
| − Total debt | 365.2 |
| − Lease liabilities | 5.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,730.1** |
| Diluted shares | 49,700,000 |
| **NAV / share** | **$34.81** |
| NAV / share (ex yard discount) | $35.64 |
| Yard-discount impact / share | $-0.83 |

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
| Terminal value (NAV, q9) | | | | 30.45 | 24.08 |
| **DivStrip implied price** | | | | | **$43.26** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.40×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $34.81 (NAV) + 0.30 × $43.26 (strip) = **$37.34**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $38.13 |
| 95% | $39.31 |
| 100% | $39.70 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.10× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **341,877** | — |
| 10-year mean | 32,360 | 10.56× |
| 12-month FFA | 110,263 | 3.10× |
| Current spot | 184,197 | 1.86× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (46% of fleet value) | 263,547 | 9.50× |
| VLCC (38% of fleet value) | 480,586 | 12.01× |
| Aframax (11% of fleet value) | 239,518 | 8.68× |
| LR1 (5% of fleet value) | 239,518 | 8.68× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.18 | $32.29 | $35.40 | $38.51 | $41.62 |
| **-15%** | $30.15 | $33.26 | $36.37 | $39.48 | $42.59 |
| **+0%** | $31.12 | $34.23 | $37.34 | $40.45 | $43.57 |
| **+15%** | $32.09 | $35.20 | $38.32 | $41.43 | $44.54 |
| **+30%** | $33.06 | $36.18 | $39.29 | $42.40 | $45.51 |

_Current price $50.95. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$37.34** is -26.7% vs the current price ($50.95) and -28.1% vs the analyst target ($51.93). The current price implies the fleet earning a value-weighted blended **$341,877/day** (3.10× the current forward) — 10.6× the value-weighted 10-yr mean ($32,360, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $73.3M (+18%) / 10yr $50.5M (+12%) [n=21], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $85.9M (-7%) / 10yr $69.7M (-13%) [n=18], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 65.3% of vessel value ($1,705M crude vs $905M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -27% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~35% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
