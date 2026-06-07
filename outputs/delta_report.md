# Pipeline Delta Report

- **This run:** 2026-06-07T15:11:36+00:00
- **Previous run:** 2026-06-04T19:26:22+00:00

## Headline changes (material moves)

- **TEN: new to watchlist** (price $44.00, position BUY (undervalued))
- **CCEC:** broker spread -6.3pp
- **STNG:** position TRIM/SHORT (overvalued) → HOLD (fairly valued); broker spread +19.8pp
- **TRMD:** broker spread +20.4pp
- **ASC:** broker spread -12.4pp

## Input files changed since last run

- `inputs/balance_sheets/ten_2026-Q1.yaml` (new)
- `inputs/cost_structures/ten.yaml` (new)
- `inputs/dividend_policies/ten.yaml` (new)
- `inputs/fleet_manifests/ten.yaml` (new)
- `inputs/market_data/transactions/lr2.yaml` (new)
- `inputs/market_data/transactions/mr.yaml` (new)
- `inputs/market_data/transactions/vlcc.yaml` (new)
- `inputs/balance_sheets/asc_2026-Q1.yaml` (modified)
- `inputs/balance_sheets/hafn_2026-Q1.yaml` (modified)
- `inputs/balance_sheets/stng_2026-Q1.yaml` (modified)
- `inputs/cost_structures/stng.yaml` (modified)
- `inputs/data_sources.yaml` (modified)
- `inputs/fleet_manifests/asc.yaml` (modified)
- `inputs/fleet_manifests/hafn.yaml` (modified)
- `inputs/fleet_manifests/stng.yaml` (modified)
- `inputs/market_data/ffa_forward_curve.yaml` (modified)
- `inputs/market_data/historical_tce_means.yaml` (modified)
- `inputs/market_data/spot_tce.yaml` (modified)
- `inputs/market_data/transactions/aframax.yaml` (modified)
- `inputs/market_data/transactions/suezmax.yaml` (modified)
- `inputs/market_data/twelve_month_tc.yaml` (modified)
- `inputs/market_data/vessel_value_curves.yaml` (modified)
- `inputs/watchlist.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $16.40 (no change) | $16.49 (no change) | $13.34 (no change) | $15.29 (no change) | TRIM/SHORT (overvalued) | -1.1pp (no change) |
| ECO | $47.70 (-0.40) | $42.56 (no change) | $32.53 (no change) | $39.93 (no change) | TRIM/SHORT (overvalued) | -0.8pp (no change) |
| FRO | $34.50 (no change) | $31.37 (no change) | $23.87 (no change) | $28.79 (no change) | TRIM/SHORT (overvalued) | -0.1pp (+0.5pp) |
| INSW | $78.00 (+1.20) | $42.18 (no change) | $52.08 (no change) | $57.91 (no change) | TRIM/SHORT (overvalued) | +22.2pp (+0.1pp) |
| TNK | $70.80 (+0.30) | $79.13 (no change) | $69.31 (no change) | $83.32 (no change) | HOLD (fairly valued) | +10.1pp (+0.4pp) |
| NAT | $5.20 (-0.20) | $3.09 (no change) | $2.28 (no change) | $2.63 (no change) | TRIM/SHORT (overvalued) | +51.1pp (-1.4pp) |
| FLNG | $29.70 (-0.53) | $26.27 (no change) | $28.04 (no change) | $28.45 (no change) | TRIM/SHORT (overvalued) | -20.2pp (+0.8pp) |
| CCEC ⚑ | $21.90 (-1.28) | $22.88 (no change) | $26.45 (no change) | $28.10 (no change) | BUY (undervalued) | -15.4pp (-6.3pp) |
| STNG ⚑ | $75.60 (-3.40) | $77.29 (-0.1%) | $73.40 (-0.2%) | $83.87 (+0.1%) | HOLD (fairly valued) ⟵ | +27.4pp (+19.8pp) |
| HAFN | $7.70 (-0.35) | $5.70 (+2.9%) | $5.41 (+2.7%) | $5.34 (+0.8%) | TRIM/SHORT (overvalued) | +30.7pp (+1.5pp) |
| TRMD ⚑ | $28.20 (+0.95) | $27.27 (no change) | $25.59 (no change) | $26.74 (no change) | TRIM/SHORT (overvalued) | +22.0pp (+20.4pp) |
| ASC ⚑ | $16.00 (-2.50) | $14.90 (+2.1%) | $14.50 (+1.8%) | $15.96 (+1.1%) | TRIM/SHORT (overvalued) | +29.0pp (-12.4pp) |
| **TEN** (new) | $44.00 | $58.42 | $49.37 | $88.56 | BUY (undervalued) | +26.4pp |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._