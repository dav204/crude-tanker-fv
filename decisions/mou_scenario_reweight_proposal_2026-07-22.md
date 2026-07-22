# Reweight proposal — retire the benign-MoU mass (mid-cycle, ahead of the Aug-16 venue)

**Status: RULED 2026-07-22 same day — Option A + conditional B′ pre-registered on the 7/29
watch (see the Decision section). No input changes today; B′ FROZEN as the conditional package.**

**(Original status:) PREPARED 2026-07-22 at owner direction ("prep mid-cycle proposal"), ruling = OWNER's.**
This is the mid-cycle move the 7/18 MoU-implementation check FLAGGED but did not propose (an
out-of-band change would cut across the locked-weights gate and the one-FV-moving-event
sequencing); the owner has now asked for the package. NOT pre-registered — a fresh owner-reviewed
reweight per the Jul-2 proposal→sign-off chain (d1544b4; hormuz_retilt_proposal_2026-07-13
precedent). **Nothing below changes any input until the owner rules.**

## Why this is on the table

The Islamabad MoU is dead as a framework, by both principals' own words, and the crude weight set
still carries **0.30 combined mass on MoU-track scenarios** (mou_base 0.18 + mou_bear 0.12):

- Round-3 never convened; Trump declared the MoU **"over"** (~Jul-12 Ankara NATO summit); Iran
  calls it **"suspended"** (Jul-18). Record: `doha_round3_check_2026-07-22.md`.
- The 30-day implementation check FAILED all three observables (`mou_implementation_check_2026-07-18.md`):
  blockade IMPOSED not lifted, TSS mine area still published, transits at ~8–11% of pre-crisis,
  war-risk ~8×, six P&I withdrawals.
- Escalation-beyond-Jun-9 legs on record: the 7/14 CENTCOM naval blockade of Iranian ports; the
  7/16 Bab el-Mandeb closure threat (Iran→Houthis, rumor-tier-plus).
- **The fast-reversion rationale that capped escalation at 0.25 is now counter-evidenced:** the
  Jun-9 comment priced flare-ups that mean-reverted in days; the current episode is at **10+
  consecutive strike days** (Jul-6 → Jul-21) with US soldiers killed, Iranian strikes on Kuwait,
  and Brent **$91** — a persistent state, not a flare.

## Why it can also wait (the honest other side)

- **The tape sits in the MoU-INEFFECTIVE leg's band, not escalation's.** DHT Q3 QTD spot
  $139.7k/day vs pre_mou_baseline q3 [128.2k, 164.2k, 201.6k] — comfortably inside — vs
  escalation's q3 base $420k. The modal state IS the 0.45 leg; the counterfactual mass is the
  0.30 MoU-track tail, and mis-weighting a LOW-rate tail biases crude FVs DOWN — the
  conservative direction. No BUY is being manufactured by the stale weights; a few are being
  suppressed (see the what-if).
- **A live de-escalation thread exists:** mediation proposals received, a 10-day ceasefire
  reported under discussion (`crude_ceasefire_mediation_watch`, due 7/29). Reweighting into a
  ceasefire announcement would be churn; the mou-mass would go straight back up.
- **Sequencing:** Stage A (≤ Aug-15, unconditional) moves the same names the OTHER way (the held
  Jun-7 war-vintage curve overstates the strip; promotion ≈ −3-4% on peak-weighted crude). The
  Aug-16 toll cliff is a PRE-REGISTERED reweight date REGARDLESS of outcome, one day later —
  the designed venue for exactly this re-derivation, with the toll question answered.
- **No sizing decision reads a crude FV before Stage A anyway:** no held name is crude; the TEN
  entry is triple-gated with Stage A as gate (iii).

## Candidate weight sets (weights ONLY; curves, shapes, and all other sectors untouched)

| Scenario (semantics) | Current (Jun-9 shape) | **B** | **B′ (minimal)** |
|---|---|---|---|
| escalation (sustained war economics) | 0.25 | **0.30** | 0.25 |
| pre_mou_baseline (= MoU-INEFFECTIVE, the observed state) | 0.45 | **0.52** | **0.57** |
| mou_base (benign three-phase implementation) | 0.18 | **0.05** | **0.05** |
| mou_bear (settlement-with-friction: tolls, partial reopening) | 0.12 | **0.13** | **0.13** |

Per-leg rationale: mou_base → 0.05 residual = the rapid-revival tail (the mediation thread's
benign landing zone) — its triggers can no longer fire as written (there is no framework left to
implement). mou_bear holds ≈ its mass as the plausible END-STATE of any new deal (reopening with
tolls/friction — also where the toll-cliff branch would shift mass anyway). The freed 0.12-0.13
goes to the observed state (pre_mou); B additionally moves +0.05 to escalation on the
persistence evidence, B′ leaves escalation untouched (the tape-check argument: $139.7k ≠ $420k).

## Scratch what-if (isolated worktree @ ac216cf, 3 full pipeline runs, 2026-07-22; prices =
## HEAD's committed vintage — PW-FV deltas are price-independent, recompute EVs at execution)

| Name | Model FV now → B → B′ | ΔB | ΔB′ | EV now → B → B′ | Band |
|---|---|---|---|---|---|
| **CAPT** | $13.14 → 14.08 → 13.38 | **+7.2%** | +1.8% | +4% → +12% → +6% | **HOLD → BUY (flips in BOTH; B real, B′ shallow-boundary — eyeball at ruling)** |
| TEN | $56.56 → 58.13 → 56.83 | +2.8% | +0.5% | +46% → +50% → +46% | BUY (extends; family-range guard re-stamp) |
| DHT | $13.10 → 13.69 → 13.24 | +4.5% | +1.1% | −27% → −23% → −26% | rich · cycle (no flip) |
| ECO | $32.10 → 34.03 → 32.57 | +6.0% | +1.5% | −41% → −37% → −40% | rich · cycle |
| FRO | $22.80 → 24.22 → 23.15 | +6.2% | +1.5% | −38% → −34% → −37% | rich · cycle |
| NAT | $2.76 → 2.90 → 2.79 | +5.1% | +1.1% | −55% → −53% → −55% | rich · cycle |
| INSW | $54.12 → 55.62 → 54.46 | +2.8% | +0.6% | −39% → −37% → −38% | rich · cycle (crude sleeve only) |
| TNK | $73.35 → 75.05 → 73.69 | +2.3% | +0.5% | +2% → +4% → +2% | HOLD (no flip) |
| CMBT | $14.09 → 14.34 → 14.15 | +1.8% | +0.4% | −7% → −5% → −6% | TRIM/SHORT (no flip; crude sleeve only) |
| BRUT | $6.21 → 7.13 → 6.45 | +14.8% | +3.9% | +15% → +32% → +19% | unreliable read — VOIDED either way, no consequence |

Controls verified: **NAV/sh, Blend FV, and fv_low–fv_high unchanged on every row** (weights touch
only the scenario PW spine — ΔNAV 0.0 book-wide); **every non-crude row byte-identical** across
all three runs (the only diff is the W-frag column de-stamping to "—" on the scenario-inputs SHA
change — the standard all-five family re-stamp step at execution). Direction is as stated above:
retiring low-rate MoU mass RAISES crude FVs uniformly — the current weights are the
conservative error.

## The one flip to eyeball — CAPT

CAPT crosses HOLD→BUY in both variants (+12% EV at B — a real move; +6% at B′ — a shallow
boundary crossing at this price vintage). GOVERNED-WIDE·newbuild-heavy, W-frag ⚠ sign-flips at
the current tape, Q2 sponsor-VLCC-deal §15 tripwire pending. Per the Stage-A ruling's standing
rider, **any flip toward BUY = halt-and-investigate** — if this proposal executes, the CAPT flip
gets its own individual eyeball in the drift annotation, not a batch acceptance.

## Sequencing (the actual decision)

One FV-moving event at a time — the standing order is Stage A (≤8/15) → D-M2 → D1, with the
toll-cliff reweight pre-registered for Aug-16, immediately after Stage A. Executing THIS reweight
now would (a) insert an FV-moving event ahead of Stage A, and (b) see-saw against it (weights
+2-7% now, strip −3-4% at promotion). Clean execution windows if ruled-now: **7/23–7/25**
(before the Q2 cluster lands 7/28+) or fold into the Aug-16 venue.

## Decision (owner)

**RULED 2026-07-22 (owner verbatim: "Rule A - conditional B′ pre-registered on the 7/29
watch"): Option A + the conditional.** No reweight now; the weights stand at the Jun-9 shape.
**B′ (0.25/0.57/0.05/0.13) is PRE-REGISTERED on `crude_ceasefire_mediation_watch` (due
2026-07-29) and FROZEN at this ruling:** if that check records another collapse-track week
(no ceasefire convened or in effect), B′ EXECUTES at the check — mechanically, per the
execution loop below, with the CAPT HOLD→BUY flip eyeballed INDIVIDUALLY (halt-and-investigate
rider) — accepting that execution lands mid-cluster (the option was ruled with that note
visible). A ceasefire outcome instead VOIDS the conditional and routes to the normal
de-escalation proposal branch (owner proposal, never unilateral). Either way the Aug-16
toll-cliff venue STANDS for the full re-derivation (retiring the MoU scenario family outright).
The B package (escalation bump) is NOT pre-registered — escalation-ward mass remains an
owner call at a future venue.

- [x] **A — HOLD to the Aug-16 venue (agent recommendation).** The venue is pre-registered
      regardless-of-outcome, 3.5 weeks out, answers the toll binary first, and follows Stage A
      as designed. The interim cost is a known, conservative, documented bias (this doc + the
      scorecard header can carry a one-line disclosure); no sizing decision reads crude before
      Stage A. The B/B′ packages above stay computed and executable the day the venue opens.
- [ ] **B now** (0.30/0.52/0.05/0.13) — the persistence evidence into escalation; execute
      7/23–7/25 with the full loop below.
- [ ] **B′ now** (0.25/0.57/0.05/0.13) — the minimal honesty move; same window and loop.
- [x] **Conditional — pre-register B′ on the 7/29 watch:** if `crude_ceasefire_mediation_watch`
      records another collapse-track week (no ceasefire convened/in-effect), execute B′ at that
      check; a ceasefire outcome instead voids this card and routes to the normal de-escalation
      proposal branch. (Note: execution would then land mid-cluster — accept that, or name the
      window.)

Execution loop on any ruled option (same as the Jul-12/Jul-14 restores): 1. weight edits with
dated comments citing this doc; 2. test re-pins (crude weight value-pins in test_scenarios.py;
doha-restore comment pins; TEN/CAPT integration bands re-checked; ev_pct family-range guard);
3. commit inputs; 4. all-five family re-stamps; 5. pipeline regen from clean HEAD; 6. drift
annotations (cause: this doc), CAPT flip eyeballed INDIVIDUALLY; 7. owner-aware baseline ratify.

**Scratch artifacts:** worktree runs at `ac216cf` (baseline reproduced, then B, then B′);
worktree removed after capture; comparison scorecards in the session scratchpad. The scenario
descriptions/curves were NOT touched in any candidate — a full re-derivation (retiring the MoU
scenario family outright, toll-regime scenarios) is explicitly the Aug-16 venue's job and out of
scope here.
