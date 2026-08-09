# Container determinant refresh — 2026-08-09 (§11.8 event; owner-authorized promotion round)

**Trigger:** `container_mb_refresh` (re-armed 7/22 → due 2026-08-21; worked EARLY at the
owner's 2026-08-09 promotion authorization after the sentinel's `UNINGESTED-PRINTS
containers` flag — W32 staged 8/7 vs Ctr vintage 7/17, 21d). **Source:** MB Container
Weekly **W31** (7/31) + **W32** (assessments **2026-08-07** — the assessment set of
record), staged via the documented Gmail→mb_harvest flow. Promoted basis being diffed:
W29 (2026-07-17), `container_mb_refresh_packet_2026-07-22.md`.

## The diff (promoted W29 state → W32)

| Determinant | Promoted (W29 7/17) | W32 (8/7) | Δ |
|---|---:|---:|---:|
| Ctr-Feeder 12M TC = avg(1,100 / 1,700) | 24,250 = avg(17,500 / 31,000) | 24,250 (both flat) | 0 |
| Ctr-Intermediate 12M TC (A3 exact-TEU weights) | 46,350 | 46,350 (all four buckets 35,000/37,500/45,000/55,000 flat) | 0 |
| **Ctr-Large 12M TC** = avg(5,500 / 6,500) | 63,000 = avg(60,000 / 66,000) | **64,000** = avg(60,000 / **68,000**) | **+1.6%** |
| **Feeder 10-yr value (MB 1,700)** | $29.0M | **$29.5M** (15-yr 23.0 → **23.5** same direction) | **+1.7%** |
| Other 2nd-hand (2,700: 35.5/32.0 · 5,000WB 63.5 · 6,700WB 75.0 · 9,000WB 97.5) | — | identical W31=W32 | 0 |
| NB assessments (all five sizes) | — | identical W31=W32 | 0 |
| MBCI | 1,344 (W31) | 1,311 | context only |

Two cells moved, on DIFFERENT legs and different weeks: the 6,500-TEU 12M ticked
66,000→68,000 **at W30 (7/24)** and held; the 1,700-TEU 2nd-hand ticked +0.5 at both
ages **at W32**. Note the W32 narrative sale "Fitz Roy" (1,740/2011, "mid/high $20s")
sits consistent with the moved 1,700 ladder — cross-check, not a determinant.

## Predicted model impact (gate expectations, LEG-SCALED — the 2026-07-22 discipline)

This refresh is **TC + VALUE JOINT** (unlike 7/22's TC-only):
- **Files that MAY move:** `twelve_month_tc.yaml` (Ctr-Large), `spot_tce.yaml` (Ctr-Large
  mirror), `ffa_forward_curve.yaml` (Ctr-Large strip re-synthesis + Ctr as_of stamps),
  `vessel_value_curves.yaml` (**Ctr-Feeder ten_year_benchmark 29.0 → 29.5 — a REAL value
  move this time**; every other number in that file FROZEN).
- **NAV predictions:** feeder-holders ONLY — **MPCC NAV up ~+1–2%** (feeder 10-yr +1.7%
  flows through the curve marks), **GSL NAV up small** (feeder cohort share of its book);
  **every other row NAV Δ = 0.00 — any nonzero non-container NAV = HALT** (a frozen file
  moved).
- **EV/cycle:** Ctr-Large 12M +1.6% → GSL/CMBT large-leg strip + cycle position nudges;
  MPCC feeder cycle unchanged (feeder TC flat). Sub-1pp EV moves expected; no predicted
  band flip. D-M4 pre-flag: feeder cycle position did NOT advance this refresh (TC flat)
  — the 1.2× boundary watch stands unchanged.

## On promote (executed this record)

1. `twelve_month_tc.yaml`: Ctr-Large 63,000 → **64,000**; `as_of` Ctr-* → **2026-08-07**
   (vintage = assessment date; Feeder/Intermediate re-stamp at unchanged values).
2. `spot_tce.yaml`: Ctr-Large 63,000 → **64,000** (the 12M mirror convention); Ctr-*
   stamps → 2026-08-07.
3. `ffa_forward_curve.yaml`: Ctr-Large strip re-synthesized start **64,000** → same
   terminal 48,000, linear over 10 quarters rounded-to-250 (64000/62250/60500/58750/
   57000/55250/53500/51750/50000/48000); Feeder/Intermediate strips byte-unchanged;
   as_of Ctr-* → 2026-08-07.
4. `vessel_value_curves.yaml`: Ctr-Feeder `ten_year_benchmark` 29,000,000 →
   **29,500,000** with the dated comment (15-yr 23.5 corroboration noted); all other
   container anchors re-dated to W32 at UNCHANGED values (the 7/22 vintage principle).
5. Pipeline regen; verify the NAV-halt condition; drift-annotate movers (expect MPCC,
   possibly GSL); suite; ratify citing this packet.
6. Re-arm `container_mb_refresh` → next due **2026-09-07** (monthly from this ingest).

---

## EXECUTION RECORD (2026-08-09)

- Steps 1-6 executed as specified. **NAV-halt condition VERIFIED: MPCC NAV +0.5% (the
  feeder value leg, inside the ~+1-2% prediction's conservative side), GSL NAV
  no-change, every other row 0.0** — no frozen file moved.
- Drift gate: **0 UNEXPLAINED, all rows sub-threshold** (MPCC EV +0.3pp, GSL −0.4pp) —
  the baseline RIDES (the DHT 8/08 green-sub-threshold precedent; no ratify).
- GSL single-point FV −3.3% while weighted FV −0.3%: the Ctr-Large 12M +1.6% advanced
  the large cycle ratio → w_nav re-mix toward NAV (41.20 < strip) — the documented
  discrete-step mechanics D-M4's ramp will smooth at the D1 round; weighted-FV and
  band both sub-threshold, no eyeball owed.
- Trigger re-armed → 2026-09-07 (monthly from ingest).
