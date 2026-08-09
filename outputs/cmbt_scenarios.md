# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.0%) + containerships (3.2%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $16.29
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.46 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.86 (-14.9% vs price)
- **Breakeven TCE (scenario-invariant):** $79,939/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $20.53 | $20.88 | $20.18–$21.64 | 6.38× | 0.70 | $21.70 | $82,119 | 1.03× |
| Pre-MoU baseline | 57% | 0.82× | $14.32 | $13.49 | $13.00–$13.99 | 2.26× | 0.70 | $12.26 | $41,233 | 0.52× |
| MoU base case | 5% | 0.76× | $11.73 | $10.63 | $10.17–$11.09 | 1.86× | 0.70 | $9.44 | $32,588 | 0.41× |
| MoU bear | 13% | 0.72× | $10.11 | $8.75 | $8.37–$9.13 | 1.53× | 0.70 | $7.21 | $27,852 | 0.35× |
| **Probability-weighted** | | | | **$13.86** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.59
- **Downside (worst scenario − price):** $-7.54
- **Expected value vs current** (weighted FV − price): $-2.43 (-14.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
