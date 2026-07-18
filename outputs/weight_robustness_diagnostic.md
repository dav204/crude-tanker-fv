# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | ⚑ driven | HOLD under Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | ✓ robust | position BUY across all 5 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Weight sets compared

| Scenario | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|---|---|
| DHT | -24.8% (TRIM/SHORT) | -35.4% (TRIM/SHORT) | -31.9% (TRIM/SHORT) | -40.0% (TRIM/SHORT) | -36.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | -40.4% (TRIM/SHORT) | -51.6% (TRIM/SHORT) | -47.9% (TRIM/SHORT) | -56.3% (TRIM/SHORT) | -52.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | -37.5% (TRIM/SHORT) | -49.8% (TRIM/SHORT) | -45.7% (TRIM/SHORT) | -55.0% (TRIM/SHORT) | -50.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | -37.6% (TRIM/SHORT) | -43.0% (TRIM/SHORT) | -41.2% (TRIM/SHORT) | -45.2% (TRIM/SHORT) | -43.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | +4.7% (HOLD) | -2.9% (HOLD) | -0.4% (HOLD) | -6.0% (TRIM/SHORT) | -3.3% (HOLD) | ⚑ driven | HOLD under Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | -54.4% (TRIM/SHORT) | -61.8% (TRIM/SHORT) | -59.4% (TRIM/SHORT) | -64.8% (TRIM/SHORT) | -62.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | +50.4% (BUY) | +37.5% (BUY) | +41.8% (BUY) | +32.5% (BUY) | +37.1% (BUY) | ✓ robust | position BUY across all 5 weight sets |
| CMBT | -5.8% (TRIM/SHORT) | -10.9% (TRIM/SHORT) | -9.2% (TRIM/SHORT) | -13.1% (TRIM/SHORT) | -11.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | +12.8% (BUY) | -40.0% (TRIM/SHORT) | -22.5% (TRIM/SHORT) | -62.8% (TRIM/SHORT) | -43.3% (TRIM/SHORT) | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | +3.3% (HOLD) | -19.6% (TRIM/SHORT) | -12.0% (TRIM/SHORT) | -29.2% (TRIM/SHORT) | -20.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $17.41, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.10 | -24.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $11.24 | -35.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.86 | -31.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $10.45 | -40.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $11.13 | -36.0% | TRIM/SHORT |

### ECO — price $53.88, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $32.10 | -40.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $26.08 | -51.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.08 | -47.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $23.54 | -56.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $25.74 | -52.2% | TRIM/SHORT |

### FRO — price $36.49, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $22.80 | -37.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $18.33 | -49.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $19.82 | -45.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $16.43 | -55.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $18.07 | -50.5% | TRIM/SHORT |

### INSW — price $86.76, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $54.12 | -37.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $49.44 | -43.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $50.99 | -41.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $47.51 | -45.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $49.21 | -43.3% | TRIM/SHORT |

### TNK — price $70.07, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $73.35 | +4.7% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $68.03 | -2.9% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $69.81 | -0.4% | HOLD |
| Crude Set D (bearish, deep normalization) | $65.84 | -6.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $67.77 | -3.3% | HOLD |

### NAT — price $6.05, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $2.76 | -54.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.31 | -61.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.46 | -59.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.13 | -64.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.29 | -62.2% | TRIM/SHORT |

### TEN — price $37.62, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $56.56 | +50.4% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $51.74 | +37.5% | BUY |
| Crude Set C (bullish, extended Phase 1) | $53.34 | +41.8% | BUY |
| Crude Set D (bearish, deep normalization) | $49.85 | +32.5% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $51.56 | +37.1% | BUY |

### CMBT — price $14.96, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $14.09 | -5.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.33 | -10.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.58 | -9.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.00 | -13.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.28 | -11.2% | TRIM/SHORT |

### BRUT — price $5.50, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $6.21 | +12.8% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $3.30 | -40.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.26 | -22.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.05 | -62.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.12 | -43.3% | TRIM/SHORT |

### CAPT — price $12.72, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.14 | +3.3% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $10.23 | -19.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.19 | -12.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.00 | -29.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $10.07 | -20.8% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
