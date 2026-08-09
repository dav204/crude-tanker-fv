# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.80
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $31.92 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.33 (+14.2% vs price)
- **Breakeven TCE (scenario-invariant):** $2,798/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.14× | $35.95 | $24.27 | $23.76–$24.77 | 1.75× | 0.70 | $22.17 | $29,249 | 10.45× |
| Moderate growth (base) | 40% | 0.99× | $31.66 | $20.66 | $20.14–$21.17 | 1.33× | 0.60 | $18.40 | $22,070 | 7.89× |
| China property drag | 25% | 0.92× | $29.60 | $18.86 | $18.28–$19.44 | 1.14× | 0.50 | $17.00 | $18,392 | 6.57× |
| Coordinated slowdown | 15% | 0.83× | $27.19 | $16.65 | $16.20–$17.09 | 0.95× | 0.50 | $14.26 | $15,521 | 5.55× |
| **Probability-weighted** | | | | **$20.33** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.47
- **Downside (worst scenario − price):** $-1.15
- **Expected value vs current** (weighted FV − price): $+2.53 (+14.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
