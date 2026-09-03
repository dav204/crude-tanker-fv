# Pipeline Delta Report

- **This run:** 2026-09-03T00:56:13+00:00
- **Previous run:** 2026-09-01T17:55:01+00:00

## Headline changes (material moves)

- **TNK:** position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- **CAPT:** position BUY (undervalued) → HOLD (fairly valued)
- **SB:** position BUY (undervalued) → HOLD (fairly valued)

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: GNK (+0.60%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $20.45 | $19.90 | parity · cheap\|fair | +2.74% | +6.96% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $26.03 | $25.88 | parity · cheap\|fair | **+0.60%** | -0.29% (@ $25.80) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $31.05 | $33.22 | parity · cheap\|fair | -6.53% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/agent_duties.yaml` (modified)
- `inputs/archive_gaps.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/notify.yaml` (modified)
- `inputs/reweight_triggers.yaml` (modified)
- `inputs/rocketchat_sources.yaml` (modified)
- `inputs/overlays.yaml` (removed)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $19.69 (+0.03) | $15.32 (no change) | $15.97 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +10.3pp (+0.1pp) |
| ECO | $67.96 (+1.10) | $39.73 (no change) | $41.71 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +8.9pp (+0.9pp) |
| FRO | $44.32 (+0.13) | $26.58 (no change) | $28.29 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +14.8pp (+0.1pp) |
| INSW | $99.76 (+0.95) | $37.59 (no change) | $59.59 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +25.3pp (+0.5pp) |
| TNK ⚑ | $88.30 (-0.40) | $83.23 (no change) | $83.93 (no change) | $84.60 (no change) | HOLD (fairly valued) ⟵ | +12.3pp (-0.4pp) |
| NAT | $6.91 (+0.14) | $2.89 (no change) | $3.00 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +67.8pp (+0.7pp) |
| FLNG | $31.47 (-0.01) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.8pp (no change) |
| CCEC | $22.61 (-0.11) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.4pp (-0.5pp) |
| STNG | $79.61 (+1.58) | $72.23 (no change) | $76.73 (no change) | $76.22 (no change) | HOLD (fairly valued) | +38.3pp (+1.8pp) |
| HAFN | $8.59 (+0.12) | $4.83 (no change) | $5.59 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +40.4pp (+0.7pp) |
| TRMD | $33.21 (+0.59) | $32.14 (no change) | $35.79 (no change) | $32.30 (no change) | BUY (undervalued) | +10.6pp (+1.6pp) |
| ASC | $17.68 (+0.32) | $17.22 (no change) | $16.38 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +30.0pp (+1.6pp) |
| TEN | $42.82 (+0.30) | $59.21 (no change) | $62.66 (no change) | $88.16 (no change) | BUY (undervalued) | +55.4pp (+0.9pp) |
| CMDB | $20.45 (-0.07) | $21.83 (no change) | $19.51 (no change) | $32.60 (no change) | HOLD (fairly valued) | +1.0pp (-0.3pp) |
| SBLK | $31.05 (+0.57) | $32.67 (no change) | $28.59 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +2.1pp (+1.5pp) |
| GNK | $26.03 (+0.15) | $25.42 (no change) | $21.45 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +6.0pp (+0.4pp) |
| CAPT ⚑ | $16.84 (+0.38) | $16.95 (no change) | $17.56 (no change) | $17.32 (no change) | HOLD (fairly valued) ⟵ | +33.3pp (+2.1pp) |
| MPCC | $2.89 (+0.04) | $2.29 (no change) | $2.15 (no change) | $2.10 (no change) | TRIM/SHORT (overvalued) | +18.3pp (+0.6pp) |
| GSL | $44.48 (-0.04) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | HOLD (fairly valued) | +31.7pp (-0.1pp) |
| BRUT | $4.98 (+0.04) | $4.70 (no change) | $5.12 (no change) | $4.92 (no change) | HOLD (fairly valued) | -1.6pp (+0.6pp) |
| CMBT | $18.27 (-0.08) | $15.94 (no change) | $13.63 (no change) | $16.54 (no change) | TRIM/SHORT (overvalued) | +20.6pp (-0.3pp) |
| SB ⚑ | $8.75 (+0.23) | $10.42 (no change) | $9.09 (no change) | $10.72 (no change) | HOLD (fairly valued) ⟵ | -27.4pp (+2.7pp) |
| LPG | $50.86 (+1.08) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +20.1pp (+1.3pp) |
| BWLP | $24.63 (+0.58) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +12.0pp (+1.3pp) |
| 2343 | $0.53 (no change) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +2.2pp (-0.7pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._