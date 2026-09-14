# Stage B open items — EXECUTED 2026-09-14 (fork `stage_b_open_items`)

Fork opened 2026-09-09 (`decisions/stage_b_promotion_2026-09-09.md` §6), silence window closed
2026-09-14 under the 2026-09-10 policy. Registered recommendation, verbatim:

> FRO 1-yr VLCC 110/120k: settle the CONCLUDED date at the FRO issuer source; if >= 2026-06-15
> they enter (VLCC 12M -> 115,000). Product routing: pure-product names read the DIRTY LR2/LR1
> lines — open a methodology note, no promotion.

## Item 1 — the FRO 1-year VLCC fixtures: SETTLED, and they do NOT enter

**Source of record:** Frontline plc Q2-2026 results, 6-K accession 0000919574-26-005942,
exhibit 1, staged at `inputs/filings/FRO/0000919574-26-005942_6-K_p15060813_ex-1.htm`. The
issuer states the conclusion date of each charter in its own words:

> "In April 2026, the Company **entered into** two one-year time charter-out agreements for two
> VLCC newbuildings delivered on April 30, 2026 and May 20, 2026, at a rate of $110,000 per day
> per vessel, which commenced in early and late May 2026."

> "In May 2026, the Company **entered into** two one-year time charter-out agreements for two
> VLCC newbuildings delivered on June 22, 2026 and July 3, 2026, at a rate of $120,000 per day
> per vessel, which commenced in late June and early July 2026."

**The condition is false.** Both pairs were concluded before 2026-06-15: the $110,000 pair in
April 2026, the $120,000 pair in May 2026. The 2026-06-22 and 2026-07-03 dates that the 8/29
Pareto digest attached to the $120,000 pair are **DELIVERY** dates of the newbuildings, and the
late-June / early-July dates are **COMMENCEMENT** dates. Neither is the date the charter was
concluded. That was precisely the ambiguity the open item named, and the issuer resolves it
against entry.

**Disposition: no promotion. VLCC 12M stays HELD at 105,700**, and the committed comment on
`inputs/market_data/twelve_month_tc.yaml` ("FRO 1-yr 110/120k are May-26 fixtures, §1.3") is
CONFIRMED by the issuer rather than corrected by it. The §1.3 exclusion (evidence base frozen to
the Stage B window 2026-08-26 → 09-04) stands on a sourced date now, not on an inference from
`fro_log.md:1544`.

**Not taken:** the +8.8% branch (VLCC 12M → 115,000). It was inside every §5 band, so nothing
about the bands blocked it — the date did.

**No file changed.** No determinant moved, so no regen is owed and the gate is untouched.

## Item 2 — product routing: methodology note opened, no promotion

Registered as a methodology question, not a change:
`decisions/product_routing_methodology_question_2026-09-14.md`. Pure-product names read the
DIRTY LR2/LR1 lines rather than the clean ones; the §4 routing finding flagged it during Stage B
and the fork explicitly directed a note and no promotion. Nothing in any rate file moves on it
until the question is ruled.

## Verification

- Issuer source read in full and quoted verbatim above; the dates are the issuer's own.
- `inputs/market_data/twelve_month_tc.yaml` VLCC unchanged at 105,700 (the value the Stage B
  promotion committed).
- Drift gate unchanged by this execution: 0 UNEXPLAINED, 7 explained at
  `git rev-parse HEAD` = the commit this record lands in.
