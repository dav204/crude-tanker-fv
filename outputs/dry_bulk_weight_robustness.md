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
| SB | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
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
| SBLK | -8.4% (TRIM/SHORT) | -5.2% (TRIM/SHORT) | -11.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| GNK | -21.9% (TRIM/SHORT) | -18.8% (TRIM/SHORT) | -25.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -17.4% (TRIM/SHORT) | -15.1% (TRIM/SHORT) | -20.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| SB | +5.2% (BUY) | +9.4% (BUY) | +0.8% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| 2343 | -30.0% (TRIM/SHORT) | -28.5% (TRIM/SHORT) | -31.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $31.34, target $34.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.71 | -8.4% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.71 | -5.2% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $27.62 | -11.9% | TRIM/SHORT |

### GNK — price $27.54, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $21.50 | -21.9% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $22.35 | -18.8% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $20.56 | -25.4% | TRIM/SHORT |

### CMDB — price $23.69, target $27.98

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $19.56 | -17.4% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.11 | -15.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $18.95 | -20.0% | TRIM/SHORT |

### SB — price $8.76, target $7.10

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.22 | +5.2% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.58 | +9.4% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.83 | +0.8% | HOLD |

### 2343 — price $0.54, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -30.0% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.38 | -28.5% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.37 | -31.6% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
