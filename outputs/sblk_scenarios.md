# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.40
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $26.91 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $26.07 (+6.9% vs price)
- **Breakeven TCE (scenario-invariant):** $15,583/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.19× | $33.12 | $32.75 | $31.94–$33.55 | 1.80× | 0.70 | $31.88 | $31,269 | 2.01× |
| Moderate growth (base) | 40% | 1.02× | $27.48 | $26.60 | $25.77–$27.42 | 1.36× | 0.60 | $25.27 | $23,435 | 1.50× |
| China property drag | 25% | 0.93× | $24.61 | $23.61 | $22.71–$24.52 | 1.14× | 0.50 | $22.62 | $19,102 | 1.23× |
| Coordinated slowdown | 15% | 0.84× | $21.68 | $19.89 | $19.19–$20.60 | 0.96× | 0.50 | $18.10 | $16,266 | 1.04× |
| **Probability-weighted** | | | | **$26.07** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.35
- **Downside (worst scenario − price):** $-4.51
- **Expected value vs current** (weighted FV − price): $+1.67 (+6.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
