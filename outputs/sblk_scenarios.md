# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $30.48
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $32.88 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.74 (-5.7% vs price)
- **Breakeven TCE (scenario-invariant):** $17,725/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.07× | $35.61 | $35.32 | $34.44–$36.19 | 1.81× | 0.70 | $34.63 | $30,520 | 1.72× |
| Moderate growth (base) | 40% | 0.93× | $30.16 | $29.24 | $28.35–$30.13 | 1.37× | 0.60 | $27.86 | $22,913 | 1.29× |
| China property drag | 25% | 0.86× | $27.49 | $26.39 | $25.41–$27.36 | 1.16× | 0.50 | $25.29 | $18,806 | 1.06× |
| Coordinated slowdown | 15% | 0.79× | $24.59 | $22.59 | $21.83–$23.35 | 0.97× | 0.50 | $20.58 | $15,977 | 0.90× |
| **Probability-weighted** | | | | **$28.74** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.84
- **Downside (worst scenario − price):** $-7.89
- **Expected value vs current** (weighted FV − price): $-1.74 (-5.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
