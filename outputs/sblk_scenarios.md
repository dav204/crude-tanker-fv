# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.81
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $26.57 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.76 (-0.2% vs price)
- **Breakeven TCE (scenario-invariant):** $22,755/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.19× | $32.74 | $32.39 | $31.58–$33.19 | 1.80× | 0.70 | $31.56 | $31,385 | 1.38× |
| Moderate growth (base) | 40% | 1.02× | $27.15 | $26.28 | $25.46–$27.11 | 1.36× | 0.60 | $24.98 | $23,516 | 1.03× |
| China property drag | 25% | 0.93× | $24.29 | $23.31 | $22.41–$24.21 | 1.14× | 0.50 | $22.33 | $19,146 | 0.84× |
| Coordinated slowdown | 15% | 0.84× | $21.40 | $19.63 | $18.92–$20.33 | 0.96× | 0.50 | $17.85 | $16,311 | 0.72× |
| **Probability-weighted** | | | | **$25.76** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.58
- **Downside (worst scenario − price):** $-6.18
- **Expected value vs current** (weighted FV − price): $-0.05 (-0.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
