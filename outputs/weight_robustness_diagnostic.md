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
| BRUT | ⚑ driven | BUY under Set A''/Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| CAPT | ⚑ driven | HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

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
| DHT | -16.7% (TRIM/SHORT) | -17.2% (TRIM/SHORT) | -18.3% (TRIM/SHORT) | -27.5% (TRIM/SHORT) | -24.4% (TRIM/SHORT) | -31.8% (TRIM/SHORT) | -28.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -35.9% (TRIM/SHORT) | -36.3% (TRIM/SHORT) | -37.2% (TRIM/SHORT) | -46.0% (TRIM/SHORT) | -43.1% (TRIM/SHORT) | -50.0% (TRIM/SHORT) | -46.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -36.1% (TRIM/SHORT) | -36.6% (TRIM/SHORT) | -37.7% (TRIM/SHORT) | -47.5% (TRIM/SHORT) | -44.2% (TRIM/SHORT) | -52.1% (TRIM/SHORT) | -48.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -39.8% (TRIM/SHORT) | -40.0% (TRIM/SHORT) | -40.5% (TRIM/SHORT) | -45.0% (TRIM/SHORT) | -43.5% (TRIM/SHORT) | -47.0% (TRIM/SHORT) | -45.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -6.8% (TRIM/SHORT) | -7.0% (TRIM/SHORT) | -7.5% (TRIM/SHORT) | -13.3% (TRIM/SHORT) | -11.4% (TRIM/SHORT) | -15.8% (TRIM/SHORT) | -13.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | -55.5% (TRIM/SHORT) | -55.8% (TRIM/SHORT) | -56.4% (TRIM/SHORT) | -62.4% (TRIM/SHORT) | -60.4% (TRIM/SHORT) | -65.1% (TRIM/SHORT) | -62.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +48.2% (BUY) | +47.8% (BUY) | +46.8% (BUY) | +36.5% (BUY) | +39.9% (BUY) | +32.0% (BUY) | +35.9% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -20.7% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | -21.3% (TRIM/SHORT) | -25.3% (TRIM/SHORT) | -24.0% (TRIM/SHORT) | -27.1% (TRIM/SHORT) | -25.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +62.7% (BUY) | +60.2% (BUY) | +54.6% (BUY) | +11.9% (BUY) | +26.0% (BUY) | -8.8% (TRIM/SHORT) | +7.8% (BUY) | ⚑ driven | BUY under Set A''/Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| CAPT | -3.1% (HOLD) | -3.9% (HOLD) | -5.9% (TRIM/SHORT) | -22.1% (TRIM/SHORT) | -16.8% (TRIM/SHORT) | -29.7% (TRIM/SHORT) | -23.5% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $19.17, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $15.97 | -16.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -17.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -18.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -27.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -24.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -31.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -28.2% | TRIM/SHORT |

### ECO — price $65.04, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.71 | -35.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.44 | -36.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -37.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -46.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -43.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -50.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -46.7% | TRIM/SHORT |

### FRO — price $43.46, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $27.79 | -36.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $27.57 | -36.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.10 | -37.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $22.81 | -47.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.24 | -44.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $20.82 | -52.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $22.46 | -48.3% | TRIM/SHORT |

### INSW — price $99.05, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.59 | -39.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.39 | -40.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -40.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -45.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -43.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -47.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -45.3% | TRIM/SHORT |

### TNK — price $90.03, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $83.93 | -6.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $83.72 | -7.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | -7.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -13.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -11.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $75.77 | -15.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -13.7% | TRIM/SHORT |

### NAT — price $6.90, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $3.07 | -55.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.05 | -55.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.01 | -56.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.59 | -62.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.73 | -60.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.41 | -65.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.57 | -62.8% | TRIM/SHORT |

### TEN — price $42.27, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $62.66 | +48.2% | BUY |
| Crude Set A' (B' reweight, history bracket) | $62.47 | +47.8% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +46.8% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +36.5% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +39.9% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +32.0% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +35.9% | BUY |

### CMBT — price $18.17, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $14.41 | -20.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $14.38 | -20.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.30 | -21.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.58 | -25.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.82 | -24.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.25 | -27.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.52 | -25.6% | TRIM/SHORT |

### BRUT — price $6.32, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A''/Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $10.28 | +62.7% | BUY |
| Crude Set A' (B' reweight, history bracket) | $10.13 | +60.2% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $9.77 | +54.6% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $7.07 | +11.9% | BUY |
| Crude Set C (bullish, extended Phase 1) | $7.97 | +26.0% | BUY |
| Crude Set D (bearish, deep normalization) | $5.77 | -8.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $6.82 | +7.8% | BUY |

### CAPT — price $16.53, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $16.02 | -3.1% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -3.9% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.56 | -5.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.87 | -22.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.76 | -16.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $11.62 | -29.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.65 | -23.5% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
