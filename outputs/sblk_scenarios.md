# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.15
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $26.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.72 (-5.3% vs price)
- **Breakeven TCE (scenario-invariant):** $28,367/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.19× | $32.38 | $32.72 | $31.95–$33.49 | 1.80× | 0.70 | $33.51 | $31,462 | 1.11× |
| Moderate growth (base) | 40% | 1.02× | $26.85 | $26.35 | $25.56–$27.13 | 1.36× | 0.60 | $25.60 | $23,569 | 0.83× |
| China property drag | 25% | 0.93× | $24.00 | $22.94 | $22.08–$23.80 | 1.14× | 0.50 | $21.88 | $19,176 | 0.68× |
| Coordinated slowdown | 15% | 0.84× | $21.14 | $19.34 | $18.66–$20.01 | 0.96× | 0.50 | $17.53 | $16,340 | 0.58× |
| **Probability-weighted** | | | | **$25.72** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.57
- **Downside (worst scenario − price):** $-7.81
- **Expected value vs current** (weighted FV − price): $-1.43 (-5.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
