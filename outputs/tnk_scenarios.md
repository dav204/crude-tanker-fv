# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $70.72
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.51 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.18 (+3.5% vs price)
- **Breakeven TCE (scenario-invariant):** $9,573/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $89.00 | $94.77 | $92.14–$97.79 | 4.23× | 0.70 | $108.24 | $134,591 | 14.06× |
| Pre-MoU baseline | 45% | 0.80× | $68.43 | $67.54 | $66.43–$68.70 | 1.66× | 0.70 | $65.45 | $52,704 | 5.51× |
| MoU base case | 18% | 0.75× | $66.19 | $64.57 | $63.24–$65.89 | 1.41× | 0.60 | $62.14 | $44,921 | 4.69× |
| MoU bear | 12% | 0.72× | $64.58 | $62.29 | $61.18–$63.40 | 1.20× | 0.60 | $58.86 | $38,261 | 4.00× |
| **Probability-weighted** | | | | **$73.18** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+24.05
- **Downside (worst scenario − price):** $-8.43
- **Expected value vs current** (weighted FV − price): $+2.46 (+3.5%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
