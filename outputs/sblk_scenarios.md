# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.90
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.04 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $30.00 (+3.8% vs price)
- **Breakeven TCE (scenario-invariant):** $11,492/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $37.56 | $37.04 | $36.17–$37.91 | 1.81× | 0.70 | $35.83 | $30,480 | 2.65× |
| Moderate growth (base) | 40% | 0.96× | $31.65 | $30.52 | $29.63–$31.41 | 1.37× | 0.60 | $28.83 | $22,886 | 1.99× |
| China property drag | 25% | 0.89× | $28.76 | $27.46 | $26.48–$28.43 | 1.16× | 0.50 | $26.16 | $18,793 | 1.64× |
| Coordinated slowdown | 15% | 0.81× | $25.62 | $23.45 | $22.69–$24.21 | 0.97× | 0.50 | $21.28 | $15,962 | 1.39× |
| **Probability-weighted** | | | | **$30.00** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.14
- **Downside (worst scenario − price):** $-5.45
- **Expected value vs current** (weighted FV − price): $+1.10 (+3.8%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
