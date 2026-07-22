# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $26.09
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $30.13 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.35 (+8.7% vs price)
- **Breakeven TCE (scenario-invariant):** $10,780/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $35.88 | $35.43 | $34.58–$36.28 | 1.81× | 0.70 | $34.37 | $30,527 | 2.83× |
| Moderate growth (base) | 40% | 0.99× | $29.85 | $28.86 | $28.00–$29.73 | 1.37× | 0.60 | $27.38 | $22,918 | 2.13× |
| China property drag | 25% | 0.91× | $26.90 | $25.80 | $24.85–$26.75 | 1.16× | 0.50 | $24.71 | $18,809 | 1.74× |
| Coordinated slowdown | 15% | 0.83× | $23.70 | $21.77 | $21.03–$22.51 | 0.97× | 0.50 | $19.84 | $15,980 | 1.48× |
| **Probability-weighted** | | | | **$28.35** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.34
- **Downside (worst scenario − price):** $-4.32
- **Expected value vs current** (weighted FV − price): $+2.26 (+8.7%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
