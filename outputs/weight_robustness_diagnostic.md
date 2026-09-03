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
| TNK | ⚑ driven | HOLD under Set A''; TRIM/SHORT under Set A'/Set A/Set B/Set C/Set D/Set E |
| NAT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | ✓ robust | position BUY across all 7 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

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
| DHT | -18.9% (TRIM/SHORT) | -19.4% (TRIM/SHORT) | -20.4% (TRIM/SHORT) | -29.4% (TRIM/SHORT) | -26.4% (TRIM/SHORT) | -33.6% (TRIM/SHORT) | -30.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -38.6% (TRIM/SHORT) | -39.0% (TRIM/SHORT) | -39.9% (TRIM/SHORT) | -48.3% (TRIM/SHORT) | -45.6% (TRIM/SHORT) | -52.2% (TRIM/SHORT) | -49.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -36.2% (TRIM/SHORT) | -36.6% (TRIM/SHORT) | -37.7% (TRIM/SHORT) | -46.8% (TRIM/SHORT) | -43.8% (TRIM/SHORT) | -51.1% (TRIM/SHORT) | -47.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -40.3% (TRIM/SHORT) | -40.5% (TRIM/SHORT) | -40.9% (TRIM/SHORT) | -45.4% (TRIM/SHORT) | -43.9% (TRIM/SHORT) | -47.4% (TRIM/SHORT) | -45.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -4.9% (HOLD) | -5.2% (TRIM/SHORT) | -5.7% (TRIM/SHORT) | -11.6% (TRIM/SHORT) | -9.6% (TRIM/SHORT) | -14.2% (TRIM/SHORT) | -12.0% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''; TRIM/SHORT under Set A'/Set A/Set B/Set C/Set D/Set E |
| NAT | -56.6% (TRIM/SHORT) | -56.9% (TRIM/SHORT) | -57.5% (TRIM/SHORT) | -63.4% (TRIM/SHORT) | -61.4% (TRIM/SHORT) | -65.9% (TRIM/SHORT) | -63.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +46.3% (BUY) | +45.9% (BUY) | +44.9% (BUY) | +34.8% (BUY) | +38.1% (BUY) | +30.3% (BUY) | +34.1% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -25.3% (TRIM/SHORT) | -25.5% (TRIM/SHORT) | -25.9% (TRIM/SHORT) | -29.8% (TRIM/SHORT) | -28.5% (TRIM/SHORT) | -31.6% (TRIM/SHORT) | -30.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +2.9% (HOLD) | +1.7% (HOLD) | -1.2% (HOLD) | -23.7% (TRIM/SHORT) | -16.3% (TRIM/SHORT) | -34.5% (TRIM/SHORT) | -25.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | +4.3% (HOLD) | +3.4% (HOLD) | +1.3% (HOLD) | -15.1% (TRIM/SHORT) | -9.6% (TRIM/SHORT) | -23.0% (TRIM/SHORT) | -16.6% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $19.69, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $15.97 | -18.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -19.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -20.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -29.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -26.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -33.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -30.1% | TRIM/SHORT |

### ECO — price $67.96, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.71 | -38.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.44 | -39.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -39.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -48.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -45.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -52.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -49.0% | TRIM/SHORT |

### FRO — price $44.32, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $28.29 | -36.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.09 | -36.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.63 | -37.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.57 | -46.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.92 | -43.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.68 | -51.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.23 | -47.6% | TRIM/SHORT |

### INSW — price $99.76, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.59 | -40.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.39 | -40.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -40.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -45.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -43.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -47.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -45.7% | TRIM/SHORT |

### TNK — price $88.30, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''; TRIM/SHORT under Set A'/Set A/Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $83.93 | -4.9% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $83.72 | -5.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | -5.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -11.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -9.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $75.77 | -14.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -12.0% | TRIM/SHORT |

### NAT — price $6.91, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $3.00 | -56.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.98 | -56.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.94 | -57.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.53 | -63.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.67 | -61.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.35 | -65.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.51 | -63.7% | TRIM/SHORT |

### TEN — price $42.82, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $62.66 | +46.3% | BUY |
| Crude Set A' (B' reweight, history bracket) | $62.47 | +45.9% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +44.9% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +34.8% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +38.1% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +30.3% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +34.1% | BUY |

### CMBT — price $18.27, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $13.65 | -25.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $13.62 | -25.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.54 | -25.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.82 | -29.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.06 | -28.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.49 | -31.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.76 | -30.1% | TRIM/SHORT |

### BRUT — price $4.98, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $5.12 | +2.9% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.06 | +1.7% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $4.92 | -1.2% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.80 | -23.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.17 | -16.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.26 | -34.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.70 | -25.7% | TRIM/SHORT |

### CAPT — price $16.84, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $17.56 | +4.3% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $17.41 | +3.4% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $17.07 | +1.3% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $14.30 | -15.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.22 | -9.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.98 | -23.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.05 | -16.6% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
