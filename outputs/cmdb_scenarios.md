# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $19.94
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $31.33 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.10 (+0.8% vs price)
- **Breakeven TCE (scenario-invariant):** $18,395/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $35.43 | $23.98 | $23.48–$24.49 | 1.75× | 0.70 | $22.07 | $29,570 | 1.61× |
| Moderate growth (base) | 40% | 1.00× | $31.20 | $20.43 | $19.90–$20.94 | 1.33× | 0.60 | $18.30 | $22,287 | 1.21× |
| China property drag | 25% | 0.92× | $29.15 | $18.65 | $18.07–$19.22 | 1.14× | 0.50 | $16.88 | $18,504 | 1.01× |
| Coordinated slowdown | 15% | 0.83× | $26.82 | $16.47 | $16.02–$16.92 | 0.95× | 0.50 | $14.16 | $15,639 | 0.85× |
| **Probability-weighted** | | | | **$20.10** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.04
- **Downside (worst scenario − price):** $-3.47
- **Expected value vs current** (weighted FV − price): $+0.16 (+0.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
