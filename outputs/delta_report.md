# Pipeline Delta Report

- **This run:** 2026-09-14T15:53:09+00:00
- **Previous run:** 2026-09-14T15:38:59+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: CMDB (+0.76%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $24.51 | $24.33 | parity · fair\|rich | **+0.76%** | -3.47% (@ $23.48) | ⚡ inside ±2.0% deadband |
| GNK | flips (cheap/fair) | $26.83 | $25.87 | parity · cheap\|fair | +3.70% | -0.28% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $31.17 | $33.22 | parity · cheap\|fair | -6.16% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/market_data/ffa_forward_curve.yaml` (modified)
- `inputs/market_data/twelve_month_tc.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $22.00 (no change) | $15.26 (no change) | $16.32 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +17.8pp (no change) |
| ECO | $76.15 (no change) | $39.87 (no change) | $42.22 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +14.5pp (no change) |
| FRO | $49.21 (no change) | $26.71 (no change) | $28.79 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +20.3pp (no change) |
| INSW | $103.65 (no change) | $37.95 (no change) | $59.91 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +27.2pp (no change) |
| TNK | $100.83 (no change) | $84.12 (no change) | $83.24 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +22.3pp (no change) |
| NAT | $7.46 (no change) | $2.95 (no change) | $2.97 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +69.2pp (no change) |
| FLNG | $31.70 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.2pp (no change) |
| CCEC | $22.32 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -3.8pp (no change) |
| STNG | $84.52 (no change) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +42.9pp (no change) |
| HAFN | $9.38 (no change) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +43.8pp (no change) |
| TRMD | $35.08 (no change) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | HOLD (fairly valued) | +15.2pp (no change) |
| ASC | $18.67 (no change) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +34.2pp (no change) |
| TEN | $47.90 (no change) | $59.49 (no change) | $61.80 (no change) | $88.16 (no change) | BUY (undervalued) | +37.1pp (no change) |
| CMDB | $24.51 (no change) | $21.93 (no change) | $19.36 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -7.5pp (no change) |
| SBLK | $31.17 (no change) | $32.78 (no change) | $28.26 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +2.4pp (no change) |
| GNK | $26.83 (no change) | $25.19 (no change) | $21.14 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +8.1pp (no change) |
| CAPT | $18.89 (no change) | $17.09 (no change) | $17.77 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +43.9pp (no change) |
| MPCC | $2.93 (no change) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +17.8pp (no change) |
| GSL | $45.82 (no change) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) | +33.5pp (no change) |
| BRUT | $5.00 (no change) | $4.71 (no change) | $5.35 (no change) | $4.92 (no change) | BUY (undervalued) | -1.2pp (no change) |
| CMBT | $19.48 (no change) | $15.94 (no change) | $13.30 (no change) | $16.46 (no change) | TRIM/SHORT (overvalued) | +25.1pp (no change) |
| SB | $8.51 (no change) | $10.43 (no change) | $8.95 (no change) | $10.72 (no change) | BUY (undervalued) | -29.9pp (no change) |
| LPG | $55.18 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +24.6pp (no change) |
| BWLP | $25.16 (no change) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +13.1pp (no change) |
| 2343 | $0.54 (no change) | $0.41 (no change) | $0.37 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +4.2pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._