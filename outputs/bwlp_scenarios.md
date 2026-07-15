# BWLP — Scenario Fair Value (LPG Set A (US-export-arb))

- **Current price:** $21.16
- **Analyst target:** $17.52
- **NAV / share (reference, unflexed):** $15.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.46 (-31.6% vs price)
- **Breakeven TCE (scenario-invariant):** $186,184/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Arb wide (US-export bull) | 15% | 1.13× | $18.34 | $18.27 | $17.85–$18.69 | 1.61× | 0.70 | $18.11 | $64,500 | 0.35× |
| Absorption base | 35% | 1.00× | $15.80 | $15.60 | $15.15–$16.05 | 1.31× | 0.60 | $15.30 | $52,500 | 0.28× |
| Orderbook overhang | 35% | 0.89× | $13.64 | $13.26 | $12.81–$13.70 | 1.10× | 0.50 | $12.87 | $44,000 | 0.24× |
| Arb collapse | 15% | 0.79× | $11.67 | $10.82 | $10.48–$11.15 | 0.86× | 0.50 | $9.96 | $34,500 | 0.19× |
| **Probability-weighted** | | | | **$14.46** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-2.88
- **Downside (worst scenario − price):** $-10.34
- **Expected value vs current** (weighted FV − price): $-6.69 (-31.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
