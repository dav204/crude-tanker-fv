# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.88
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $29.34 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.19 (+8.9% vs price)
- **Breakeven TCE (scenario-invariant):** $12,503/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $35.76 | $35.33 | $34.48–$36.19 | 1.81× | 0.70 | $34.33 | $30,572 | 2.45× |
| Moderate growth (base) | 40% | 1.01× | $29.66 | $28.71 | $27.84–$29.57 | 1.37× | 0.60 | $27.28 | $22,948 | 1.84× |
| China property drag | 25% | 0.93× | $26.66 | $25.62 | $24.67–$26.57 | 1.16× | 0.50 | $24.58 | $18,823 | 1.51× |
| Coordinated slowdown | 15% | 0.84× | $23.43 | $21.55 | $20.81–$22.29 | 0.97× | 0.50 | $19.68 | $15,996 | 1.28× |
| **Probability-weighted** | | | | **$28.19** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.45
- **Downside (worst scenario − price):** $-4.33
- **Expected value vs current** (weighted FV − price): $+2.31 (+8.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
