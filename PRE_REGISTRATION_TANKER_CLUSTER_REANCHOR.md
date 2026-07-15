# Q2-cluster tanker forward re-anchor — pre-registration

**To be frozen on owner signature, no later than 2026-07-27 EOD — ahead of the first
cluster prints (STNG/ASC/SB, Jul-28/29).** This document is committed *before* any Q2
disclosure is read. Its purpose is to make the August re-anchor an out-of-sample
construction, not a fit to rate levels already seen. Eligible evidence, aggregation
rules, tenor mapping, predictions (with halt conditions), the two-stage schedule, and
the fallback are pinned here; if a computed value lands outside its registered band, the
response is to investigate the **input**, not adjust the output. Governing ruling:
`decisions/tanker_forward_print_ruling_2026-07-14.md` (Riders 2–4). If this document is
not frozen by 2026-07-27, Stage A executes on the §7 DHT-print fallback — the method may
not be written by someone who has seen the results.

## 0. Framing — what this replaces and what it must not touch

Replaces: the tanker lines of `inputs/market_data/ffa_forward_curve.yaml` (VLCC, Suezmax,
Aframax, LR2, LR1, MR, LR1_clean, LR2_clean) and `twelve_month_tc.yaml` (same classes),
HELD at the 2026-06-07 war vintage since the Jul-02 owner decision.

Out of scope, explicitly: dry-bulk lines (re-anchored 2026-07-13, own cadence);
LNGC/MGC and container lines (own source-of-record cadences); `cycle.py` and the band
machinery (owner decision D1 — the refreshed 12M TC flows into cycle position through
the existing frozen mechanics, which is a data refresh, not a methodology change);
scenario weights (the Hormuz re-tilt is its own thread; scenario *deltas* stay expressed
relative to whatever base curve this re-anchor lands); the DHT Jaguar company-input
update (ruling §7 — batched into the Stage-A regen but governed as a normal input
update, not by this method).

## 1. Eligible evidence (registered source classes)

**Qualifying, in priority order:**

1. **Dailies/weeklies FFA or 12M TC prints** (the original trigger observable). If one
   lands before Stage A it supersedes this entire method for the classes it covers
   (ruling Rider 4) and this pre-reg governs only the residual classes.
2. **Issuer Q2-2026 disclosures** (6-K/press release/earnings deck/prepared remarks),
   limited to: (a) individual TC fixtures with rate + tenor + start date; (b) disclosed
   fleet coverage tables with average charter rates and coverage percentages by period;
   (c) QTD spot bookings with the booked-days share.
3. **Fixture-date filter:** fixtures **concluded on/after 2026-06-15** only
   (post-stand-down market). War-era fixtures are not evidence of the forward market
   this re-anchor is trying to read; they enter coverage schedules (a different input)
   but not the curve.

**Not qualifying, registered now:** analyst estimates and price targets; consensus rate
decks; our own scenario values (circular); broker "market commentary" ranges without a
transacted or assessed print behind them; anything from the sanctioned/shadow-fleet
fixture tape (unrepresentative counterparty risk premium).

## 2. Tenor buckets and what each sets

| Bucket | Evidence | Sets |
|---|---|---|
| Front (strip Q1–Q2) | QTD spot bookings; spot fixtures | ffa_forward_curve quarters 1–2 |
| ~1-year | fixtures 9–15 months | `twelve_month_tc` line directly; curve Q3–Q4 |
| Term (2–3+ years) | fixtures ≥ 21 months | curve Q5–Q8 via §3 decomposition |

12M TC line: set from the ~1-year bucket median where N≥2; else interpolated as the
average of the front-bucket level and the term-bucket year-1 decomposition, tagged
`derived-interp` in the machine vintage.

## 3. Aggregation and decomposition (registered)

- **Per class per bucket: median of qualifying prints.** Minimum N=2 prints per
  class-bucket for a direct anchor; N=1 is used but tagged `single-print`; N=0 →
  §4 scaling.
- **Term decomposition** (turning a flat multi-year TC into strip quarters): year-1 =
  linear decay from the front-bucket level toward the fixture rate; remaining years =
  the level that makes the fixture's tenor-average hold. Quarters within a year are
  flat (no intra-year shape is evidenced by a flat fixture). This is the same
  decomposition used for the ruling §2 quantification — registered here so Stage A
  cannot pick a friendlier one.
- **Clean/dirty:** LR2_clean/LR1_clean anchored from product-name disclosures (STNG,
  ASC, TRMD, HAFN); dirty LR2/LR1 from crude/mixed names; where only one side prints,
  the other carries the 2026-06-07 vintage's clean-dirty spread on top of the printed
  side, tagged `derived-spread`.

## 4. Classes without prints

Scale by the class's ratio to the nearest printed class **in the 2026-06-07 joint
vintage** (the last coherent all-class snapshot), tagged `derived-ratio` with the
donor class named. Expected to matter for: Aframax (if INSW/TNK disclose thinly) and
LR1. Registered preference order of donors: Suezmax → VLCC for Aframax; LR2 → MR
for LR1.

## 5. Registered predictions (halt conditions, house discipline)

Written before any Q2 print is read; a landing outside its band halts the run for input
investigation (unit errors, sanctioned-tape contamination, mislabeled tenor) before any
value is accepted:

- VLCC front (Q1–Q2 avg): **$120k–$155k** (QTD $139.7k already in evidence)
- VLCC 12M TC: **$90k–$130k** (held: $111.5k Compass — expected to survive roughly)
- VLCC term-implied Q5–Q8 avg: **$55k–$90k** (held: $125k — expected to break)
- Suezmax/VLCC 12M ratio: **0.55–0.80** · Aframax/Suezmax: **0.75–1.05**
  (structure preservation check — the breakeven machinery assumes inter-class ordering)
- MR 12M TC: **$18k–$32k**
- Every class: front ≥ 12M ≥ term-implied back (backwardation is the registered
  expectation post-stand-down; a contango print is not forbidden but halts for a look)

## 6. Two-stage schedule (ruling Rider 2)

**Stage A — no later than 2026-08-15**, on everything landed by Aug-14 close.
*Minimum viable basis:* direct (non-derived) anchors in ≥3 of the 4 major classes
(VLCC, Suezmax, Aframax, MR/LR2-family) with VLCC among them. Expected coverage by
Aug-14 per the vetted calendar: DHT, ECO (Aug-4), INSW, TNK (~Aug-5), STNG/ASC
(Jul-28/29), SB/SBLK, NAT, BRUT (Aug-13) — all four classes reachable. Basis met →
promote per §§1–4. Basis not met → §7 fallback fires the same day; no extension.

**Stage B — window 2026-08-26 → 2026-09-04** (TRMD Aug-26, CMBT Aug-27, HAFN Aug-28,
FRO Aug-31). Recompute the §3 medians with the tail included. Execute a second
promotion **only if** any class-bucket median moves **>±10%** vs the Stage-A anchor;
otherwise commit a record-no-change note in decisions/ and stand down. (FRO is the
likeliest band-breaker — largest VLCC/Suezmax disclosure in the family.)

## 7. Fallback (unconditional retirement of the war vintage)

If Stage A's minimum basis is unmet on 2026-08-15: promote on the **DHT print alone** —
front from the QTD bookings, VLCC term from the §3 decomposition of the Jaguar fixture,
all other classes `derived-ratio` off VLCC per §4 — documented as a single-print anchor
with every derived tag carried into the vintage notes. This is the outcome the Jul-02
decision declined when the alternative was a war-spike anchor; by Aug-15 the alternative
is a 10-week-old war-spike anchor, and the single-print anchor is the lesser evil **by
registered pre-commitment, not by August-mood judgment**. The 2026-06-07 vintage does
not exist in any post-Aug-15 state of the world.

## 8. Execution procedure (both stages)

1. Refresh the YAML lines with machine `as_of` per class + per-row provenance comments
   (issuer, filing date, fixture tenor, tag: direct/single-print/derived-interp/
   derived-spread/derived-ratio).
2. Rerun the C-2 rates layer (the Jul-02 decomposition's tanker rate-effect is
   understated pending this — registered trigger action, now executable).
3. Full regen; drift gate. Expected-flip inventory, registered now so surprises stand
   out: near-edge HOLDs (TNK +3%, ASC +3%, TRMD −1%, CAPT −1%) may cross toward TRIM —
   the expected direction; each flip still individually eyeballed per house rule, and
   any flip *toward* BUY is a halt-and-investigate (wrong-direction under a
   curve-lowering re-anchor).
4. One ratify per stage, cause string naming this pre-reg; RATIFY_LOG entry; trigger
   re-armed to its original observable/action text with `status: armed` and the hold
   language deleted.
5. Batch in the DHT Jaguar coverage update (ruling §7) at Stage A only.

## 9. Signature

Owner sign-off (freezes §§1–8; amendments after 2026-07-27 only via a dated addendum
that does not loosen §5 bands or §6/§7 dates): **OWNER — SIGNED ("sign as specified",
with the 2026-07-15 pre-freeze addendum included in the frozen text)** · Date: **2026-07-15**

---

## PRE-FREEZE ADDENDUM (2026-07-15 — permitted: document not yet frozen)

§8.3's expected-flip inventory was drafted against the pre-re-tilt scorecard. Post the
2026-07-14 EVE Hormuz re-tilt (RESTORE BOTH), the registered inventory reads: TNK +1.3%,
ASC +4.0%, CAPT −1.9%, STNG −1.0% (near-edge HOLDs, may cross toward TRIM — expected
direction) and **TRMD BUY +8.4% — may drift toward the +5% boundary at Stage A; a
TRMD BUY→HOLD flip is EXPECTED-direction and individually eyeballed; any flip toward
BUY anywhere remains halt-and-investigate.** No band, date, or §5 prediction is loosened
by this addendum.
