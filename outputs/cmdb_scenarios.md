# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $18.84
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.47 (+8.6% vs price)
- **Breakeven TCE (scenario-invariant):** $8,510/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.14× | $36.13 | $24.41 | $23.90–$24.91 | 1.75× | 0.70 | $22.35 | $29,484 | 3.46× |
| Moderate growth (base) | 40% | 0.99× | $31.83 | $20.80 | $20.28–$21.32 | 1.33× | 0.60 | $18.57 | $22,229 | 2.61× |
| China property drag | 25% | 0.92× | $29.76 | $18.99 | $18.41–$19.57 | 1.14× | 0.50 | $17.15 | $18,474 | 2.17× |
| Coordinated slowdown | 15% | 0.83× | $27.38 | $16.79 | $16.34–$17.24 | 0.95× | 0.50 | $14.41 | $15,607 | 1.83× |
| **Probability-weighted** | | | | **$20.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.57
- **Downside (worst scenario − price):** $-2.05
- **Expected value vs current** (weighted FV − price): $+1.63 (+8.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
