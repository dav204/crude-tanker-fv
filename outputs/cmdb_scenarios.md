# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $18.23
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.13 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.11 (+10.3% vs price)
- **Breakeven TCE (scenario-invariant):** $4,628/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $35.44 | $23.95 | $23.44–$24.45 | 1.75× | 0.70 | $21.94 | $29,267 | 6.32× |
| Moderate growth (base) | 40% | 0.97× | $31.28 | $20.43 | $19.91–$20.94 | 1.33× | 0.60 | $18.22 | $22,080 | 4.77× |
| China property drag | 25% | 0.90× | $29.29 | $18.67 | $18.10–$19.25 | 1.14× | 0.50 | $16.84 | $18,393 | 3.97× |
| Coordinated slowdown | 15% | 0.82× | $26.97 | $16.51 | $16.06–$16.96 | 0.95× | 0.50 | $14.14 | $15,526 | 3.35× |
| **Probability-weighted** | | | | **$20.11** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.72
- **Downside (worst scenario − price):** $-1.72
- **Expected value vs current** (weighted FV − price): $+1.88 (+10.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
