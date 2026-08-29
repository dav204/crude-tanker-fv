# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $4.94
- **Analyst target:** $4.56
- **NAV / share (reference, unflexed):** $4.92 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $5.12 (+3.6% vs price)
- **Breakeven TCE (scenario-invariant):** $203,013/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $7.71 | $8.54 | $8.22–$8.92 | 8.44× | 0.70 | $10.48 | $337,500 | 1.66× |
| Pre-MoU baseline | 62% | 0.96× | $4.49 | $4.33 | $4.21–$4.45 | 2.65× | 0.70 | $3.94 | $106,100 | 0.52× |
| MoU base case | 0% | 0.86× | $3.31 | $3.10 | $3.00–$3.18 | 2.12× | 0.70 | $2.59 | $84,875 | 0.42× |
| MoU bear | 13% | 0.79× | $2.55 | $2.33 | $2.26–$2.41 | 1.63× | 0.70 | $1.83 | $65,250 | 0.32× |
| **Probability-weighted** | | | | **$5.12** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.60
- **Downside (worst scenario − price):** $-2.61
- **Expected value vs current** (weighted FV − price): $+0.18 (+3.6%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
