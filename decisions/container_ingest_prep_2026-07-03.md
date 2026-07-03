# Container ingest DRY-RUN prep — 2026-07-03 (for the 2026-07-04 §11.8 event)

Prep only — NO determinant changed. Source: the newest STAGED MB Container
Weekly, W26 (`inputs/research_mb/container_weekly/2026/2026-06-26_Container_
Weekly_26_2026.pdf`, assessments dated Jun-26). Tomorrow's session harvests
the MB Gmail first (W27, expected dated Jul-3) — if W27's tables differ,
update the figures below from W27 and proceed identically; the geometry and
procedure don't change. Trigger: `container_mb_refresh` (due 2026-07-04).

## W26 12-month TC assessments (USD/day) vs the frozen Apr-01 vintage

MB standard sizes (p.2 "TC rate assessment"): 1,100: 17,500 · 1,700: 29,000 ·
2,500: 35,000 · 2,700: 37,500 · 3,500: 45,000 · 4,250: 55,000 · 5,500: 60,000 ·
5,400 WB: 65,000 (excluded, design premium §11.8.1) · 6,500: 66,000.

| Class (recipe §11.8.1) | Frozen Apr-01 | W26 candidate | Δ |
|---|---:|---:|---:|
| Ctr-Feeder (avg 1,100/1,700) | 20,500 | **23,250** | **+13.4%** |
| Ctr-Intermediate (A3 TEU-weighted) | 43,400 | **≈44,550** (see fork 1) | +2.7% underlying |
| Ctr-Large (avg 5,500/6,500) | 62,500 | **63,000** | +0.8% |

Intermediate underlying: simple average moved 42,000 → 43,125 (+2.7%); the
≈44,550 candidate applies the onboarding A3 uplift ratio (43,400/42,000) as a
PLACEHOLDER — the exact A3 recompute is fork 1, do not promote the placeholder.

`spot_tce.yaml` Ctr rows = the same numbers (no spot market exists; §11.8
convention). `ffa_forward_curve.yaml` Ctr strips re-synthesize per §11.8.6.4:
start at the new TC, mean-revert toward the FY21-25 anchor, 10 elements.

## W26 value assessments vs the current curve anchors (USD M)

| Curve anchor | Current (Apr-01 basis) | W26 | Δ |
|---|---:|---:|---|
| Feeder newbuild (MB 1,800 China) | 32.0 | 32.0 | unchanged |
| **Feeder 10yr (MB 1,700)** | 28.0 | **29.0** | **+3.6%** |
| Intermediate newbuild (MB 2,800 China) | 44.0 | 44.0 | unchanged |
| Intermediate 10yr (MB 2,700) | 35.5 | 35.5 | unchanged |
| Large newbuild (MB 5,400 China) | 63.0 | 63.0 | unchanged |
| Large 10yr inputs (5,000WB 63.5 / 6,700WB 75.0) | same pair | same pair | unchanged → derived 56.0 stands |

(The weekly's own S&P text: "pricing unchanged at the established high
level." W26 also quotes 9,000WB 97.5 and feeder 15yr 23.0 / intermediate
15yr 32.0 — the 15yr points stay deliberately un-consumed, §11.8.5(b).)

## Computed NAV impact (scratch inputs copy, feeder 10yr 28→29 only)

- **MPCC: $2.02 → $2.04 (+0.92%)** — feeder-heavy, mid-age fleet near the anchor.
- **GSL: $38.59 → $38.59 (+0.00%)** — negligible feeder-10yr exposure.

The NAV side of this ingest is small. The MATERIAL move is the rate side
(+13.4% feeder TC) flowing through the strip and cycle position — expect the
scenario FV shift to dominate the diff you review, and the drift-gate
annotation to cite the rate legs, not the marks.

## Open forks for tomorrow (owner)

1. **Exact A3 weights** — rebuild the intermediate TEU distribution from the
   issuer fleet lists (manifests carry class/dwt, not TEU); the onboarding
   session (2026-06-12) derived them the same way. Promote the A3 figure, not
   the placeholder.
2. **W27 supersession** — harvest first; if W27 differs, re-derive from W27.
3. **as_of discipline** — all Ctr rows across the three rate files move to the
   ingested weekly's assessment date in the same commit; the three as_of
   agreement tests re-pin automatically; §11.8 revision note + lock-test
   re-pin per the trigger's action text; annotate the MPCC/GSL gate rows;
   re-arm `container_mb_refresh` to the next monthly boundary.
