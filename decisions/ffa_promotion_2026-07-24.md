# FFA dry-bulk promotion — 2026-07-24 (owner-directed: "eyeball the flagged OCR rows and promote the curves")

**Decision:** promote the 2026-07-24 FFA print into the three dry-bulk market-data
surfaces, after a full human eyeball of ALL flagged OCR rows (7/21–7/24) against
their source images. First promotion from the NEW sender's captures
(Chris.Palun phone screenshots, stacked layout — see CHANGELOG 2026-07-24);
prior vintage 2026-07-13 (Joeri widget).

## The eyeball — every flagged row vs its source image (this is the record)

| Day | Panel | Jul | Aug | Q3 | Q4 | Cal27 | OCR errors caught by the eyeball |
|---|---|---|---|---|---|---|---|
| 7/21 | Cape | 34,175 | 31,875 | 33,600 | 34,675 | 28,675 | OCR dropped Q3+Cal27 rows |
| 7/21 | Pmax | 19,825 | 18,625 | 19,250 | 18,900 | 16,350 | — (all 5 exact) |
| 7/21 | Smax | 19,425 | 18,800 | 19,050 | 18,075 | *cropped* | OCR dropped Q3 |
| 7/22 | Cape | 34,675 | 32,750 | 34,266 | 35,125 | 28,875 | OCR dropped Aug+Q3 |
| 7/22 | Pmax | 19,650 | 18,550 | 19,141 | 18,950 | 16,375 | — (all 5 exact) |
| 7/22 | Smax | 19,450 | 18,825 | 19,091 | 18,200 | *cropped* | **OCR misread Aug 18,825→18,625 AND Q4 18,200→16,200** |
| 7/23 | Cape | 35,125 | 33,875 | 34,950 | 35,500 | 28,950 | (PM capture 9255) OCR dropped Q3; **misread Cal27 28,950→23,950** |
| 7/23 | Pmax | 19,600 | 18,600 | 19,200 | 19,050 | 16,450 | OCR dropped Q3 |
| 7/23 | Smax | 19,450 | 18,800 | 19,125 | 18,300 | *cropped* | **OCR misread Aug 18,800→138,800** (guard caught the 3x spread) |
| **7/24** | **Cape** | **35,175** | **33,625** | **34,891** | **35,725** | **29,175** | promotion basis (IMG_9272) |
| **7/24** | **Pmax** | **19,600** | **18,625** | **19,158** | **19,100** | **16,425** | promotion basis |
| **7/24** | **Smax** | **19,450** | **18,725** | **19,108** | **18,450** | ***cropped*** | promotion basis; Cal27 structurally absent |

Every OCR error above was inside a FLAGGED row — the guards (day-move band,
intra-curve spread, incomplete grid) caught 100% of the misreads; nothing wrong
sat in an "ok" row. The db entries stay flagged; THIS document is the eyeball
disposition. Also triaged from the same staging sweep: `2026-07-24_IMG_9273.jpg`
is a DHT fleet-update PR (→ dht_log triage entry, not a widget);
`2026-07-23_IMG_9252.jpg` is a Drewry WCI container-spot table (no consumer;
§11.8's source of record is MB — noted, not staged further).

## THE ONE JUDGMENT — Smax Cal27 is cropped out of every capture (held node)

Palun's viewport cuts the Smax panel at Q4 in all four days' captures. The
freshest Smax Cal27 print therefore remains the **7/13 value 14,175**. Per the
held-node precedent (tanker held curves / age-5 WIDE flag): promote what
printed — Supra front (q1/q2, 12M proxy, spot proxy) moves to 7/24 — and HOLD
the Cal27-derived back half of the Supra strip (four 2027 quarters + 2028 tail)
at its 7/13 synthesis. Estimated staleness risk is small (Cape Cal27 moved +2.0%
over the same 11 days; Pmax Cal27 +1.4%) and one-sided rich-side conservative if
Smax Cal27 drifted up. Disclosed in `vintage_notes` (rides into the scorecard
Rate-basis header). **Retires at the next capture showing Smax Cal27 — owner:
one channel ask to Palun ("include the Smax Cal27 row when you screenshot")
resolves this permanently.**

## Raw anchors promoted (7/24 print, human-verified)

| Panel | m1 (jul) | m2 (aug) | Qn | Qf | Cal-27 |
|---|---|---|---|---|---|
| Cape | 35,175 | 33,625 | 34,891 | 35,725 | 29,175 |
| Pmax | 19,600 | 18,625 | 19,158 | 19,100 | 16,425 |
| Smax | 19,450 | 18,725 | 19,108 | 18,450 | HELD 14,175 (7/13) |

## Surfaces written (7/13 conventions preserved byte-for-byte; only anchors moved)

1. **`ffa_forward_curve.yaml`** — q1 = Qn→50, q2 = Qf exact; 2027 linear decay
   averaging to Cal-27 (committed steps Cape −1,000 / Pana −600 / Supra −600);
   2028 committed tail deltas (Cape −500/−500, Pana −400/−300, Supra −300/−300):
   - Cape: 34900 / 35725 / 30675 / 29675 / 28675 / 27675 / 27175 / 26675
   - Pana + Post-Panamax (§11.7.10): 19150 / 19100 / 17325 / 16725 / 16125 / 15525 / 15125 / 14825
   - Supra-Ultra: 19100 / 18450 / **15075 / 14475 / 13875 / 13275 / 12975 / 12675 (HELD 7/13 — Cal27 node)**
   - Handy-Bulk (= Supra × 0.90, §11.7.11): 17190 / 16600 / then held ×0.90 values unchanged
     (16600 not 16605: the identity guard rounds to nearest 10 with round-half-to-even — the guard IS the convention)
2. **`twelve_month_tc.yaml`** — mean(Qn,Qf)→50: Cape **35,300** (unchanged) ·
   Pana/Post-Panamax **19,150** (−1.8%) · Supra-Ultra **18,800** (+2.5%).
3. **`spot_tce.yaml`** — front-month proxy (Pareto silence to ~Sep-1): Cape
   **35,175** · Pana/Post-Panamax **19,600** · Supra-Ultra **19,450**.

**as_of restructure (all three files):** `default` → 2026-07-24; dry-bulk
overrides removed (ride default); containers → explicit holds at 2026-07-17;
Handy-Bulk keeps its 2026-07-10 MB-cadence hold (12M side) / derived-row note
(curve side). Trigger `container_mb_refresh` unaffected (re-armed 8/21).

## Market shape note

**The Cape quarterly front flipped BACK to contango** (Qn 34,891 < Qf 35,725;
the 7/13 print was backwardated 35,416 > 35,200) — the near-dated war/C5TC spike
has rolled into Q4 strength instead. Cal-27 +2.0% over 11 days; Pmax little
changed (12M −1.8%); Supra front firmed (+2.5% 12M). Faithfully captured — raw
anchors, no re-level.

## Verification (fill-in at close)

- Strip identities re-checked by hand: Cape 2027 mean (30675+29675+28675+27675)/4
  = 29,175 ✓ · Pana (17325+16725+16125+15525)/4 = 16,425 ✓ · Supra held legs
  byte-identical to 7/13 ✓ · Handy-Bulk = Supra × 0.90 under the guard's round-half-to-even-to-10 ✓ (caught my hand-rounded 16605 → 16600).
- Suite / reconcile / drift-gate results recorded in the commit + log
  annotations (SB/SBLK/GNK/CMDB/2343/CMBT gate rows annotated to this record).
