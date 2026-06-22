# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $74.45
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.47 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $79.56 (+6.9% vs price)
- **Breakeven TCE (scenario-invariant):** $41,889/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $88.95 | $94.73 | $92.10–$97.76 | 4.23× | 0.70 | $108.22 | $134,435 | 3.21× |
| Pre-MoU baseline | 45% | 1.04× | $79.37 | $81.74 | $80.04–$83.62 | 2.82× | 0.70 | $87.29 | $89,207 | 2.13× |
| MoU base case | 18% | 0.75× | $66.16 | $64.55 | $63.22–$65.87 | 1.41× | 0.60 | $62.13 | $44,890 | 1.07× |
| MoU bear | 12% | 0.72× | $64.56 | $62.27 | $61.16–$63.38 | 1.20× | 0.60 | $58.84 | $38,241 | 0.91× |
| **Probability-weighted** | | | | **$79.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+20.28
- **Downside (worst scenario − price):** $-12.18
- **Expected value vs current** (weighted FV − price): $+5.11 (+6.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
