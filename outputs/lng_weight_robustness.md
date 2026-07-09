# LNG Weight Robustness Diagnostic — Set B vs Set B-revised

**Purpose** (METHODOLOGY §13): the recurring per-LNG-name weight-
sensitivity diagnostic. Identifies which calls are weight-robust
(small EV% spread across plausible weight sets) vs weight-driven
(call would flip under reasonable alternative weights). Refresh at
the start of each quarterly cycle alongside the refresh checklist.

**Current production lock:** Set B-revised (v3, 2026-06-01).
Comparison reference: Set B (v2, prior lock, same day).

**Lock driver:** Ras Laffan Trains 4 & 6 (12.8 mtpa / ~17% of Qatar LNG) offline through end-summer 2026 at earliest; restart risk from subsurface complications. Partially offsets Cheniere Stage 3 ramp through H2 2026. Empirical pricing: spot $67.5k (+391% YoY), TFDE $98.5k — tight-market levels, not glut levels.

**Weights:**

| Scenario | Set B (v2, prior) | **Set B-revised (v3, current)** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.10 | 0.15 | +0.05 |
| moderate_tightening | 0.15 | 0.25 | +0.10 |
| glut_base | 0.55 | 0.45 | -0.10 |
| glut_intensifies | 0.20 | 0.15 | -0.05 |
| structural_reset | 0.00 | 0.00 | +0.00 |

## FLNG — at price $29.30, target $25.00

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $41.93 | $39.36 | $33.37 | $147,500 |
| moderate_tightening | 1.13× | $35.59 | $33.67 | $31.75 | $78,750 |
| glut_base | 0.96× | $26.34 | $26.25 | $26.19 | $58,000 |
| glut_intensifies | 0.84× | $19.84 | $20.36 | $20.71 | $43,250 |
| structural_reset | 0.72× | $13.60 | $16.11 | $17.19 | $40,500 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $27.50 | $29.19 | $+1.69 (+6.2%) |
| EV% | -6.2% | -0.4% | +5.8pp |
| Position | TRIM/SHORT | HOLD | **FLIP** |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $27.84, EV ≥ -5%): alpha ≥ **0.20**
- BUY threshold (FV ≥ $30.77, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

**Weights at the minimum HOLD threshold (alpha = 0.20):**

| Scenario | Weight at HOLD threshold | vs Set B |
|---|--:|--:|
| tight_resurgence | 0.110 | +0.010 |
| moderate_tightening | 0.170 | +0.020 |
| glut_base | 0.530 | -0.020 |
| glut_intensifies | 0.190 | -0.010 |
| structural_reset | 0.000 | +0.000 |

---

## CCEC — at price $21.60, target $25.17

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $52.98 | $49.70 | $42.05 | $137,383 |
| moderate_tightening | 1.13× | $41.36 | $41.36 | $41.36 | $74,327 |
| glut_base | 0.96× | $24.44 | $28.84 | $31.77 | $54,921 |
| glut_intensifies | 0.84× | $12.48 | $18.18 | $21.98 | $41,075 |
| structural_reset | 0.72× | $0.69 | $7.81 | $12.55 | $38,068 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $30.67 | $33.50 | $+2.83 (+9.2%) |
| EV% | +42.0% | +55.1% | +13.1pp |
| Position | BUY | BUY | unchanged |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $20.52, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $22.68, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

---
