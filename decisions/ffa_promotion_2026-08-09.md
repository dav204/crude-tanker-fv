# FFA dry-bulk promotion — 2026-08-09 (owner: "let's work on the marks/assessment promotion"; sentinel UNINGESTED-PRINTS ffa_forward_curve 14d)

**Decision:** promote the **2026-08-06 FFA print** (newest usable capture) into the three
dry-bulk surfaces. Prior vintage 2026-07-24. No FFA grid exists for 8/07 on disk
(the 8/07 image is a BreakWave X-post: "Capesize flat / Panamax flat" — corroborates
8/06 ≈ 8/07); the 8/05 grid was read as the consistency check.

## The eyeball — image-verified grids vs the OCR queue (this is the record)

Tenor set has ROLLED since 7/24: **Aug / Sep / Q4 / Q1[-27] / Cal27** (was Jul/Aug/Q3/Q4/Cal27).

| Day | Panel | Aug | Sep | Q4 | Q1-27 | Cal27 | OCR-queue errors caught |
|---|---|---|---|---|---|---|---|
| 8/05 (IMG_9544) | Cape | 40,925 | 39,625 | 37,925 | 26,125 | 30,250 | queue dropped Q1 |
| 8/05 | Pmax | 20,900 | 21,525 | **20,825** | 16,400 | 17,150 | **queue misread Q4 20,825→20,625**; dropped Q1 |
| 8/05 | Smax | 19,050 | 20,400 | 19,525 | 14,400 | *cropped* | queue dropped panel entirely |
| **8/06 (IMG_9577)** | **Cape** | **39,875** | **37,725** | **37,250** | **25,875** | **29,900** | queue dropped Sep+Q1 |
| **8/06** | **Pmax** | **20,325** | **20,675** | **20,325** | **16,250** | **16,975** | queue dropped Q1 |
| **8/06** | **Smax** | **18,550** | **19,800** | **19,158** | **14,325** | ***cropped*** | queue dropped panel entirely |

Also triaged from the same image sweep (not FFA): 8/05 IMG_9575 = SBLK Q3-coverage
slide (62% @ $23,547 fleet-wide — sblk_log-grade corroboration of the fresh BUY's rate
leg) · 8/05 IMG_9541 = NMM Form 4 (Frangou 10b5-1 buys — no consumer) · 8/06 IMG_9590 =
Drewry WCI container-spot table (§11.8's source of record is MB — noted only).

## Judgments (three, all documented)

1. **q1 (Q3-26) is now SYNTHESIZED = mean(Aug, Sep)** — the widget no longer quotes Q3
   as a quarterly (rolled to months). Cape 38,800 · Pmax 20,500 · Smax 19,175→19,200
   (nearest-50, half-to-even).
2. **Q1-27 is now PRINTED** (7/24 had only Cal27): q3 = Q1-27 exact; q4-q6 = the level
   set making the Cal27 identity hold exactly (Cape 31,225/31,250/31,250 → 2027 avg
   29,900 ✓; Pmax 17,200/17,225/17,225 → 16,975 ✓). 2028 tail keeps the committed
   deltas off the 2027 exit (Cape −500/−500, Pana −400/−300).
3. **Smax Cal27 is STILL cropped** (both 8/05 and 8/06) → the whole-2027+2028 hold at
   the 7/13 synthesis CONTINUES (7/24 precedent). NEW disclosure: the now-printed Smax
   Q1-27 (**14,325**) vs the held q3 (15,075) says the held year runs **~5% rich** —
   one-sided, rich-side; recorded here and in vintage_notes. Retires at the first
   full capture (the Palun channel ask stands).

## 12M TC proxy — the tenor-roll composition shift (FLAGGED)

Convention (committed 7/13): 12M = mean(Qn, Qf) → 50. The quoted quarterlies rolled
from Q3+Q4-26 (summer+autumn) to **Q4-26+Q1-27 (autumn + the winter TROUGH)** — the
proxy now includes the seasonal low quarter:

| Class | 7/24 12M | 8/06 12M (letter of convention) | Δ | MB Dry W32 1yr (cross-check, NOT calibration) |
|---|---|---|---|---|
| Cape | 35,300 | **31,550** | −10.6% | — (MB prints no Cape TC row; Cape/Ncx ladder only) |
| Pana / PPMX | 19,150 | **18,300** | −4.4% | Kamsarmax 18,750 (−2.4% vs ours) |
| Supra-Ultra | 18,800 | **16,750** | −10.9% | Ultramax 19,250 (**ours −13% vs MB** — the FFA winter leg vs MB's "modern Japanese Pacific prompt" premium basis) |

Roughly half the Cape/Supra drop is the WINDOW composition (Q1-trough entering), not
level: same-tenor drift Q4 37,250 vs 35,725 (7/24 Qf) is −4.2% wait — like-for-like,
the 8/06 Q4 (37,250) vs the 7/24 Q4 (35,725) is **+4.3%** (Q4 FIRMED); the drop is
ENTIRELY the Q1-27 leg replacing Q3-26 in the mean. Cycle-position consumers (dry
tiers) therefore see a 12M step-down that is seasonal-composition, not market
weakness — the drift gate run below carries this note; any dry flip triggered by the
12M leg alone is frozen-for-owner-review per the G6-family discipline.

## Raw anchors promoted (8/06 print, image-verified)

| Panel | m1 (Aug) | m2 (Sep) | Q4-26 | Q1-27 | Cal-27 |
|---|---|---|---|---|---|
| Cape | 39,875 | 37,725 | 37,250 | 25,875 | 29,900 |
| Pmax | 20,325 | 20,675 | 20,325 | 16,250 | 16,975 |
| Smax | 18,550 | 19,800 | 19,158 | 14,325 | HELD 14,175 (7/13) |

## Surfaces written

1. **ffa_forward_curve.yaml**:
   - Cape: 38800 / 37250 / 25875 / 31225 / 31250 / 31250 / 30750 / 30250
   - Pana + Post-Panamax: 20500 / 20325 / 16250 / 17200 / 17225 / 17225 / 16825 / 16525
   - Supra-Ultra: 19200 / 19158 / **15075 / 14475 / 13875 / 13275 / 12975 / 12675 (HELD 7/13)**
   - Handy-Bulk (= Supra × 0.90, guard-rounded): 17280 / 17240 / held ×0.90 unchanged
2. **twelve_month_tc.yaml**: Cape **31,550** · Pana/Post-Panamax **18,300** · Supra-Ultra
   **16,750** (mean(Q4,Q1)→50; the composition note above rides the entry).
3. **spot_tce.yaml** (front-month proxy, Pareto dry silence CONTINUES — 8/7 daily
   carries dry PROSE only, "cape-rates above $40,000/day in early August" ✓ corroborates):
   Cape **39,875** · Pana/PPMX **20,325** · Supra-Ultra **18,550**.
4. as_of default → **2026-08-06** all three files (dry lines ride default; every
   explicit hold/override unchanged).

## Verification (fill-in at close)

- Identities: Cape 2027 (25875+31225+31250+31250)/4 = 29,900 ✓ · Pana (16250+17200+
  17225+17225)/4 = 16,975 ✓ · Supra held legs byte-identical ✓ · Handy = Supra×0.90
  under the nearest-10 half-even guard ✓.
- Suite / gate results + any flip dispositions recorded in the commit + log annotations.
