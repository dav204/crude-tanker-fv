# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.3% of vessel value) + product sleeve (34.7%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $96.13
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $54.46 (-43.3% vs price)
- **Breakeven TCE (scenario-invariant):** $408,978/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $65.62 | $77.73 | $73.83–$82.24 | 6.11× | 0.70 | $106.01 | $166,090 | 0.41× |
| Pre-MoU baseline | 57% | 0.82× | $50.70 | $52.49 | $50.67–$54.49 | 2.15× | 0.70 | $56.67 | $65,383 | 0.16× |
| MoU base case | 5% | 0.75× | $42.46 | $42.23 | $40.65–$43.89 | 1.77× | 0.70 | $42.10 | $47,986 | 0.12× |
| MoU bear | 13% | 0.71× | $39.49 | $38.47 | $36.81–$40.20 | 1.45× | 0.60 | $37.42 | $38,757 | 0.09× |
| **Probability-weighted** | | | | **$54.46** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-18.40
- **Downside (worst scenario − price):** $-60.13
- **Expected value vs current** (weighted FV − price): $-41.67 (-43.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.3% | $62.79 | $34.66 | -44.8% | TRIM/SHORT |
| Product | 34.7% | $33.34 | $19.80 | -40.6% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$96.13** | **$54.46** | **-43.3%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
