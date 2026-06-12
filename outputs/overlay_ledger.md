# Overlay ledger

Single registry of active qualitative overlays (METHODOLOGY §16).
Auto-generated — edit `inputs/overlays.yaml` (curated rows) or the
balance-sheet `governance_discount_pct` (§15 rows), then re-render.

| Name | Overlay | Dir | Magnitude | Applied | Retire trigger |
|---|---|:---:|---|---|---|
| CMDB | §15 | ↓ | 30% haircut (blend layer + strip terminal; NAV untouched) | per decision log | reopen triggers in decisions/cmdb_log.md |
| DHT | §14.4 | ↑ | residual only under Jun-9 weights (see §14.4 double-count warning) | 2026-06-03 | MEG export volumes confirmed ramping in step with transit, or Hormuz physical resolution re-bases weights |
| ECO | §14.4 | ↑ | residual only under Jun-9 weights (see §14.4 double-count warning) | 2026-06-03 | same as DHT §14.4 row |
| FRO | §14.4 | ↑ | residual only under Jun-9 weights (see §14.4 double-count warning) | 2026-06-03 | same as DHT §14.4 row |
| MPCC | §11.8.5(b) | ↓ | unquantified — marks-vintage premium on aged feeder tonnage | 2026-06-11 | fresh MB assessment set lands (direct subscription) and old-age leg re-fit |
| NAT | §12 | ↑ | qualitative — treat tool FV as the NAV floor, not the call | 2026-06-05 | payout window closes (cycle normalization) or payout ratio drops below ~90% |
| SBLK | §12 | ↑ | qualitative | 2026-06-09 | dry-bulk cycle position back inside ~1.2x of anchor |
| STNG | §14.6.1 | ↑ | qualitative — uncaptured clean/dirty switching option on 32 coated LR2s | 2026-06-05 | clean-dirty LR2 spread normalizes, or the option is modeled (backlog) |
| TEN | §15 | ↓ | 30% haircut (blend layer + strip terminal; NAV untouched) | per decision log | reopen triggers in decisions/ten_log.md |
| crude | §14.6.2 | ↓ | qualitative, date-specific binary | 2026-06-03 | waiver expiry date passes or is renewed |

## Notes

- **CMDB §15** — Auto-populated from balance_sheets/cmdb_2026-Q1.yaml governance_discount_pct.
- **DHT §14.4** — High-MEG VLCC exposure; full +10-15%/+5-10% adjustment applies ONLY under v1-style normalization-leaning weights.
- **ECO §14.4** — All-spot, MEG-routed; near-term TRIM signals may resolve opposite over 1-2 quarters.
- **FRO §14.4** — High-spot VLCC/Suezmax MEG exposure.
- **MPCC §11.8.5(b)** — Boom-flat old-age curve at a 10-week-stale vintage, concentrated in old feeders; no external NAV anchor to catch it. First container ledger row, per §11.8.5.
- **NAT §12** — High-payout pure-play at peak; the dividend stream IS the thesis the strip undercounts.
- **SBLK §12** — Peak dry bulk per §12.2; tool TRIM at band-edge — read §12 before acting on the short side.
- **STNG §14.6.1** — Framework routes STNG LR2s through lr2_clean only; the embedded switch option is invisible to the strip.
- **TEN §15** — Auto-populated from balance_sheets/ten_2026-Q1.yaml governance_discount_pct.
- **crude §14.6.2** — Sanction-waiver expiry; sector-wide event risk on Iran-adjacent crude flows.
