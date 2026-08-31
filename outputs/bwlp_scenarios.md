# BWLP — Scenario Fair Value (LPG Set A (US-export-arb))

- **Current price:** $24.05
- **Analyst target:** $17.52
- **NAV / share (reference, unflexed):** $15.83 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.52 (-39.6% vs price)
- **Breakeven TCE (scenario-invariant):** $252,777/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Arb wide (US-export bull) | 15% | 1.13× | $18.32 | $18.28 | $17.85–$18.70 | 1.61× | 0.70 | $18.16 | $64,500 | 0.26× |
| Absorption base | 35% | 1.00× | $15.83 | $15.65 | $15.20–$16.10 | 1.31× | 0.60 | $15.37 | $52,500 | 0.21× |
| Orderbook overhang | 35% | 0.89× | $13.71 | $13.33 | $12.89–$13.77 | 1.10× | 0.50 | $12.95 | $44,000 | 0.17× |
| Arb collapse | 15% | 0.79× | $11.77 | $10.92 | $10.59–$11.25 | 0.86× | 0.50 | $10.07 | $34,500 | 0.14× |
| **Probability-weighted** | | | | **$14.52** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-5.77
- **Downside (worst scenario − price):** $-13.13
- **Expected value vs current** (weighted FV − price): $-9.53 (-39.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
