# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.39
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.14 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $9.52 (+49.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.17× | $12.38 | $12.14 | $11.86–$12.41 | 1.96× | 0.70 | $11.56 | $27,680 | 67961705704616153188594089984.00× |
| Moderate growth (base) | 40% | 1.00× | $10.09 | $9.65 | $9.38–$9.92 | 1.49× | 0.60 | $8.99 | $20,886 | 51281131973225890214005702656.00× |
| China property drag | 25% | 0.93× | $9.20 | $8.65 | $8.41–$8.88 | 1.28× | 0.60 | $7.81 | $17,592 | 43194024967280813649931796480.00× |
| Coordinated slowdown | 15% | 0.83× | $7.90 | $7.16 | $6.93–$7.38 | 1.07× | 0.50 | $6.41 | $14,842 | 36442015397288170954281713664.00× |
| **Probability-weighted** | | | | **$9.52** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.75
- **Downside (worst scenario − price):** $+0.77
- **Expected value vs current** (weighted FV − price): $+3.13 (+49.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
