# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.03
- **Analyst target:** $4.56
- **NAV / share (reference, unflexed):** $4.92 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.35 (+6.5% vs price)
- **Breakeven TCE (scenario-invariant):** $201,672/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $7.71 | $8.54 | $8.22–$8.92 | 8.44× | 0.70 | $10.48 | $337,500 | 1.67× |
| Pre-MoU baseline | 59% | 0.98× | $4.66 | $4.48 | $4.37–$4.60 | 2.65× | 0.70 | $4.06 | $106,100 | 0.53× |
| MoU base case | 0% | 0.87× | $3.45 | $3.22 | $3.13–$3.30 | 2.12× | 0.70 | $2.68 | $84,875 | 0.42× |
| MoU bear | 13% | 0.80× | $2.66 | $2.43 | $2.36–$2.51 | 1.63× | 0.70 | $1.90 | $65,250 | 0.32× |
| **Probability-weighted** | | | | **$5.35** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.52
- **Downside (worst scenario − price):** $-2.59
- **Expected value vs current** (weighted FV − price): $+0.33 (+6.5%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
