# Container determinant refresh packet — 2026-07-22 (DRAFT for owner promotion; §11.8 event)

**Trigger:** `container_mb_refresh` (registered due 2026-08-07; worked EARLY at owner ask
2026-07-22 after the sentinel's `UNINGESTED-PRINTS containers` flag hit 14d). **Source:** MB
Container Weekly **W28** (assessments 2026-07-10) + **W29** (assessments **2026-07-17** — the
assessment set of record), both staged via the documented Gmail→`mb_harvest` flow
(`inputs/research_mb/container_weekly/2026/`). Promoted basis being diffed: the W27 (2026-07-03)
ingest, `decisions/container_ingest_2026-07-06.md`. **Nothing below is wired — ingestion of
determinants is a deliberate, cited, owner-promoted event. On "promote" the steps at the bottom
execute.**

## The diff (promoted state → W29; every cell read from the W28/W29 p.2 TC table + p.3 assessments)

| Determinant | Promoted (W27 Jul-3) | W29 (Jul-17) | Δ |
|---|---:|---:|---:|
| **Ctr-Feeder 12M TC** = avg(1,100 / 1,700) | 23,750 = avg(17,500 / 30,000) | **24,250** = avg(17,500 / **31,000**) | **+2.1%** |
| Ctr-Intermediate 12M TC (A3) | 46,350 | 46,350 (buckets 35,000 / 37,500 / 45,000 / 55,000 — A3 recomputes to 46,355 ≈ same) | 0 |
| Ctr-Large 12M TC = avg(5,500 / 6,500) | 63,000 | 63,000 (60,000 / 66,000; 5,400 WB 65,000 still excluded, design premium) | 0 |
| Feeder 10-yr value (MB 1,700) | $29.0M | $29.0M (15-yr 23.0) | 0 |
| Other 2nd-hand (2,700: 35.5/32.0 · 5,000WB 63.5 · 6,700WB 75.0 · 9,000WB 97.5) | — | identical W28=W29, all trend → | 0 |
| NB assessments (1,800: 37/32 · 2,800: 52/44 · 5,400: 79/63 · 11,000: 135/115 · 15,000: 170/160) | — | identical W28=W29, all trend → | 0 |
| Ctr forward strips | W27 starts → wire-up terminals (19,000 / 37,200 / 48,000), linear | **feeder strip re-synthesizes only** (start 24,250 → same terminal, linear); intermediate/large strips byte-unchanged | — |

**The entire refresh is ONE cell:** the 1,700-TEU 12M assessment ticked 30,000 → **31,000 in W28
(Jul-10) and HELD in W29** — the same cell that ticked +1,000 in W27. Every other assessed value
across both weeklies is flat with → trends. MBCI eased 1,375 (W28) → 1,356 (W29) but assessments
did not follow.

**A3 shares note:** bucket weights (2,500: 11.5% / 2,700: 21.8% / 3,500: 25.3% / 4,250: 41.4%)
carry over unchanged — no fleet re-derivation owed (MPCC/GSL on-water intermediate fleets
unchanged since the 7/06 derivation; GSL's Jun-26 NB order is future delivery, out of the
on-water buckets by construction).

## Predicted model impact (gate expectations, scaled off the 7/06 elasticity)

- **MPCC:** the 7/06 ingest moved feeder +15.9% → NAV +1.0%, EV −4.4pp (rate lift richens the
  cycle position against a ~99%-covered 2026 book). This refresh is feeder **+2.1%** → predicted
  **NAV ≈ +0.1-0.2%, EV sub-1pp, cycle 1.14x → ~1.16x**; position stays "unreliable read (not
  actionable)". No band flip expected.
- **GSL:** **zero** — no determinant GSL touches moved (intermediate + large flat).
- Drift gate: expect 0 UNEXPLAINED with at most a small explained MPCC row; no re-ratify beyond
  the routine post-promotion absorb.

## Market color (not determinants; dated to the weeklies)

- **Orderbook:** W28 = MSC up-to-20 × 21,000 TEU LNG dual-fuel at Hengli (~$206M/unit, 2029-30;
  ~424k TEU — ultra-large, outside our classes); W29 = ~73,200 TEU of mid-size orders (Guoyu
  6+2 × 6,150; Minerva 4 × 6,000 at Hengli ~$80M/unit, Apr-Aug 2028); EGPN's first container NB
  2 × 1,900 at ~$32M (corroborates the 1,800 NB China 32.0 assessment).
- **Fixtures:** 4,250 'Wadi Bani Khalid' extended at $74,500 × 6mo (short-period premium — the
  12M assessment stays 55,000); 2,800 fixed 12mo at ~42k from a Q3-26 position; Panamax 3-yr
  positions low-to-mid-30s for H1-2027 delivery; 2 × 5,300 WB NBs took 3-yr charters
  high-USD30s basis end-2027 delivery.
- **Governance-adjacent (surface, no action):** W29 2nd-hand — **Capital Maritime sold its four
  3,700-TEU 2007-built "Spirit of—" vessels en bloc, ~$150M with charters attached.** Capital
  Maritime = the CAPT/CCEC sponsor. This is the PRIVATE fleet selling to a third party — NOT a
  §15.7 tripwire (no CCEC dropdown, no CAPT↔CCEC cross-dealing) — but it is sponsor
  capital-recycling color worth having on file the week of the CCEC print (7/29).

## On "promote" (the normal promote→rerun→drift loop)

1. `twelve_month_tc.yaml`: `Ctr-Feeder` 23,750 → **24,250** + vintage stamps `Ctr-*` →
   **2026-07-17** (intermediate/large re-stamp at unchanged values — the vintage is the
   assessment date, not the delta); dated comment citing this packet.
2. Strip re-synthesis: feeder start → 24,250, same wire-up terminal, linear (the documented
   §11.8.6.4 convention); intermediate/large untouched.
3. Pipeline regen; drift-annotate `mpcc_log.md` (cause: this packet); suite + SANITY.
4. Re-arm `container_mb_refresh` → next due **2026-08-21** (monthly from this ingest; the 8/7
   registration was monthly-from-W27).
5. Owner-aware baseline absorb per the standing batch-ratify discipline (this lands inside the
   Q2-cluster window — keep the ingest commit ISOLATED from any report-day refresh commit).
