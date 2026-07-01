# SB — date-consistency + scrubber correction, PRE-REGISTRATION (2026-07-01)

Audit vs the Q1-2026 earnings deck + primary filings found the manifest **mixes two
dates** (fleet status 2026-06-12 valued against the 2026-03-31 balance sheet) and carries a
**blanket scrubber default** (the CAPT peer-borrowed-flag bug) on the book's single most
important actionable name. This pre-registers the ONE date-consistency correction to the
2026-03-31 snapshot + the verified scrubber set, with the predicted NAV committed AHEAD of
the recompute. Discipline: commit this, recompute, halt on a miss.

## Sources of record
- **Q1-2026 6-K** (acc 0001317861-26-000033): line 398 "As of March 31, 2026 … 45 vessels,
  **one of which was held for sale**, and an orderbook of **eight** newbuilds"; line 292 Katerina
  delivered April 2026; line 294 Michalis H (2012 Cape) sale agreed Feb, delivered April; line
  295 Xenia + Pedhoulas Commander sales agreed **May** 2026.
- **FY2025 20-F** (acc 0001628280-26-014408): "Scrubbers on **21** of our vessels, incl. all 8
  Capesize" → 13 non-Cape; the fleet table's footnote (15)/(16) ("Scrubber benefit") marks
  exactly those 13. Per-vessel scrubber source (no clean scrubber column exists in any filing).

## Corrections — one 2026-03-31 snapshot
1. **Katerina** — drop the operating row (`SB_Katerina`); it was a NEWBUILD at 3/31 (`SB_NB_Katerina`
   stays). Removes a double-count ($47.7M operating mark).
2. **Held-for-sale = Michalis H** (2012 Cape, $30.2M carrying) — the ONE 3/31 HFS. The
   `working_capital_net` $30.236M line is unchanged; only the label was wrong.
3. **Xenia + Pedhoulas Commander → operating** (sales agreed May, subsequent to 3/31). Add as
   on-curve: Xenia (PPMX, 87k, 2006, scrubber TRUE per ftn-15) + Pedhoulas Commander (Kamsarmax,
   83.7k, 2008, scrubber FALSE — no ftn-15).
4. **Scrubber set → 20-F actual (20 operating, all 7 Capes + 13 non-Cape).** Kamsarmax: only
   **Pedhoulas Rose** is scrubber-fitted (set TRUE); Cedrus/Vassos/Trader/Rizokarpaso/Ammoxostos/
   Farmer → FALSE. Post-Panamax: drop scrubber on Venus Harmony / Troodos Oak / Climate Respect /
   Ethics / Justice (5). Net operating scrubber **29 → 20**.
   - Fleet counts: operating 43→44 (Pana 20 unchanged [−Katerina +P.Commander]; PPMX 16→17 [+Xenia];
     Cape 7); held_for_sale 2→1; on_curve_total 51→52; NBs 8 (unchanged, 6-K-confirmed).

## PRE-REGISTERED PREDICTION (committed ahead of recompute)
- **NAV/sh: $10.12** — band **$10.05 – $10.18**. (Current txn-anchored $10.4689 reproduced;
  corrected in-memory to $10.1157, delta −$0.353 = scrubber −9×$2M ≈ −$0.18 + Katerina-out
  (−$47.7M) / Xenia+Commander-in / HFS-relabel net ≈ −$0.17.)
- SB stays **cheap** (~0.63× P/NAV vs price $6.39) — thesis intact; VALIDATED-TIGHT.
- **Tier:** SB leaves `OPERATING_SCRUBBER_QUEUE` → `OPERATING_SCRUBBER_VERIFIED = {…, "SB": 20}`
  (scrubber set now traced to the 20-F). This TIGHTENS SB's validated standing.
- Suite stays green (cross-foot, scrubber-provenance, confidence-tier); drift gate expects an
  annotated NAV move on SB → re-ratify SB-only after acceptance.

## HALT criteria (investigate the INPUT; do not tune)
- Recomputed NAV/sh outside **$10.05 – $10.18** → halt.
- Any guard red that isn't the expected SB scrubber-queue clearance → halt.
- SANITY ≠ OK/n-a → halt.

## Caveat (the one judgment call)
The per-vessel scrubber set rests on the 20-F fleet-table footnote (15)/(16), which lands the
disclosed aggregate exactly (21 = 8 Cape + 13 non-Cape) and fits SB's retrofit-the-old-hulls
history — but no filing has a clean scrubber column, so it is a sourced inference, not a column read.
