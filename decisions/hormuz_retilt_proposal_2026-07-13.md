# Reweight proposal — restore the remaining Jun-9 legs (LNG v4 + product war shape)

**Status: PREPARED 2026-07-13, ruling STAGED for the round-2 outcome (trigger
`crude_doha_round2_outcome`, due 2026-07-15).** Owner directed the prep 2026-07-13 ("Prep it");
NOT pre-registered — this is a fresh owner-reviewed reweight per the Jul-2 proposal→sign-off
chain (d1544b4 precedent). Nothing below changes any input until the owner rules.

## Why this is on the table

The Jun-9 vintage was a THREE-sector coherent war state; the Jul-2 stand-down unwound all three
"as one vintage"; the Jul-12 pre-registered restore (doha trigger fired) brought back **crude
only**. The book now prices the same Hormuz state two ways: crude at war-persistence (0.70 mass
on escalation+pre_mou) while LNG and product sit normalization-leaning. Symmetric evidence since
Jul-7/8:

- **LNG:** the Qatari LNG carrier *Al Rekayat* was among the three vessels struck (engine-room
  fire, evacuated) — Qatar ≈ 20% of global LNG, all through Hormuz; transit threat 'severe'.
  This is STRONGER than the Jun-8 helicopter-downing basis that justified LNG v4 in June.
- **Product:** MB Tanker Weekly 28 (archived Jul-13): Hormuz "slowed to near standstill following
  further US strikes"; NE-Asia CPP exports +600 kb/d; MR/LR repositioning; "renewed disruption in
  Hormuz could... materially strengthen freight rates"; plus the Russian diesel-export ban
  tightening product supply — the refinery_squeeze/moderate_correction mechanics, verbatim.

## The restore shapes (byte-exact Jun-9 values, commit 2b9895c)

| Sector | Scenario | Current | Restored |
|---|---|---|---|
| LNG | tight_resurgence | 0.15 | **0.25** |
| LNG | moderate_tightening | 0.25 | 0.25 |
| LNG | glut_base | 0.45 | **0.38** |
| LNG | glut_intensifies | 0.15 | **0.12** |
| Product | refinery_squeeze | 0.15 | **0.25** |
| Product | moderate_correction | 0.25 | **0.30** |
| Product | glut_base | 0.45 | **0.30** |
| Product | demand_softening | 0.15 | 0.15 |

## Per-name impact (scratch what-if, 2026-07-13; static-vintage watchlist prices — PW-FV deltas
## are price-independent; recompute EVs at live marks at execution)

| Name | PW FV now → restored | ΔFV | EV now → restored | Band |
|---|---|---|---|---|
| STNG | $73.81 → $80.30 | **+8.8%** | +1.1% → +10.0% | **HOLD → BUY (flip; at live $76.25 lands ~+5.3%, a boundary case — eyeball at ruling)** |
| TRMD | $29.68 → $33.03 | **+11.3%** | +7.2% → +19.2% | BUY (bigger) |
| HAFN | $5.70 → $6.33 | +11.1% | −18.6% → −9.6% | TRIM (narrower) |
| ASC | $16.30 → $16.85 | +3.4% | +9.4% → +13.1% | BUY |
| FLNG | $29.19 → $30.67 | +5.1% | −0.4% → +4.7% | HOLD (near BUY boundary — eyeball) |
| CCEC | $33.50 → $35.91 | **+7.2%** | +55.1% → +66.2% | BUY (the book's biggest read, extends) |
| INSW | $57.15 → $58.44 | +2.3% | −30.6% → −29.1% | TRIM (product sleeve only) |
| TEN | $61.09 → $62.35 | +2.1% | +64.5% → +67.9% | BUY (product+LNG sleeves) |
| CMBT | $14.12 (no change) | 0 | — | no product/LNG sleeve ✓ |

Dry bulk / containers / LPG / crude: untouched. No held portfolio name is affected (SB/SBLK are
dry bulk) — this is book-truth, not a portfolio action.

## Test re-pin inventory (expected; the suite run at execution is the final authority)

- LNG weight value-pins — tests/test_scenarios.py ~217-221 (0.15/0.25/0.45/0.15 → v4 values).
- Product weight value-pins — ~515-518 (0.15/0.25/0.45/0.15 → war values).
- CCEC integration band ~452-473: [31.82, 35.17] — restored $35.91 EXCEEDS → re-pin ±5% around
  the executed value.
- INSW whole-co band [55.7, 58.6]: restored $58.44 sits at the edge — re-pin deliberately.
- TEN 3-sleeve band [58.04, 64.14]: restored $62.35 inside — likely survives.
- Plus any wnav-direction/documentation pins the suite surfaces (the Jul-12 precedent: run,
  read, re-pin with dated narratives — never force).

## Execution plan (on the owner's ruling — same loop as the Jul-12 crude restore)

1. Weight edits with dated RESTORED comments citing this doc; 2. test re-pins; 3. commit inputs;
4. all-five family re-stamps; 5. pipeline regen from clean HEAD; 6. drift annotations (cause:
this doc) with any NEW price-driven flips eyeballed individually; 7. owner-aware baseline ratify.

## Decision (owner) — rule AFTER the round-2 outcome lands (due Jul-15)

- [x] **RESTORE BOTH legs** (LNG v4 + product war shape) — the coherence default if round-2
      collapses/no-shows or strikes persist. **OWNER RULED 2026-07-14 EVE (verbatim): "Yes, of
      course, all three are affected by hormuz, so should all move together coherently. restore
      both as coherence default." EXECUTED same evening — weights restored byte-exact, 7 pins
      re-pinned (the scratch what-if reproduced TO THE CENT on all five bands: 35.905/16.853/
      6.329/33.031/80.298), INSW + TEN bands survived as predicted; drift/ratify record in
      RATIFY_LOG + the execution commit.**
- [ ] **LNG only** (the carrier hit is LNG-specific evidence; product rides on rate mechanics
      that MB already documents — but this leaves product incoherent with crude; state why).
- [ ] **NEITHER — document why crude-only stands** (e.g., round-2 de-escalates credibly enough
      to expect a full unwind imminently; then the pending question becomes unwinding CRUDE).

**Round-2 evidence slot (filled 2026-07-14 EVE):** NO-SHOW/STALL branch — no credible report
the Jul-14 round convened (freshest coverage Jul-10: timetable "unclear", Iran reluctant
amid ongoing strikes; sanctions re-imposition stands). Record:
`decisions/doha_round2_check_2026-07-15.md`; successor watch `crude_doha_round3_watch`
armed (due 2026-07-22). The de-escalation branch did NOT trigger.
