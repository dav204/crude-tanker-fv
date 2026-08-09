# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $28.90
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $32.78 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.79 (+3.1% vs price)
- **Breakeven TCE (scenario-invariant):** $12,307/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $37.27 | $36.79 | $35.92–$37.67 | 1.81× | 0.70 | $35.67 | $30,537 | 2.48× |
| Moderate growth (base) | 40% | 0.96× | $31.40 | $30.31 | $29.42–$31.20 | 1.37× | 0.60 | $28.67 | $22,925 | 1.86× |
| China property drag | 25% | 0.89× | $28.52 | $27.26 | $26.29–$28.23 | 1.16× | 0.50 | $26.00 | $18,813 | 1.53× |
| Coordinated slowdown | 15% | 0.81× | $25.40 | $23.27 | $22.51–$24.03 | 0.97× | 0.50 | $21.14 | $15,984 | 1.30× |
| **Probability-weighted** | | | | **$29.79** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.89
- **Downside (worst scenario − price):** $-5.63
- **Expected value vs current** (weighted FV − price): $+0.89 (+3.1%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
