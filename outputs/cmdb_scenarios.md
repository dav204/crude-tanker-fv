# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.80
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.43 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.27 (+13.9% vs price)
- **Breakeven TCE (scenario-invariant):** $930/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $35.77 | $24.15 | $23.64–$24.65 | 1.75× | 0.70 | $22.06 | $29,191 | 31.40× |
| Moderate growth (base) | 40% | 0.97× | $31.57 | $20.60 | $20.08–$21.11 | 1.33× | 0.60 | $18.34 | $22,028 | 23.69× |
| China property drag | 25% | 0.90× | $29.57 | $18.83 | $18.26–$19.41 | 1.14× | 0.50 | $16.96 | $18,366 | 19.75× |
| Coordinated slowdown | 15% | 0.82× | $27.22 | $16.65 | $16.20–$17.10 | 0.95× | 0.50 | $14.25 | $15,497 | 16.67× |
| **Probability-weighted** | | | | **$20.27** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.35
- **Downside (worst scenario − price):** $-1.15
- **Expected value vs current** (weighted FV − price): $+2.47 (+13.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
