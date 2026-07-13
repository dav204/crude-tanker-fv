# crude_doha_talks_resumption — trigger check, 2026-07-12 (owner-prompted)

**Verdict: the STRIKE leg FIRED 2026-07-07/08 — the pre-registered restore is OWED.**
Checked 5 days after the event: the trigger was due Jul-10 but the watch layer was mute during
install week; the sentinel's FIRST live run (2026-07-12 21:06 ET) surfaced it as TRIGGER-DUE and
the owner ordered this check. This gap is the WO2 case study — the layer's first catch was its
own installation lag.

## Observable, as found (sources at foot)

- **Jul-1:** Doha technical round concluded — Qatar reported "positive progress" on the Islamabad
  MoU items (Hormuz maritime traffic, unfreezing Iranian funds); next round scheduled AFTER the
  Khamenei funeral processions (Jul-4→9).
- **Jul-7:** Iran struck THREE vessels near the Strait — Qatari LNG carrier *Al Rekayat*
  (engine-room fire, evacuated), Saudi VLCC *Wedyan*, and a third vessel within 24h (IRGC).
- **US response:** Treasury RE-IMPOSED the oil-export sanctions lifted under the Islamabad MoU;
  CENTCOM struck "dozens" of Iranian military sites near the Strait.
- **Transit status:** US-led naval coalition raised the Hormuz threat level to **"severe"** (Jul-7).
- **Diplomacy:** a further technical round was reported as scheduled for Tue Jul-14; timetable
  "unclear" per live coverage. So: strikes-during-diplomacy — the trigger's "any resumed strike"
  clause is satisfied several times over regardless of whether Jul-14 convenes.

## The pre-registered action (trigger text, verbatim)

> "Collapse or strikes: restore a Jun-9-shape risk-on weight set the SAME DAY."

The restore target exists in the §9.10 family as **"Crude Set A (Jun-9 war tilt, history
bracket)"** = {escalation 0.25, pre_mou_baseline 0.45, mou_base 0.18, mou_bear 0.12}
(vs the current locked post-stand-down set {0.10, 0.20, 0.45, 0.25}, owner-approved 2026-07-02,
commit d1544b4).

## Per-name impact — ALREADY COMPUTED (2026-07-10 §9.10 run, current FVs, Jul-9/10 prices)

| Name | EV under Jun-9 war tilt | EV current locked | Position change |
|---|---|---|---|
| FRO | −37.3% | −50.3% | TRIM (unchanged, narrower) |
| INSW | −36.2% | −42.2% | TRIM (unchanged) |
| TNK | **+5.6%** | −2.4% | **HOLD → BUY** |
| NAT | −54.0% | −61.8% | TRIM (unchanged) |
| TEN | **+47.5%** | +33.2% | BUY (bigger) |
| CMBT | −5.2% | −10.6% | TRIM (unchanged, narrower) |
| BRUT | **+9.6%** | −44.9% | **TRIM → BUY** (label stays "unreliable read" — POSITION_UNRELIABLE) |
| CAPT | **+0.6%** | −22.9% | **TRIM → HOLD** |

Direction: war-persistence scenarios re-weighted → crude FVs UP across the complex; three
position flips, all toward less-short/longer. NOTE these EVs are at Jul-9/10 prices — the tape
has continued to move (crude names rallied into Friday); the post-restore pipeline run gives the
live numbers.

## Execution plan (awaiting the owner's go — locked weights are owner-gated)

1. Edit `sectors.crude` weights to the Jun-9 shape (a §11.x revision note + the locked-weight
   test re-pin, per the d1544b4 precedent).
2. Pipeline regen → delta report → drift-gate rows annotated (weights-change cause, this file).
3. Baseline re-ratify (owner-aware; FVs move materially — an attributable, deliberate re-anchor).
4. Interplay notes: `crude_mou_implementation_check` (due Jul-17) is largely PRE-EMPTED — the
   sanctions re-imposition IS the implementation break; keep it due for the record. The day-60
   toll cliff (Aug-16) pre-registered reweight stands. Re-arm THIS trigger toward the Jul-14
   round's outcome (talks may still convene).

## Sources

- [Al Jazeera — US-Iran talks in Doha: outcomes and what's next (Jul-2)](https://www.aljazeera.com/news/2026/7/2/us-iran-talks-in-doha-what-were-the-outcomes-and-whats-next)
- [Al Jazeera — Iran to open 'communication channel' on MoU (Jul-1)](https://www.aljazeera.com/news/2026/7/1/iran-to-open-communication-channel-on-mou-with-us-after-talks-in-qatar)
- [CNN — Iran strikes three vessels near Strait of Hormuz (Jul-7)](https://www.cnn.com/2026/07/07/middleeast/hormuz-tanker-iran-attack-intl-hnk)
- [Al Jazeera — Ships attacked in the Strait of Hormuz (Jul-7)](https://www.aljazeera.com/news/2026/7/7/ships-attacked-in-the-strait-of-hormuz-what-that-means-for-ongoing-talks)
- [CBS — US hits dozens of Iranian targets in retaliatory strikes](https://www.cbsnews.com/live-updates/iran-us-war-strait-of-hormuz-trump-nato/)
- [CNBC — Hormuz threat level raised to 'severe' (Jul-7)](https://www.cnbc.com/2026/07/07/iran-strait-hormuz-oil-tanker-lng.html)
- [The Hill — Another tanker targeted amid shaky ceasefire](https://thehill.com/policy/international/5956347-oil-tanker-oman-strait-of-hormuz-attack-iran-war/)
- [CBS — talks timetable unclear amid Hormuz clashes](https://www.cbsnews.com/live-updates/us-iran-war-peace-talks-timetable-unclear-strait-of-hormuz-clashes/)
