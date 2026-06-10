# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.20
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $26.19 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.64 (-5.7% vs price)
- **Breakeven TCE (scenario-invariant):** $28,969/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.19× | $32.30 | $32.63 | $31.86–$33.41 | 1.80× | 0.70 | $33.42 | $31,512 | 1.09× |
| Moderate growth (base) | 40% | 1.02× | $26.77 | $26.27 | $25.48–$27.05 | 1.36× | 0.60 | $25.52 | $23,603 | 0.81× |
| China property drag | 25% | 0.93× | $23.92 | $22.86 | $22.00–$23.72 | 1.14× | 0.50 | $21.80 | $19,194 | 0.66× |
| Coordinated slowdown | 15% | 0.84× | $21.07 | $19.27 | $18.59–$19.94 | 0.96× | 0.50 | $17.46 | $16,359 | 0.56× |
| **Probability-weighted** | | | | **$25.64** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.43
- **Downside (worst scenario − price):** $-7.93
- **Expected value vs current** (weighted FV − price): $-1.56 (-5.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
