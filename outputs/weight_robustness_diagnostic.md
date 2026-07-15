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
| TNK | ⚑ driven | HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E |
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
| DHT | -26.6% (TRIM/SHORT) | -37.0% (TRIM/SHORT) | -33.5% (TRIM/SHORT) | -41.4% (TRIM/SHORT) | -37.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | -43.4% (TRIM/SHORT) | -54.1% (TRIM/SHORT) | -50.5% (TRIM/SHORT) | -58.5% (TRIM/SHORT) | -54.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | -40.3% (TRIM/SHORT) | -52.0% (TRIM/SHORT) | -48.1% (TRIM/SHORT) | -56.9% (TRIM/SHORT) | -52.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | -38.5% (TRIM/SHORT) | -43.8% (TRIM/SHORT) | -42.0% (TRIM/SHORT) | -46.0% (TRIM/SHORT) | -44.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | +1.3% (HOLD) | -6.1% (TRIM/SHORT) | -3.6% (HOLD) | -9.1% (TRIM/SHORT) | -6.4% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E |
| NAT | -56.8% (TRIM/SHORT) | -63.8% (TRIM/SHORT) | -61.5% (TRIM/SHORT) | -66.7% (TRIM/SHORT) | -64.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | +45.0% (BUY) | +31.9% (BUY) | +36.3% (BUY) | +26.6% (BUY) | +31.3% (BUY) | ✓ robust | position BUY across all 5 weight sets |
| CMBT | -12.1% (TRIM/SHORT) | -17.0% (TRIM/SHORT) | -15.4% (TRIM/SHORT) | -19.0% (TRIM/SHORT) | -17.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | +11.3% (BUY) | -40.8% (TRIM/SHORT) | -23.5% (TRIM/SHORT) | -63.3% (TRIM/SHORT) | -44.0% (TRIM/SHORT) | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -1.9% (HOLD) | -23.7% (TRIM/SHORT) | -16.5% (TRIM/SHORT) | -32.8% (TRIM/SHORT) | -24.9% (TRIM/SHORT) | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $18.18, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.34 | -26.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $11.46 | -37.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $12.08 | -33.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $10.66 | -41.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $11.35 | -37.6% | TRIM/SHORT |

### ECO — price $56.73, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $32.09 | -43.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $26.06 | -54.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.07 | -50.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $23.52 | -58.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $25.73 | -54.6% | TRIM/SHORT |

### FRO — price $38.38, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $22.91 | -40.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $18.43 | -52.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $19.92 | -48.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $16.53 | -56.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $18.17 | -52.7% | TRIM/SHORT |

### INSW — price $88.12, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $54.21 | -38.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $49.52 | -43.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $51.07 | -42.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $47.58 | -46.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $49.28 | -44.1% | TRIM/SHORT |

### TNK — price $72.27, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $73.18 | +1.3% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $67.88 | -6.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $69.65 | -3.6% | HOLD |
| Crude Set D (bearish, deep normalization) | $65.69 | -9.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $67.61 | -6.4% | TRIM/SHORT |

### NAT — price $6.29, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $2.72 | -56.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.27 | -63.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.42 | -61.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.09 | -66.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.25 | -64.2% | TRIM/SHORT |

### TEN — price $39.75, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $57.64 | +45.0% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $52.43 | +31.9% | BUY |
| Crude Set C (bullish, extended Phase 1) | $54.18 | +36.3% | BUY |
| Crude Set D (bearish, deep normalization) | $50.33 | +26.6% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $52.20 | +31.3% | BUY |

### CMBT — price $15.78, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.87 | -12.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.10 | -17.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.36 | -15.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.78 | -19.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.06 | -17.2% | TRIM/SHORT |

### BRUT — price $5.57, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $6.20 | +11.3% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $3.30 | -40.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.26 | -23.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.04 | -63.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.12 | -44.0% | TRIM/SHORT |

### CAPT — price $13.40, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.14 | -1.9% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $10.23 | -23.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.19 | -16.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.00 | -32.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $10.07 | -24.9% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
