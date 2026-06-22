# Terminal-NAV-Multiple Sensitivity Sweep — METHODOLOGY §9.2

**Open methodology decision #2.** The dividend strip terminates at q9 with a terminal value = `TERMINAL_NAV_MULTIPLE × NAV(aged 9q)`. Production multiple is **1.0×**. §9.2 flags two open priors: 0.9× (mid-cycle discount) and 1.1× (structural undersupply). This sweep tests {0.85, 0.9, 1.0, 1.1, 1.15} for every watchlist name.

**How to read it.** The strip terminal sits inside the *earnings* leg of the blend, so the FV impact scales with `w_earn`. Late-cycle names (w_earn = 0.30) absorb the smallest swing; below-mid-cycle names (w_earn = 0.60) the largest. **Position flips are what matter** — they identify calls that are sensitive to the §9.2 choice. A name with no flip across the full ±15% range is *multiple-robust* on its current position.

## DHT — price $16.40, baseline 1.0× FV $14.31

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $8.81/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $13.91 | -2.8% | -15.2% | $16.83 | +2.6% | **HOLD** ⚑ |
| 0.90× | $14.04 | -1.8% | -14.4% | $16.99 | +3.6% | **HOLD** ⚑ |
| 1.00×  ← | $14.31 | +0.0% | -12.8% | $17.32 | +5.6% | BUY |
| 1.10× | $14.57 | +1.8% | -11.2% | $17.65 | +7.6% | BUY |
| 1.15× | $14.70 | +2.8% | -10.3% | $17.81 | +8.6% | BUY |

**⚑ Position flips across the sweep: BUY / HOLD.**

## ECO — price $47.70, baseline 1.0× FV $36.67

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $22.82/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $35.64 | -2.8% | -25.3% | $44.09 | -7.6% | **TRIM/SHORT** ⚑ |
| 0.90× | $35.99 | -1.9% | -24.6% | $44.53 | -6.6% | **TRIM/SHORT** ⚑ |
| 1.00×  ← | $36.67 | +0.0% | -23.1% | $45.41 | -4.8% | HOLD |
| 1.10× | $37.35 | +1.9% | -21.7% | $46.29 | -3.0% | HOLD |
| 1.15× | $37.70 | +2.8% | -21.0% | $46.72 | -2.0% | HOLD |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## FRO — price $34.50, baseline 1.0× FV $27.09

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $15.72/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $26.39 | -2.6% | -23.5% | $32.83 | -4.8% | HOLD |
| 0.90× | $26.62 | -1.7% | -22.8% | $33.15 | -3.9% | HOLD |
| 1.00×  ← | $27.09 | +0.0% | -21.5% | $33.77 | -2.1% | HOLD |
| 1.10× | $27.57 | +1.7% | -20.1% | $34.39 | -0.3% | HOLD |
| 1.15× | $27.80 | +2.6% | -19.4% | $34.70 | +0.6% | HOLD |

## INSW — price $78.00, baseline 1.0× FV $37.31

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $24.06/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $36.23 | -2.9% | -53.6% | $62.59 | -19.8% | TRIM/SHORT |
| 0.90× | $36.59 | -1.9% | -53.1% | $63.26 | -18.9% | TRIM/SHORT |
| 1.00×  ← | $37.31 | +0.0% | -52.2% | $64.59 | -17.2% | TRIM/SHORT |
| 1.10× | $38.04 | +1.9% | -51.2% | $65.92 | -15.5% | TRIM/SHORT |
| 1.15× | $38.40 | +2.9% | -50.8% | $66.58 | -14.6% | TRIM/SHORT |

## TNK — price $70.80, baseline 1.0× FV $73.94

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $55.31/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $71.45 | -3.4% | +0.9% | $76.02 | +7.4% | BUY |
| 0.90× | $72.28 | -2.2% | +2.1% | $76.98 | +8.7% | BUY |
| 1.00×  ← | $73.94 | +0.0% | +4.4% | $78.90 | +11.4% | BUY |
| 1.10× | $75.60 | +2.2% | +6.8% | $80.82 | +14.2% | BUY |
| 1.15× | $76.43 | +3.4% | +8.0% | $81.79 | +15.5% | BUY |

## NAT — price $5.20, baseline 1.0× FV $2.59

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $1.07/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $2.55 | -1.9% | -51.0% | $3.30 | -36.5% | TRIM/SHORT |
| 0.90× | $2.56 | -1.2% | -50.7% | $3.33 | -36.0% | TRIM/SHORT |
| 1.00×  ← | $2.59 | +0.0% | -50.1% | $3.37 | -35.2% | TRIM/SHORT |
| 1.10× | $2.63 | +1.2% | -49.5% | $3.42 | -34.3% | TRIM/SHORT |
| 1.15× | $2.64 | +1.9% | -49.2% | $3.44 | -33.8% | TRIM/SHORT |

## FLNG — price $29.70, baseline 1.0× FV $26.27

_Cycle band: **below-mid** (w_nav = 0.40, w_earn = 0.60). Discounted terminal at 1.0× = $19.46/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $24.51 | -6.7% | -17.5% | $28.18 | -5.1% | **TRIM/SHORT** ⚑ |
| 0.90× | $25.10 | -4.4% | -15.5% | $28.70 | -3.4% | HOLD |
| 1.00×  ← | $26.27 | +0.0% | -11.6% | $29.73 | +0.1% | HOLD |
| 1.10× | $27.43 | +4.4% | -7.6% | $30.76 | +3.6% | HOLD |
| 1.15× | $28.02 | +6.7% | -5.7% | $31.28 | +5.3% | **BUY** ⚑ |

**⚑ Position flips across the sweep: BUY / HOLD / TRIM/SHORT.**

## CCEC — price $21.90, baseline 1.0× FV $22.88

_Cycle band: **below-mid** (w_nav = 0.40, w_earn = 0.60). Discounted terminal at 1.0× = $18.33/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $21.23 | -7.2% | -3.1% | $28.08 | +28.2% | BUY |
| 0.90× | $21.78 | -4.8% | -0.6% | $28.60 | +30.6% | BUY |
| 1.00×  ← | $22.88 | +0.0% | +4.5% | $29.63 | +35.3% | BUY |
| 1.10× | $23.98 | +4.8% | +9.5% | $30.66 | +40.0% | BUY |
| 1.15× | $24.52 | +7.2% | +12.0% | $31.18 | +42.4% | BUY |

## STNG — price $75.60, baseline 1.0× FV $74.00

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $55.96/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $71.48 | -3.4% | -5.5% | $73.32 | -3.0% | HOLD |
| 0.90× | $72.32 | -2.3% | -4.3% | $74.34 | -1.7% | HOLD |
| 1.00×  ← | $74.00 | +0.0% | -2.1% | $76.37 | +1.0% | HOLD |
| 1.10× | $75.68 | +2.3% | +0.1% | $78.40 | +3.7% | HOLD |
| 1.15× | $76.52 | +3.4% | +1.2% | $79.42 | +5.0% | **BUY** ⚑ |

**⚑ Position flips across the sweep: BUY / HOLD.**

## HAFN — price $7.70, baseline 1.0× FV $5.59

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $3.34/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $5.44 | -2.7% | -29.3% | $5.69 | -26.0% | TRIM/SHORT |
| 0.90× | $5.49 | -1.8% | -28.7% | $5.75 | -25.3% | TRIM/SHORT |
| 1.00×  ← | $5.59 | +0.0% | -27.4% | $5.87 | -23.8% | TRIM/SHORT |
| 1.10× | $5.69 | +1.8% | -26.1% | $5.99 | -22.3% | TRIM/SHORT |
| 1.15× | $5.74 | +2.7% | -25.4% | $6.05 | -21.5% | TRIM/SHORT |

## TRMD — price $28.20, baseline 1.0× FV $26.09

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $16.25/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $25.36 | -2.8% | -10.1% | $26.96 | -4.4% | HOLD |
| 0.90× | $25.60 | -1.9% | -9.2% | $27.25 | -3.4% | HOLD |
| 1.00×  ← | $26.09 | +0.0% | -7.5% | $27.83 | -1.3% | HOLD |
| 1.10× | $26.58 | +1.9% | -5.8% | $28.41 | +0.7% | HOLD |
| 1.15× | $26.82 | +2.8% | -4.9% | $28.70 | +1.8% | HOLD |

## ASC — price $16.00, baseline 1.0× FV $14.88

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $10.85/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $14.23 | -4.4% | -11.1% | $14.50 | -9.4% | TRIM/SHORT |
| 0.90× | $14.45 | -2.9% | -9.7% | $14.69 | -8.2% | TRIM/SHORT |
| 1.00×  ← | $14.88 | +0.0% | -7.0% | $15.07 | -5.8% | TRIM/SHORT |
| 1.10× | $15.31 | +2.9% | -4.3% | $15.46 | -3.4% | **HOLD** ⚑ |
| 1.15× | $15.53 | +4.4% | -2.9% | $15.65 | -2.2% | **HOLD** ⚑ |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## TEN — price $37.14, baseline 1.0× FV $57.74

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $40.08/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $55.94 | -3.1% | +50.6% | $65.43 | +76.2% | BUY |
| 0.90× | $56.54 | -2.1% | +52.2% | $66.23 | +78.3% | BUY |
| 1.00×  ← | $57.74 | +0.0% | +55.5% | $67.81 | +82.6% | BUY |
| 1.10× | $58.94 | +2.1% | +58.7% | $69.39 | +86.8% | BUY |
| 1.15× | $59.54 | +3.1% | +60.3% | $70.18 | +89.0% | BUY |

## CMDB — price $17.25, baseline 1.0× FV $20.00

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $15.88/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $19.04 | -4.8% | +10.4% | $19.07 | +10.6% | BUY |
| 0.90× | $19.36 | -3.2% | +12.2% | $19.40 | +12.5% | BUY |
| 1.00×  ← | $20.00 | +0.0% | +15.9% | $20.06 | +16.3% | BUY |
| 1.10× | $20.63 | +3.2% | +19.6% | $20.73 | +20.2% | BUY |
| 1.15× | $20.95 | +4.8% | +21.5% | $21.06 | +22.1% | BUY |

## SBLK — price $27.20, baseline 1.0× FV $26.00

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $17.77/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $24.94 | -4.1% | -8.3% | $24.41 | -10.2% | TRIM/SHORT |
| 0.90× | $25.29 | -2.7% | -7.0% | $24.77 | -8.9% | TRIM/SHORT |
| 1.00×  ← | $26.00 | +0.0% | -4.4% | $25.49 | -6.3% | TRIM/SHORT |
| 1.10× | $26.71 | +2.7% | -1.8% | $26.21 | -3.6% | **HOLD** ⚑ |
| 1.15× | $27.07 | +4.1% | -0.5% | $26.57 | -2.3% | **HOLD** ⚑ |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## GNK — price $24.00, baseline 1.0× FV $25.30

_Cycle band: **mid-cycle** (w_nav = 0.50, w_earn = 0.50). Discounted terminal at 1.0× = $17.50/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $23.99 | -5.2% | -0.1% | $23.96 | -0.2% | HOLD |
| 0.90× | $24.42 | -3.5% | +1.8% | $24.32 | +1.3% | HOLD |
| 1.00×  ← | $25.30 | +0.0% | +5.4% | $25.02 | +4.3% | HOLD |
| 1.10× | $26.17 | +3.5% | +9.1% | $25.73 | +7.2% | **BUY** ⚑ |
| 1.15× | $26.61 | +5.2% | +10.9% | $26.08 | +8.7% | **BUY** ⚑ |

**⚑ Position flips across the sweep: BUY / HOLD.**

## CAPT — price $12.20, baseline 1.0× FV $16.71

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $11.02/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $16.21 | -3.0% | +32.9% | $17.56 | +44.0% | BUY |
| 0.90× | $16.38 | -2.0% | +34.3% | $17.76 | +45.6% | BUY |
| 1.00×  ← | $16.71 | +0.0% | +37.0% | $18.15 | +48.8% | BUY |
| 1.10× | $17.04 | +2.0% | +39.7% | $18.54 | +52.0% | BUY |
| 1.15× | $17.21 | +3.0% | +41.0% | $18.74 | +53.6% | BUY |

## MPCC — price $2.78, baseline 1.0× FV $2.13

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $1.39/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $2.05 | -3.9% | -26.4% | $1.88 | -32.4% | TRIM/SHORT |
| 0.90× | $2.07 | -2.6% | -25.4% | $1.90 | -31.5% | TRIM/SHORT |
| 1.00×  ← | $2.13 | +0.0% | -23.4% | $1.96 | -29.6% | TRIM/SHORT |
| 1.10× | $2.18 | +2.6% | -21.4% | $2.01 | -27.6% | TRIM/SHORT |
| 1.15× | $2.21 | +3.9% | -20.4% | $2.04 | -26.7% | TRIM/SHORT |

## GSL — price $38.99, baseline 1.0× FV $34.23

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $23.24/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $32.83 | -4.1% | -15.8% | $30.59 | -21.5% | TRIM/SHORT |
| 0.90× | $33.30 | -2.7% | -14.6% | $30.98 | -20.5% | TRIM/SHORT |
| 1.00×  ← | $34.23 | +0.0% | -12.2% | $31.76 | -18.5% | TRIM/SHORT |
| 1.10× | $35.16 | +2.7% | -9.8% | $32.53 | -16.6% | TRIM/SHORT |
| 1.15× | $35.62 | +4.1% | -8.6% | $32.92 | -15.6% | TRIM/SHORT |

---

## Summary

**Position flips (multiple-driven calls):**

| Ticker | Cycle | w_earn | Positions seen | Pt FV range | PW FV range |
|---|---|--:|---|--:|--:|
| DHT | late-cycle/peak | 0.30 | HOLD → HOLD → BUY → BUY → BUY | 5.5% | 5.7% |
| ECO | late-cycle/peak | 0.30 | TRIM/SHORT → TRIM/SHORT → HOLD → HOLD → HOLD | 5.6% | 5.8% |
| FLNG | below-mid | 0.60 | TRIM/SHORT → HOLD → HOLD → HOLD → BUY | 13.3% | 10.4% |
| STNG | late-cycle/peak | 0.30 | HOLD → HOLD → HOLD → HOLD → BUY | 6.8% | 8.0% |
| ASC | elevated | 0.40 | TRIM/SHORT → TRIM/SHORT → TRIM/SHORT → HOLD → HOLD | 8.7% | 7.7% |
| SBLK | elevated | 0.40 | TRIM/SHORT → TRIM/SHORT → TRIM/SHORT → HOLD → HOLD | 8.2% | 8.5% |
| GNK | mid-cycle | 0.50 | HOLD → HOLD → HOLD → BUY → BUY | 10.4% | 8.5% |

**Sensitivity rank** (single-point FV % range across 0.85× → 1.15×, highest → lowest):

| Ticker | Cycle | w_earn | Pt FV @ 0.85× | Pt FV @ 1.15× | % range |
|---|---|--:|--:|--:|--:|
| CCEC | below-mid | 0.60 | $21.23 | $24.52 | 14.4% |
| FLNG | below-mid | 0.60 | $24.51 | $28.02 | 13.3% |
| GNK | mid-cycle | 0.50 | $23.99 | $26.61 | 10.4% |
| CMDB | elevated | 0.40 | $19.04 | $20.95 | 9.5% |
| ASC | elevated | 0.40 | $14.23 | $15.53 | 8.7% |
| SBLK | elevated | 0.40 | $24.94 | $27.07 | 8.2% |
| GSL | elevated | 0.40 | $32.83 | $35.62 | 8.1% |
| MPCC | elevated | 0.40 | $2.05 | $2.21 | 7.8% |
| STNG | late-cycle/peak | 0.30 | $71.48 | $76.52 | 6.8% |
| TNK | late-cycle/peak | 0.30 | $71.45 | $76.43 | 6.7% |
| TEN | late-cycle/peak | 0.30 | $55.94 | $59.54 | 6.2% |
| CAPT | late-cycle/peak | 0.30 | $16.21 | $17.21 | 5.9% |
| INSW | late-cycle/peak | 0.30 | $36.23 | $38.40 | 5.8% |
| TRMD | late-cycle/peak | 0.30 | $25.36 | $26.82 | 5.6% |
| ECO | late-cycle/peak | 0.30 | $35.64 | $37.70 | 5.6% |
| DHT | late-cycle/peak | 0.30 | $13.91 | $14.70 | 5.5% |
| HAFN | late-cycle/peak | 0.30 | $5.44 | $5.74 | 5.4% |
| FRO | late-cycle/peak | 0.30 | $26.39 | $27.80 | 5.2% |
| NAT | late-cycle/peak | 0.30 | $2.55 | $2.64 | 3.7% |

## Interpretation

The single-point FV % range tracks `w_earn` as expected: names at peak (w_earn = 0.30) move ~3% across the full ±15% multiple range; names below mid-cycle (w_earn = 0.60) move ~6-8%. Any position flip is therefore a name that already sits close to the ±5% HOLD band and gets pushed across by the multiple alone. **For those names, the §9.2 choice is a material input to the call** and should be named explicitly in the decision log; for non-flippers, the §9.2 decision is informational only.

**This diagnostic does not pick a multiple.** It quantifies how much the open §9.2 decision matters. A resolution still needs a methodological prior — mid-cycle reversion (0.9×), undisturbed (1.0×), or structural undersupply (1.1×) — applied uniformly.

See METHODOLOGY §9 (open methodology decisions) and §3.2 (dividend strip / terminal value construction).
