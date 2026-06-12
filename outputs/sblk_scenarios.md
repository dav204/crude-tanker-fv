# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.15
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $26.57 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.98 (-4.3% vs price)
- **Breakeven TCE (scenario-invariant):** $27,187/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.19× | $32.74 | $33.04 | $32.26–$33.81 | 1.80× | 0.70 | $33.73 | $31,385 | 1.15× |
| Moderate growth (base) | 40% | 1.02× | $27.15 | $26.61 | $25.82–$27.39 | 1.36× | 0.60 | $25.79 | $23,516 | 0.86× |
| China property drag | 25% | 0.93× | $24.29 | $23.18 | $22.31–$24.04 | 1.14× | 0.50 | $22.06 | $19,146 | 0.70× |
| Coordinated slowdown | 15% | 0.84× | $21.40 | $19.55 | $18.87–$20.22 | 0.96× | 0.50 | $17.69 | $16,311 | 0.60× |
| **Probability-weighted** | | | | **$25.98** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.89
- **Downside (worst scenario − price):** $-7.60
- **Expected value vs current** (weighted FV − price): $-1.17 (-4.3%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
