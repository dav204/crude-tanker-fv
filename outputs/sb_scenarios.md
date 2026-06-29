# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.39
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $9.82 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.35 (+46.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.17× | $12.02 | $11.66 | $11.51–$11.82 | 1.96× | 0.70 | $10.83 | $27,782 | 68034519245570886423585751040.00× |
| Moderate growth (base) | 40% | 1.00× | $9.78 | $9.46 | $9.31–$9.60 | 1.48× | 0.60 | $8.97 | $20,956 | 51320091539688304436410580992.00× |
| China property drag | 25% | 0.93× | $8.91 | $8.53 | $8.41–$8.66 | 1.28× | 0.60 | $7.97 | $17,631 | 43176801456741777026838429696.00× |
| Coordinated slowdown | 15% | 0.83× | $7.64 | $7.34 | $7.22–$7.46 | 1.07× | 0.50 | $7.04 | $14,881 | 36442336181577732259558981632.00× |
| **Probability-weighted** | | | | **$9.35** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.27
- **Downside (worst scenario − price):** $+0.95
- **Expected value vs current** (weighted FV − price): $+2.96 (+46.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
