# Pipeline Delta Report

- **This run:** 2026-06-29T22:10:56+00:00
- **Previous run:** 2026-06-29T14:48:15+00:00

## Headline changes (material moves)

- **ECO:** NAV/sh -5.1%
- **FRO:** NAV/sh -6.4%
- **CAPT:** single-point FV -19.6%; scenario PW FV -18.8%; broker spread +25.9pp; NAV/sh -23.0%
- **BRUT:** single-point FV -47.6%; scenario PW FV -44.6%; broker spread +92.2pp; NAV/sh -53.8%
- **SB:** broker spread -6.3pp

## Input files changed since last run

- `inputs/market_data/basis_status.yaml` (new)
- `inputs/market_data/newbuild_contract_prices.yaml` (new)
- `inputs/market_data/vessel_value_curves.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $17.65 (no change) | $13.67 (-3.4%) | $14.42 (-3.4%) | $12.51 (-4.5%) | TRIM/SHORT (overvalued) | +19.1pp (+3.1pp) |
| ECO ⚑ | $49.88 (no change) | $35.41 (-3.7%) | $38.18 (-3.6%) | $32.16 (-5.1%) | TRIM/SHORT (overvalued) | +16.8pp (+3.2pp) |
| FRO ⚑ | $35.52 (no change) | $25.28 (-4.7%) | $27.53 (-4.5%) | $22.67 (-6.4%) | TRIM/SHORT (overvalued) | +18.1pp (+4.1pp) |
| INSW | $79.51 (no change) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +33.7pp (no change) |
| TNK | $67.99 (no change) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +15.4pp (no change) |
| NAT | $5.85 (no change) | $2.51 (no change) | $2.78 (no change) | $2.07 (no change) | TRIM/SHORT (overvalued) | +74.6pp (no change) |
| FLNG | $29.48 (no change) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -21.8pp (no change) |
| CCEC | $20.71 (no change) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -23.0pp (no change) |
| STNG | $72.58 (no change) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +28.2pp (no change) |
| HAFN | $6.97 (no change) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +26.6pp (no change) |
| TRMD | $26.81 (no change) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +22.5pp (no change) |
| ASC | $15.12 (no change) | $15.09 (no change) | $15.15 (no change) | $15.93 (no change) | HOLD (fairly valued) | +24.5pp (no change) |
| TEN | $36.72 (no change) | $60.34 (-0.7%) | $64.54 (-0.6%) | $86.95 (-0.9%) | BUY (undervalued) | +36.5pp (+1.3pp) |
| CMDB | $17.47 (no change) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -10.9pp (no change) |
| SBLK | $24.40 (no change) | $26.00 (no change) | $26.07 (no change) | $26.91 (no change) | BUY (undervalued) | +10.1pp (no change) |
| GNK | $23.57 (no change) | $23.99 (+0.1%) | $24.05 (+0.1%) | $24.69 (+0.2%) | HOLD (fairly valued) | +8.9pp (-0.2pp) |
| CAPT ⚑ | $12.79 (no change) | $12.59 (-19.6%) | $13.62 (-18.8%) | $11.58 (-23.0%) | BUY (undervalued) | +55.9pp (+25.9pp) |
| MPCC | $2.61 (no change) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +15.1pp (no change) |
| GSL | $37.79 (no change) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.5pp (no change) |
| BRUT ⚑ | $5.34 (no change) | $5.16 (-47.6%) | $5.99 (-44.6%) | $4.34 (-53.8%) | BUY (undervalued) | +50.7pp (+92.2pp) |
| CMBT | $14.10 (no change) | $14.93 (+1.7%) | $15.69 (+0.3%) | $15.40 (+0.9%) | BUY (undervalued) | +23.3pp (-0.9pp) |
| SB ⚑ | $6.39 (no change) | $9.80 (+3.4%) | $9.67 (+3.4%) | $10.31 (+5.0%) | BUY (undervalued) | -41.0pp (-6.3pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._