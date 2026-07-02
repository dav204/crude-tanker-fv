# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.0%) + dry_bulk (72.7%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.05
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.87 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.34 (-5.0% vs price)
- **Breakeven TCE (scenario-invariant):** $40,799/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $21.28 | $21.51 | $20.81–$22.26 | 6.38× | 0.70 | $22.04 | $82,455 | 2.02× |
| Pre-MoU baseline | 20% | 0.82× | $14.81 | $13.88 | $13.39–$14.38 | 2.26× | 0.70 | $12.47 | $41,369 | 1.01× |
| MoU base case | 45% | 0.76× | $12.04 | $10.85 | $10.38–$11.31 | 1.86× | 0.70 | $9.55 | $32,695 | 0.80× |
| MoU bear | 25% | 0.72× | $10.31 | $8.87 | $8.49–$9.25 | 1.53× | 0.70 | $7.25 | $27,948 | 0.69× |
| **Probability-weighted** | | | | **$13.34** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.46
- **Downside (worst scenario − price):** $-5.18
- **Expected value vs current** (weighted FV − price): $-0.71 (-5.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
