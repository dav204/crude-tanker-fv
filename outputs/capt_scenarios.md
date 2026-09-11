# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $18.41
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $17.32 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.77 (-3.5% vs price)
- **Breakeven TCE (scenario-invariant):** $230,787/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $25.26 | $25.92 | $25.43–$26.48 | 7.18× | 0.70 | $27.45 | $257,867 | 1.12× |
| Pre-MoU baseline | 59% | 0.95× | $15.84 | $15.51 | $15.32–$15.71 | 2.36× | 0.70 | $14.75 | $84,322 | 0.37× |
| MoU base case | 0% | 0.86× | $12.75 | $12.50 | $12.33–$12.67 | 1.93× | 0.70 | $11.93 | $68,539 | 0.30× |
| MoU bear | 13% | 0.79× | $10.69 | $10.49 | $10.35–$10.62 | 1.51× | 0.70 | $10.01 | $53,686 | 0.23× |
| **Probability-weighted** | | | | **$17.77** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.51
- **Downside (worst scenario − price):** $-7.92
- **Expected value vs current** (weighted FV − price): $-0.64 (-3.5%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
