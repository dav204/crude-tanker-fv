# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.0%) + dry_bulk (72.7%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.05
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.87 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.56 (+10.7% vs price)
- **Breakeven TCE (scenario-invariant):** $40,799/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.91 | $22.07 | $21.36–$22.82 | 6.38× | 0.70 | $22.43 | $82,455 | 2.02× |
| Pre-MoU baseline | 45% | 1.11× | $17.15 | $16.56 | $15.99–$17.16 | 4.00× | 0.70 | $16.01 | $54,989 | 1.35× |
| MoU base case | 18% | 0.76× | $12.40 | $11.15 | $10.69–$11.61 | 1.86× | 0.70 | $9.80 | $32,695 | 0.80× |
| MoU bear | 12% | 0.72× | $10.60 | $9.11 | $8.73–$9.49 | 1.53× | 0.70 | $7.45 | $27,948 | 0.69× |
| **Probability-weighted** | | | | **$15.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.02
- **Downside (worst scenario − price):** $-4.94
- **Expected value vs current** (weighted FV − price): $+1.51 (+10.7%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
