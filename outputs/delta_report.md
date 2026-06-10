# Pipeline Delta Report

- **This run:** 2026-06-10T02:49:54+00:00
- **Previous run:** 2026-06-10T02:09:54+00:00

## Headline changes (material moves)

- **DHT:** position BUY (undervalued) → TRIM/SHORT (overvalued); single-point FV -13.2%; scenario PW FV -12.9%; broker spread +13.4pp; NAV/sh -15.4%
- **ECO:** position HOLD (fairly valued) → TRIM/SHORT (overvalued); single-point FV -13.9%; scenario PW FV -13.4%; broker spread +12.3pp; NAV/sh -15.6%
- **FRO:** position HOLD (fairly valued) → TRIM/SHORT (overvalued); single-point FV -13.6%; scenario PW FV -13.1%; broker spread +12.0pp; NAV/sh -15.3%
- **INSW:** single-point FV -11.5%; broker spread +6.8pp; NAV/sh -9.5%
- **TNK:** position BUY (undervalued) → HOLD (fairly valued); broker spread +7.4pp; NAV/sh -7.0%
- **NAT:** single-point FV -15.9%; scenario PW FV -14.8%; broker spread +10.0pp; NAV/sh -20.9%
- **TRMD:** position HOLD (fairly valued) → TRIM/SHORT (overvalued)
- **TEN:** broker spread +11.4pp; NAV/sh -8.8%

## Input files changed since last run

- `inputs/market_data/transactions/vlcc.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT ⚑ | $16.40 (no change) | $14.31 (-13.2%) | $15.08 (-12.9%) | $12.93 (-15.4%) | TRIM/SHORT (overvalued) ⟵ | +12.0pp (+13.4pp) |
| ECO ⚑ | $47.70 (no change) | $36.66 (-13.9%) | $39.32 (-13.4%) | $33.70 (-15.6%) | TRIM/SHORT (overvalued) ⟵ | +11.3pp (+12.3pp) |
| FRO ⚑ | $34.50 (no change) | $27.09 (-13.6%) | $29.36 (-13.1%) | $24.39 (-15.3%) | TRIM/SHORT (overvalued) ⟵ | +11.9pp (+12.0pp) |
| INSW ⚑ | $78.00 (no change) | $37.34 (-11.5%) | $59.50 (-7.9%) | $52.43 (-9.5%) | TRIM/SHORT (overvalued) | +33.4pp (+6.8pp) |
| TNK ⚑ | $70.80 (no change) | $73.96 (-6.5%) | $73.74 (-6.5%) | $77.49 (-7.0%) | HOLD (fairly valued) ⟵ | +19.8pp (+7.4pp) |
| NAT ⚑ | $5.20 (no change) | $2.60 (-15.9%) | $2.87 (-14.8%) | $2.08 (-20.9%) | TRIM/SHORT (overvalued) | +72.0pp (+10.0pp) |
| FLNG | $29.70 (no change) | $26.27 (no change) | $29.73 (no change) | $28.45 (no change) | HOLD (fairly valued) | -21.1pp (no change) |
| CCEC | $21.90 (no change) | $22.88 (no change) | $29.63 (no change) | $28.10 (no change) | BUY (undervalued) | -16.1pp (no change) |
| STNG | $75.60 (no change) | $74.00 (-4.3%) | $73.13 (-4.2%) | $80.35 (-4.2%) | HOLD (fairly valued) | +32.7pp (+4.1pp) |
| HAFN | $7.70 (no change) | $5.59 (-1.9%) | $5.77 (-1.7%) | $5.22 (-2.2%) | TRIM/SHORT (overvalued) | +33.4pp (+1.4pp) |
| TRMD ⚑ | $28.20 (no change) | $26.09 (-4.3%) | $26.68 (-4.1%) | $25.43 (-4.9%) | TRIM/SHORT (overvalued) ⟵ | +27.1pp (+4.2pp) |
| ASC | $16.00 (no change) | $14.88 (-0.1%) | $15.05 (-0.1%) | $15.93 (-0.2%) | TRIM/SHORT (overvalued) | +30.1pp (+0.1pp) |
| TEN ⚑ | $44.00 (no change) | $53.31 (-8.7%) | $57.61 (-8.2%) | $80.78 (-8.8%) | BUY (undervalued) | +43.0pp (+11.4pp) |
| SBLK | $27.20 (no change) | $25.66 (+0.5%) | $25.64 (+0.6%) | $26.19 (+0.8%) | TRIM/SHORT (overvalued) | +22.5pp (-0.7pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._