# BRUT — Stage-A void disposition: UPHELD (WO5/R4 Phase 4, 2026-09-18)

**RULING: UPHOLD the void.** BRUT stays in `POSITION_UNRELIABLE`; the cell keeps printing
`unreliable read (not actionable)`. **RE-ARMED** to the Oslo Børs uplisting prospectus (~end-Sep
2026), with a dated fallback re-read at the Q3 report, 2026-11-19.

Ruled 2026-09-18 from the owner's chat on the Phase-3 frozen evidence. This is the one of the three
dispositions that does NOT retire, and the work order anticipated it: "BRUT — re-reads, does not
auto-retire (the 8/31 scope word) ... A legitimate outcome is UPHOLD."

## The decisive fact: BRUT has TWO grounds and the re-expression reaches only one

**Ground 1 (primary, 2026-07-01)**, `provenance.py`:

> the position cell must reflect the untrustworthiness, not the 0.59x discount, so it can't sit as
> a raw BUY next to PROVISIONAL⛔NO

with its definition: "a NAV built on stacked structural uncertainties (BRUT — a 0.59x 'BUY' resting
on a cash floor pending H1 AND going-concern doubt)".

**Ground 2 (junior, 2026-08-10)**: the Stage-A deck-incoherence artifact.

Ground 2 IS resolved — the re-expression landed and is guard-held, and BRUT's own move reproduced
its frozen prediction exactly (+3.1pp, +2.99% FV). **Ground 1 is not, and cannot be reached by this
work at all.** It is a balance-sheet and solvency ground. The re-expression moves no mark, no
manifest and no balance sheet: ΔNAV/share was **exactly 0.00 on all 25 names**, by construction and
verified. A scenario re-levelling is definitionally incapable of resolving a cash-floor or
going-concern question. CAPT and TNK each had one ground and it was the deck; BRUT does not.

Both of Ground 1's legs are, if anything, in a weaker state than the registry text implies. The cash
leg resolved on 2026-08-13 and was immediately re-opened in a new form by the demerger: the $50M OMC
contribution and the sale-leaseback inflows that funded it are both post-6/30 and neither is
separately disclosed, so true post-demerger cash and debt resolve only at the uplisting prospectus
or FY2026. The going-concern leg persists in the issuer's own words but as-of 6/30 on the 12-hull
object that no longer exists, and no post-demerger statement replaces it either way.

**And the live 4-hull entity has never filed a balance sheet.** The Q2 sheet is a constructed
as-adjusted derivation, with Mount Vision deliberately held as a §9.6 stand-in rather than fabricate
an undisclosed debt figure. The sheet header states the premise on which that construction was
accepted, in terms: *"the read is VOID regardless (R4)."* Retiring the void would remove the premise
under which the balance sheet the read is computed from was allowed to stand. That alone settles it.

## The evidence the re-expression newly supplies — and it argues for upholding

The re-expression carried BRUT's raw band **across the BUY edge**, EV +2.1 → **+5.2** against a
+5.0 edge. That is not an argument for retirement; it is the sharpest argument against one.

1. **The margin is about one cent per share.** Back-solving the unrounded numbers, the BUY label
   dies at roughly $5.25 against a tape of $5.2406. The quote is Oslo-native (NOK 49.4 × FX): **a
   +0.25% move in NOK/USD alone, with the share unchanged in its own currency, flips the label.**
2. **It has already strobed three times in nine days**, on price alone: BUY +5.6 on 9/10, HOLD +2.0
   on 9/16, BUY +5.2 on 9/18. There is no hysteresis — BRUT is `read_blocked`, so `read_flag` is
   `n/a`.
3. **+5.2 is the weight family's MAXIMUM, not its centre.** The family runs −31.2 to +5.2 with
   `ev_sign_stable: false`: **one of eight weight sets says BUY, and it happens to be the live
   one.** The surface already prints ⚠ sign flips.
4. This is the registered BRUT lesson, verbatim from its own log: "BRUT's modeled margin was
   concentrated in scenarios a model update removed ... What worked was the GOVERNANCE LAYER:
   PROVISIONAL ⛔ + POSITION_UNRELIABLE prevented the model from fighting a correct tape."

Publishing a BUY on a one-cent, FX-sized, single-weight-set margin, on a name whose live entity has
never filed a balance sheet, is exactly the failure the 7/01 ground was written to prevent.

## The case for retiring, stated fairly

The honest argument is symmetry: CAPT and TNK are being retired on the same re-expression, and a
void that never comes off is a mask rather than a judgement. If the only thing holding BRUT is a
disclosure gap, the surface arguably ought to print the read and let the tier cell carry the caveat
— which is what `GOVERNED-WIDE · going-concern-unfinanced` exists to do.

It does not carry here for a reason specific to BRUT rather than general: the caveat machinery
cannot express "this number rests on a sheet we constructed under the assumption that the read would
not be published". CAPT and TNK have filed, reconcilable balance sheets; BRUT's live entity does
not. The asymmetry in the disposition tracks a real asymmetry in the evidence, which is why the
answer is not the same for all three.

## Re-arm, with dates

- **Primary trigger: the Oslo Børs uplisting prospectus (~end-September 2026)** — imminent as of
  this ruling. It is the first document that resolves post-demerger cash and debt for the 4-hull
  entity.
- **Dated fallback: the Q3 report, 2026-11-19.** If the prospectus does not land or does not
  disclose, re-read there regardless rather than letting the void drift.
- On either trigger the question is Ground 1 only — Ground 2 is closed and should not be re-argued.

## What this ruling does not do

It changes no registry membership, no tier, no number and no rendering. Going-concern-unfinanced and
the §15 flags stand regardless, as they did before. The re-read of Ground 2 is recorded as closed so
that the next sitting does not re-litigate the deck.
