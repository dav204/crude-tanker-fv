# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.34
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $4.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.99 (+12.2% vs price)
- **Breakeven TCE (scenario-invariant):** $181,776/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $10.56 | $11.90 | $11.57–$12.28 | 8.44× | 0.70 | $15.04 | $337,500 | 1.86× |
| Pre-MoU baseline | 45% | 1.11× | $7.09 | $7.99 | $7.79–$8.22 | 4.74× | 0.70 | $10.08 | $189,500 | 1.04× |
| MoU base case | 18% | 0.74× | $-2.03 | $-1.46 | $-1.55–$-1.37 | 2.12× | 0.70 | $-0.11 | $84,875 | 0.47× |
| MoU bear | 12% | 0.70× | $-3.19 | $-2.63 | $-2.71–$-2.55 | 1.63× | 0.70 | $-1.30 | $65,250 | 0.36× |
| **Probability-weighted** | | | | **$5.99** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.56
- **Downside (worst scenario − price):** $-7.97
- **Expected value vs current** (weighted FV − price): $+0.65 (+12.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
