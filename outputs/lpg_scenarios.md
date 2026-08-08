# LPG — Scenario Fair Value (LPG Set A (US-export-arb))

- **Current price:** $45.76
- **Analyst target:** $54.00
- **NAV / share (reference, unflexed):** $35.69 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $31.82 (-30.5% vs price)
- **Breakeven TCE (scenario-invariant):** $223,619/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Arb wide (US-export bull) | 15% | 1.13× | $39.86 | $38.58 | $37.90–$39.26 | 1.61× | 0.70 | $35.59 | $64,500 | 0.29× |
| Absorption base | 35% | 1.00× | $35.69 | $33.82 | $33.10–$34.55 | 1.31× | 0.60 | $31.02 | $52,500 | 0.23× |
| Orderbook overhang | 35% | 0.89× | $32.13 | $29.60 | $28.88–$30.31 | 1.10× | 0.50 | $27.06 | $44,000 | 0.20× |
| Arb collapse | 15% | 0.79× | $28.88 | $25.61 | $25.08–$26.14 | 0.86× | 0.50 | $22.33 | $34,500 | 0.15× |
| **Probability-weighted** | | | | **$31.82** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-7.18
- **Downside (worst scenario − price):** $-20.15
- **Expected value vs current** (weighted FV − price): $-13.94 (-30.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
