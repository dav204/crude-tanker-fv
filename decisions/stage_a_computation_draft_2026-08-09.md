# Stage A tanker forward re-anchor — COMPUTATION DRAFT (2026-08-09, NOT YET WIRED)

**Status: DRAFT pending four owner rulings (§5 below).** Method executed to the letter of
the frozen `PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md` (§§1-4) on the basis landed
through 2026-08-08 close; every §5 band was checked and the breaches investigated before
any value is proposed. Nothing in `ffa_forward_curve.yaml` / `twelve_month_tc.yaml` /
`spot_tce.yaml` moves until the rulings land. Minimum viable basis (§6): **MET** — direct
anchors in VLCC + Suezmax + MR/LR2-family, Aframax single-print (3+ of 4 majors with
VLCC among them).

## 1. Evidence set (qualifying under §1, fixtures concluded ≥ 2026-06-15)

**Front (Q3-2026 QTD spot bookings):**
- VLCC: ECO **$206,600** (48% of spot days, 6-K 8/4) · DHT **$152,700** (58%, Q2 ER 8/5 —
  SUPERSEDES the stale 7/13 $139.7k print, newest-wins) → median **179,650**
- Suezmax: TNK **$104,800** (44%, 7/29) · ECO **$133,000** (42%, 8/4) → median **118,900**
- Aframax(+LR2 dirty, blended): TNK **$59,900** (44%, 7/29) → single-print
- LR2_clean: STNG **$65,000** (34%, 7/30) → single-print
- MR: STNG **$29,000** (46%) · ASC **~$29,600** (~45%) → median **29,300**
- Handymax: STNG **$20,800** (38%) → single-print

**~1-year bucket (9-15mo fixtures):**
- VLCC: BRUT "Mount Horizon" 12-15mo **$105,700/day** (Pareto daily 8/6; **dual-fuel
  scrubber NB, Nov-26 yard delivery — spec-premium unit, VLCC per BRUT manifest**) — N=1
- MR: Baltic Champion 10-12mo 30,000 (2026-blt) · Sea Eagle 12mo 32,000 (2019, scrubber) ·
  Golden Horizon 9-15mo 25,000 (2008) · Midnight Glory 12mo 28,500 (MB W29) → **N=4,
  median 29,250** (direct 12M anchor)
- LR2_clean: Torm Herdis 12mo **$51,500** (MB W32; 2018 scrubber LR2, Petrochina) — N=1
- **EXCLUDED — STI Guide +1y option @ $33,000**: an OPTION EXERCISE prices at the strike
  agreed when the original charter was signed, not at today's market — not a fresh print.

**Term (≥21mo):**
- VLCC: DHT Jaguar 36mo **$75,000** (double-sourced; DHT Q2 ER term-book avg $75,900
  corroborates) — N=1
- Aframax: Blue Moon 24mo front-loaded **43,000/38,000** (year-1/year-2 printed legs) — N=1
- MR: STI Notting Hill 25,000×3y + STI Westminster 25,000×3y + STI Bronx 23,900×3y (all
  2015-blt MRs per the 6-K) + Midnight Glory 36mo 23,800 + Sunny Beach 24mo 25,000 (MB
  W31, 2009 scrubber MR) → **N=5, median 25,000**
- LR2_clean: **STI Rambla 8y $30,500 EXCLUDED** — Mar-26 start, concluded pre-6/15 (§1.3)

## 2. Proposed strips (Q1-2 / Q3-4 [=12M] / Q5-8), with provenance tags

| Class | Q1-2 (front) | 12M / Q3-4 | Q5-8 (term) | Tags |
|---|---|---|---|---|
| VLCC | **179,650** | **[owner: 127,300 or 105,700]** | **48,850** | front direct N=2 · 12M see D-2 · term single-print §3-decomposed |
| Suezmax | **118,900** | **69,900** (or 58,050 under D-2b) | **26,950** | front direct N=2 · 12M+term derived-ratio (donor VLCC; Jun-7 ratios .549/.552) |
| Aframax | **59,900** | **51,450** | **38,000** | front single-print (TNK blended) · 12M derived-interp · term = Blue Moon printed year-2 leg |
| LR2 (dirty) | 59,900 | 51,450 | 38,000 | = Aframax (TNK blends the classes; Jun-7 strips identical) |
| LR2_clean | **65,000** | **51,500** | **[owner: 28,000 or 44,000]** | front+12M single-prints · term see D-3 |
| LR1 | 59,900 | 51,450 | 38,000 | derived-ratio (donor LR2 dirty, Jun-7 ratio 1.0) |
| LR1_clean | 46,400 | 37,000 | 20,250-31,800 (tracks D-3 ×.7225) | derived-ratio off LR2_clean (Jun-7 per-bucket .714/.718/.723) |
| MR | **29,300** | **29,250** | **25,000** | ALL DIRECT (N=2/4/5) — the strongest legs in the book |
| Handymax | **20,800** | 20,750 | 17,750 | front single-print · 12M/term MR-shape scaled ×.71 |
| Handysize | 20,800 | 20,750 | 17,750 | derived-ratio (donor Handymax) |

§3 decomposition (VLCC): year-1 decays 179,650 → 75,000 linearly (avg 127,325); years
2-3 level 48,838 makes the 36mo tenor-average hold. Backwardation holds in every class
under either D-2 option.

**Cross-checks (recorded, NOT calibration):** MB W32 1yr/3yr — VLCC 117,500/72,500 ·
Suez 75,000/47,500 · Afra 52,500/39,000 (ours 51,450/38,000 ✓) · LR2[TC1-clean]
52,500/39,000 (our 12M 51,500 ✓; term low, see D-3) · LR1[TC5-clean] 37,000/30,000
(our LR1_clean 12M 37,000 — exact) · MR 29,000/23,500 (ours 29,250/25,000 ✓ transacted).
The derived Suez/VLCC term legs sit far BELOW MB's 3yr assessments — the §3 decomposition
of one flat fixture against a hot front mechanically depresses the back (see D-1b).

## 3. §5 registered-band scoreboard + investigations

| Check | Band | Computed | Verdict |
|---|---|---|---|
| VLCC front | 120-155k | **179,650** | **BREACH-HIGH** — investigated, input REAL (see below) |
| VLCC 12M | 90-130k | 127,300 (D-2a) / 105,700 (D-2b) | INSIDE either way |
| VLCC term-implied | 55-90k | **48,850** | **BREACH-LOW** — mechanical consequence of the hot front |
| Suez/VLCC 12M | 0.55-0.80 | 0.549 (D-2a, by construction) | at-edge INSIDE |
| Afra/Suez 12M | 0.75-1.05 | **0.736** | **MARGINAL-LOW** (0.886 under D-2b) |
| MR 12M | 18-32k | 29,250 | INSIDE |
| Backwardation all classes | front ≥ 12M ≥ back | holds | INSIDE |

**Front-breach investigation (the §5-mandated look, completed):** no unit error (both
prints are $/day QTD bookings with booked-day shares from 6-Ks); no mislabeled tenor;
no sanctioned-tape contamination (ECO/DHT compliant fleets). The assessed tape
CORROBORATES: MB VLCC basket spot 242,270 (7/31) → 246,906 (8/7); Pareto TD3C eco
439,500 (8/6) → 488,900 (8/7) with TD22 ~128k; BreakWave 8/7 AM "VLCC +7%". Both
issuer prints sit BELOW the current assessed tape. **The breach is the market**: the
bands were frozen 7/15, five days BEFORE the 7/20 Houthi blockade escalation; the war
bid moved beyond them. The low term-implied back is the same input propagating through
the registered tenor-average conservation (sensitivity: on DHT's print alone, front
152,700 / term 55,575 — ALL VLCC bands pass; the entire tension is ECO's $206.6k level,
which is verified real).

## 4. Batched riders (execute WITH the promotion)

- **DHT Jaguar coverage update** (ruling §7, dht_log §7): manifest DHT_Jaguar →
  time_charter @ 75,000, charter_end 2029-08-31; `spot_coverage_pct.VLCC` 0.55 → 0.52
  (12 of 23 operating on spot after the flip; 6-K acc 0000950157-26-000799 + Q2 ER).
- **spot_tce.yaml promotion** from the Pareto 8/7 daily (ECO no-scrubber column):
  VLCC 488,900 (TD3C; TD22 128,300 noted) · Suez 77,600 · Afra 75,400 · LR2-dirty
  proxies Afra 75,400 · LR2_clean 92,200 · LR1_clean 95,300 · MR-East 31,500 (West
  24,600 noted) · Handies 31,500 (proxy MR, convention) — plus **LNGC 65,000 / DFDE
  basis from MB W32** (first LNG spot print since the 6/07 hold; MGC stays held).
- C-2 rates layer rerun; full regen; drift gate with the ADDENDUM flip inventory
  (TRMD BUY +8.0% post-marks — expected drift toward the +5 boundary; ANY flip toward
  BUY = halt-and-investigate); one ratify citing the prereg; trigger re-armed to its
  original text; RATIFY_LOG entry.

## 5. OWNER DECISION POINTS (the draft blocks here)

- **D-1a. VLCC front 179,650 breaches 120-155k.** Investigation complete, input real.
  Accept the computed median? (My rec: ACCEPT — the band did its job; the prereg's
  response to a breach is input investigation, not output adjustment, and the input
  verified.)
- **D-1b. VLCC term-implied 48,850 breaches the 55k floor** (same input, mechanically).
  Accept? (My rec: ACCEPT with the sensitivity documented; Stage B's ±10% gate
  re-checks when FRO/HAFN/TRMD land, and a dailies/weeklies 12M print supersedes at
  any time under Rider 4.)
- **D-2. VLCC 12M line**: (a) §2-letter derived-interp **127,300** (the ~1yr bucket
  has N=1 < 2, so the line interpolates front↔term; lands at the band edge) vs
  (b) the Mount Horizon print **105,700** tagged single-print (§3's N=1-used rule; a
  spec-premium dual-fuel NB, but a REAL 12-15mo fixture; also repairs the Afra/Suez
  structure ratio to 0.886). MB assesses 117,500 between them. (My rec: **(b)** —
  a transacted print over an interpolation, single-print + spec-premium tags carried;
  it is also the conservative choice for the strip.)
- **D-3. LR2_clean term**: (i) §4-letter Jun-7 clean/dirty ratio on the Afra back leg →
  **28,000** (the Jun-7 ratio is WAR-INVERTED — clean below dirty — and encodes that
  distortion) vs (ii) MR term-shape on the LR2_clean 12M → **44,000** (donor-shape,
  cleaner economics, nearer MB's 39,000 assessment but NOT registered §4 language).
  (My rec: **(i) 28,000** — the registered letter; flag the distortion; HAFN 8/28 /
  TRMD 8/26 at Stage B are the natural correction venue.)
- **D-4. Timing**: execute now on the 8/8-close basis, or **wait for INSW tomorrow
  (8/10 pre-market)** — the last major crude name before the window, directly
  strengthens the two thinnest legs (Aframax single-print → N≥2; possibly LR1's first
  print) and adds a third VLCC/Suez front print to the breach-sensitive medians; BRUT
  (8/13, H1) is marginal. The prereg's own basis language is "everything landed by
  Aug-14 close." (My rec: **wait for INSW**, wire 8/10 after the pre-market print —
  still 5 days inside the deadline; one promotion, one ratify, prereg-faithful.)

---

## OWNER RULINGS (2026-08-09, in-session — the draft unblocks)

- **D-4 RULED: WAIT FOR INSW** (8/10 pre-market) — Stage A wires 2026-08-10 after the
  INSW print: run the INSW report-day refresh FIRST (pair flow), extract its Q3 QTD
  bookings + any fixtures, RECOMPUTE the §2 medians and §5 checks with the new prints
  (Aframax off single-print; LR1 possibly direct; VLCC/Suez front medians three-wide),
  then one promotion + one ratify. BRUT 8/13 rides Stage B unless Rider 4 fires.
- **D-1a/b RULED: ACCEPT POST-INVESTIGATION** — the computed VLCC front/term stand as
  recomputed tomorrow; breach documentation carries into the promotion record verbatim.
- **D-2 RULED: MOUNT HORIZON $105,700** sets the VLCC 12M line, tagged single-print +
  spec-premium (dual-fuel NB); derived-interp rejected. Suezmax 12M consequently
  derives to ~0.549 × the ruled VLCC 12M (≈58,050 pre-INSW; recomputes tomorrow).
- **D-3 RULED: §4 LETTER $28,000** for LR2_clean term, war-inverted-ratio distortion
  flagged in vintage_notes; Stage B (HAFN 8/28 / TRMD 8/26) is the correction venue.

Standing items into tomorrow's wiring: the §4 batched riders (DHT Jaguar coverage +
spot_tce promotion incl. the LNGC 65,000 MB W32 print + C-2 rerun + ADDENDUM flip
inventory with TRMD's BUY under the halt-toward-BUY rule) execute with the promotion;
SBLK's 8/09 BUY→HOLD band-mech flip remains FROZEN-FOR-OWNER-REVIEW (composition-
driven; one-word disposition at review); the watchlist vintage rebase docket item is
now URGENT-adjacent (the k_broker premium collapsed to ~1.00-1.04 partly on pnav
vintage skew — rebase re-reads it cleanly).
