# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (68.4% of vessel value) + product sleeve (31.6%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Per-sleeve FVs flow through the same scenario set (METHODOLOGY 6 v2).

- **Current price:** $78.00
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $57.91 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $52.08 (-33.2% vs price)
- **Breakeven TCE (scenario-invariant):** $303,978/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $72.40 | $80.33 | $77.49–$83.60 | 6.21× | 0.70 | $98.81 | $173,879 | 0.57× |
| Pre-MoU baseline | 15% | 1.09× | $65.94 | $69.11 | $67.37–$71.08 | 3.74× | 0.70 | $76.50 | $103,739 | 0.34× |
| MoU base case | 50% | 0.75× | $47.22 | $46.70 | $45.61–$47.81 | 1.79× | 0.70 | $45.49 | $51,090 | 0.17× |
| MoU bear | 25% | 0.70× | $43.13 | $41.31 | $40.13–$42.55 | 1.36× | 0.60 | $39.04 | $37,841 | 0.12× |
| **Probability-weighted** | | | | **$52.08** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.33
- **Downside (worst scenario − price):** $-36.69
- **Expected value vs current** (weighted FV − price): $-25.92 (-33.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 68.4% | $53.32 | $34.47 | -35.4% | TRIM/SHORT |
| Product | 31.6% | $24.68 | $18.88 | -23.5% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$78.00** | **$52.08** | **-33.2%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
