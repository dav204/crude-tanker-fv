# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TNK | ⚑ driven | HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TEN | ✓ robust | position BUY across all 6 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| BRUT | ⚑ driven | BUY under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| CAPT | ⚑ driven | BUY under Set A'/Set A; TRIM/SHORT under Set B/Set D/Set E; HOLD under Set C |

## Weight sets compared

| Scenario | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -15.2% (TRIM/SHORT) | -16.3% (TRIM/SHORT) | -25.7% (TRIM/SHORT) | -22.6% (TRIM/SHORT) | -30.1% (TRIM/SHORT) | -26.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| ECO | -34.1% (TRIM/SHORT) | -35.1% (TRIM/SHORT) | -44.2% (TRIM/SHORT) | -41.2% (TRIM/SHORT) | -48.3% (TRIM/SHORT) | -44.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| FRO | -30.3% (TRIM/SHORT) | -31.5% (TRIM/SHORT) | -42.4% (TRIM/SHORT) | -38.8% (TRIM/SHORT) | -47.4% (TRIM/SHORT) | -43.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| INSW | -35.7% (TRIM/SHORT) | -36.2% (TRIM/SHORT) | -41.0% (TRIM/SHORT) | -39.4% (TRIM/SHORT) | -43.2% (TRIM/SHORT) | -41.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TNK | +3.5% (HOLD) | +2.9% (HOLD) | -3.5% (HOLD) | -1.4% (HOLD) | -6.3% (TRIM/SHORT) | -3.9% (HOLD) | ⚑ driven | HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | -52.6% (TRIM/SHORT) | -53.3% (TRIM/SHORT) | -59.7% (TRIM/SHORT) | -57.6% (TRIM/SHORT) | -62.6% (TRIM/SHORT) | -60.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TEN | +58.9% (BUY) | +57.8% (BUY) | +46.8% (BUY) | +50.5% (BUY) | +42.0% (BUY) | +46.1% (BUY) | ✓ robust | position BUY across all 6 weight sets |
| CMBT | -14.2% (TRIM/SHORT) | -14.6% (TRIM/SHORT) | -18.9% (TRIM/SHORT) | -17.5% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | -19.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| BRUT | +61.8% (BUY) | +56.1% (BUY) | +13.0% (BUY) | +27.3% (BUY) | -7.9% (TRIM/SHORT) | +8.9% (BUY) | ⚑ driven | BUY under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| CAPT | +11.0% (BUY) | +8.8% (BUY) | -10.0% (TRIM/SHORT) | -3.8% (HOLD) | -18.8% (TRIM/SHORT) | -11.6% (TRIM/SHORT) | ⚑ driven | BUY under Set A'/Set A; TRIM/SHORT under Set B/Set D/Set E; HOLD under Set C |

## Per-name detail

### DHT — price $18.72, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $15.88 | -15.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -16.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -25.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -22.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -30.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -26.5% | TRIM/SHORT |

### ECO — price $62.88, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $41.44 | -34.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -35.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -44.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -41.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -48.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -44.9% | TRIM/SHORT |

### FRO — price $39.57, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $27.57 | -30.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.10 | -31.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $22.81 | -42.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.24 | -38.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $20.82 | -47.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $22.46 | -43.2% | TRIM/SHORT |

### INSW — price $92.38, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $59.39 | -35.7% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -36.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -41.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -39.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -43.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -41.4% | TRIM/SHORT |

### TNK — price $80.89, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $83.72 | +3.5% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | +2.9% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -3.5% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -1.4% | HOLD |
| Crude Set D (bearish, deep normalization) | $75.77 | -6.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -3.9% | HOLD |

### NAT — price $6.44, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $3.05 | -52.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.01 | -53.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.59 | -59.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.73 | -57.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.41 | -62.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.57 | -60.2% | TRIM/SHORT |

### TEN — price $39.31, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $62.47 | +58.9% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +57.8% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +46.8% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +50.5% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +42.0% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +46.1% | BUY |

### CMBT — price $16.75, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $14.38 | -14.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.30 | -14.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.58 | -18.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.82 | -17.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.25 | -20.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.52 | -19.3% | TRIM/SHORT |

### BRUT — price $6.26, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $10.13 | +61.8% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $9.77 | +56.1% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $7.07 | +13.0% | BUY |
| Crude Set C (bullish, extended Phase 1) | $7.97 | +27.3% | BUY |
| Crude Set D (bearish, deep normalization) | $5.77 | -7.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $6.82 | +8.9% | BUY |

### CAPT — price $14.31, target $18.90

**Classification:** WEIGHT-DRIVEN. BUY under Set A'/Set A; TRIM/SHORT under Set B/Set D/Set E; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $15.88 | +11.0% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.56 | +8.8% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $12.87 | -10.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.76 | -3.8% | HOLD |
| Crude Set D (bearish, deep normalization) | $11.62 | -18.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.65 | -11.6% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
