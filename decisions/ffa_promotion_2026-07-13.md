# FFA dry-bulk promotion — 2026-07-13 (owner-ratified, all three classes)

**Decision:** promote the 2026-07-13 FFA OCR print (status **ok**, no flags;
source `inputs/ffa_drybulk/2026/07/2026-07-13_Clipboard - 13 juli 2026 09:17.png`
→ `state/ffa_ocr_curves.json`) into the three dry-bulk market-data surfaces.
Owner ratified in-session 2026-07-13 ("promote changes to all three classes")
after reviewing the Cape diff + the Pana/Supra deltas. Prior vintage: 2026-07-02.

## Raw anchors promoted (13-Jul widget)

| Panel | m1 (jul) | m2 (aug) | Qn | Qf | Cal-27 |
|---|---|---|---|---|---|
| Cape | 36,000 | 34,625 | 35,416 | 35,200 | 28,600 |
| Pmax | 20,000 | 19,450 | 19,716 | 19,250 | 16,200 |
| Smax | 19,050 | 18,800 | 18,800 | 17,875 | 14,175 |

## Surfaces written (conventions preserved per-class; ONLY market anchors moved)

1. **`ffa_forward_curve.yaml`** — mapping rule per the file header: q3_2026 = Qn
   rounded to nearest 50; q4_2026 = Qf exactly; four 2027 quarters decay linearly
   (per-class step: Cape −1,000 / Pana −600 / Supra −600) and AVERAGE to Cal-27;
   2028 preserves each class's committed tail deltas (Cape −500/−500, Pana
   −400/−300, Supra −300/−300). Rebuild of the 2-Jul committed strips under these
   conventions is **byte-exact** for all three classes (verified twice: in-session
   + independent workflow agent). Post-Panamax mirrors Pana (§11.7.10).
   - Cape: 35400 / 35200 / 30100 / 29100 / 28100 / 27100 / 26600 / 26100
   - Pana + Post-Panamax: 19700 / 19250 / 17100 / 16500 / 15900 / 15300 / 14900 / 14600
   - Supra-Ultra: 18800 / 17875 / 15075 / 14475 / 13875 / 13275 / 12975 / 12675
     (75-ending values: the average-to-Cal identity binds; Cal-27 printed 14,175)
2. **`twelve_month_tc.yaml`** — 12M TC proxy = mean(Qn, Qf) rounded to nearest 50
   (the documented 2-Jul rule): Cape 35,300 · Pana/Post-Panamax 19,500 ·
   Supra-Ultra 18,350.
3. **`spot_tce.yaml`** — dry-bulk rows re-proxied to the FFA **front month (jul)**:
   Cape 36,000 · Pana/Post-Panamax 20,000 · Supra-Ultra 19,050. Basis change from
   the 2-Jul Pareto-daily spot prints is deliberate: **no Pareto daily exists**
   (seasonal silence to ~Sep-1, PLAN 3b-ii); extends the 2-Jul Supra-Ultra
   FFA-proxy precedent to Cape/Pana for the silence window. Revert to daily spot
   prints when the dailies resume.

**as_of restructure (all three files):** `default` → 2026-07-13 (= newest
deliberate refresh event per the WO2 1.2 semantics); dry-bulk overrides removed
(ride the default); containers now explicit holds at 2026-07-03. Clears the
sentinel's OCR→FFA UNINGESTED-PRINTS lane (newest widget == default). A dated
`vintage_notes` entry was added so the scorecard handoff announces the re-anchor.

## Market shape note

**The Cape front flipped to BACKWARDATION** (q3 35,416 > q4 35,200; 2-Jul was
contango 32,508 < 33,650) — near-dated C5TC spike (the same move that fired the
governance dry-bulk tranche-2 add trigger on 2026-07-13), Cal-27 barely moved
(+2.1%). Faithfully captured — raw anchors, no re-level.

## Verification (all run 2026-07-13)

- **Suite:** 567 passed + 16 xfailed after the as_of restructure (the two
  `test_market_data_vintages.py` reds the mid-state produced are the designed
  guards; both green at the final state).
- **Adversarial workflow** (3 read-only agents): strip-math independent
  re-derivation PASS (0 findings); YAML-hygiene PASS (diff touches only intended
  surfaces; 16 other class arrays byte-identical); consumer-sweep PASS (no test
  pins the dry-bulk tenors — no re-pins needed).
- **Delta isolation** (13:00 UTC pre-change run → 15:31 UTC post-change run,
  identical prices): only the five dry-bulk-exposed names moved — scenario PW FV
  CMDB −1.2% · SBLK −1.8% · GNK −1.7% · CMBT −2.0% · SB −2.6%; single-point FVs
  +0.3–0.6%; **no band flips from the re-anchor itself**. Mechanism: front-end
  rates up → cycle position richer → heavier strip discount at the blend.
- **Reconcile:** SBLK SANITY=OK (−9.2%) · GNK OK (−10.3%) · CMBT OK (−20.7%) ·
  SB n/a-APPROX (+39.4%) · CMDB n/a-APPROX (+12.6%); all Δ vs last +0.0pp —
  NAV-side untouched, as an FFA-side re-anchor must be.
- **Drift gate:** the live gate holds 18 UNEXPLAINED at this state — the
  DOMINANT term is Jul-10→Jul-13 price-vintage drift (ΔNAV 0.0% on every name),
  the same class as owner decision #1 resolved 2026-07-10; the FFA component
  rides only the five dry-bulk names. Ratify ruling staged for the owner —
  see "Owner queue" below.

## Finding logged in passing — queue m1/m2 column mislabel (fixed value, open code)

`ffa_ocr._write_queue`'s `fmt()` sorts month tenors **alphabetically**, so for
Jun/Jul/Aug prints the queue's "m1" column is not the front month ("aug" < "jul"
< "jun" lexically). Consequence found: the **2-Jul Supra-Ultra spot proxy took
18,500 — the AUG value — while the true front month (jul) was 18,975** (−2.6%,
display-only surface, never fed the strip). Today's spot proxies use the true
front month from the JSON, not the queue column. **Open item:** fix `fmt()` to
chronological month order + a regression test, so the queue header's m1/m2
labels are honest. (Compounding-knowledge rule: guard over prose.)

## Owner queue arising from this promotion

1. **Baseline re-ratify** (`./scripts/ratify_baseline.sh "<cause>"`) — the
   Jul-10→13 price-vintage drift (13 non-dry-bulk names UNEXPLAINED, ΔNAV 0.0%)
   + the FFA-annotated five. Band flips needing INDIVIDUAL eyeballs per the
   don't-batch-accept rule: **BRUT** TRIM/SHORT→BUY (+56.1pp — biggest mover),
   **CAPT** TRIM/SHORT→HOLD (+24.0pp), **ASC** BUY→HOLD (−6.9pp), **GNK**
   HOLD→TRIM/SHORT (−6.1pp; the flip was already present pre-FFA at the 13:00
   state on price alone, and GNK's price is tender-pinned to Jul-24 — read
   through the deal lens, gnk_log).
2. ~~The `fmt()` chronological-sort fix + test~~ — **DONE same session** at
   `3a77235` (fix + regression test incl. the Dec→Jan wrap; queue regenerated).
3. ~~Spot-basis reversion trigger~~ — **REGISTERED same session**:
   `drybulk_spot_daily_resumes` (due 2026-09-01, sentinel-paged) in
   `inputs/reweight_triggers.yaml`.
