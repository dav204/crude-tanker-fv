# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position BUY across all 3 weight sets |
| GNK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | ✓ robust | position BUY across all 3 weight sets |
| SB | ✓ robust | position BUY across all 3 weight sets |

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
| SBLK | +11.9% (BUY) | +16.2% (BUY) | +7.1% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| GNK | -3.9% (HOLD) | +0.1% (HOLD) | -8.3% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | +17.9% (BUY) | +21.5% (BUY) | +14.0% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +53.7% (BUY) | +60.4% (BUY) | +46.5% (BUY) | ✓ robust | position BUY across all 3 weight sets |

## Per-name detail

### SBLK — price $25.20, target $34.50

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.19 | +11.9% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.28 | +16.2% | BUY |
| Bulk Set C (China-property-drag bracket) | $26.99 | +7.1% | BUY |

### GNK — price $24.50, target $24.80

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.56 | -3.9% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.52 | +0.1% | HOLD |
| Bulk Set C (China-property-drag bracket) | $22.48 | -8.3% | TRIM/SHORT |

### CMDB — price $17.25, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.34 | +17.9% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.95 | +21.5% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.67 | +14.0% | BUY |

### SB — price $6.39, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.82 | +53.7% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $10.25 | +60.4% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.36 | +46.5% | BUY |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
