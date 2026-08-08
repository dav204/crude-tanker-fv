# LPG — Scenario Fair Value (LPG Set A (US-export-arb))

- **Current price:** $45.76
- **Analyst target:** $54.00
- **NAV / share (reference, unflexed):** $34.11 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $30.55 (-33.2% vs price)
- **Breakeven TCE (scenario-invariant):** $206,288/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Arb wide (US-export bull) | 15% | 1.13× | $39.26 | $38.50 | $37.67–$39.33 | 1.61× | 0.70 | $36.72 | $64,500 | 0.31× |
| Absorption base | 35% | 1.00× | $34.11 | $32.91 | $32.02–$33.80 | 1.31× | 0.60 | $31.11 | $52,500 | 0.25× |
| Orderbook overhang | 35% | 0.89× | $29.71 | $27.98 | $27.11–$28.86 | 1.10× | 0.50 | $26.25 | $44,000 | 0.21× |
| Arb collapse | 15% | 0.79× | $25.70 | $23.06 | $22.42–$23.72 | 0.86× | 0.50 | $20.43 | $34,500 | 0.17× |
| **Probability-weighted** | | | | **$30.55** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-7.26
- **Downside (worst scenario − price):** $-22.70
- **Expected value vs current** (weighted FV − price): $-15.21 (-33.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
