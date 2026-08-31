# Pipeline Delta Report

- **This run:** 2026-08-31T18:47:26+00:00
- **Previous run:** 2026-08-31T18:22:13+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: GNK (-0.07%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $20.52 | $19.94 | parity · cheap\|fair | +2.91% | +6.72% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $25.88 | $25.90 | parity · cheap\|fair | **-0.07%** | -0.38% (@ $25.80) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $30.48 | $33.25 | parity · cheap\|fair | -8.34% | -8.58% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/balance_sheets/mpcc_2026-Q2.yaml` (new)
- `inputs/earnings_calendar.yaml` (modified)
- `inputs/fleet_manifests/mpcc.yaml` (modified)
- `inputs/market_data/spot_tce.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $19.66 (no change) | $15.32 (no change) | $15.97 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +10.2pp (no change) |
| ECO | $66.86 (no change) | $39.73 (no change) | $41.71 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +8.0pp (no change) |
| FRO | $44.19 (no change) | $25.94 (no change) | $27.79 (no change) | $25.34 (no change) | TRIM/SHORT (overvalued) | +16.1pp (no change) |
| INSW | $98.81 (no change) | $37.59 (no change) | $59.59 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +24.8pp (no change) |
| TNK | $88.70 (no change) | $83.23 (no change) | $83.93 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +12.7pp (no change) |
| NAT | $6.77 (no change) | $2.97 (no change) | $3.07 (no change) | $2.85 (no change) | TRIM/SHORT (overvalued) | +66.1pp (no change) |
| FLNG | $31.48 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.8pp (no change) |
| CCEC | $22.72 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -1.9pp (no change) |
| STNG | $78.03 (no change) | $72.23 (no change) | $76.73 (no change) | $76.22 (no change) | HOLD (fairly valued) | +36.5pp (no change) |
| HAFN | $8.47 (no change) | $5.71 (no change) | $6.56 (no change) | $5.56 (no change) | TRIM/SHORT (overvalued) | +29.0pp (no change) |
| TRMD | $32.62 (no change) | $32.14 (no change) | $35.79 (no change) | $32.30 (no change) | BUY (undervalued) | +9.0pp (no change) |
| ASC | $17.36 (no change) | $17.22 (no change) | $16.38 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +28.4pp (no change) |
| TEN | $42.52 (no change) | $59.21 (no change) | $62.66 (no change) | $88.16 (no change) | BUY (undervalued) | +54.5pp (no change) |
| CMDB | $20.52 (no change) | $21.48 (no change) | $19.53 (no change) | $32.20 (no change) | HOLD (fairly valued) | +2.4pp (no change) |
| SBLK | $30.48 (no change) | $32.46 (no change) | $28.74 (no change) | $32.88 (no change) | TRIM/SHORT (overvalued) | +1.6pp (no change) |
| GNK | $25.88 (no change) | $25.02 (no change) | $21.66 (no change) | $25.12 (no change) | TRIM/SHORT (overvalued) | +6.4pp (no change) |
| CAPT | $16.46 (no change) | $15.10 (no change) | $16.02 (no change) | $15.48 (no change) | HOLD (fairly valued) | +41.5pp (no change) |
| MPCC | $2.85 (no change) | $2.29 (+3.2%) | $2.15 (+3.9%) | $2.10 (+2.4%) | TRIM/SHORT (overvalued) | +17.7pp (-1.5pp) |
| GSL | $44.52 (no change) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | HOLD (fairly valued) | +31.8pp (no change) |
| BRUT | $4.94 (no change) | $4.70 (no change) | $5.12 (no change) | $4.92 (no change) | HOLD (fairly valued) | -2.2pp (no change) |
| CMBT | $18.35 (no change) | $15.83 (no change) | $13.87 (no change) | $16.50 (no change) | TRIM/SHORT (overvalued) | +21.3pp (no change) |
| SB | $8.52 (no change) | $10.34 (no change) | $9.23 (no change) | $10.65 (no change) | BUY (undervalued) | -29.9pp (no change) |
| LPG | $49.78 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +18.8pp (no change) |
| BWLP | $24.05 (no change) | $15.43 (no change) | $14.46 (no change) | $15.80 (no change) | TRIM/SHORT (overvalued) | +10.8pp (no change) |
| 2343 | $0.53 (no change) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +3.5pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._