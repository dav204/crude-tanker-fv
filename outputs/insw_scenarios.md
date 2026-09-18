# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.0% of vessel value) + product sleeve (35.0%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $111.21
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $54.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $61.81 (-44.4% vs price)
- **Breakeven TCE (scenario-invariant):** $636,044/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $68.10 | $80.41 | $76.43–$85.01 | 6.17× | 0.70 | $109.14 | $169,742 | 0.27× |
| Pre-MoU baseline | 59% | 1.00× | $59.35 | $61.53 | $59.46–$63.79 | 2.51× | 0.70 | $66.60 | $73,976 | 0.12× |
| MoU base case | 0% | 0.90× | $49.45 | $49.36 | $47.59–$51.21 | 2.06× | 0.70 | $49.55 | $54,492 | 0.09× |
| MoU bear | 13% | 0.80× | $44.38 | $42.87 | $41.42–$44.41 | 1.50× | 0.70 | $40.59 | $40,244 | 0.06× |
| **Probability-weighted** | | | | **$61.81** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-30.80
- **Downside (worst scenario − price):** $-70.89
- **Expected value vs current** (weighted FV − price): $-49.40 (-44.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.0% | $72.24 | $41.42 | -42.7% | TRIM/SHORT |
| Product | 35.0% | $38.97 | $20.39 | -47.7% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$111.21** | **$61.81** | **-44.4%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
