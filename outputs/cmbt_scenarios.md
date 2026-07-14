# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.0%) + dry_bulk (72.7%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $15.44
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.87 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.87 (-10.2% vs price)
- **Breakeven TCE (scenario-invariant):** $73,724/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $20.82 | $21.10 | $20.40–$21.86 | 6.38× | 0.70 | $21.75 | $82,455 | 1.12× |
| Pre-MoU baseline | 45% | 0.82× | $14.48 | $13.59 | $13.10–$14.09 | 2.26× | 0.70 | $12.25 | $41,369 | 0.56× |
| MoU base case | 18% | 0.76× | $11.78 | $10.63 | $10.16–$11.09 | 1.86× | 0.70 | $9.37 | $32,695 | 0.44× |
| MoU bear | 12% | 0.72× | $10.10 | $8.69 | $8.31–$9.07 | 1.53× | 0.70 | $7.10 | $27,948 | 0.38× |
| **Probability-weighted** | | | | **$13.87** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.66
- **Downside (worst scenario − price):** $-6.75
- **Expected value vs current** (weighted FV − price): $-1.57 (-10.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
