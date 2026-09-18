# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| SB | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| 2343 | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Weight sets compared

| Scenario | Set A | Set B | Set C |
|---|--:|--:|--:|
| china_acceleration | 0.20 | 0.30 | 0.12 |
| moderate_growth | 0.40 | 0.40 | 0.33 |
| china_property_drag | 0.25 | 0.18 | 0.35 |
| coordinated_slowdown | 0.15 | 0.12 | 0.20 |

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Robustness | Notes |
|---|--:|--:|--:|---|---|
| SBLK | -11.6% (TRIM/SHORT) | -8.6% (TRIM/SHORT) | -14.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| GNK | -24.8% (TRIM/SHORT) | -21.8% (TRIM/SHORT) | -28.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -19.3% (TRIM/SHORT) | -17.1% (TRIM/SHORT) | -21.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| SB | +1.9% (HOLD) | +5.9% (BUY) | -2.3% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| 2343 | -29.8% (TRIM/SHORT) | -28.3% (TRIM/SHORT) | -31.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $32.06, target $34.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.34 | -11.6% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.31 | -8.6% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $27.27 | -14.9% | TRIM/SHORT |

### GNK — price $28.10, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $21.14 | -24.8% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $21.96 | -21.8% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $20.22 | -28.0% | TRIM/SHORT |

### CMDB — price $24.01, target $27.98

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $19.37 | -19.3% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $19.91 | -17.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $18.77 | -21.8% | TRIM/SHORT |

### SB — price $8.91, target $7.10

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.08 | +1.9% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.44 | +5.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.71 | -2.3% | HOLD |

### 2343 — price $0.53, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.37 | -29.8% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.38 | -28.3% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.36 | -31.4% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
