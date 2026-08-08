# LPG Weight-Robustness Diagnostic (§9.10 — WO3 Phase 1)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked LPG Set A weights. Surfaces which LPG calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Shipped WITH the sector (family-from-birth, WO3 Phase 1).

**Axis:** US-export-arb vs orderbook overhang — the four scenarios' own parameter (arb_wide ↔ overhang / arb_collapse). Set A is the ratified evidence-first overhang-tilted lock (China PDH soft, ~30% orderbook contracted); LPG Set B brackets the arb-bull / PDH-recovery case; LPG Set C the deep-overhang case; both are ±~10pp shifts.

**Naming namespace:** labels are LPG families ("LPG Set …"); crude, LNG, and dry bulk each use "Set A/B" for their own — a bare unprefixed label would be a methodology error.

## Weight sets compared

| Scenario | Set A | Set B | Set C |
|---|--:|--:|--:|
| arb_wide | 0.15 | 0.25 | 0.10 |
| absorption_base | 0.35 | 0.35 | 0.28 |
| overhang | 0.35 | 0.28 | 0.45 |
| arb_collapse | 0.15 | 0.12 | 0.17 |

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| LPG | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| BWLP | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Robustness | Notes |
|---|--:|--:|--:|---|---|
| LPG | -33.2% (TRIM/SHORT) | -30.6% (TRIM/SHORT) | -35.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| BWLP | -33.0% (TRIM/SHORT) | -30.4% (TRIM/SHORT) | -35.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### LPG — price $45.76, target $54.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| LPG Set A (locked 2026-07-07, evidence-first overhang-tilted) | $30.55 | -33.2% | TRIM/SHORT |
| LPG Set B (arb-bull / PDH-recovery bracket) | $31.75 | -30.6% | TRIM/SHORT |
| LPG Set C (deep-overhang bracket) | $29.58 | -35.4% | TRIM/SHORT |

### BWLP — price $21.60, target $17.52

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| LPG Set A (locked 2026-07-07, evidence-first overhang-tilted) | $14.46 | -33.0% | TRIM/SHORT |
| LPG Set B (arb-bull / PDH-recovery bracket) | $15.04 | -30.4% | TRIM/SHORT |
| LPG Set C (deep-overhang bracket) | $14.00 | -35.2% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the LPG sector; crude / LNG / dry-bulk analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md` / `outputs/dry_bulk_weight_robustness.md`.
