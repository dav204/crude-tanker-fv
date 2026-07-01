# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.31
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.47 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.97 (+58.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.16× | $13.24 | $12.84 | $12.67–$13.01 | 1.96× | 0.70 | $11.90 | $26,798 | 67314717301970895342290337792.00× |
| Moderate growth (base) | 40% | 0.99× | $10.36 | $10.08 | $9.91–$10.24 | 1.49× | 0.60 | $9.66 | $20,277 | 50934954774002193068575424512.00× |
| China property drag | 25% | 0.93× | $9.32 | $9.00 | $8.85–$9.14 | 1.29× | 0.60 | $8.51 | $17,256 | 43347065341715046635153653760.00× |
| Coordinated slowdown | 15% | 0.83× | $7.64 | $7.49 | $7.35–$7.63 | 1.08× | 0.50 | $7.34 | $14,506 | 36439165052250964533182464000.00× |
| **Probability-weighted** | | | | **$9.97** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.53
- **Downside (worst scenario − price):** $+1.18
- **Expected value vs current** (weighted FV − price): $+3.66 (+58.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
