# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.4% of vessel value) + product sleeve (34.6%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Per-sleeve FVs flow through the same scenario set (METHODOLOGY 6 v2).

- **Current price:** $76.59
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $61.34 (-19.9% vs price)
- **Breakeven TCE (scenario-invariant):** $252,764/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $65.76 | $77.87 | $73.97–$82.38 | 6.14× | 0.70 | $106.13 | $167,398 | 0.66× |
| Pre-MoU baseline | 45% | 1.09× | $60.37 | $65.86 | $63.44–$68.59 | 3.78× | 0.70 | $78.67 | $102,372 | 0.41× |
| MoU base case | 18% | 0.75× | $42.54 | $42.30 | $40.72–$43.96 | 1.77× | 0.70 | $42.17 | $48,249 | 0.19× |
| MoU bear | 12% | 0.71× | $39.55 | $38.53 | $36.88–$40.27 | 1.45× | 0.60 | $37.49 | $38,938 | 0.15× |
| **Probability-weighted** | | | | **$61.34** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.28
- **Downside (worst scenario − price):** $-38.06
- **Expected value vs current** (weighted FV − price): $-15.25 (-19.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.4% | $50.11 | $40.41 | -19.4% | TRIM/SHORT |
| Product | 34.6% | $26.48 | $19.78 | -25.3% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$76.59** | **$61.34** | **-19.9%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
