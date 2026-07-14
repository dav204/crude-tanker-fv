# FLNG — Scenario Fair Value (LNG glut-cycle framework)

- **Current price:** $30.14
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $28.45 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.19 (-3.2% vs price)
- **Breakeven TCE (scenario-invariant):** $169,874/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Tight resurgence | 15% | 1.25× | $41.93 | $39.36 | $39.12–$39.65 | 1.74× | 0.70 | $33.37 | $147,500 | 0.87× |
| Moderate tightening | 25% | 1.13× | $35.59 | $33.67 | $33.46–$33.93 | 0.93× | 0.50 | $31.75 | $78,750 | 0.46× |
| Glut base case | 45% | 0.96× | $26.34 | $26.25 | $26.06–$26.47 | 0.68× | 0.40 | $26.19 | $58,000 | 0.34× |
| Glut intensifies | 15% | 0.84× | $19.84 | $20.36 | $20.20–$20.55 | 0.51× | 0.40 | $20.71 | $43,250 | 0.25× |
| Structural reset | 0% | 0.72× | $13.60 | $16.11 | $15.93–$16.30 | 0.48× | 0.30 | $17.19 | $40,500 | 0.24× |
| **Probability-weighted** | | | | **$29.19** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.22
- **Downside (worst scenario − price):** $-14.03
- **Expected value vs current** (weighted FV − price): $-0.95 (-3.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
