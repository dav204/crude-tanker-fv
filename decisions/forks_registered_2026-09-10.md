# Forks registered 2026-09-10 from the owner's parked list — BWLP newbuild treatment · spot_tce promotion · R4/WO5 deck re-expression

Three items had sat on the owner's list as "rulings". Under the 2026-09-10 policy (inputs/forks.yaml)
each is a registered JUDGMENT fork: a verified recommendation that executes on 2026-09-15 unless the
owner answers. The agent's drafts (Appendix A) were adversarially verified (Appendix B); corrections:

- **BWLP** (`bwlp_nb_order_treatment`): the draft's clause (c) — a `structural_exempt` registry line for
  BWLP with a "far-dated, zero-paid, bought-at-market" rationale — is DROPPED: the registry's own header
  forbids exactly that. The recommendation is Option 3, advances-only interim (hulls and the ~$940M
  commitment both OUT, matching the 6/30 statements; ΔNAV/ΔEV 0.0). The 9/08 6-K is the ex-dividend
  notice only and settles nothing on the order. Record-only: `bwlp.yaml:90-91` still says the order
  "enters at the Q2 refresh" — corrected to HELD OUT in this commit so the next agent does not re-wire it.
  The $300M 2.25% convert (settled 9/09, "partly finance the newbuild program") is Q3 wiring, not this fork.
- **Spot** (`spot_tce_promote_2026-09-10`): the draft labelled it state-tracking (execute on verification).
  CORRECTED to judgment: the owner reserved the spot disposition twice on the OWNER OWES list; the silence
  window applies. Every number reproduces (Pareto 9/10 p.1 "Average of key routes", column-1 convention);
  the consumer trace confirms spot feeds breakeven / validate / report only — nav.py, the strip and the
  scenario deck never read it, so ΔNAV and ΔEV are exactly 0.0 on all 25 names. Vintage coherence holds
  (spot holds ⊆ 12M holds after promotion). Note for tomorrow: CAPT trades ex-dividend NOK 3.00 on 9/10
  and BRUT ex-distribution $0.025 — a step in their tapes, not drift.
- **R4/WO5** (`r4_wo5_deck_reexpression_schedule`): SAFE as drafted, two wording fixes. Execute WO5
  Phases 0–3b on the post-Stage-B base with the C3 vector frozen; no void retires here — the three Phase-4
  dispositions (CAPT / TNK / BRUT) stay execution-day owner words by WO5's own law.

---
# APPENDIX A — the three pre-registration notes (agent, read-only)

# Track FORKS — three registered forks + pre-registration notes (2026-09-10, read-only audit)

Policy basis: `inputs/forks.yaml:1-13` — judgment forks execute at their recommendation after 3 business days of silence (`execute_after` 2026-09-15); `kind: state-tracking` executes on verification (amendment `:5-9`, `:13`). Nothing below was run or written; every number is read from the cited file.

---

## Fork entries for `inputs/forks.yaml`

```yaml
  - id: bwlp_nb_order_treatment
    kind: judgment
    doc: decisions/bwlp_nb_order_fork_2026-08-31.md   # + this note when landed
    opened: 2026-09-10
    execute_after: 2026-09-15
    recommendation: "Option 3 ADVANCES-ONLY interim (=$0; hulls + $940M commitment both OUT, matching the 6/30 statements): ΔNAV 0.0 / ΔEV 0.0, BWLP stays T/S -40% PROVISIONAL. Record the HHI yard + the $300M convert (9/09, 'partly finance the newbuild program') as Q3 wiring; re-opens on any instalment/schedule disclosure (Q3 report ~Nov)"
    status: open

  - id: spot_tce_promote_2026-09-10
    kind: state-tracking
    doc: decisions/spot_tce_promotion_2026-09-10.md   # this note
    opened: 2026-09-10
    execute_after: 2026-09-11   # on verification (the day the verified proposal returns)
    recommendation: "Promote spot_tce.yaml from the 8/07 daily to Pareto 9/10 (column-1 convention pinned on 8/07): VLCC 790,800 · Suez 135,000 · Afra/LR2 72,500 · LR2c 141,800 · LR1c 148,100 · MR(East)/Handy 55,100 · Cape 54,538 · Pana/PPmx 21,725 · Supra 21,537; as_of.default 2026-09-10; Ctr-* mirror to 12M W36 (25,500/47,567/64,000, as_of 9/04). Diagnostic-only: ΔNAV 0.0, ΔEV 0.0 on all 25"
    status: open

  - id: r4_wo5_deck_reexpression_schedule
    kind: judgment
    doc: WO5_R4_DECK_REEXPRESSION.md   # + decisions/r4_deck_reexpression_method_2026-09-XX.md (Phase 0, method already RULED B+C)
    opened: 2026-09-10
    execute_after: 2026-09-15
    recommendation: "Execute WO5 Phases 0-3b on the post-Stage-B base (12M as_of 2026-09-09) with the C3 vector 0.28/0.59/0.00/0.13 as the FROZEN weight input; ΔNAV 0.0, 10 crude names move >2pp EV by design, non-crude exactly 0.00. No void retires here: the three Phase-4 dispositions stay execution-day owner words (WO5 law); TNK destination pre-ruled cycle-relabel"
    status: open
```

---

## (1) BWLP newbuild fork — pre-registration note

**The decision.** How the Q2-2026 snapshot carries the 8 × 90,000-cbm Panamax-VLGC order (~US$940M, signed 30-May-2026, deliveries early-2029 → Q2-2030; `decisions/bwlp_nb_order_fork_2026-08-31.md:8-10`). Three treatments, quantified at the 8/31 curve (`:18-35`): (1) on-curve §9.6 ≈ −$260M ≈ −$1.7/sh (the PV-asymmetry artifact for a bought-at-market, far-dated program); (2) one-sided commitment ≈ −$6.2/sh; (3) advances-only = $0.0/sh. Current sheet holds both sides at 0 (`inputs/balance_sheets/bwlp_2026-Q2.yaml:55-56`, rationale `:45-54`); manifest `vessels_under_construction: 0` (`inputs/fleet_manifests/bwlp.yaml:90`).

**Evidence.**
- The Q2 interim report is silent on the order: no commitments note, vessels cost flat 2,994,895 vs 2,994,896, H1 investing outflow $2.9M net → advances paid through 6/30 = $0 (`bwlp_2026-Q2.yaml:46-49`; `decisions/bwlp_log.md:123-131`). "Present but uncited" would fail; here the issuer's own presentation IS the citation.
- Contract ≈ market: the Q2 deck (p.9) prints "~$114M" as the "VLGC newbuilding price" for an "88-91k dual-fuel non-ammonia capacity VLGC, at 'first class competitive yard'" vs the order's ≈$117.5M/hull arithmetic (fork doc `:9`) — a ~3% gap, which is the premise of the NPV≈0 stance (`:20-24`). Same page: "157 Total orderbook" (the 8/31 R-2 read used the report's 155, `bwlp_log.md:147-148`).
- **The 9/08 6-K (acc 0001213900-26-097809) settles nothing on the order.** Ex 99.1 is the ex-dividend notice only: "the shares of the Company will be traded ex-dividend on the Oslo Stock Exchange from today and on the New York Stock Exchange from 8 September 2026 … US$0.95 per share" (`inputs/filings/BWLP/0001213900-26-097809_6-K_ea030475201ex99-1.htm`, cover "Date: September 8, 2026"). No instalment, no schedule, no capex line.
- **What did land is the convertible (not in the fork doc):** "USD 300 million senior unsecured convertible bonds due 2031 … The Company intends to use the net proceeds to partly finance the newbuild program with Hyundai Heavy Industries for eight Panamax VLGCs" (`inputs/filings/BWLP/newsweb_2026-09-02_da6ce467….txt:9-10`; 2.25% coupon, conversion price US$30.4870, settlement "on or around 9 September 2026", `:13`). This names the yard (HHI — the fork doc had no yard) and confirms the program is being financed; it does NOT disclose an instalment paid or a schedule. Q3 sheet consequence (not this fork): cash +~$300M / debt +$300M, NAV-neutral pre-conversion; conversion at $30.49 (> NAV $15.83) would be ~9.8M shares (6.5% of 151,814,600, `bwlp_2026-Q2.yaml:58`).
- Convention registry: `newbuild_convention.yaml:11-17` limits `structural_exempt` to classes with NO resale mark; VLGC has a §9.9 fit, so option 3 rests on a *far-dated/zero-paid* rationale the registry doesn't yet enumerate — the scope extension only the owner can make (`fork doc:30-35`).
- **Guard blindness (new finding):** `tests/test_newbuild_convention.py:41-52` classifies a name by `commitments>0 / advances>0 / years_to_delivery>0`; with 0/0/0 BWLP returns `"no-NB"` and is never parametrized (`:55-60`). Under option 3 the order is invisible to the structural guard — nothing reds if it is never re-opened. The `OFF_CONVENTION_QUEUE` (`:31-33`) can't hold it either (an un-parametrized name can't xfail).

**Recommendation: Option 3 (advances-only interim), executed as a record-only commit.** Predicted impact: ΔNAV exactly 0.0 (NAV/sh stays $15.83), ΔEV 0.0, BWLP stays TRIM/SHORT −40% at $24.15, PROVISIONAL · v1-lock-miss, relabelled "rich · cycle position (not a short)" (`outputs/book_scorecard.md:58`; `provenance.py:150-151`). Band: NAV $15.83 ± $0.00; the other 24 names exactly 0.0. What the commit must carry: (a) the ruling recorded in the fork doc + sheet comment (`:45-54` already says HELD OUT); (b) a dated re-open trigger — first instalment / schedule disclosure, earliest the Q3 report (~Nov; the sentinel's filing lane catches a 6-K earlier, `fork doc:41-43`) — because the guard cannot see this state; (c) a registry line in `newbuild_convention.yaml` extending the enumerated rationale to "far-dated, zero-paid, bought-at-market, no schedule disclosed" so the next such name (STNG's 10-hull program is queued) can't land unclassified.

**Alternative:** Option 1 on-curve now → NAV ≈ $14.1 (−$1.7/sh, −10.7%), still T/S; prints a discounting artifact the GSL ruling already named, on a name that is flag-don't-pass. Option 2 → ≈ $9.6/sh, "clearly not economics" (`:26-28`). Neither changes the position; both put an uncited per-hull price (no per-hull split is disclosed, `:10`) into the NAV equation, which the provenance rule forbids.

**UNVERIFIED and what settles it:** whether a first instalment was paid at signing/in Q3 (typical 10% ≈ $94M) — only the Q3 interim (Nov) or a 6-K instalment note settles it; the convert's "partly finance" language is not evidence of payment.

---

## (2) The spot disposition — pre-registration note

**What is held, and why.** `spot_tce.yaml` carries the 8/07 Pareto vintage on every tanker and dry row (`inputs/market_data/spot_tce.yaml:32`, rows `:45-59`). The 8/31 annotation (`:19-24`): "Pareto dailies staged through 8/31 vs the 8/07 vintage below — promotion DELIBERATELY DEFERRED to the next owner round (the 8/31 seven-cause ratify closed today; refresh backlog … one FV-event at a time). Spot feeds the breakeven diagnostic + validate warning only, NOT the strip — staleness here is display-grade." PLAN carries it as "spot promote disposition (hold annotated)" (`PLAN.md:155-156`, owner-owes list `:78`).

**What spot feeds (the consumer, verified in src).** `loaders.py:289` → `schemas.py:182` → (a) `breakeven.py:110-121` (`current_spot_tce`, `blended_spot_tce`) → `report.py:262-263` the "Current spot" row of the breakeven table; (b) `validate.py:32-42` the ">5× the 10-yr mean" warning (`SPOT_HIGH_MULTIPLE = 5.0`, `:18`); (c) `carveout.py:228` re-maps clean rows to LR1/LR2/MR for product carve-outs (identity-pinned, `tests/test_carveout.py:495-500`). It reaches neither `nav.py`, the scenario deck, nor the strip ("Does NOT feed the dividend strip (that runs off ffa_forward_curve.yaml)", `spot_tce.yaml:1-3`). The owner already ruled this 9/02: F17 dropped spot from the UNINGESTED-PRINTS lane because it is "diagnostic, not NAV/strip … never a valuation event" and "no spot parser exists" (`decisions/prune_ledger_2026-09-02.md:101,177`; `sentinel.py:275-277`; `CHANGELOG.md:66`). So the hold's stated reason — one FV-event at a time — does not bind: a promotion is not an FV event.

**What a promotion does — class by class** (Pareto 9/10 p.1 "Average of key routes", pypdf extract; the file's convention is the FIRST value column, pinned by matching all six 8/07 file values to the 8/07 daily: "VLCC (TD3_C) USD/day $488 900 … Suezmax (TD20) $77 600 … Aframax $75 400 … LR2 $92 200 … LR1 $95 300 … MR (East) $31 500"):

| Class | 8/07 (file) | 9/10 daily (verbatim) | Δ |
|---|---:|---|---:|
| VLCC (TD3C) | 488,900 | "$790 800 3.3%" | +61.7% |
| Suezmax (TD20) | 77,600 | "$135 000 2.2%" | +74.0% |
| Aframax; LR2 dirty (= Afra, `:48`) | 75,400 | "$72 500 6.8%" | −3.8% |
| LR2_clean | 92,200 | "$141 800 25.7%" | +53.8% |
| LR1_clean | 95,300 | "$148 100 5.0%" | +55.4% |
| MR (East); Handysize/Handymax (= MR, `:52-53`) | 31,500 | "MR (East) $55 100 5.0%" | +74.9% |
| Cape | 42,313 | "Capesize USD/day $54 538 1.5%" | +28.9% |
| Pana; Post-Panamax (`:58`) | 20,473 | "Panamax $21 725 0.0%" | +6.1% |
| Supra-Ultra | 20,326 | "Ultramax $21 537 0.6%" | +6.0% |

9/09 daily for the record: VLCC $765,400 · Suez $132,000 · Afra $67,900 · LR2 $112,900 · LR1 $141,000 · MR(East) $52,400 · Cape $53,750 · Pana $21,724 · Ultramax $21,403. Note the MR row relabel: 8/07 printed "MR (West)/(East)"; 9/09-10 print "MR (Atlantic triangulation)/(East)" — the file's MR (East) convention (`:51`) holds; the Atlantic row ($26,400) is not the file's row. Unchanged: LNGC (8/06 MB override), MGC (6/07), Handy-Bulk (7/10 BHSI) — no Pareto column (`:38-40`, `:60-64`).

**Coherence rule** (`tests/test_market_data_vintages.py:28-33`): no override may be newer than `as_of.default`; (`:36-47`): spot's hold set (override < default) ⊆ 12M's hold set. 12M holds today (default 2026-09-09, `twelve_month_tc.yaml:35-49`): Cape/Pana/PPmx/Supra (9/01), VLGC (6/02), LNGC/MGC (6/07), Handy-Bulk (7/10), Ctr-* (9/04). After promotion (spot default 2026-09-10): spot holds = {LNGC, MGC, Handy-Bulk, Ctr-*} ⊆ 12M holds — passes; dry rows ride default. **The container mirror lag** (`spot_tce.yaml:69-72`, recorded 2026-09-10): the 12M surface moved to W36 (Feeder 25,500; Intermediate 47,567; Large 64,000 held, `twelve_month_tc.yaml:83-92`, as_of 2026-09-04) but the spot mirror is stuck at W32 (24,250 / 46,350 / 64,000) because an override of 9/04 would exceed the 8/07 default (`:32-33`). Promoting the default to 9/10 is exactly what unlocks the mirror; the same commit should move Ctr-* to the W36 values with `as_of` 2026-09-04.

**Predicted impact.** ΔNAV exactly 0.0 and ΔEV exactly 0.0 on all 25 names; drift gate 0 rows; no tier, band, or read moves. Observable changes: the "Current spot" row in each report, and the validate warning set — VLCC 790,800 = 19.8× the 40,000 mean (already firing at 12.2×), NEW fires on LR2_clean (141,800 / 28,000 = 5.1×) and LR1_clean (148,100 / 25,000 = 5.9×); Suez 4.9× stays just under (`historical_tce_means.yaml:2-14`). Only `test_handy_bulk_class.py:85` pins a spot value (Handy-Bulk 16466 — untouched). `test_refresh`/`test_notify` clock the file's mtime (a promote refreshes it).

**Recommendation:** promote from the 9/10 daily as a state-tracking fork, execute on verification; the hold's own rationale expired with F17. **Alternative:** keep holding to the Q3 cluster — costs a 34-day-stale diagnostic row and leaves the container mirror permanently one vintage behind the 12M surface (a two-surfaces disagreement the 7/02 rule exists to prevent).

---

## (3) The R4 deck re-expression docket — pre-registration note

**What the voids are.** At the 8/10 Stage-A re-anchor (12M VLCC 111.5k → 105.7k), the crude scenario legs — ABSOLUTE 8-quarter paths built 2026-05-29 — stopped measuring anything: pre_mou_baseline's Vessel× went 0.82 → 0.96 against the new base, mou_bear 0.70 → 0.79, "the deck measuring ~nothing" (`decisions/stage_a_halt_investigation_2026-08-10.md:15-31`). The resulting BUY-ward flips (BRUT +44.3pp / CAPT +17.8 / TNK +5.0) were ruled deck-incoherence ARTIFACTS and masked via `POSITION_UNRELIABLE = {MPCC, BRUT, CAPT, TNK}` (`src/crude_tanker_fv/provenance.py:147-153`, disposition B `:38-42`). R4 (8/16): "Stage-A voids STAND. CAPT/TNK do not retire and BRUT does not re-read today. The 8/10 retire condition is the deck re-expression against the landed Stage-A base … docketed as its own work order" (`decisions/crude_day60_toll_cliff_2026-08-16.md:192-196`; `:269`), carrying correction 2: "one void name reads BUY-ward at tape, not two" (`:244-249`).

**What "re-read" means.** WO5 (`WO5_R4_DECK_REEXPRESSION.md`, ISSUED + RATIFIED 9/01, `:3-7`): Phase 0 method RULED Fork B + C — a one-time re-derivation of new absolute per-quarter paths against the post-Stage-B base, each leg re-expressed as a real spread (escalation = upside tail; pre_mou ≈ observed state; mou_bear = normalization-disappoints), plus a deck-coherence guard test (`:12-14`, `:124-150`). Only on that honest deck do the three per-name dispositions get ruled — "retire / uphold / re-read" — as execution-day owner words (`:26-27`, `:205-256`). A retired void produces a raw governed surface read, not a trade (`:47-49`).

**Has the retirement condition been met? No.** No `decisions/r4_deck_reexpression_method_*.md` exists (`ls decisions | grep -i r4` → empty); `scenario_inputs.yaml` crude legs are still the 5/29 absolute curves ("Added 2026-05-29", `:122-141`) — every event since has moved WEIGHTS only (7/02, 7/12, 7/31, 8/16 C2, 9/10 C3 `:142-149`). WO5's sequencing gate ruled "R4 executes 2026-09-04/05, after the Stage B disposition" (`:15-17`); Stage B was disposed 9/09, so the kill-switch "Stage B not disposed by 2026-09-05 → the sequencing gate returns to the owner" (`:66-67`) fired — that returned gate IS this fork. PLAN still records "no void retires outside the deck re-expression work order" (`PLAN.md:207,216`); today's reweight record repeats it (`decisions/escalation_c3_rearm_2026-09-10.md:163`).

**Evidence landed since 8/16, per name.**
- **CAPT.** 9/01 H1 refresh: NAV $15.48 → $17.32, "landing 0.02 above the frozen band [14.70,17.30]; the hairline breach was investigated and accepted" (`decisions/capt_log.md:71-72`); the acquired Hengli VLCC trio at shipbuilding-contract price via the $336.9M contribution in kind, every figure filing-cited (`:180-188`); 9/09 price leg ΔEV −2.4pp and Stage B ΔEV −5.9pp, "band HOLD → TRIM/SHORT (mechanical crossing on the price leg)" (`:11,31`); today's reweight +1.63pp → EV −6.98%, T/S, masked, 1.98pp from HOLD (`escalation_c3_rearm:47`). **The "one BUY-ward void at tape" framing (`PLAN.md:207`) is stale: at $19.11 vs PW-FV $17.77 CAPT reads T/S −7%** (`book_scorecard.md:44`). The artifact-shaped read has reversed on the price + Stage B legs before any re-expression. The test pin `tests/test_capt.py:53-58` guards FV>price arithmetic at the 8/28 price only.
- **TNK.** T/S −13.57% at $96.31, VALIDATED-TIGHT, read_flag robust, rich/rich (`book_scorecard.md:38,88`); Stage B −9.0pp, price −7.5pp, reweight +0.79 (`decisions/tnk_log.md:3-15`). Retirement is "uncontroversial mechanically" but freeing TNK flips the named-shorts prose — destination PRE-RULED to `POSITION_CYCLE_RELABEL` (`WO5:19-21`, `:225-245`). A retire commit must move `tests/test_tier_semantics_amendment.py:156` (`assert "TNK" in POSITION_UNRELIABLE`) and respect `tests/test_scorecard.py:659-660` (disjointness), and re-arms the B1 docket (item 7).
- **BRUT.** Live 4-hull object per the 8/31 scope word (`decisions/brut_demerger_carry_2026-08-25.md:100-106`). Today the predicted weight-leg flip landed: PW-FV $5.35, EV +5.6%, raw position BUY, displayed "unreliable read (not actionable)", "⚠ sign flips" (`decisions/brut_log.md` auto 2026-09-10T18:37; `book_scorecard.md:43`; predicted at `escalation_c3_rearm:46,145`). Stage B −0.4pp, price −2.5pp (`brut_log.md:22-30`). The uphold rider — post-6/30 cash/debt known-unknown (July SLB draws, $50M OMC contribution) resolves "at the ~end-Sep uplisting prospectus or FY2026" (`WO5:246-256`; `brut_log.md:269-270`) — is NOT resolved: the three September filings are an August commercial update ("approximately US$95,073 per day, net" on the fixed-rate vessel; US$0.025 distribution, `newsweb_2026-09-04…txt:7-9`), a financial calendar ("19.11.2026 - Quarterly Report - Q3", `newsweb_2026-09-07…txt`), and the ex-distribution notice (`newsweb_2026-09-10…txt:5`). No prospectus, no cash/debt figure.

**Recommendation.** Register the returned sequencing gate as a judgment fork and execute WO5 Phases 0-3b at the first sitting after 2026-09-15 on the settled base: 12M VLCC 105,700 / Suez 74,500 / Afra-LR2 56,000 / MR 30,000, as_of 2026-09-09 (`twelve_month_tc.yaml:51-58`), transaction-anchored marks as they stand, with two scope notes the WO needs before it runs: (a) its frozen weight input is now the C3 vector 0.28/0.59/0.00/0.13, not C2 (`scenario_inputs.yaml:142-149`) — a scope note, not a weight decision (weights stay a non-goal, `WO5:278-286`); (b) the CAPT framing correction above (the BUY-ward void at tape is now BRUT, masked). **Predicted impact:** ΔNAV exactly 0.0 on all 25 names (rates never touch NAV); the 10 crude names (DHT/ECO/FRO/INSW/TNK/NAT/TEN/CMBT/BRUT/CAPT) move >2pp EV by the WO's own design (`WO5:71-74`) — sign per name is the Phase-3 freeze output, not pre-registrable here without running the sim, which this audit could not; pure-product/non-tanker exactly 0.00; fv_low/fv_high widen as the de-escalation legs regain real spread; any BUY-ward flip on a non-void name = halt (`WO5:63-66`). **What the silence policy can and cannot execute:** Phases 0-3b (the re-expression, guard, sidecars, landing) — yes, the owner ratified the WO 9/01; the three Phase-4 dispositions, the ratify, and the push — no, they are owner acts "by this WO's own law" (`:26-31`). Recommended dispositions as evidence for that eyeball: CAPT — retire WITH whatever shape the honest deck prints (the T/S read already stands at tape; strobe-pin per `:213-219`); TNK — retire → cycle-relabel (pre-ruled); BRUT — UPHOLD on the prospectus rider, re-armed to the Q3 report 2026-11-19 or the Euronext admission document, whichever lands first.

**Alternative:** leave the voids standing until the Q3 refresh cluster. Cost: the crude deck keeps pricing de-escalation twice for another quarter, every crude EV read (not just the three voids) carries the incoherence, and the 9/10 reweight's per-name EVs — including BRUT's masked BUY — were computed on the no-op deck.
---
# APPENDIX B — verification

**VERDICTS**
- **Fork 1 `bwlp_nb_order_treatment` — REGISTER WITH CORRECTIONS** (drop or re-scope clause (c); fix two mis-framings; kind = judgment is right).
- **Fork 2 `spot_tce_promote_2026-09-10` — REGISTER WITH CORRECTIONS** (kind must be `judgment`, execute_after 2026-09-15; everything numeric reproduces).
- **Fork 3 `r4_wo5_deck_reexpression_schedule` — SAFE TO REGISTER** (two wording corrections, neither load-bearing).

---

## Fork 1 — BWLP newbuild order

**What reproduces (opened myself).**
- 9/08 6-K acc 0001213900-26-097809: cover lists one exhibit, "99.1 Press release … dated September 7, 2026 – Ex-dividend on the Oslo Stock Exchange today", signed "Date: September 8, 2026"; Ex 99.1 text is the ex-dividend notice verbatim as quoted ("…on the New York Stock Exchange from 8 September 2026 … US$0.95 per share"). No instalment, schedule, or capex language anywhere. Claim CONFIRMED.
- Convert: `inputs/filings/BWLP/newsweb_2026-09-02_da6ce467….txt:9-10` verbatim "USD 300 million senior unsecured convertible bonds due 2031" / "partly finance the newbuild program with Hyundai Heavy Industries for eight Panamax VLGCs"; `:13` 2.25%, USD 30.4870, settlement "on or around 9 September 2026". 300/30.487 = 9.84M sh = 6.48% of 151,814,600 (`bwlp_2026-Q2.yaml:58`). CONFIRMED.
- Q2 deck p.9 (pypdf): "~$114M VLGC2 newbuilding price", fn 2 "88-91k dual-fuel non-ammonia capacity VLGC, at 'first class competitive yard'", "157 Total orderbook"; p.10 "VLGC orderbook currently consists of 155 ships". 940/8 = 117.5 → 3.1% gap. CONFIRMED (the "155" is deck p.10, not "the report" as `bwlp_log.md:148-149` says — cosmetic).
- Sheet `bwlp_2026-Q2.yaml:55-56` both 0, rationale `:45-54`; manifest `bwlp.yaml:90` `vessels_under_construction: 0`; fork doc options/figures `:18-35`; ΔNAV 0.0 is trivially true (option 3 = current state; scorecard `:58` NAV $15.83, EV −40%, "rich · cycle position (not a short)").
- Guard blindness CONFIRMED: `tests/test_newbuild_convention.py:41-52` returns `"no-NB"` at 0/0/0 → `_nb_names()` (`:55-60`) never parametrizes BWLP; `OFF_CONVENTION_QUEUE` (`:31-33`) is a strict-xfail marker on parametrized names only. Nothing reds if the order is never re-opened.

**Findings.**
1. **CORRUPTING (as written) — clause (c), the registry line.** The recommendation asks silence to add BWLP to `newbuild_convention.yaml` `structural_exempt` with a "far-dated, zero-paid, bought-at-market" rationale. The registry's own header forbids what that line would enshrine: `:11-13` "Exempt from the on-curve requirement; **still required to be commitment-net**", and `test_newbuild_convention.py:76-81` asserts exempt names are `commitment-net`/`on-curve`, never advances-only. Worse, the sibling open fork `cmbt_commitments_convention` (`forks.yaml:34-39`, execute_after **2026-09-15 — the same day**) moves CMBT *off* advances-only "per newbuild_convention.yaml's own 'must move to'". Two forks executing the same morning would write opposite conventions into one file. The 8/31 fork doc never asked for a registry line — it said "folded into the pending GSL/CMBT commitment-net prereg" (`:39-40`), i.e. the rationale question belongs to that prereg. **Fix:** strip (c); record the ruling in the fork doc + sheet comment + a dated re-open trigger only, and route the registry-scope question into the CMBT/GSL commitment-net prereg where the fork doc placed it. RECOVERABLE once (c) is out.
2. **RECOVERABLE — mis-stated reason for rejecting options 1/2.** "Both put an uncited per-hull price … into the NAV equation" is wrong on the mechanics: `nav.py:13-16,98-118` values a hull at the curve's age-0 node PV-discounted `1.11^(−years_to_delivery)` and subtracts the *aggregate* `newbuild_capex_commitments` (the sourced ~$940M, 6-K acc 0001213900-26-063117) — no per-hull price enters. The genuine provenance gap for option 1 is `years_to_delivery` (only a window "early-2029 → Q2-2030" is disclosed, fork doc `:9,:25`). Also note the "PV-asymmetry artifact" is the convention's uniform output already applied to CAPT/FRO/MPCC/BRUT (`test_newbuild_convention.py:6`); VLGC has a §9.9 fit, so under the registry BWLP is a clause-1 name. The recommendation may still be option 3, but the record should say why the tool's own convention is being set aside (far-dated + window-only dates), not a per-hull-price argument that does not exist.
3. **RECOVERABLE — stale manifest instruction.** `bwlp.yaml:90-91` still reads "SUBSEQUENT event, enters at the Q2 refresh (§9.6)" and the header (`:8-12`) describes the 3/31 state; `report_date: 2026-Q2` (`:40`). A record-only commit should correct the comment to HELD OUT, or the next agent re-wires the order on the manifest's word.
4. **RECOVERABLE — citation slip.** BWLP's cycle-relabel lives at `provenance.py:145-146`, not `:150-151` (those lines are the `POSITION_UNRELIABLE` comment).
5. Kind = judgment: CORRECT (fork doc `:33-34` "a scope extension only the owner can make"). The Q3 convert consequence (cash/debt +$300M at face) is correctly excluded from this fork.

**UNVERIFIED (as the track says):** any instalment paid at signing or in Q3 — only the Q3 interim or a 6-K instalment note settles it.

---

## Fork 2 — spot_tce promotion

**What reproduces.**
- Every value in the Δ table matches the dailies (pypdf p.1 "Average of key routes"): 9/10 VLCC $790 800 · Suez $135 000 · Afra $72 500 · LR2 $141 800 · LR1 $148 100 · MR (East) $55 100 · Cape $54 538 · Pana $21 725 · Ultramax $21 537; 9/09 row likewise; 8/07 col-1 values match all six file rows. Rendered p.1 header (pdftoppm) confirms column 1 is labelled **"ECO - no scrubber"**, column 2 "Non-ECO - no scrubber", column 3 "Scrubber premium" — the file's stated convention (`spot_tce.yaml:9-10`). All nine Δ% recompute exactly (VLCC 1.6175, Suez 1.7397, Afra 0.9615, LR2c 1.538, LR1c 1.554, MR 1.749, Cape 1.289, Pana 1.061, Supra 1.060).
- Consumer trace CONFIRMED in src: `loaders.py:289` → `schemas.py:182` → `breakeven.py:110,117,121` → `report.py:262-263`; `validate.py:18,32-42`; `carveout.py:228`; `refresh.py:69` (mtime clock). `grep spot_tce src/` hits nothing in nav.py, strip, or scenarios. ΔNAV/ΔEV 0.0 on 25 names is grounded.
- Validate multiples recompute: VLCC 19.8×, LR2c 5.06× (new), LR1c 5.92× (new), Suez 4.87× (under), against `historical_tce_means.yaml:2-11`.
- Vintage coherence CONFIRMED: `test_market_data_vintages.py:28-33` (override ≤ default) and `:36-47` (spot holds ⊆ 12M holds). Post-promotion spot holds {LNGC, MGC, Handy-Bulk, Ctr-×3} ⊆ 12M holds {Cape, Pana, PPmx, Supra, VLGC, LNGC, MGC, Handy-Bulk, Ctr-×3} (`twelve_month_tc.yaml:35-49`). Mirror-lag note `spot_tce.yaml:69-72` is committed (b5d304b). Only pin touched by nothing: `test_handy_bulk_class.py:85` (Handy-Bulk 16466). No test asserts the Ctr spot/12M mirror equality.

**Findings.**
1. **CORRUPTING — kind.** `kind: state-tracking` executes on verification (9/11) and skips the silence window. The record does not support that: (a) PLAN carries "spot promote disposition" on the **OWNER OWES** list twice (`PLAN.md:78`, `:154-156`) — an item the owner reserved; (b) the F17 owner ruling the track leans on was literally "Drop spot_tce from the UNINGESTED lane (**no auto-promote** — no parser exists)? **yes**" (`prune_ledger_2026-09-02.md:177`; row 66 `:101`) — the owner said yes to no-auto-promote, and a fork that executes the next day without an owner word is an auto-promote by another name; (c) the 9/10 amendment defines state-tracking as "a **reweight** that tracks an OBSERVED STATE" (`forks.yaml:5-9`) — a data-file promotion the owner explicitly parked is not that. The track's "the hold's rationale expired with F17" is agent inference about owner intent, which is exactly what the silence window exists to test. **Fix:** `kind: judgment`, `execute_after: 2026-09-15`. RECOVERABLE.
2. **RECOVERABLE — doc path does not exist.** `decisions/spot_tce_promotion_2026-09-10.md` is not in the tree (`ls decisions | grep -i spot` → empty); the sentinel prints the path (`sentinel.py:365-367`) with no existence check. Land the note in the registering commit.
3. Minor: the Pareto 9/10 front page notes "Today, CAPT (NOK 3.0) and BRUT ($0.025) trade ex-dividend" — irrelevant to spot, but the CAPT tape in `prices_daily.yaml:36-39` is the 9/09 close; anyone reading CAPT's "1.98pp from HOLD" tomorrow should expect an ex-div step, not drift.

---

## Fork 3 — R4 / WO5 sequencing gate

**What reproduces.**
- WO5 ratification record: Phase 0 RULED B+C (`WO5:10-14`); sequencing gate RULED 9/04-05 after Stage B + CMBT (`:15-18`); TNK destination pre-ruled cycle-relabel (`:19-21`); B1 re-arms at TNK's disposition (`:22-24`); the three dispositions + ratify + push are owner acts (`:25-27`); kill-switch "Stage B not disposed by 2026-09-05 → the sequencing gate returns to the owner" (`:66-67`). Stage B disposed 9/09 (0e6c518/f38cedb) → the gate did return. Registering the returned gate as a judgment fork is the record-consistent move.
- Retirement condition unmet: no `decisions/r4_*` file; `scenario_inputs.yaml:122-150` crude legs still "Added 2026-05-29", only weight comments since (7/02, 7/12, 9/10). `stage_a_halt_investigation:15-31` and `crude_day60:192-196, 244-249, 269` say what the track says. `PLAN.md:207,216`, `escalation_c3_rearm:163` "No void retires".
- Per-name evidence: CAPT `capt_log.md:5,11,31,70-75,178-190`, scorecard `:44` $19.11 / $17.77 / −7% masked — the PLAN:207 "CAPT is the ONE BUY-ward void at tape" framing is indeed stale; BRUT `brut_log.md:3-18` raw HOLD→BUY at +5.6% masked, `:269-270` rider unresolved; the three September newsweb files are exactly what the track says (9/04 "approximately US$95,073 per day, net", US$0.025; 9/07 "19.11.2026 - Quarterly Report - Q3"; 9/10 ex-distribution). TNK `tnk_log.md:5,11,17`, `c3_rearm:42`, scorecard `:38,88`; pins `test_tier_semantics_amendment.py:156`, `test_scorecard.py:659-660`, `test_capt.py:53-58` all as cited.
- C3 is live and committed (c8a4d0f → e6b6299 → 4907a35 → fa857a3; `scenario_inputs.yaml:150` weight 0.28), so "frozen weight input = C3" is a statement of the live state, not a weight decision; WO5 `:48,278-280` freezes weights, it does not require the C2 numbers. Scope note is legitimate.
- Impact: ΔNAV 0.0 (nav.py reads no rate/scenario file — every Stage B/C3 annotation and `nav.py` confirm); "10 crude names" is right — CMBT's sector is `crude` (scorecard `:45`) and it sits in the C3 table (`c3_rearm:45`); WO5's "~9" (`:71-72`) omitted it.

**Findings (both RECOVERABLE, neither changes the verdict).**
1. **BRUT re-arm target mislabelled.** The record's rider is "the uplisting prospectus (~end-Sep) or FY2026" (`brut_log.md:269-270`; `WO5:251-253`). "Euronext admission document" is OMC's staged lead (`brut_demerger_carry:102-104`), not BRUT's — and BRUT already trades on Euronext Growth (9/10 newsweb). Word the re-arm as "uplisting prospectus (~end-Sep) or the Q3 report 2026-11-19, whichever first" so the trigger keys on the right filing.
2. **Silence scope should be stated in the YAML line itself.** The recommendation string says "Execute WO5 Phases 0-3b" but the sentinel page truncates at 140 chars (`sentinel.py:366`); put "Phases 0-3b ONLY; Phase 4-5 owner words" inside the first 140 characters so the executing agent never reads a truncated "Execute WO5" as licence for the dispositions.

Nothing in fork 3 is CORRUPTING: kind = judgment is correct, the predicted impact is the WO's own frozen-band mechanism, and the owner surface (dispositions/ratify/push) is preserved.