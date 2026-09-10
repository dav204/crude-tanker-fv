# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | ✓ robust | position BUY across all 7 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ✓ robust | position TRIM/SHORT across all 7 weight sets |

## Weight sets compared

| Scenario | Set A'' | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.62 | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.00 | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A'' EV | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -23.9% (TRIM/SHORT) | -24.4% (TRIM/SHORT) | -25.4% (TRIM/SHORT) | -33.6% (TRIM/SHORT) | -30.9% (TRIM/SHORT) | -37.5% (TRIM/SHORT) | -34.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -42.1% (TRIM/SHORT) | -42.5% (TRIM/SHORT) | -43.3% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | -48.7% (TRIM/SHORT) | -55.0% (TRIM/SHORT) | -51.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -40.1% (TRIM/SHORT) | -40.5% (TRIM/SHORT) | -41.4% (TRIM/SHORT) | -50.0% (TRIM/SHORT) | -47.2% (TRIM/SHORT) | -54.0% (TRIM/SHORT) | -50.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -43.3% (TRIM/SHORT) | -43.5% (TRIM/SHORT) | -43.9% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | -46.8% (TRIM/SHORT) | -50.1% (TRIM/SHORT) | -48.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -14.4% (TRIM/SHORT) | -14.6% (TRIM/SHORT) | -15.0% (TRIM/SHORT) | -20.6% (TRIM/SHORT) | -18.7% (TRIM/SHORT) | -22.9% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | -60.0% (TRIM/SHORT) | -60.2% (TRIM/SHORT) | -60.7% (TRIM/SHORT) | -66.5% (TRIM/SHORT) | -64.6% (TRIM/SHORT) | -68.9% (TRIM/SHORT) | -66.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +38.0% (BUY) | +37.6% (BUY) | +36.8% (BUY) | +26.6% (BUY) | +30.0% (BUY) | +22.3% (BUY) | +26.1% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -29.8% (TRIM/SHORT) | -30.0% (TRIM/SHORT) | -30.4% (TRIM/SHORT) | -34.1% (TRIM/SHORT) | -32.9% (TRIM/SHORT) | -35.8% (TRIM/SHORT) | -34.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +3.2% (HOLD) | +2.0% (HOLD) | -0.9% (HOLD) | -22.9% (TRIM/SHORT) | -15.6% (TRIM/SHORT) | -33.4% (TRIM/SHORT) | -24.9% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -8.6% (TRIM/SHORT) | -9.4% (TRIM/SHORT) | -11.2% (TRIM/SHORT) | -25.7% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | -32.6% (TRIM/SHORT) | -27.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |

## Per-name detail

### DHT — price $21.20, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $16.12 | -23.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.03 | -24.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.82 | -25.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.07 | -33.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.65 | -30.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.24 | -37.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.91 | -34.4% | TRIM/SHORT |

### ECO — price $71.67, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.50 | -42.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.23 | -42.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.63 | -43.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $34.88 | -51.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $36.79 | -48.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.27 | -55.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.45 | -51.9% | TRIM/SHORT |

### FRO — price $47.21, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $28.30 | -40.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.10 | -40.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.64 | -41.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.59 | -50.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.93 | -47.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.70 | -54.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.25 | -50.8% | TRIM/SHORT |

### INSW — price $104.62, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.32 | -43.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.13 | -43.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.70 | -43.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.21 | -48.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.70 | -46.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.23 | -50.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $53.90 | -48.5% | TRIM/SHORT |

### TNK — price $96.31, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $82.48 | -14.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $82.29 | -14.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $81.86 | -15.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $76.51 | -20.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $78.30 | -18.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $74.21 | -22.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $76.19 | -20.9% | TRIM/SHORT |

### NAT — price $7.27, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $2.91 | -60.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.89 | -60.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.85 | -60.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.44 | -66.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.57 | -64.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.26 | -68.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.41 | -66.8% | TRIM/SHORT |

### TEN — price $44.32, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $61.17 | +38.0% | BUY |
| Crude Set A' (B' reweight, history bracket) | $61.00 | +37.6% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.62 | +36.8% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $56.13 | +26.6% | BUY |
| Crude Set C (bullish, extended Phase 1) | $57.61 | +30.0% | BUY |
| Crude Set D (bearish, deep normalization) | $54.21 | +22.3% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $55.87 | +26.1% | BUY |

### CMBT — price $19.35, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $13.58 | -29.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $13.55 | -30.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.48 | -30.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.75 | -34.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $12.99 | -32.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.42 | -35.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.69 | -34.4% | TRIM/SHORT |

### BRUT — price $5.07, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $5.23 | +3.2% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.17 | +2.0% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.02 | -0.9% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.91 | -22.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.28 | -15.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.37 | -33.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.81 | -24.9% | TRIM/SHORT |

### CAPT — price $19.11, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $17.46 | -8.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $17.31 | -9.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.97 | -11.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.19 | -25.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.12 | -20.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.87 | -32.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.94 | -27.0% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
