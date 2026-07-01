# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.31
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.68 (+53.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.16× | $12.83 | $12.49 | $12.32–$12.67 | 1.96× | 0.70 | $11.70 | $26,868 | 67367714328564057539967188992.00× |
| Moderate growth (base) | 40% | 0.99× | $10.01 | $9.79 | $9.61–$9.96 | 1.49× | 0.60 | $9.45 | $20,326 | 50963311329016459630970142720.00× |
| China property drag | 25% | 0.93× | $8.99 | $8.72 | $8.57–$8.86 | 1.29× | 0.60 | $8.31 | $17,283 | 43334529282706018361552142336.00× |
| Coordinated slowdown | 15% | 0.83× | $7.34 | $7.24 | $7.10–$7.38 | 1.08× | 0.50 | $7.14 | $14,533 | 36439398533733974883969269760.00× |
| **Probability-weighted** | | | | **$9.68** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.18
- **Downside (worst scenario − price):** $+0.93
- **Expected value vs current** (weighted FV − price): $+3.37 (+53.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
