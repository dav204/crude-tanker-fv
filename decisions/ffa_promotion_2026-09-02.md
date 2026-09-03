# Dry FFA promote — the 2026-09-01 print (executed 2026-09-02)

**Authority:** the owner's 2026-09-02 ruling on `decisions/autopilot_authority_2026-09-02.md`
("accept all Q recs") fixes every mapping question this round would otherwise have raised —
Q-1 unrounded 12M proxies, Q-2 the straddling-panel shape, Q-3 no per-leg move cap, Q-7 a
cycle-band crossing is the ONE condition that freezes for an owner word. Plus the owner's
direct instruction the same day: *"Why not promote ffa… That will happen. That makes
mathematical sense."*

**Q-7 does not fire** (§3). Under the ruled predicate this promote is mechanically
determined, so it executes without a further word. That is the point of having ruled the
predicate.

## 1. The print, and why it is the day's authoritative one

Source image `inputs/ffa_drybulk/2026/09/2026-09-01_Clipboard - 1 september 2026 09:42.png`,
status `ok`, no sanity issues. Panel, image-verified:

| | Sep | Oct | Q4 | Q1-27 | Cal-27 |
|---|--:|--:|--:|--:|--:|
| Cape | 45,125 | 46,000 | 44,125 | 29,925 | 33,200 |
| Pmax | 22,200 | 23,800 | 23,083 | 18,100 | 18,225 |
| Smax | 19,775 | 21,725 | 20,883 | 15,900 | 16,150 |

**Best-of-day is now established, not assumed.** 2026-09-01 carries NINE captures. Until the
parser fix committed earlier today (`ffa_ocr`: per-image tracking + a 7-day lookback), a day
was skipped wholesale once it held any accepted entry, so five of those nine — including the
18:09 end-of-day print — had never been read. The re-scan parsed all of them and the 09:42
capture still wins on fewest issues. Before that fix this round would have promoted a print
whose primacy was an artefact of scan order.

**2026-09-02 is NOT promotable and is not the vintage here.** Its cape panel parses four
tenors against pmax/smax's five on the 2nd of the month — an incomplete parse, not a
month-end roll-off — so it is `flagged` and the predicate refuses it. The "which vintage"
question raised during review dissolves on that fact; there is one promotable print.

## 2. Construction (the ratified rule, applied)

The panel straddles: Sep is the remaining month of the CURRENT quarter, Oct is a component
of Q4. Per Q-2, `q1` = the front month alone — putting Oct in both `q1` and `q2` would
double-count it.

- `q1` = Sep · `q2` = Q4 · `q3` = Q1-27
- `q4..q6` solve the Cal-27 identity EXACTLY (mean of the four 2027 quarters = Cal-27)
- `q7,q8` = the committed per-class 2028 deltas (Cape −500/−500 · Pana −400/−300 · Supra −300/−300)
- Post-Panamax = Pana · Handy-Bulk = Supra-Ultra × 0.90 to nearest 10 (locked §11.7.11)
- 12M proxy = (Q4 + Q1-27)/2, unrounded per Q-1 (half-up to the integer the file stores)

Cal-27 identity arithmetic: Cape 4×33,200 = 132,800 − 29,925 = 102,875 → 34,292/34,292/34,291.
Pana 4×18,225 = 72,900 − 18,100 = 54,800 → 18,267/18,267/18,266. Smax 4×16,150 = 64,600 −
15,900 = 48,700 → 16,234/16,233/16,233.

Derived twice independently (the main session and a separate investigation agent) with
identical results before either touched the file.

## 3. Cycle-band check — the ONE conjunct that could have frozen this

| class | 12M was | 12M now | move | ratio was | ratio now | band |
|---|--:|--:|--:|--:|--:|---|
| Cape | 37,300 | 37,025 | −0.74% | 1.5772 | 1.5655 | late-cycle/peak → **unchanged** |
| Pana | 20,550 | 20,592 | +0.20% | 1.7269 | 1.7304 | late-cycle/peak → **unchanged** |
| Supra-Ultra | 18,467 | 18,392 | −0.41% | 1.3257 | 1.3203 | elevated → **unchanged** |

Ten-year means from `scenario_inputs.yaml` `cycle_anchors` (Cape 23,650 · Pana 11,900 ·
Supra-Ultra 13,930). GNK's blended position — the name nearest a boundary — moves
**1.4899 → 1.4804**, i.e. AWAY from the 1.5 step, not through it. No name changes `w_nav`,
`w_earn` or `terminal_multiple`.

This is the material difference from the 24-Aug and 31-Aug rounds, where the ratio DEEPENED
and the elevated-cycle reweight faded dry EV ~3pp book-wide. Here the cycle channel is inert.

## 4. PREDICTED IMPACT — frozen BEFORE the regen

Both channels stated, per the 2026-08-31 lesson that a rate promote has two and their net
sign is ambiguous ex ante.

- **Direct rate channel:** sub-1% on every dry leg, and mixed in sign (Cape down, Pana up,
  Supra down). Expect dry EV moves of **|ΔEV| ≤ 0.5pp**, direction mixed by name.
- **Cycle channel: INERT.** No band crossing (§3), so no weight or terminal-multiple step.
- **ΔNAV EXACTLY 0.0 on every name in the book.** `nav.py` contains no reference to
  `twelve_month_tc`, `ffa_forward_curve` or `spot_tce` (verified by grep this session) — a
  rate-only promote cannot move NAV. Any nonzero ΔNAV is a HALT: it would mean a frozen file
  moved.
- **Non-dry names EXACTLY 0.0 on both NAV and EV.** Movers are confined to the dry five
  (SBLK, GNK, CMDB, SB, 2343) plus CMBT's dry sleeve.
- **No band flip expected** on a sub-1% rate move with no reweight. Any flip toward BUY is a
  halt-and-investigate regardless of size (standing rule).

## 5. Attribution — why this is its own commit

The 2026-09-02 price vintage was committed FIRST and separately (`499f0bf`) and regenerated
on its own, so the price leg's EV moves — including SB's expected BUY→HOLD crossing, a
price event on a name sitting +7% against a 5% band — are attributed to the tape and not to
this promote. CLAUDE.md's "prices absorb only as their own commit" exists for exactly this,
and the 8/16 two-cause ratify is the precedent for keeping legs separable.

## 6. Disposition

Inputs commit first, regen second. Gate rows annotated per name against §4. Sub-threshold
moves need no ratify row; anything that breaches rides the owner's next ratify with this
document as its cause.
