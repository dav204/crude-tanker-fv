# Container MB refresh packet — 2026-09-10 (trigger container_mb_refresh DUE 2026-09-07; MB Container Weekly 36, 2026-09-04)

**TWO legs, landed SEPARATELY (the 7/22 leg-scaled discipline):**

**Leg A — TC (this commit): EV-only, ΔNAV EXACTLY 0.0 on every row.** Ctr-Feeder 12M 24,250 →
25,500 (1,100: 17,500→19,000; 1,700: 31,000→32,000); Ctr-Intermediate 47,567 (A3 on the 7/06
canonical shares 11.5/21.8/25.3/41.4 over buckets 37,500/40,000/46,500/55,000); Ctr-Large 64,000
HELD (6,500 bucket flat W33-W36). Curve strips re-derived linear to the same terminals (feeder
nearest-250, intermediate nearest-25); Ctr-* as_of → 2026-09-04 on the 12M and curve surfaces
(≤ default). **Spot mirror NOT moved:** spot's default is 2026-08-07 and an override may not be
newer than the default; the mirror waits for the owner's separate spot disposition (comment on
the rows). Value curves untouched in this leg.

Predicted impact (verifier-corrected): unflexed NAV 0.00 on all 25 rows; MPCC EV ≈ −0.7pp, GSL
≈ −0.1pp (the deck's scenario cycle is DECK-driven, not strip-driven — no step fires); CMBT
exactly 0.0; every other name invariant. No band flips. Any nonzero ΔNAV = HALT.

**Leg B — VALUE (separate commit, own band): NAV-moving.** MB 1,700 TEU 10-yr 29.5 → 31.5 (+0.5/wk
W33-W36), 5-yr midpoint 30.0 → 31.75; 2,700 TEU 10-yr 35.5 → 36.0, 5-yr 39.8 → 40.0. Predicted:
MPCC NAV +2.28% / EV +1.25pp, GSL NAV +0.40% / EV +0.27pp, all under the 2pp gate, no flip.
Combined A+B: MPCC ≈ +0.55pp net, GSL ≈ +0.1pp.

Verifier findings folded: Leg A mechanism corrected (deck-driven); GSL Leg A sign corrected
(−0.14pp, not +); Leg B EV was understated in the draft; the A3 census story is the 7/06 IR-page
census (exact-TEU vector not on disk — display-rounded shares used, as the 8/09 packet did); the
landed Ctr-Large strip's "linear-to-250" comment is false (pre-existing, not touched); MB "Julie"
(2,262 TEU) vs gsl.yaml Julie (2,207 TEU) UNVERIFIED — settle via IMO at GSL's Q2 fleet table.

Trigger: outcome recorded on the card; next due 2026-10-02 (the October monthly boundary).

---
# APPENDIX A — the packet (agent, read-only)

# Container MB refresh — W36 packet (READ-ONLY draft, 2026-09-10)

**Trigger** `container_mb_refresh` (due 2026-09-07; sentinel: W36 staged 9/04 vs Ctr vintage 8/07, 28d). **Source of record:** MB Container Weekly 36, assessments **2026-09-04** (`inputs/research_mb/container_weekly/2026/2026-09-04_Container_Weekly_36_2026.pdf`). All cells below are in the pypdf text layer (cited p:line of the extracted text); the **Trend arrows are NOT in the text layer** (glyphs) — direction is read from the week-to-week diff, not the arrow. Diffed basis: W32 (8/07), `decisions/container_mb_refresh_packet_2026-08-09.md`.

## 1. Assessment set — W32 promoted → W33 → W34 → W35 → W36

12M TC (USD/day; W36 p.2:602-619; W33 p.2:559-576; W34 p.2:542-559; W35 p.2:558-575):

| Size | W32 (promoted) | W33 8/14 | W34 8/21 | W35 8/28 | **W36 9/04** |
|---|---:|---:|---:|---:|---:|
| 1,100 | 17,500 | 18,000 | 19,000 | 19,000 | **19,000** |
| 1,700 | 31,000 | 31,000 | 32,000 | 32,000 | **32,000** |
| 2,500 | 35,000 | 35,000 | 37,500 | 37,500 | **37,500** |
| 2,700 | 37,500 | 37,500 | 40,000 | 40,000 | **40,000** |
| 3,500 | 45,000 | 45,000 | 46,500 | 46,500 | **46,500** |
| 4,250 | 55,000 | flat | flat | flat | **55,000** |
| 5,500 | 60,000 | flat | flat | flat | **60,000** |
| 5,400 WB (excluded, §11.8.1) | 65,000 | flat | flat | flat | 65,000 |
| 6,500 | 68,000 | flat | flat | flat | **68,000** |

2nd-hand ($M, 10yr / 15yr; W36 p.3:580-598; W33 p.3:563-581; W34 p.3:605-623; W35 p.3:575-593):

| Size | W32 | W33 | W34 | W35 | **W36** |
|---|---:|---:|---:|---:|---:|
| 1,700 | 29.5 / 23.5 | 30.0 / 24.0 | 30.5 / 24.5 | 31.0 / 25.0 | **31.5 / 25.5** |
| 2,700 | 35.5 / 32.0 | flat | flat | flat | **36.0 / 32.5** |
| 5,000 WB / 6,700 WB / 9,000 WB | 63.5 / 75.0 / 97.5 | flat | flat | flat | flat (15yr "*" no vessels) |

NB assessments (Korea/China; W36 p.3:546-565): 1,800 37.0/32.0 · 2,800 52.0/44.0 · 5,400 79.0/63.0 · 11,000 135/115 · 15,000 170/160 — **identical W32–W36**. MBCI (context only): 1,311 (W32) → 1,418 (W33 p.2:456-457) → 1,351 (W34 p.2:439-440) → 1,376 (W35 p.2:455-456) → **1,364** (W36 p.2:499-500). The FY-average anchor table (W36 p.2:541-594) still prints FY21-25 unchanged; a 2026 YTD column exists (feeder bands 16,939 / 25,051) — not an anchor input.

Market color (W36 p.2 narrative, p.3): CSBC 3,200 'Source Blessing' 2 yrs $45,000 (p.2:440-450); Imabari 2,000 'Marla Bull' 12-14 mo $37,000 (p.2:451-463) — corroborates the 1,700 ladder at 32,000; MSC bought 4,363 'Newnew Panda 1' + 2,262 'Julie' rumoured $13.5M (p.3:44-56) — **'Julie' is a GSL hull under agreed sale** (gsl.yaml disposal flag; $65.5M en-bloc, no per-vessel split) — cross-check only, never back-solve into the manifest.

**This is NOT a one-moving-cell refresh:** five TC cells (all at W33/W34, held W35/W36) and the feeder 10yr ticked +0.5 four weeks running (+2.0 cumulative), the 2,700 10yr +0.5 at W36.

## 2. Re-derived class values (§11.8.1 collapse)

- **Ctr-Feeder 12M** = avg(1,100 19,000 / 1,700 32,000) = **25,500** (was 24,250; +5.2%). Cycle 25,500/20,850 = **1.223×** — crosses the 1.2× band (D-M4 ramp NOT wired, `cycle.py` docstring: steps are live).
- **Ctr-Intermediate 12M (A3)** on the 7/06 canonical shares (2,500: 11.5% / 2,700: 21.8% / 3,500: 25.3% / 4,250: 41.4%; exact-TEU shares declared canonical 7/22 but **not on disk** — only the rounded shares and the 72/256,234 totals are recorded): 0.115×37,500 + 0.218×40,000 + 0.253×46,500 + 0.414×55,000 = **47,567** (was 46,350; +2.6%). Cycle 47,567/33,700 = 1.411×. **A3 fleet-change check:** GSL intermediate on-curve unchanged at 30 (4 agreed sales stay on-curve to delivery); MPCC intermediate on-water 30→29 (AS Clementina, 2,800 TEU, delivered to buyer Q2 — commit a901315). Removing 2,800 TEU from the 2,700 bucket moves the shares to 11.63/20.94/25.58/41.86 → A3 ≈ **47,651** (+$84/day, +0.18%) — sub-gate; but the exact recompute needs the per-vessel TEU census (manifests carry dwt, not TEU) → **Fork F1** below.
- **Ctr-Large 12M** = avg(60,000 / 68,000) = **64,000** — flat, no cell moves.
- **Value-curve cells** (MB → `vessel_value_curves.yaml`): Ctr-Feeder `ten_year_benchmark` 29.5 → **31.5** (+6.8%); Ctr-Intermediate `ten_year_benchmark` 35.5 → **36.0** (+1.4%); NB anchors (32.0 / 44.0 / 63.0) flat; Ctr-Large WB basis (63.5/75.0) flat → 56.0 stands. **Guard conflict:** feeder 10yr 31.5 > `five_year_benchmark` 30.0 → `test_curve_anchors_monotonic` (≥) and `test_containerships_sector::test_market_data_carries_container_classes` (strict >) both RED unless the 5yr moves. The file's own stated convention "5yr = NB↔10yr midpoint" gives feeder (32.0+31.5)/2 = **31.75** and intermediate (44.0+36.0)/2 = **40.0** (file 39.8 = the 35.5-era midpoint; the feeder 5yr was NOT re-derived at the W27/W32 10yr ticks — latent drift, 30.0 vs a 30.75 convention value). → **Fork F2**.

## 3. Exact diffs (one moving cell per line; as_of = assessment date 2026-09-04)

`inputs/market_data/twelve_month_tc.yaml`
- as_of: `Ctr-Feeder: 2026-08-07 # MB W32 …` → `Ctr-Feeder: 2026-09-04    # MB W36 container refresh (2026-09-10 event, packet 2026-09-10)`; `Ctr-Intermediate` / `Ctr-Large` likewise → `2026-09-04`. (Override 2026-09-04 ≤ default 2026-09-09 — `test_as_of_blocks_internally_coherent` OK; Ctr-* remain in the hold set on both 12M and FFA — `test_held_class_sets_agree_across_surfaces` OK.)
- `Ctr-Feeder: 24250 # avg(1,100: 17,500 / 1,700: 31,000) …` → `Ctr-Feeder: 25500         # avg(1,100: 19,000 / 1,700: 32,000) — 1,100 ticked +500 W33 +1,000 W34, 1,700 +1,000 W34; both held W35/W36 — container_mb_refresh_packet_2026-09-10.md`
- `Ctr-Intermediate: 46350 …` → `Ctr-Intermediate: 47567   # A3 on the 7/06 canonical shares (11.5/21.8/25.3/41.4): buckets 37,500/40,000/46,500/55,000 (2,500 +2,500, 2,700 +2,500, 3,500 +1,500 all at W34, held W35/W36; 4,250 flat); Clementina census re-derivation queued (≈+84/day) — packet 2026-09-10` (keep the RE-DERIVED 2026-07-06 census sub-comment).
- `Ctr-Large: 64000` — value unchanged; comment `held W31/W32` → `held W31-W36`.
- Header comment lines 80-82 ("MB Container Weekly 29 assessments (2026-07-17)…") → W36 (2026-09-04), packet 2026-09-10.

`inputs/market_data/ffa_forward_curve.yaml`
- as_of `Ctr-Feeder/Intermediate/Large: 2026-08-07` → `2026-09-04    # MB W36 container refresh (2026-09-10 event)`.
- `Ctr-Feeder:` strip (start 25,500 → same wire-up terminal 19,000, linear, nearest-250 — the 7/22 feeder rounding): `24250/23750/23000/22500/22000/21250/20750/20250/19500/19000` → **`25500/24750/24000/23250/22500/22000/21250/20500/19750/19000`**; comment line "re-synthesized 2026-07-22 (W29 start 24,250 …)" → "re-synthesized 2026-09-10 (W36 start 25,500 → SAME terminal 19,000 — packet 2026-09-10)".
- `Ctr-Intermediate:` (start 47,567 → 37,200, linear, nearest-25 — the 7/06 intermediate rounding): `46350/45325/44325/43300/42275/41275/40250/39225/38225/37200` → **`47567/46425/45275/44100/42950/41800/40650/39500/38350/37200`** + dated comment.
- `Ctr-Large:` byte-unchanged (comment "W32 refresh" → "held through W36").

`inputs/market_data/spot_tce.yaml` (mirror surface, = 12M by convention)
- `Ctr-Feeder: 24250` → `25500`; `Ctr-Intermediate: 46350 # …` → `47567   # A3, W36 2026-09-04 — packet 2026-09-10`; `Ctr-Large: 64000` comment "held W31/W32" → "held W31-W36".
- **as_of: CANNOT stamp `2026-09-04` while `default: 2026-08-07`** (override newer than default → `test_as_of_blocks_internally_coherent` RED), and the 7/22 "containers become default" precedent is closed here: promoting spot default to 9/04 would force explicit 8/07 holds on every tanker class, which are NOT held in `twelve_month_tc` (they ride the 9/09 Stage-B default) → `holds(spot) ⊆ holds(12M)` RED. → **Fork F3**.

`inputs/market_data/vessel_value_curves.yaml` (VALUE leg — separate commit, see §4)
- `ten_year_benchmark: 29500000  # MB 1,700 TEU 10yr 29.5 (W32 …)` → `ten_year_benchmark: 31500000  # MB 1,700 TEU 10yr 31.5 (W36 2026-09-04; +0.5/wk W33-W36 from 29.5; 15-yr 23.5->25.5 same direction corroborates — packet 2026-09-10)`
- `five_year_benchmark: 30000000   # W32 2026-08-07 re-assessed flat` → `five_year_benchmark: 31750000   # NB<->10yr midpoint convention re-applied (32.0+31.5)/2 — was left at the 28.0-era 30.0 through W27/W32; monotone guard requires it — packet 2026-09-10`
- `ten_year_benchmark: 35500000  # MB 2,700 10yr 35.5 (W32 …)` → `ten_year_benchmark: 36000000  # MB 2,700 10yr 36.0 (W36 2026-09-04, +0.5 — first move since Apr-01; 15-yr 32.0->32.5)`
- `five_year_benchmark: 39800000` → `40000000  # midpoint (44.0+36.0)/2`
- Ctr-Large: comment re-dates "W32 2026-08-07 re-assessed FLAT" → "W36 2026-09-04 re-assessed FLAT"; numbers frozen. Block header "last re-assessed MB Container Weekly 29" → W36. The NOTE "MB's 15yr marks (23.0 @1,700 / 32.0 @2,700)" → 25.5 / 32.5.

Also owed: METHODOLOGY §11.8.5 table still reads "Current class rate (2026-07-17)" with large 63,000 / 1.54× — the W32 64,000 was never carried; revise to W36 (25,500 / 47,567 / 64,000 → 1.22× / 1.41× / 1.56×).

## 4. Predicted impact — TWO legs, land separately (the 7/22 leg-scaled discipline)

**Leg A — TC only** (`twelve_month_tc`, `spot_tce`, `ffa_forward_curve`; `vessel_value_curves` FROZEN): **ΔNAV = 0.00 on all 25 rows, to the cent — any nonzero NAV = HALT.**
- **MPCC** (Ctr-Intermediate 72% / Feeder 28% of fleet value; unflexed position 1.316× → 1.359×, stays elevated w_nav 0.60). Scenario numerators are the strip front-4 (feeder 23,375→24,375 +4.3%; intermediate 44,825→45,842 +2.3%): base scenario 1.17× → ≈1.20–1.21× — **sits ON the 1.2× step** (w_nav 0.50→0.60, terminal 1.00→0.95). If it fires: base FV 2.23 → ≈2.17 before the strip lift; strip NPV +1–2% on the uncovered 2027-28 fraction partly offsets. **EV −27.0% → −27.5 to −28.5pp if the step fires, −26.5 to −27.5 if not**; no position change (TRIM/SHORT / unreliable read). This IS the 7/22 D-M4 pre-flagged step event — eyeball owed under D-M5 if it fires.
- **GSL** (Large 70% / Intermediate 30%): position 1.505× → 1.516× (stays peak); all four scenario positions stay in-band (recession 1.21→≈1.22). Strip lead curve is Ctr-Large (unchanged); intermediate share lifts the blended rate ≈+0.7% on a ~100%/86-89% covered book → **EV −4.8% → ≈−4.5 to −4.8 (+0.0 to +0.3pp)**, HOLD stands.
- CMBT: Ctr-* rows in its book (newbuild_convention) — expect sub-0.2pp; any other row moving = HALT.

**Leg B — value** (`vessel_value_curves` only; rate files FROZEN), computed read-only via `compute_nav` on the current Q2 inputs with the four cells above:
- **MPCC NAV/sh 2.1039 → 2.1519 (+2.28%)** (feeder fleet value +3.6%, intermediate +0.55%); 10yr-only variant (F2 alt) +2.17%. Consistent with the W32 elasticity (+0.5 tick → +0.5%).
- **GSL NAV/sh 41.2038 → 41.3701 (+0.40%)** (intermediate +1.16%, large 0.00).
- Every other row **0.00**; EV moves sub-1pp (NAV-led, w_nav 0.6/0.7), no band flip predicted.

## 5. Forks (silence executes the recommendation)

- **F1 A3 census:** land 47,567 on the canonical 7/06 shares; queue the Clementina re-derivation (≈+84/day) for the next MPCC deck with per-hull TEU. Alt: 47,651 on the adjusted shares (uncited per-bucket TEU → violates the citation rule).
- **F2 curve monotonicity:** import both 10yr ticks AND re-apply the file's stated midpoint convention to both 5yr cells (31.75 / 40.0). Alt (a) clamp feeder 10yr at 30.0 (`transactions.py` monotone-clamp analogue, under-marks vs source); alt (b) hold the whole value leg (§11.8.5(b) tilt argument — but the precedent imported the W27/W32 ticks).
- **F3 spot_tce vintage:** Pareto dailies 9/03–9/09 are staged; the 8/31 spot hold deferred "to the next owner round" — that round is this one: refresh spot tankers/dry from the 9/09 daily FIRST (own commit; default → 2026-09-09), then Ctr-* 2026-09-04 is a legal override. Alt: mirror values now, keep Ctr stamps at default 8/07 with the true date in the row comment (28-day vintage understatement on the sentinel lane).

Sequence: fresh price vintage committed alone → spot refresh (F3) → Leg A regen (halt on any NAV ≠ 0) → Leg B regen (halt on any non-MPCC/GSL NAV ≠ 0) → suite/SANITY → ratify citing this packet.

## 6. Trigger card outcome text (`container_mb_refresh`)

```
  due: 2026-10-07   # re-armed 2026-09-10 on the W36 ingest (monthly, the 7th boundary
                    # the last two arms used; was 2026-09-07). Observable CHECKED
                    # 2026-09-10 (3 days late): W36 (9/04) vs W32 basis — FIVE TC cells
                    # (1,100 +1,500 / 1,700 +1,000 / 2,500 +2,500 / 2,700 +2,500 /
                    # 3,500 +1,500, all W33-W34, held W35-W36) + feeder 10yr 29.5→31.5
                    # (+0.5/wk) + 2,700 10yr 35.5→36.0 (W36). Feeder 24,250→25,500,
                    # A3 46,350→47,567 (shares held; Clementina census queued), Large
                    # 64,000 flat. Landed as TWO legs (TC: ΔNAV 0.0 halt; value: MPCC
                    # +2.28% / GSL +0.40% predicted). Feeder cycle 1.16x→1.22x crosses
                    # the 1.2x step (D-M4 pre-flag). Forks F1-F3 + record:
                    # decisions/container_mb_refresh_packet_2026-09-10.md.
```

**UNVERIFIED:** the exact-TEU A3 shares (settled only by a per-hull TEU census); whether the MPCC base-scenario step fires (settled only by the regen).
---
# APPENDIX B — verification

**VERDICT: APPLY WITH CORRECTIONS** — every source cell and every landed number in §1–§3 re-derives exactly; the §4 Leg A prediction rests on a wrong mechanism (deck-driven scenario cycle, not strip-driven), the GSL Leg A sign is backwards, and the A3 census story is mis-framed. Nothing found is CORRUPTING.

## Verified (my own extraction / read-only recompute)

- **W32–W36 cells** (pypdf, all five PDFs under `inputs/research_mb/container_weekly/2026/`): 12M 19,000/32,000/37,500/40,000/46,500/55,000/60,000/65,000 WB/68,000; 2nd-hand 1,700 31.5/25.5, 2,700 36/32.5, WB 63.5/75.0/97.5 (15yr "*"); NB 37/32 · 52/44 · 79/63 · 135/115 · 170/160 identical W32→W36; MBCI 1,311→1,418→1,351→1,376→1,364; W33/W34/W35 ladders exactly as tabled; FY21-25 columns byte-identical W32=W36, 2026 YTD 16,939/25,051; Source Blessing 45,000 2 yrs, Marla Bull 37,000 12–14 mo, Newnew Panda 1 + Julie $13.5M. (Packet p:line cites are off by ≤9 lines vs my extraction — immaterial.)
- **Collapses:** 25,500 · 47,567 (0.115×37,500+0.218×40,000+0.253×46,500+0.414×55,000) · 64,000; cycle 1.2230 / 1.4115 / 1.5610.
- **Strips:** feeder 25,500→19,000 nearest-250 and intermediate 47,567→37,200 nearest-25 reproduce the packet's ten points exactly; front-4 23,375→24,375 and 44,825→45,841.75.
- **Guards:** 12M/FFA override 2026-09-04 ≤ default 2026-09-09 (`test_market_data_vintages.py:22-33`); Ctr-* stay in `holds()` on both surfaces so `holds(ffa)==holds(12M)` holds (`:36-46`); spot 9/04 > default 8/07 would RED — packet correct. F2 values pass both monotone guards (32.0>31.75>31.5>4.0; 44>40>36>5; `test_thread1_resale_anchor.py:52`, `test_containerships_sector.py:85`); no container depreciation-floor test exists (`DEPRECIATION_FLOOR` is crude-`MARKED` only), so the 0.8% new→5yr feeder step passes silently.
- **Leg A ΔNAV = 0.000000** for MPCC/GSL/CMBT via `compute_nav` with the new 12M+strip patched in (nav.py reads only `vessel_value_curves` + balance sheet; `nav.py:80-125`). Unflexed positions 1.3191→1.3615 (MPCC, elevated 0.60/0.95 unchanged; packet's 1.316/1.359 is value-weight rounding), 1.5051→1.5160 (GSL, peak 0.70/0.90).
- **Leg B** via `compute_nav` with 31.5/31.75 + 36.0/40.0: MPCC 2.1039→**2.1519 (+2.28%)**, 10yr-only 2.1494 (+2.17%); GSL 41.2038→**41.3701 (+0.40%)**; CMBT 15.8417 (0.00). Feeder fleet +3.68%, intermediate +0.59% (packet 0.55%).

## Findings

1. **Leg A step-fire mechanism is wrong — RECOVERABLE (rewrite §4 Leg A, §6 card text).** Scenario cycle numerators are the *scenario deck's* base front-4 (`scenarios.py:343` `tc[cls] = sum(_curve(cells,"base",keys)[:4])/4`), not the FFA strip; `inputs/scenario_inputs.yaml` has no container commit since 7/01 (`git log`), and the MPCC base "Cycle" column has printed 1.16×/1.17× across every regen since 8/16 (moved only at the 8/31 manifest refresh). Read-only `run_scenarios` under Leg A: MPCC base scenario stays **1.1654×, w_nav 0.50** — the 1.2× step cannot fire from an MB refresh; no D-M5 eyeball is owed; the 7/22 pre-flag's premise is void under current code (a step can only fire at a deck re-synthesis). The real Leg A channel is unnamed: the strip lifts `forward_ref` (+1.69% MPCC, +0.35% GSL; `scenarios.py:444-468`, elasticity 0.5) → vessel_scale ×0.9917/×0.9982 in every scenario → *flexed* scenario NAV/sh −1.3% MPCC (2.0914→2.0641 disruption) — must be stated so the regen operator does not read the scenario table's NAV column as a halt.
2. **GSL Leg A sign is backwards — RECOVERABLE.** Packet: EV −4.8 → −4.5/−4.8 (+0.0 to +0.3pp). Recompute at $45.02: **−4.75% → −4.89% (−0.14pp)**; MPCC at $2.94: **−27.03% → −27.72% (−0.69pp)** (inside the packet's "fired" band for the wrong reason). No band flips; no position change.
3. **Leg B EV understated — RECOVERABLE.** Packet: "sub-1pp". Recompute: MPCC **−27.03 → −25.78% (+1.25pp)**, GSL −4.75 → −4.48% (+0.27pp). Combined A+B: MPCC −26.48% (+0.55pp net), GSL −4.62%. All under the 2pp gate, no flip. Label the "10yr-only +2.17%" as a counterfactual — 5yr 30.0 < 10yr 31.5 cannot land (both guards red).
4. **A3 census framing — RECOVERABLE (rewrite F1).** 47,567 is correct on the display-rounded shares, but the 7/22 declaration says future recomputes must use the exact-TEU vector, which is nowhere on disk: the 7/06 census was the IR page/PR (MPCC 44/151,246 + GSL 28/104,988, `container_ingest_2026-07-06.md:22-29`), not the manifests, and no manifest bucket rule reproduces 11.5/21.8/25.3/41.4 (closest: nearest-size incl. NBs on the 7/06 manifests → 12.48/23.24/25.78/38.50 → 45,859 at W32 vs promoted 46,350). So the "Clementina-only, +84/day" fleet-change check compares manifests against a census that never was the manifests (GSL's Q1 PR also excluded Manet+Kumasi = 4,508 TEU exactly, which the manifest carries). A current-manifest census (71 hulls incl. NB, 249,696 TEU, nearest-size) gives **≈47,219 (−348/day, −0.7%; cycle 1.401 — same band)**. Also: the manifests DO carry per-hull TEU in the cited row comments (`mpcc.yaml:43-102`, `gsl.yaml:73-102`), contradicting "manifests carry dwt, not TEU" — queue the re-derivation from them with an explicit, written bucket rule; drop the +84 figure.
5. **Unnamed cells the diff must touch or explicitly leave — RECOVERABLE.** (a) `twelve_month_tc.yaml:37` and `ffa_forward_curve.yaml:37` default-block comments "containers 8/07 (W32)" go stale (comment-only, untested). (b) §6 card text omits the two NAV-moving 5yr re-derivations (31.75/40.0). (c) "Feeder cycle 1.16x→1.22x crosses the 1.2x step" is misleading — the step reads the fleet-weighted position (`cycle.py:133-134`), already 1.32× elevated; reword. (d) CMBT: Ctr-Large strip byte-unchanged → CMBT is exactly 0.0 on NAV, position (1.8676) and forward_ref — tighten "sub-0.2pp" to "exactly 0.0, any movement = HALT".
6. **F3 executes an un-packeted tanker+dry spot promotion under "silence executes" — RECOVERABLE.** The recommended path is test-legal (spot default→9/09 leaves holds {LNGC 8/06, MGC, Handy-Bulk, Ctr-* 9/04} ⊆ 12M holds; 9/09 daily is staged at `inputs/research_pareto/2026/09/`), and spot is display-grade (`spot_tce.yaml:18-24`: breakeven/validate only, not the strip), but it needs its own one-line predicted-impact (breakeven columns move; NAV/EV 0.0). The alt (mirror values, keep 8/07 stamps) is also legal — no test pins spot Ctr == 12M Ctr.
7. **Pre-existing, out of scope — RECOVERABLE.** The landed Ctr-Large strip (`ffa_forward_curve.yaml:317-327`: 55,250/53,500/51,750/50,000) is not "linear-to-250" as its comment claims (nearest gives 55,000/53,250/51,500/49,750). Correct not to touch it here; the comment is false.
8. **Cross-check identity UNVERIFIED (nothing rides on it).** MB "Julie" is 2,262 TEU blt 2002; `gsl.yaml:102` Julie is 2,207 TEU, age 24.05 (built 2002). Same build year, TEU differs — settle via IMO in GSL's Q2 fleet table. `gsl.yaml` has no per-row disposal field; the "flag" is the header comment (`:6-9`).

**Corrected gate expectations to carry into the packet:** Leg A — unflexed NAV 0.00 on all 25 rows (verified structurally), MPCC EV ≈ −0.7pp, GSL ≈ −0.1pp, CMBT exactly 0.0, scenario NAV columns flex −1.3%/−0.2% (not a halt), no step. Leg B — MPCC NAV +2.28%/EV +1.25pp, GSL NAV +0.40%/EV +0.27pp, every other row 0.00.