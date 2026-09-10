# Crude escalation reweight — fork `escalation_c3_rearm`, EXECUTED ON VERIFICATION 2026-09-10

**Owner, 2026-09-10:** *"scenarios should be reweighted to whatever the scenario is in real life at
present today 9/10. what are you expect to learn between 9/10 and 9/15 that would change that"* —
nothing; the silence window is for judgment forks, and a weight that tracks an observed state
executes on verification (policy amended in `inputs/forks.yaml`). Venue: the folded card
`crude_geopolitics_weekly` LEG 2 (fired 2026-09-10: the strike pause ended 2026-08-30 —
`decisions/escalation_pause_check_2026-09-10.md`).

## The set (the original C3, on the deck's own semantics)

`inputs/scenario_inputs.yaml` crude: **escalation 0.25 → 0.28 · pre_mou_baseline 0.62 → 0.59 ·
mou_base 0.00 · mou_bear 0.13** (mass 1.00). R5 (2026-08-16) declined C3 on two grounds:
ground 1 ("exceeds the registered action") was jurisdictional to the toll-cliff card — the folded
card's LEG 2 action registers exactly this reweight; ground 2 ("an uncorroborated pause status")
is moot in the opposite direction. R3/R5 stand on their 8/16 evidence; this is a new decision on
a new record.

**Why the donor is pre_mou_baseline, not mou_bear (the verifier's one corrupting correction to
the draft):** the deck's weighting rule (`scenario_inputs.yaml:131-136`) locates "fast-reverting
flare-up" mass in `pre_mou_baseline`; the corrected record's new fact is that the flare-up
stopped reverting (CENTCOM Larak Island 8/30; campaign from 9/01; Iranian strikes on US bases;
TD3C $790,800 on 9/10 after seven consecutive rises, above the escalation leg's own Q3 upper
bound of $500k). `mou_bear` at 0.13 was deliberately RETAINED at R1 as the fee-regime tail R3
points at (LEG 1 is unaffected). Not matched: escalation's "wider MEG closure" — Hormuz ~7 mb/d
via STS, MEG 10 mb/d — so pre_mou keeps 0.59, the open-strait leg. Also on the record, both
ways: Pareto 9/03 "Trump is considering declaring the war with Iran over" and 9/04 "no further
flare-up"; 9/07 and 9/09 the attacks.

## PRE-REGISTERED BAND (frozen before the regen; engine-reproduced to the cent by the verifier)

ΔNAV = 0.0000 on every name (nav.py reads no scenario weight; `scenarios.py:423` computes NAV
before any weight is used). Non-crude 15 names = 0.000 on PW-FV, EV and NAV. Crude, ΔPW-FV ±
$0.01 at the 9/09 tape:

| name | PW-FV → | EV% → (Δpp) | band |
|---|---|---|---|
| DHT | 16.12 → 16.32 | −23.94 → −23.00 (+0.94) | T/S |
| ECO | 41.50 → 42.22 | −42.10 → −41.09 (+1.01) | T/S |
| FRO | 28.30 → 28.79 | −40.05 → −39.03 (+1.03) | T/S |
| INSW | 59.32 → 59.91 | −43.30 → −42.73 (+0.57) | T/S |
| TNK | 82.48 → 83.24 | −14.36 → −13.57 (+0.79) | T/S (masked) |
| NAT | 2.91 → 2.97 | −60.01 → −59.21 (+0.81) | T/S |
| TEN | 61.17 → 61.80 | +38.01 → +39.45 (+1.44) | BUY (unchanged) |
| CMBT | 13.45 → 13.54 | −30.50 → −30.02 (+0.48) | T/S |
| **BRUT** | 5.23 → 5.35 | +3.21 → **+5.61 (+2.40)** | **HOLD → BUY — MASKED** (`POSITION_UNRELIABLE`: displayed "unreliable read (not actionable)"; cannot enter the long set; 0.61pp past the edge, inside the deadband) |
| CAPT | 17.46 → 17.77 | −8.62 → −6.98 (+1.63) | T/S (masked), 1.98pp from HOLD |

Tripwires: BRUT's predicted BUY-ward flip is disclosed here and to the owner; it is the standing
"owner eyeball" — masked, non-actionable, and not a halt because it is PREDICTED, not a surprise.
Any OTHER flip toward BUY, any nonzero ΔNAV, any non-crude movement = HALT for input investigation.
Drift gate: BRUT breaches (+2.40pp) — annotated; all ten crude logs annotated with the weight leg.

## Corrections folded from the verification

Donor leg (above). "3pp is the deck's quantum" struck (executed moves were 15/15/5pp; no 3pp move
has executed). "Risen nine straight sessions" → seven (9/01 was flat). "12 sessions" → 10 Pareto
prints 8/28–9/10. "Third-party strike" is undefined in the repo — the match is on "no MoU" and
"$400k+", stated as such. The identity ΔPW-FV = Δw × (FV_esc − FV_donor) holds for pure crude
names only; the table is engine output. HEAD label corrected (bf2d3ad, not f48ddcd).

## What this does not do
No NAV input moves; no rate moves; no ratify by itself — the landing lane ratifies the morning
after this regen; R3/R5 stand as rulings on their evidence.

---
# APPENDIX A — the proposal (agent, read-only, engine-reproduced)

# Pre-registered proposal — fork `escalation_c3_rearm` (crude deck reweight)

Read-only. Everything below was computed in memory on HEAD (`f48ddcd`); `git status` empty before and after every run; `state/`, `outputs/`, `inputs/` untouched. Book quarter 2026-Q2; tape = `prices_daily.yaml` asof `2026-09-09T20:00Z`, the same vintage as `state/last_run.json` (`run_at 2026-09-10T18:07:37Z`).

## 1. What C3 was, and why R5 declined it

`decisions/crude_day60_toll_cliff_2026-08-16.md` §4 table (lines 103-108): C3 = "escalation tilt (+3pp esc)" at **0.28 / 0.59 / 0.00 / 0.13** (esc / pre_mou / mou_base / mou_bear), against production A′ 0.25/0.57/0.05/0.13. Relative to C2 as executed (0.25/0.62/0.00/0.13, R1 line 168), C3 is **+3pp escalation taken from `pre_mou_baseline`**.

R5 verbatim (lines 198-199): "**R5 — C3 DECLINED.** Exceeds the registered action; rests on one week's tape plus an uncorroborated pause status." §5 adds (line 137-139): "it re-bases the escalation leg on a state the 8/09 record already priced as ambiguous, and it breaches the gate broadly."

- **Ground 1 — "Exceeds the registered action."** The toll-cliff card's registered action was mou_base-only: R1 executed C2 as "WITHIN the card's registered action ('shift mou_base toward mou_bear/pre_mou')" (line 169-170). Ground 1 was jurisdictional to that card, not a finding on the merits of an escalation tilt. Today's venue is a different card: `reweight_triggers.yaml:41-46` (LEG 2) registers exactly this action — "the escalation question is re-run against the corrected record ... A reweight proposal is pre-registered (predicted impact per crude name, band, flip tripwires), verified, then registered in inputs/forks.yaml under the silence rule (owner policy 2026-09-10)". **Ground 1 does not bind**: an escalation move is inside this card's action.
- **Ground 2 — "one week's tape plus an uncorroborated pause status."** Moot in the opposite direction: the pause is corroborated as ENDED 8/30 (`escalation_pause_check_2026-09-10.md:1-4`), the tape is 12 sessions, not one week, and it is rising, not reverting (§2).

## 2. The deck as it stands (`inputs/scenario_inputs.yaml`)

| scenario | weight | registered premise (verbatim) |
|---|---|---|
| `escalation` | 0.25 (:142) | "Conflict escalates beyond current intensity (third-party strike, wider MEG closure, no MoU). MEG-loading VLCC/LR2 sustain $400k+ near-term" (:144-146) |
| `pre_mou_baseline` | 0.62 (:226) | "MoU-INEFFECTIVE ... the signed framework fails in practice — tolls imposed post-day-60, demining incomplete, sporadic fast-reverting flare-ups. Strait mostly OPEN; rates carry a toll/risk premium and an episodic-spike expectation, NOT sustained war economics (that tail lives in escalation)" (:229-233) |
| `mou_base` | 0.00 (:307) | "MoU signs, three-phase path materializes" (:309) — retained at zero for series continuity (R1) |
| `mou_bear` | 0.13 (:371) | "Framework holds but normalization disappoints — tolls imposed post-day-60" (:367); "MoU signs but Iran fails to ramp exports ... No Phase 1 backlog spike. Phase 2 onset immediate" (:373-375) |

The deck's own weighting rule (:131-136): "scenario weights price persistent states over the valuation horizon, not event frequency — fast-reverting flare-ups inside a holding framework are evidence for the MoU-ineffective leg ..., not for sustained war economics." Line 225 names `escalation_pause_corroboration` as C3's successor.

**Corrected record vs the premises.**
- **Falsified: `mou_bear`.** "Framework holds / MoU signs" was already "CONTRADICTED by the observed state" at R1 (toll_cliff:182-184) and is now contradicted by a bilateral strike campaign: MB W36 9/04 "resumed strikes on Iran for the first time in a month ... Iran retaliated by striking US bases in Jordan, Bahrain and Kuwait ... both sides intensified their attacks" (record:35-36, VERIFIED at :92). Also falsified: `pre_mou_baseline`'s sub-clause "sporadic fast-reverting flare-ups" — day 12 and widening (record:59-60), against the deck's June benchmark of "days-to-a-week" (:198-199).
- **Best match: `escalation`**, on two of its three elements. "Third-party strike ... no MoU": Iranian strikes on US bases in third countries; US struck 3 Iranian tankers 9/05 and 5 vessels 9/08, one sunk; IRGC claims 8 vessels + 2 destroyers 9/09 (Pareto 9/07, 9/09, quoted record:37-38). "$400k+ sustained": TD3C, Pareto "Average of key routes" row, scrubber column — 8/28 $634,500 · 8/31 $636,100 · 9/01 $636,100 · 9/02 $680,200 · 9/03 $690,300 · 9/04 $707,700 · 9/07 $710,000 · 9/08 $733,600 · 9/09 $765,400 · 9/10 $790,800 (no-scrubber $783,200). That sits above the escalation leg's own Q3 upper bound of $500k (:149) and has risen nine straight sessions — the opposite of "fast-reverting". **Not matched: "wider MEG closure."** Hormuz ~7 mb/d via STS, MEG visible exports 10 mb/d (MB W35/W36, record:91-92) — flows are partly recovering. The record's own reading (record:67): the tape "sits between" the open-strait-with-premium leg and escalation. (Correction owed when that record is next touched: line 67 attributes "Strait mostly OPEN ... episodic-spike" to `mou_bear`; that text is `pre_mou_baseline`'s, :232-233.)
- Caveats stated plainly: TD3C was already $634k on 8/28, before the pause ended — the rate level is corroboration of persistence, not a pause-end fact. And §13.3's spot trigger needs deviation "over a full quarter" (METHODOLOGY:2567); Q3 has 20 days left, so the rate tape does not fire a trigger on its own.

## 3. The proposed weight set

Mass conserved at 1.00 in every candidate (asserted in the sim).

**MIN (recommended): 0.25 / 0.62 / 0.00 / 0.13 → 0.28 / 0.62 / 0.00 / 0.10.**
- `mou_bear` 0.13 → 0.10: the mass leaves the leg whose "framework holds / MoU signs" premise the corrected record falsifies (MB W36 9/04, record:92; R1 toll_cliff:182-184).
- `escalation` 0.25 → 0.28: to the leg whose "third-party strike, no MoU, $400k+" premise the same record matches (Iranian strikes on Jordan/Bahrain/Kuwait bases, record:35; TD3C $790,800, Pareto 9/10).
- `pre_mou_baseline` untouched at 0.62: it still describes the FLOW state (7 mb/d STS / MEG 10 mb/d, record:91-92); the "wider MEG closure" element of escalation is not met, so the open-strait leg keeps its mass.
- `mou_bear` kept ≥ 0.10, not zeroed: `fv_low`/`fv_high` are taken over weight>0 scenarios (R1, toll_cliff:171-173) — DHT's fv_low 11.78 IS mou_bear's FV 11.7765 (sim); zeroing it would silently narrow every crude range.

**C3-as-proposed: → 0.28 / 0.59 / 0.00 / 0.13** (+3pp escalation from `pre_mou_baseline`). Same lift; drains the best-fit leg and leaves the falsified one whole. Shown for the range; not recommended on the deck's own semantics.

**Bracket, +5pp (0.30/0.60/0.00/0.10)**: gradient only. No dated primary supports >3pp — escalation has never exceeded 0.25 in the deck's history (0.25 was the Jun-9 "war tilt", :127/:137), and the facts that would justify exceeding it (tankers sunk 9/05, 9/08) are three sessions old. Why not 1-2pp: 3pp is the deck's quantum (C3 itself), and a smaller step chosen to keep BRUT under its edge would be sizing to the tripwire.

## 4. §9.10 rerun — predicted impact, computed

Mechanism: `_run_scenarios_for_ticker` on the production routing path, `load_watchlist(live_prices=True)` (the §9.10 `main()` mandate, `scripts/crude_weight_robustness.py:162-165`), transaction-anchored marks on, override applied to `sector_docs["crude"]` only. **Parity first:** under production weights the sim reproduced `state/last_run.json` PW-FV and EV% to the cent on all 25 names (DHT 16.12/−23.94 … BRUT 5.23/+3.21 … 2343 0.38/−30.70).

**Crude roster** = the 10 names with `sector: crude` in `state/last_run.json` (DHT/ECO/FRO/INSW/TNK/NAT default to crude, `loaders.py:437`; TEN/CAPT/BRUT/CMBT explicit) = `CRUDE_TICKERS` (script:113-114). Band = ±5pp (`scenarios.py:169`, `_REC_BAND 0.05`). ΔNAV = `base_nav_per_share` after − before.

| name | price | PW-FV now → MIN → C3 | EV% now → MIN (Δpp) → C3 (Δpp) | band now → MIN / C3 | ΔNAV | nearest edge after MIN |
|---|---|---|---|---|---|---|
| DHT | 21.20 | 16.12 → 16.42 → 16.32 | −23.94 → −22.56 (+1.38) → −23.00 (+0.94) | T/S → T/S / T/S | 0.0000 | 17.6pp |
| ECO | 71.67 | 41.50 → 42.48 → 42.22 | −42.10 → −40.72 (+1.37) → −41.09 (+1.01) | T/S → T/S / T/S | 0.0000 | 35.7 |
| FRO | 47.21 | 28.30 → 28.99 → 28.79 | −40.05 → −38.60 (+1.46) → −39.03 (+1.03) | T/S → T/S / T/S | 0.0000 | 33.6 |
| INSW | 104.62 | 59.32 → 60.10 → 59.91 | −43.30 → −42.56 (+0.75) → −42.73 (+0.57) | T/S → T/S / T/S | 0.0000 | 37.6 |
| TNK | 96.31 | 82.48 → 83.43 → 83.24 | −14.36 → −13.37 (+0.99) → −13.57 (+0.79) | T/S → T/S / T/S | 0.0000 | 8.4 |
| NAT | 7.27 | 2.91 → 2.98 → 2.97 | −60.01 → −59.01 (+1.00) → −59.21 (+0.81) | T/S → T/S / T/S | 0.0000 | 54.0 |
| TEN | 44.32 | 61.17 → 61.96 → 61.80 | +38.01 → +39.80 (+1.79) → +39.45 (+1.44) | BUY → BUY / BUY | 0.0000 | 34.8 |
| CMBT | 19.35 | 13.45 → 13.57 → 13.54 | −30.50 → −29.85 (+0.65) → −30.02 (+0.48) | T/S → T/S / T/S | 0.0000 | 24.9 |
| **BRUT** | 5.07 | 5.23 → 5.41 → 5.35 | +3.21 → **+6.83 (+3.62)** → **+5.61 (+2.40)** | **HOLD → BUY / BUY** | 0.0000 | **1.83 past BUY edge (C3: 0.61)** |
| **CAPT** | 19.11 | 17.46 → 17.92 → 17.77 | −8.62 → −6.20 (+2.42) → −6.98 (+1.63) | T/S → T/S / T/S | 0.0000 | **1.20 from HOLD edge (C3: 1.98)** |

+5pp bracket ΔEV: DHT +2.01, ECO +2.05, FRO +2.14, INSW +1.13, TNK +1.52, NAT +1.54, TEN +2.75, CMBT +0.97, BRUT +5.22 (→ +8.43), CAPT +3.51 (→ −5.11, 0.11 from HOLD).

**ΔNAV is exactly 0.0000 on all ten**, and must be: `nav.py` contains zero occurrences of "scenario" or "weight" (grep count 0); `compute_nav(inputs: CompanyInputs)` (`nav.py:80`) reads company inputs only. Weights enter once, in the blend Σ wₛ·FVₛ.

**Non-crude names — exactly 0.000 on PW-FV, EV and NAV under every candidate** (FLNG, CCEC, STNG, HAFN, TRMD, ASC, CMDB, SBLK, GNK, MPCC, GSL, SB, LPG, BWLP, 2343 — all printed `+0.000`). The deck is sector-namespaced: the override touches `sector_docs["crude"]` only, and the multi-sleeve names prove it — INSW product sleeve 20.3884 unchanged (crude sleeve 38.929 → 39.710); TEN product 12.6696 / LNG 7.7399 unchanged (crude 40.757 → 41.550); CMBT dry_bulk 8.9151 / containerships 0.5348 unchanged (crude sleeve 3.998 → 4.123).

**Full arithmetic** (per-scenario FVs from the production run; ΔPW-FV = Δw × (FV_esc − FV_donor), price-invariant):

- **DHT** — FV_esc 21.5265, FV_pre 14.8571, FV_bear 11.7765. Now: 0.25×21.5265 + 0.62×14.8571 + 0.13×11.7765 = 5.3816 + 9.2114 + 1.5309 = **16.124**; EV = (16.124−21.20)/21.20 = **−23.94%**. MIN: +0.03×(21.5265−11.7765) = +0.2925 → 16.4165; EV **−22.56%**. C3: +0.03×(21.5265−14.8571) = +0.2001 → 16.324; EV **−23.00%**.
- **BRUT** (tape 5.0686) — FV_esc 8.5438, FV_pre 4.4825, FV_bear 2.4327. Now: 2.1359 + 2.7792 + 0.3163 = **5.2314**; EV +3.21%. MIN: +0.03×(8.5438−2.4327) = +0.1833 → 5.4147; EV (5.4147−5.0686)/5.0686 = **+6.83% → BUY**. C3: +0.03×(8.5438−4.4825) = +0.1218 → 5.3532; **+5.61% → BUY**.
- **CAPT** (tape 19.1064) — FV_esc 25.9188, FV_pre 15.5105, FV_bear 10.4884. Now: 6.4797 + 9.6165 + 1.3635 = **17.4597**; EV −8.62%. MIN: +0.03×(25.9188−10.4884) = +0.4629 → 17.9226; EV **−6.20%**. C3: +0.03×(25.9188−15.5105) = +0.3122 → 17.7719; **−6.98%**.

## 5. Tripwires and the band

- **BRUT flips HOLD → BUY under both MIN and C3.** A flip toward BUY is halt-and-investigate ("any flip toward BUY = halt-and-investigate", `stage_a_halt_investigation_2026-08-10.md:3`; WO5:64-65 "a predicted BUY-ward flip is still an owner eyeball, never auto-accepted"). BRUT is already 1.79pp from its BUY edge at baseline and carries "⚠ sign flips" in the scorecard's W-frag column (`book_scorecard.md:43`). Pre-registered disposition: the flip is 100% weight leg (the +0.1833 identity above), on a name whose position cell is already masked "unreliable read (not actionable)" (`POSITION_UNRELIABLE`, `provenance.py:147`; scorecard:43) pending R4, which is ISSUED, not executed (`WO5_R4_DECK_REEXPRESSION.md:3`; "BRUT — re-reads, does not auto-retire", :246). The flip therefore changes no actionable read and no GTC; it still gets the owner eyeball and a `brut_log.md` annotation. C3's variant lands 0.61pp past the edge — inside the 2pp deadband, strobe-prone; MIN lands 1.83pp past — also inside. Both are inside 2pp; neither is clear.
- **CAPT** is the second-order tripwire: T/S at −6.20 (MIN), 1.20pp from the HOLD edge; the +5pp bracket puts it 0.11pp from a T/S → HOLD flip (BUY-ward direction). Also masked (`provenance.py:148`). No other crude name is within 8pp of any edge (TNK −13.37).
- **Drift gate** (2.0pp EV, `drift_gate.py:75`): MIN breaches on BRUT (+3.62) and CAPT (+2.42) — two annotations owed, weight-leg only; C3 breaches on BRUT alone.
- **The band the regen must land inside** (frozen before the regen, C2/CMBT shape): per crude name **ΔPW-FV = the table value ± $0.01**, ΔNAV **= 0.0000 exactly**, all 15 non-crude names **= 0.000 exactly**; ΔEV is re-derived at the landing tape as ΔPW-FV ÷ price (ΔPW-FV is price-invariant, EV is not — if a fresh vintage is committed first, per the 2026-07-26/09-09 rule, the pp figures shift by the price move only). A landing outside = **HALT for input investigation, never output adjustment** (`cmbt_q2_landing_2026-09-10.md:39`); suspects in order: a curve/transaction print between HEAD and the regen, a scenario-forward edit, a vintage change.

## 6. The recommendation, registry-ready

**Recommendation (≤300 chars):** "Crude 0.25/0.62/0.00/0.13 → 0.28/0.62/0.00/0.10: +3pp escalation from mou_bear (pause ended 8/30, campaign from 9/01, TD3C $790.8k 9/10); ΔNAV 0.0; crude EV +0.5..+3.6pp, non-crude 0.0; BRUT HOLD→BUY predicted (masked, owner eyeball); CAPT T/S −6.2."

**Alternative:** "Leave 0.25/0.62/0.00/0.13; dated note under the escalation comment (`scenario_inputs.yaml:142`) that the 8/30–9/09 campaign is recorded and unpriced; re-decide at the 9/17 `crude_geopolitics_weekly` check."

Registry note: the 9/10 record's Appendix A §5 cautioned against entering this as a silence-executing fork; the owner's same-day ruling (`reweight_triggers.yaml:52`, "aren't we doing that part as well") and the card's amended action (:44-46) supersede that caution. `forks.yaml` does not yet carry `escalation_c3_rearm`; `reweight_triggers.yaml:47-51` names it with `stage_a_deadline: 2026-09-15`.

## 7. What this does NOT do

- **No NAV change** — ΔNAV 0.0000 by construction (§4). **No rate change** — no scenario forward, 12M TC, FFA or spot input moves; the TD3C prints are evidence, not inputs (spot is display-grade, `spot_tce.yaml` header), and the §13.3 spot trigger is not fired.
- **No ratify by itself** — the landing lane regens the morning after, checks the band, annotates the two gate rows and the BRUT flip, then ratifies with cause.
- **R3/R5 stand** as rulings on their 8/16 evidence; this is a new decision on the corrected record under a different card's registered action. C3 is not "re-armed" — this is a fresh candidate that happens to share its escalation number and differs in its donor leg.
- **No void retires** — BRUT/CAPT/TNK stay `POSITION_UNRELIABLE` until R4 executes (WO5 law, PLAN.md:207); no GTC, sizing or watchlist field is touched.

**UNVERIFIED:** CENTCOM's own release text and the UKMTO 124-26 PDF (403 to fetchers; record Appendix B). Everything else above traces to the cited file:line or verbatim quote.
---
# APPENDIX B — verification

**VERDICT: REGISTER WITH CORRECTIONS** — the arithmetic, parity, ΔNAV=0 and non-crude=0 claims all reproduce exactly; the one corrupting defect is the donor leg, which makes the registered "MIN" the larger-impact of the two 3pp variants against the deck's own text. Corrected sentence and numbers in §4.

Method: git status clean before/after (0 lines; no file under `state/ outputs/ inputs/` newer than the run marker). Engine rerun in memory via `_run_scenarios_for_ticker` + `load_watchlist(live_prices=True)` + `_maybe_apply_transactions(…, True)` on all 25 names under PROD / MIN / C3 / +5pp.

## 1. R5 grounds — VERIFIED, ground 1 honestly handled
- R5 verbatim at `toll_cliff:198-199` matches the quote. The §5 "re-bases … priced as ambiguous" text (`:137-139`) is the agent's recommendation, not R5 — the proposal labels it "§5 adds", correctly.
- Ground 1 was jurisdictional: that card's two branches were `mou_base → mou_bear/pre_mou` and `pre_mou → 0` (`toll_cliff:75-78`). The folded card's LEG 2 action now authorises exactly a pre-registered escalation reweight (`reweight_triggers.yaml:41-46`; `:47` status, `:51` deadline, `:52` ruling). Ground 1 does not bind. RECOVERABLE nothing.
- Ground 2: pause end 8/30 corroborated (`record:2-3`; Appendix B table `:88-92`). But "the tape is 12 sessions" is loose — 10 Pareto prints 8/28–9/10, 8 of them post-8/30. RECOVERABLE.

## 2. Premise mapping — partly fit-to-desire
- Deck lines cited all check: `:142` 0.25, `:144-146`, `:149` Q3 [350k,420k,500k], `:226` 0.62, `:229-233`, `:307`, `:309`, `:367`, `:371`, `:373-375`, `:131-136`, `:198-199`, `:225`.
- **"third-party strike" is undefined anywhere in the repo** (sole occurrence `scenario_inputs.yaml:144`; zero hits in METHODOLOGY/decisions/CHANGELOG). Reading Iranian strikes on US bases in Jordan/Bahrain/Kuwait as a third-party strike is an interpretation, not a text match — it is still bilateral US–Iran. "No MoU" was already the state at 8/16 when escalation was held at 0.25 (R1). So on the deck's text the NEW match since 8/16 is 0-of-3 elements; what is genuinely new is persistence (day 12) and the rate level. RECOVERABLE — restate as such.
- **Selective evidence**: the record's Pareto 9/03 "Trump is considering declaring the war with Iran over" and 9/04 "no further flare-up … tanker traffic seemingly moving" (`record:41-42`) are omitted; 9/07 and 9/09 are cited. RECOVERABLE — cite both.
- TD3C prints: all ten VERIFIED from the PDFs ("Average of key routes … VLCC (TD3_C)" scrubber column: 634,500 / 636,100 / 636,100 / 680,200 / 690,300 / 707,700 / 710,000 / 733,600 / 765,400 / 790,800; no-scrubber 783,200 on 9/10). **"risen nine straight sessions" is false** — 9/01 printed 0.0% (flat); seven consecutive rises 9/02–9/10. RECOVERABLE.
- mou_bear "falsified": true but not new — contradicted at R1 (`toll_cliff:182-184`) and deliberately RETAINED at 0.13 as the fee-regime tail R3 points at (`:189-192`; LEG 1 unaffected per `record:73`). This matters for §4.

## 3. §9.10 rerun — REPRODUCED TO THE CENT
Parity: PW-FV and EV% match `state/last_run.json` on all 25 names. Under MIN / C3 / +5pp every table cell in the proposal reproduces (DHT 16.4165/−22.56 · BRUT 5.4147/+6.83 and 5.3532/+5.61 · CAPT 17.9226/−6.20 and 17.7720/−6.98 · +5pp BRUT +8.43, CAPT −5.11). Per-scenario FVs match (DHT 21.5265/14.8571/11.7765; BRUT 8.5438/4.4825/2.4327; CAPT 25.9188/15.5105/10.4884). DHT fv_low = mou_bear FV 11.7765 confirmed.
- **ΔNAV = 0.000000 on all 10, structurally**: `scenarios.py:423` `base_nav = compute_nav(inputs)` precedes any weight use; `:445-449` forward_ref is a FIXED anchor ("decouples the base-case NAV from the scenario set"); weights enter only at `:509` `weighted = Σ w·fv / total_w`. `nav.py` 0 hits for scenario/weight. CONFIRMED.
- Non-crude: 15 names exactly +0.000000 on PW/EV/NAV under all three sets; INSW product 20.3884, TEN product 12.6696 / LNG 7.7399, CMBT dry_bulk 8.9151 / containers 0.5348 unchanged. CONFIRMED.
- Flips: BRUT HOLD→BUY only, under all three sets, BUY-ward, FLAGGED. No unflagged flip. CAPT stays T/S under all (−5.11 at +5pp). CONFIRMED.
- RECOVERABLE: the stated identity ΔPW-FV = Δw×(FV_esc−FV_donor) holds for pure names only; on headline per-scenario FVs it gives INSW 60.45 / TEN 62.27 / CMBT 13.78 vs engine 60.10 / 61.96 / 13.57 (it holds on the crude sleeve). No table number is affected (table = engine output); say so.
- RECOVERABLE: "computed on HEAD (f48ddcd)" — HEAD is `bf2d3ad`; forks.yaml, the folded card and the CMBT Q2 numbers exist only post-f48ddcd, so the run was on the current tree and the hash label is stale. `METHODOLOGY:2567` → the full-quarter bullet is `:2564`. `record:35-36` (MB W36) → `:43`; `record:37-38` (Pareto 9/07, 9/09) → `:44-45`. Tape asof is per-ticker (BRUT `2026-09-09T14:25Z` OSL; 2343 `09-10T03:22Z`), not one `20:00Z` stamp.

## 4. Mass / smallest move — CORRUPTING (the recommendation's number)
Mass = 1.00 in every set (asserted). Escalation never exceeded 0.25 in history — VERIFIED across all six committed weight vintages (07523c5 0.10 · 819ac70 0.25 · 0e65a11 0.10 · fb00ede 0.25 · 6c508fb 0.25 · 42517fe 0.25).

**"3pp is the deck's quantum (C3 itself)" is false**: executed moves were 15pp, 15pp, 5pp; no 3pp move has ever executed and C3 was declined. RECOVERABLE — strike it.

**The donor is the defect.** The deck's own weighting text (`:131-136`) locates the "fast-reverting flare-up" mass in `pre_mou_baseline` ("raised to 0.20 over v1's 0.15 for exactly that reason"); the corrected record's new fact is that the flare-up stopped reverting — on the deck's registered semantics that is the mass that migrates to escalation, i.e. C3's shape. The proposal's own §2 concedes pre_mou's flare-up clause is falsified, then drains mou_bear instead, whose contradiction is 8/16 news that R1 knowingly retained for the R3 fee-regime tail. Because mou_bear has the lowest FV on every name, the labelled "MIN" is the **larger-impact** 3pp variant everywhere (BRUT +3.62 vs +2.40; CAPT +2.42 vs +1.63; adds a second gate breach; BRUT lands 1.83pp past the edge vs 0.61). The move the evidence supports is +3pp from `pre_mou_baseline`; the mou_bear donor is a permissible owner reading but must not be the silence-executing default. (Under the pre_mou donor, BRUT per pp = +0.80pp EV: 1pp → +4.01, 2pp → +4.81 HOLD, 3pp → +5.61 BUY, 0.61 inside the ±2% deadband — the proposal's "don't size to the tripwire" point stands; I do not recommend <3pp.)

Corrected registry numbers (0.28/0.59/0.00/0.13; PW-FV / EV%): DHT 16.32/−23.00 · ECO 42.22/−41.09 · FRO 28.79/−39.03 · INSW 59.91/−42.73 · TNK 83.24/−13.57 · NAT 2.97/−59.21 · TEN 61.80/+39.45 BUY · CMBT 13.54/−30.02 · **BRUT 5.35/+5.61 HOLD→BUY** · CAPT 17.77/−6.98 T/S. ΔEV +0.48..+2.40pp; ΔNAV 0.0; non-crude 0.0; drift-gate breach BRUT only; band = ΔPW-FV ± $0.01 per name.

## 5. Recommendation sentence
Original is 256 chars and faithful to its own numbers except the floor: "+0.5..+3.6pp" — min ΔEV is CMBT +0.65 (RECOVERABLE). Corrected sentence (≈286 chars):

"Crude 0.25/0.62/0.00/0.13 → 0.28/0.59/0.00/0.13: +3pp escalation from pre_mou_baseline (pause ended 8/30, campaign from 9/01, TD3C $790.8k 9/10); ΔNAV 0.0; crude EV +0.5..+2.4pp, non-crude 0.0; BRUT HOLD→BUY predicted +5.6 (masked, owner eyeball, inside deadband); CAPT T/S −7.0."

Keep the proposal's mou_bear-donor set as the documented alternative alongside the hold alternative; the record-line correction on `record:67` (mou_bear vs pre_mou attribution) is correctly owed.

**UNVERIFIED (unchanged from the proposal):** CENTCOM release text, UKMTO 124-26 PDF.