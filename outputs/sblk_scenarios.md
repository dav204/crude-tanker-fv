# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.14
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $30.13 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.19 (+0.2% vs price)
- **Breakeven TCE (scenario-invariant):** $18,761/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $35.63 | $35.21 | $34.35–$36.06 | 1.81× | 0.70 | $34.21 | $30,527 | 1.63× |
| Moderate growth (base) | 40% | 0.99× | $29.66 | $28.70 | $27.83–$29.56 | 1.37× | 0.60 | $27.25 | $22,918 | 1.22× |
| China property drag | 25% | 0.91× | $26.74 | $25.67 | $24.72–$26.62 | 1.16× | 0.50 | $24.60 | $18,809 | 1.00× |
| Coordinated slowdown | 15% | 0.82× | $23.57 | $21.66 | $20.92–$22.40 | 0.97× | 0.50 | $19.75 | $15,980 | 0.85× |
| **Probability-weighted** | | | | **$28.19** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.07
- **Downside (worst scenario − price):** $-6.48
- **Expected value vs current** (weighted FV − price): $+0.05 (+0.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
