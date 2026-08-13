# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ✓ robust | position BUY across all 3 weight sets |
| SB | ✓ robust | position BUY across all 3 weight sets |
| 2343 | ✓ robust | position HOLD across all 3 weight sets |

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
| SBLK | +6.8% (BUY) | +10.7% (BUY) | +2.6% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| GNK | -10.2% (TRIM/SHORT) | -6.6% (TRIM/SHORT) | -14.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | +13.7% (BUY) | +17.1% (BUY) | +10.0% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +27.8% (BUY) | +33.0% (BUY) | +22.3% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | +1.4% (HOLD) | +3.6% (HOLD) | -1.1% (HOLD) | ✓ robust | position HOLD across all 3 weight sets |

## Per-name detail

### SBLK — price $27.89, target $34.50

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $29.79 | +6.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $30.86 | +10.7% | BUY |
| Bulk Set C (China-property-drag bracket) | $28.61 | +2.6% | HOLD |

### GNK — price $25.26, target $24.80

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $22.67 | -10.2% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $23.60 | -6.6% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $21.63 | -14.4% | TRIM/SHORT |

### CMDB — price $17.68, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.11 | +13.7% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +17.1% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.45 | +10.0% | BUY |

### SB — price $7.46, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.53 | +27.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.92 | +33.0% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +22.3% | BUY |

### 2343 — price $0.39, target $0.44

**Classification:** WEIGHT-ROBUST. position HOLD across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.40 | +1.4% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.40 | +3.6% | HOLD |
| Bulk Set C (China-property-drag bracket) | $0.39 | -1.1% | HOLD |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
