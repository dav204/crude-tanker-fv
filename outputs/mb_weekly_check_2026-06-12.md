# MB Shipbrokers weeklies — first direct-delivery ingest + anchor once-over (2026-06-12)

First delivery of the direct subscription (signed up 2026-06-11): **Container,
Tanker, Dry Bulk Weekly 24/2026** (6–12 Jun), all three PDFs archived under
`inputs/research_mb/<feed>/2026/`. **LNG Weekly did not arrive — check the
subscription.** Ingest route: Gmail link harvest (read-only sanctioned API)
→ `scripts/fetch_pdf.py` (cdn.flxml.eu allowlisted via data_sources.yaml)
→ archive. All PDFs parse as real text with pypdf (the email-body tables are
images; the PDFs are the artifact).

**This is a REVIEW note. Nothing was promoted, no input changed.** Owner
actions queued at the bottom.

---

## 1. Container — the frozen Apr-01 vintage vs the live market (§11.8.5)

The 10 frozen weeks were not sideways. The staleness concentrates in ONE leg:

| Class | Anchor (FY21-25) | Apr-01 rate | Jun-12 rate | Position Apr-01 → Jun-12 |
|---|--:|--:|--:|:--|
| ctr_feeder | 20,850 | 20,500 | **23,250 (+13.4%)** | 0.98x → **1.12x** (regime read-change) |
| ctr_intermediate | 33,700 | 43,400 | 44,738 (+3.1%) | 1.29x → 1.33x (normal drift) |
| ctr_large | 41,000 | 62,500 | 63,000 (+0.8%) | 1.53x → 1.54x (flat) |

- **MBCI 1,318 → 1,501 (+13.9% in 10 weeks)** — above everything the 19-month
  archive saw except the 1,556 high. FY21-25 history columns identical in both
  issues → the anchor BASIS is stable; this is a current-rate move only.
- **Marks layer essentially current**: NB-China assessments all flat and equal
  to our curve anchors (2,800 $44.0M etc.); 2,700 10yr $35.5M = our mark
  exactly; only mover is 1,700 10yr $28→29M, leaving our feeder 10yr mark ~3%
  BELOW MB — the §11.8.5(b) conservative tilt holds.
- **No promotable prints** (S&P quiet; two charter fixtures only — Pearlton
  Thrive 3,928 TEU 24mo $51,000/day; Ten Venus 1,740 TEU 12mo $30,500/day).
- **Impact skew: MPCC** (feeder-heavy, oldest fleet). Bounded by ~99% FY-26
  coverage — re-fix exposure is back-of-strip — but the feeder position
  read-change (mid-cycle → clearly above) shifts blend weights when refreshed.

**Recommended (owner-gated):** refresh `twelve_month_tc.yaml` container rows
+ the §11.8.5 position table to the Jun-12 vintage. Current-rate refresh, NOT
an anchor restatement — the FY21-25 anchors need no touch.

## 2. Tanker — first independent check of the k_broker band and marks (§9.9)

**The band holds on independent data.** MB 5-yr assessments over our
txn-anchored 5-yr marks: VLCC 1.24 / Suezmax 1.09 / MR 1.11 / LR1 1.08 /
LR2 1.04 / Aframax 0.97 — five of six inside or at the edge of
`TXN_PURE_PLAY_K_BAND (1.05–1.25)`. An independent broker lands exactly where
the B4 two-regime semantics predict brokers sit over transaction levels.

- **Cycle read consistent**: MB 1-yr VLCC TC $104,000 → 2.60× vs our 2.79×
  (Compass $111,500) — same late-cycle/peak regime, ~7% softer. The VL
  Brilliant fixture (2014 VLCC, 12mo @ $107,000/day) brackets both.
- **NEW divergence — the NB leg** (untouched by txn-anchoring by design):
  our crude NB anchors run 14–35% ABOVE MB Korea NB (VLCC $175M vs $130M,
  Suezmax $108M vs $90M, Afra/LR2 $90M vs $77–79M; product fine). MB also
  assesses **5yr ABOVE NB** on all four crude classes (prompt-tonnage
  inversion) — a shape our 3-point NB→5yr→10yr curve cannot express.
  Review item; matters most for NB-heavy names (CAPT, FRO, CCEC NB legs).
- **Promotable print candidates (per-vessel, disclosed):**
  1. **Seamusic** — Aframax 112,922 dwt, blt 2009 (~age 17), Thenamaris →
     undisclosed, **$52.5M**. Our txn fit implies ~$31.9M at age 17 — print
     ~65% above; strongest single datapoint that the 2026 S&P market has
     rallied past our 2025-weighted fit window. Promotion → drift loop on
     every Aframax/LR2 holder.
  2. **Shanhaiguan P110k-70** — 115,000 dwt NB resale, blt 2026 Dalian,
     Union Maritime → Ditas, **$90.0M**, scrubber, prompt. Lands on our $90M
     LR2/Afra NB anchor (and +17% over MB's own Korea NB — prompt premium).
- **Hormuz / US-Iran (standing trigger): NOT met.** MB verbatim: *"Iranian
  state media reported that a draft memorandum would see the US lift its
  blockade and Iran reopen Hormuz within 30 days, though final talks
  reportedly depend on the US suspending oil sanctions, lifting the naval
  blockade and releasing part of Iran's frozen funds."* Draft memo + 30-day
  window + conditions ≠ physical-transit confirmation; MB calls signals
  "mixed" after same-week strikes. Brent −4% to $86. **Closest signal yet —
  watch the Jun-13/Jun-20 digests; the weight revisit preempts everything on
  physical transit.**
- Other: Guyana VLCC liftings record 7 cargoes May; Atlantic→Pacific crude
  flows record 11 mbpd (+3.5 vs pre-conflict); MR USG-Europe doubled w/w
  (FFAs point to easing); Suezmax softening vs VLCC.

## 3. Dry bulk — marks validated by MB's own prints; Pana anchor flagged LOW

**The txn-anchored curves survive their first independent check.**
MB's realized S&P prints straddle or land on our fitted curves:
- **Proteas** (Pana, blt 2005, $12.10M) vs our age-21 curve $12.09M —
  **dead-on**. The thin n=6 Pana fit is independently validated.
- Supra prints bracket us both sides (Santa Rita +8.5% above, Ausone −27%
  below, White Bay −10%) → no support for marking up to MB's modern-64k
  Japanese assessment basis; the refit's "Supra-Ultra −10/−13% rich" read
  survives. The headline −17.5% assessment gap is basis, not error.
- Cape: MB $68.5M (5yr) lands between our pre-refit ($62M) and post-refit
  ($71.8M) curves — the GNK-era lift direction confirmed, our level
  defensible on 2026 prints ($73.5–76.25M).

**Cycle/anchor observations:**
- MB 1-yr period rates (Kmax 19,500 / Ultra 19,500, modern-Japanese Pacific
  basis) run +11%/+22% above our Compass-derived TC inputs → positions would
  shift Pana 1.47×→1.64× (elevated → late-cycle/peak) and Supra 1.15×→1.40×
  (mid → elevated) on a TC-input refresh. Direction is w_nav-UP —
  conservative for the dry-bulk signals.
- **Pana anchor (11,900) reads structurally LOW**: MB's term structure never
  decays below ~16,000 even at 5-yr tenors (+41% over the anchor). Concrete
  independent datapoint that the 22-month archive median understates the
  through-cycle mean — feeds the Q3 anchor refinement and the B5
  anchor-basis thread (this is exactly what `archive_median_22m` vs
  `tc_10yr_mean` non-composability looks like in the wild).
- **Promotable print candidates (5 in-class, none already held):**
  Pana — **Vulcania** (82,036, blt 2015 YZJ, eco, TC-attached 13/15mo,
  $26.0M; our eco-adj curve $24.76M) and **Proteas** (above). Supra-Ultra —
  **Ausone** (56,812, blt 2012, Chinese, eco, $13.7M), **Santa Rita**
  (55,677, blt 2010 Mitsui, $17.2M), **White Bay** (52,502, blt 2004,
  scrubber, $10.0M). Handysize prints (Interlink en-bloc $44M no-split;
  Marina R) — NO CLASS, document-only per §9.9 scope discipline.
  **Pana promotion is the most valuable** (thickens the n=6 fit behind the
  SBLK −21% diagnosis).
- **Ethanol-as-marine-fuel corn driver**: RFA estimate — 5% marine-fuel share
  = +1.5bn bushels (~38.1Mt) corn demand; Brazil/Santos as bunkering hub;
  net "potentially lowering grain trade volumes and tonne-mile demand for
  Panamax and Supramax vessels." Slow-burn structural Pana/Supra negative —
  exactly the registered demand-destruction-overlay backlog's territory.
  SBLK (46 Pana) / CMDB most exposed; GNK (zero Pana) least.
- No GNK/SBLK/CMDB/Diana mentions in the issue.

---

## Owner actions queued (nothing applied)

1. **Print promotions** (human-only; each triggers prints→rerun→drift loop):
   Seamusic (Aframax, the big one), Shanhaiguan (NB resale), Vulcania +
   Proteas (Pana — most valuable), Ausone + Santa Rita + White Bay
   (Supra-Ultra). Caveats noted above (TC-attached, build-country basis).
2. **Container current-rate refresh** (`twelve_month_tc.yaml` rows +
   §11.8.5 position table → Jun-12 vintage; anchors untouched).
3. **Crude NB anchor review** — ours 14–35% above MB Korea; 5yr>NB inversion
   unrepresentable in the 3-point curve. (CAPT/FRO/CCEC sensitivity.)
4. **Pana anchor structurally low** — fold into Q3 anchor refinement; B5
   cross-reference.
5. **LNG Weekly** — not delivered; verify the subscription confirm.
6. Cadence: fold the weekly MB harvest into the Saturday digest routine
   (Gmail link harvest needs an interactive/authed session — agent half,
   not cron).
