# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.81
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $29.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.37 (+14.3% vs price)
- **Breakeven TCE (scenario-invariant):** $8,164/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $36.05 | $35.58 | $34.73–$36.44 | 1.81× | 0.70 | $34.51 | $30,572 | 3.74× |
| Moderate growth (base) | 40% | 1.01× | $29.87 | $28.89 | $28.02–$29.75 | 1.37× | 0.60 | $27.42 | $22,948 | 2.81× |
| China property drag | 25% | 0.93× | $26.84 | $25.77 | $24.82–$26.72 | 1.16× | 0.50 | $24.70 | $18,823 | 2.31× |
| Coordinated slowdown | 15% | 0.84× | $23.57 | $21.67 | $20.93–$22.41 | 0.97× | 0.50 | $19.78 | $15,996 | 1.96× |
| **Probability-weighted** | | | | **$28.37** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+10.77
- **Downside (worst scenario − price):** $-3.14
- **Expected value vs current** (weighted FV − price): $+3.56 (+14.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
