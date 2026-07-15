# Thread (d) — crude age-0 RESALE level: CONFIRMED CURRENT (close packet)

**2026-07-15. Confirm-only — zero number movement.** Proposed status: thread (d)
RESOLVED, pending owner sign-off. This packet documents a dated freshness check of
the wired crude age-0 anchors against the newest in-repo xclusiv issue, per the
Thread-1B protocol (PRE_REGISTRATION_CRUDE_RESALE_LEVEL.md §2–§4).

## 0. What thread (d) still asked

Thread (d) had two components (PLAN.md P1(d); stng_reconciliation_prereg §9.6 item 2):

1. **`curve.newbuild` basis inconsistency** (contract for dry-bulk vs resale for crude)
   — RESOLVED 2026-06-29 by Thread 1 + Amendment B: every wired class's age-0 is the
   xclusiv Resale line, single dated source, guard-tested
   (`test_curve_age0_equals_xclusiv_resale`). Nothing left here.
2. **Level currency** — the wired anchors are the 2026-06-22 xclusiv extract; the
   Hormuz-distorted market made a stale-print scenario live, and the STNG §9.6
   deferral (2026-07-01) quoted the level as "still provisional." This check closes
   that component.

## 1. The check (wired 2026-06-22 vintage vs xclusiv weekly 2026-07-13)

Source: xclusiv weekly report **2026-07-13** (in-repo:
`shipping_harvester/data/pdfs/xclusiv/2026W29_f76ec738.pdf`, parsed to
`data/marks/xclusiv/2026Q3.json`; PDF text re-read directly for the label check).
Threshold: Thread-1B ±2% per class; BRUT carve-out ±0.5% on VLCC.

| Class | wired age-0 | xclusiv Resale 2026-07-13 | Δ | verdict |
|---|--:|--:|--:|---|
| VLCC | 175.0 | 175.0 | **0.0%** | CONFIRMED (passes even the ±0.5% BRUT carve-out) |
| Suezmax | 114.3 | 116.0 | **+1.49%** | CONFIRMED (within ±2%) |
| Aframax | 92.5 | 92.5 | **0.0%** | CONFIRMED |
| LR2 (= Aframax hull) | 92.5 | 92.5 | **0.0%** | CONFIRMED |

**Label check (the crude-cascade lesson):** the 2026-07-13 issue carries the same
footnote as the committed extract — "*Resale prices refer to prompt delivery ex
yard*" — i.e. the Resale line is the just-delivered top of the secondhand curve,
the exact basis Amendment B locked. Read against the 5-Year row (VLCC 145.0,
Suezmax 102.5, Aframax 80.0) to confirm no row-slip: the Resale figures above are
the Resale row.

## 2. Independent corroboration (different broker, different week)

Advanced Shipping & Trading weekly W28 (**2026-07-10**, in-repo
`data/pdfs/advanced/2026W28_7fe0bf78.pdf`, INDICATIVE PRICES table):

| Class | advanced Resale | vs wired | note |
|---|--:|--:|---|
| VLCC 310k | 174 | −0.6% | corroborates |
| Suezmax 160k | 118 | +3.2% | larger hull basis (160k vs xclusiv 157k); corroborates direction |
| Aframax 110k | 95 | +2.7% | advanced moved +3.8% W27→W28; xclusiv held 92.5 — watch item, not a miss (xclusiv is the locked source of record) |

Intermodal W29 (2026-07-14) 5yr lines cross-check the xclusiv 5yr row: VLCC 145.0
(exact), Suezmax 103.0 (vs 102.5), MR 51.0 (vs 50.0). Consistent curve, two
independent houses.

## 3. Verdict

The crude age-0 RESALE level is **confirmed current** on a dated print 21 days
after the wired vintage, within the pre-registered ±2% on every crude class and
exact on VLCC (the max-torque class). The stale-print scenario did not occur.
With component 1 resolved by Amendment B and component 2 confirmed here, **thread
(d) has no remaining open question.**

## 4. Consequences (each its own owner-gated step — nothing executed here)

- **STNG §9.6 VLCC portion UN-GATED in principle.** The 2-VLCC park
  (stng_reconciliation_prereg 2026-07-01, item 2) rested on "the crude level is
  provisional"; that reason is now closed. The 10-hull wiring (~+$9.6/sh) remains
  its OWN pre-registered, owner-ruled step and **queues behind Stage A** per the
  2026-07-15 sequencing principle (one FV-moving event in flight at a time). Even
  fully wired, STNG classifies GOVERNED-WIDE at best (Handymax basis still
  pending), per the original deferral's classification note.
- **BRUT / crude-name language retires.** "Resale-level-provisional" phrasing
  (brut narrative, provenance.py comment) is superseded — BRUT's binding flags
  remain `cash-pending-H1-report` + going-concern (§15), unchanged by this check.
- **Suezmax +1.49% / Supra-Ultra +1.16% drift vs the 2026-07-13 issue is NOT
  absorbed here.** The full extract refresh (with its sub-drift-bar movers:
  CAPT/CMBT/ECO/TEN young Suezmax, 2343/GNK young Ultras) is registered in
  `decisions/mr_secondhand_resumption_2026-07-15.md` §5 as the deferred rider —
  it rides the next anchor-refresh cycle, post-Stage-A.
- PLAN.md P1(d) text (which still carried pre-Amendment-B "VLCC $175M plausibly
  stale-high" prose) is rewritten to point here.

**Owner sign-off line:** thread (d) closed as CONFIRMED — ______ (date / verbatim).
