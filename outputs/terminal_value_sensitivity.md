# Terminal-NAV-Multiple Sensitivity Sweep — METHODOLOGY §9.2

**Open methodology decision #2.** The dividend strip terminates at q9 with a terminal value = `TERMINAL_NAV_MULTIPLE × NAV(aged 9q)`. Production multiple is **1.0×**. §9.2 flags two open priors: 0.9× (mid-cycle discount) and 1.1× (structural undersupply). This sweep tests {0.85, 0.9, 1.0, 1.1, 1.15} for every watchlist name.

**How to read it.** The strip terminal sits inside the *earnings* leg of the blend, so the FV impact scales with `w_earn`. Late-cycle names (w_earn = 0.30) absorb the smallest swing; below-mid-cycle names (w_earn = 0.60) the largest. **Position flips are what matter** — they identify calls that are sensitive to the §9.2 choice. A name with no flip across the full ±15% range is *multiple-robust* on its current position.

## DHT — price $16.40, baseline 1.0× FV $16.49

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $10.58/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $16.01 | -2.9% | -2.4% | $12.92 | -21.2% | TRIM/SHORT |
| 0.90× | $16.17 | -1.9% | -1.4% | $13.06 | -20.4% | TRIM/SHORT |
| 1.00×  ← | $16.49 | +0.0% | +0.5% | $13.34 | -18.7% | TRIM/SHORT |
| 1.10× | $16.80 | +1.9% | +2.5% | $13.61 | -17.0% | TRIM/SHORT |
| 1.15× | $16.96 | +2.9% | +3.4% | $13.75 | -16.2% | TRIM/SHORT |

## ECO — price $47.70, baseline 1.0× FV $42.56

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $27.95/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $41.31 | -3.0% | -13.4% | $31.50 | -34.0% | TRIM/SHORT |
| 0.90× | $41.73 | -2.0% | -12.5% | $31.84 | -33.2% | TRIM/SHORT |
| 1.00×  ← | $42.56 | +0.0% | -10.8% | $32.53 | -31.8% | TRIM/SHORT |
| 1.10× | $43.40 | +2.0% | -9.0% | $33.22 | -30.4% | TRIM/SHORT |
| 1.15× | $43.82 | +3.0% | -8.1% | $33.56 | -29.6% | TRIM/SHORT |

## FRO — price $34.50, baseline 1.0× FV $31.37

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $19.71/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $30.48 | -2.8% | -11.7% | $23.16 | -32.9% | TRIM/SHORT |
| 0.90× | $30.77 | -1.9% | -10.8% | $23.40 | -32.2% | TRIM/SHORT |
| 1.00×  ← | $31.37 | +0.0% | -9.1% | $23.87 | -30.8% | TRIM/SHORT |
| 1.10× | $31.96 | +1.9% | -7.4% | $24.35 | -29.4% | TRIM/SHORT |
| 1.15× | $32.25 | +2.8% | -6.5% | $24.58 | -28.7% | TRIM/SHORT |

## INSW — price $78.00, baseline 1.0× FV $42.18

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $27.72/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $40.93 | -3.0% | -47.5% | $50.34 | -35.5% | TRIM/SHORT |
| 0.90× | $41.35 | -2.0% | -47.0% | $50.92 | -34.7% | TRIM/SHORT |
| 1.00×  ← | $42.18 | +0.0% | -45.9% | $52.08 | -33.2% | TRIM/SHORT |
| 1.10× | $43.01 | +2.0% | -44.9% | $53.23 | -31.8% | TRIM/SHORT |
| 1.15× | $43.43 | +3.0% | -44.3% | $53.81 | -31.0% | TRIM/SHORT |

## TNK — price $70.80, baseline 1.0× FV $79.13

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $58.96/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $76.48 | -3.4% | +8.0% | $66.15 | -6.6% | **TRIM/SHORT** ⚑ |
| 0.90× | $77.36 | -2.2% | +9.3% | $67.21 | -5.1% | **TRIM/SHORT** ⚑ |
| 1.00×  ← | $79.13 | +0.0% | +11.8% | $69.31 | -2.1% | HOLD |
| 1.10× | $80.90 | +2.2% | +14.3% | $71.41 | +0.9% | HOLD |
| 1.15× | $81.78 | +3.4% | +15.5% | $72.46 | +2.3% | HOLD |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## NAT — price $5.20, baseline 1.0× FV $3.09

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $1.41/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $3.02 | -2.0% | -41.9% | $2.23 | -57.0% | TRIM/SHORT |
| 0.90× | $3.04 | -1.4% | -41.5% | $2.25 | -56.7% | TRIM/SHORT |
| 1.00×  ← | $3.09 | +0.0% | -40.7% | $2.28 | -56.1% | TRIM/SHORT |
| 1.10× | $3.13 | +1.4% | -39.8% | $2.31 | -55.5% | TRIM/SHORT |
| 1.15× | $3.15 | +2.0% | -39.4% | $2.33 | -55.2% | TRIM/SHORT |

## FLNG — price $29.70, baseline 1.0× FV $26.27

_Cycle band: **below-mid** (w_nav = 0.40, w_earn = 0.60). Discounted terminal at 1.0× = $19.46/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $24.51 | -6.7% | -17.5% | $26.48 | -10.9% | TRIM/SHORT |
| 0.90× | $25.10 | -4.4% | -15.5% | $27.00 | -9.1% | TRIM/SHORT |
| 1.00×  ← | $26.27 | +0.0% | -11.6% | $28.04 | -5.6% | TRIM/SHORT |
| 1.10× | $27.43 | +4.4% | -7.6% | $29.08 | -2.1% | **HOLD** ⚑ |
| 1.15× | $28.02 | +6.7% | -5.7% | $29.61 | -0.3% | **HOLD** ⚑ |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## CCEC — price $21.90, baseline 1.0× FV $22.88

_Cycle band: **below-mid** (w_nav = 0.40, w_earn = 0.60). Discounted terminal at 1.0× = $18.33/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $21.23 | -7.2% | -3.1% | $24.95 | +13.9% | BUY |
| 0.90× | $21.78 | -4.8% | -0.6% | $25.45 | +16.2% | BUY |
| 1.00×  ← | $22.88 | +0.0% | +4.5% | $26.45 | +20.8% | BUY |
| 1.10× | $23.98 | +4.8% | +9.5% | $27.45 | +25.3% | BUY |
| 1.15× | $24.52 | +7.2% | +12.0% | $27.95 | +27.6% | BUY |

## STNG — price $75.60, baseline 1.0× FV $77.29

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $58.75/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $74.65 | -3.4% | -1.3% | $70.67 | -6.5% | **TRIM/SHORT** ⚑ |
| 0.90× | $75.53 | -2.3% | -0.1% | $71.58 | -5.3% | **TRIM/SHORT** ⚑ |
| 1.00×  ← | $77.29 | +0.0% | +2.2% | $73.40 | -2.9% | HOLD |
| 1.10× | $79.06 | +2.3% | +4.6% | $75.21 | -0.5% | HOLD |
| 1.15× | $79.94 | +3.4% | +5.7% | $76.12 | +0.7% | HOLD |

**⚑ Position flips across the sweep: HOLD / TRIM/SHORT.**

## HAFN — price $7.70, baseline 1.0× FV $5.70

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $3.42/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $5.54 | -2.7% | -28.0% | $5.26 | -31.7% | TRIM/SHORT |
| 0.90× | $5.60 | -1.8% | -27.3% | $5.31 | -31.1% | TRIM/SHORT |
| 1.00×  ← | $5.70 | +0.0% | -26.0% | $5.41 | -29.7% | TRIM/SHORT |
| 1.10× | $5.80 | +1.8% | -24.7% | $5.51 | -28.4% | TRIM/SHORT |
| 1.15× | $5.85 | +2.7% | -24.0% | $5.57 | -27.7% | TRIM/SHORT |

## TRMD — price $28.20, baseline 1.0× FV $27.27

_Cycle band: **late-cycle/peak** (w_nav = 0.70, w_earn = 0.30). Discounted terminal at 1.0× = $17.16/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $26.50 | -2.8% | -6.0% | $24.82 | -12.0% | TRIM/SHORT |
| 0.90× | $26.76 | -1.9% | -5.1% | $25.08 | -11.1% | TRIM/SHORT |
| 1.00×  ← | $27.27 | +0.0% | -3.3% | $25.59 | -9.3% | TRIM/SHORT |
| 1.10× | $27.78 | +1.9% | -1.5% | $26.10 | -7.4% | TRIM/SHORT |
| 1.15× | $28.04 | +2.8% | -0.6% | $26.36 | -6.5% | TRIM/SHORT |

## ASC — price $16.00, baseline 1.0× FV $14.90

_Cycle band: **elevated** (w_nav = 0.60, w_earn = 0.40). Discounted terminal at 1.0× = $10.87/sh._

| Multiple | Pt FV | Δ vs 1.0× | Pt EV% | PW FV | PW EV% | Position |
|---:|--:|--:|--:|--:|--:|---|
| 0.85× | $14.25 | -4.4% | -10.9% | $13.92 | -13.0% | TRIM/SHORT |
| 0.90× | $14.47 | -2.9% | -9.6% | $14.11 | -11.8% | TRIM/SHORT |
| 1.00×  ← | $14.90 | +0.0% | -6.9% | $14.50 | -9.4% | TRIM/SHORT |
| 1.10× | $15.34 | +2.9% | -4.1% | $14.89 | -6.9% | TRIM/SHORT |
| 1.15× | $15.55 | +4.4% | -2.8% | $15.09 | -5.7% | TRIM/SHORT |

---

## Summary

**Position flips (multiple-driven calls):**

| Ticker | Cycle | w_earn | Positions seen | Pt FV range | PW FV range |
|---|---|--:|---|--:|--:|
| TNK | late-cycle/peak | 0.30 | TRIM/SHORT → TRIM/SHORT → HOLD → HOLD → HOLD | 6.7% | 9.1% |
| FLNG | below-mid | 0.60 | TRIM/SHORT → TRIM/SHORT → TRIM/SHORT → HOLD → HOLD | 13.3% | 11.2% |
| STNG | late-cycle/peak | 0.30 | TRIM/SHORT → TRIM/SHORT → HOLD → HOLD → HOLD | 6.8% | 7.4% |

**Sensitivity rank** (single-point FV % range across 0.85× → 1.15×, highest → lowest):

| Ticker | Cycle | w_earn | Pt FV @ 0.85× | Pt FV @ 1.15× | % range |
|---|---|--:|--:|--:|--:|
| CCEC | below-mid | 0.60 | $21.23 | $24.52 | 14.4% |
| FLNG | below-mid | 0.60 | $24.51 | $28.02 | 13.3% |
| ASC | elevated | 0.40 | $14.25 | $15.55 | 8.8% |
| STNG | late-cycle/peak | 0.30 | $74.65 | $79.94 | 6.8% |
| TNK | late-cycle/peak | 0.30 | $76.48 | $81.78 | 6.7% |
| INSW | late-cycle/peak | 0.30 | $40.93 | $43.43 | 5.9% |
| ECO | late-cycle/peak | 0.30 | $41.31 | $43.82 | 5.9% |
| DHT | late-cycle/peak | 0.30 | $16.01 | $16.96 | 5.8% |
| TRMD | late-cycle/peak | 0.30 | $26.50 | $28.04 | 5.7% |
| FRO | late-cycle/peak | 0.30 | $30.48 | $32.25 | 5.7% |
| HAFN | late-cycle/peak | 0.30 | $5.54 | $5.85 | 5.4% |
| NAT | late-cycle/peak | 0.30 | $3.02 | $3.15 | 4.1% |

## Interpretation

The single-point FV % range tracks `w_earn` as expected: names at peak (w_earn = 0.30) move ~3% across the full ±15% multiple range; names below mid-cycle (w_earn = 0.60) move ~6-8%. Any position flip is therefore a name that already sits close to the ±5% HOLD band and gets pushed across by the multiple alone. **For those names, the §9.2 choice is a material input to the call** and should be named explicitly in the decision log; for non-flippers, the §9.2 decision is informational only.

**This diagnostic does not pick a multiple.** It quantifies how much the open §9.2 decision matters. A resolution still needs a methodological prior — mid-cycle reversion (0.9×), undisturbed (1.0×), or structural undersupply (1.1×) — applied uniformly.

See METHODOLOGY §9 (open methodology decisions) and §3.2 (dividend strip / terminal value construction).
