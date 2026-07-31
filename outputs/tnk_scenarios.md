# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $79.95
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.73 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.69 (-7.8% vs price)
- **Breakeven TCE (scenario-invariant):** $87,258/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $89.27 | $95.01 | $92.38–$98.03 | 4.23× | 0.70 | $108.40 | $134,380 | 1.54× |
| Pre-MoU baseline | 57% | 0.80× | $68.61 | $67.69 | $66.59–$68.86 | 1.66× | 0.70 | $65.55 | $52,654 | 0.60× |
| MoU base case | 5% | 0.75× | $66.36 | $64.71 | $63.38–$66.04 | 1.41× | 0.60 | $62.24 | $44,880 | 0.51× |
| MoU bear | 13% | 0.72× | $64.75 | $62.43 | $61.32–$63.54 | 1.20× | 0.60 | $58.96 | $38,239 | 0.44× |
| **Probability-weighted** | | | | **$73.69** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+15.05
- **Downside (worst scenario − price):** $-17.53
- **Expected value vs current** (weighted FV − price): $-6.27 (-7.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
