# Pipeline Delta Report

- **This run:** 2026-06-29T23:45:25+00:00
- **Previous run:** 2026-06-29T22:10:56+00:00

## Headline changes (material moves)

- **DHT:** broker spread -5.3pp
- **ECO:** NAV/sh +7.5%
- **FRO:** NAV/sh +6.8%
- **ASC:** position HOLD (fairly valued) → TRIM/SHORT (overvalued); broker spread +5.1pp
- **TEN:** broker spread -7.2pp
- **CAPT:** single-point FV +28.1%; scenario PW FV +26.7%; broker spread -30.6pp; NAV/sh +34.6%
- **BRUT:** single-point FV +90.7%; scenario PW FV +80.5%; broker spread -96.5pp; NAV/sh +116.6%

## Input files changed since last run

- `inputs/market_data/xclusiv_age_curve.yaml` (new)
- `inputs/market_data/newbuild_contract_prices.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/market_data/vessel_value_curves.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT ⚑ | $17.08 (-0.57) | $14.15 (+3.5%) | $14.92 (+3.5%) | $13.10 (+4.7%) | TRIM/SHORT (overvalued) | +13.8pp (-5.3pp) |
| ECO ⚑ | $49.60 (-0.28) | $37.33 (+5.4%) | $40.17 (+5.2%) | $34.56 (+7.5%) | TRIM/SHORT (overvalued) | +11.9pp (-4.9pp) |
| FRO ⚑ | $35.44 (-0.08) | $26.54 (+5.0%) | $28.82 (+4.7%) | $24.22 (+6.8%) | TRIM/SHORT (overvalued) | +13.8pp (-4.3pp) |
| INSW | $77.81 (-1.70) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +32.3pp (-1.4pp) |
| TNK | $65.99 (-2.00) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +12.4pp (-3.0pp) |
| NAT | $5.78 (-0.07) | $2.51 (no change) | $2.78 (no change) | $2.07 (no change) | TRIM/SHORT (overvalued) | +74.2pp (-0.4pp) |
| FLNG | $29.29 (-0.19) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -22.4pp (-0.6pp) |
| CCEC | $20.87 (+0.16) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -22.1pp (+0.9pp) |
| STNG | $70.09 (-2.49) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +24.7pp (-3.5pp) |
| HAFN | $6.86 (-0.11) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +25.5pp (-1.1pp) |
| TRMD | $26.31 (-0.50) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +20.9pp (-1.6pp) |
| ASC ⚑ | $16.00 (+0.88) | $15.09 (no change) | $15.15 (no change) | $15.93 (no change) | TRIM/SHORT (overvalued) ⟵ | +29.6pp (+5.1pp) |
| TEN ⚑ | $35.76 (-0.96) | $61.29 (+1.6%) | $65.49 (+1.5%) | $88.70 (+2.0%) | BUY (undervalued) | +29.3pp (-7.2pp) |
| CMDB | $17.99 (+0.52) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -7.8pp (+3.1pp) |
| SBLK | $24.64 (+0.24) | $26.00 (no change) | $26.07 (no change) | $26.91 (no change) | BUY (undervalued) | +11.0pp (+0.9pp) |
| GNK | $24.39 (+0.82) | $23.99 (no change) | $24.05 (no change) | $24.69 (no change) | HOLD (fairly valued) | +11.9pp (+3.0pp) |
| CAPT ⚑ | $12.73 (-0.06) | $16.13 (+28.1%) | $17.26 (+26.7%) | $15.59 (+34.6%) | BUY (undervalued) | +25.3pp (-30.6pp) |
| MPCC | $2.62 (+0.01) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +15.3pp (+0.2pp) |
| GSL | $37.74 (-0.05) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.4pp (-0.1pp) |
| BRUT ⚑ | $5.21 (-0.13) | $9.84 (+90.7%) | $10.81 (+80.5%) | $9.40 (+116.6%) | BUY (undervalued) | -45.8pp (-96.5pp) |
| CMBT | $14.08 (-0.02) | $15.26 (+2.2%) | $16.07 (+2.4%) | $15.87 (+3.1%) | BUY (undervalued) | +20.1pp (-3.2pp) |
| SB | $6.36 (-0.03) | $9.80 (no change) | $9.67 (no change) | $10.31 (no change) | BUY (undervalued) | -41.6pp (-0.6pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._