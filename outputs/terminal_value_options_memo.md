# Terminal-value options memo — METHODOLOGY §9.2 (B6)

**Status:** DECISION PENDING (owner) · **Written:** 2026-06-21 · **Basis:** the
19-name sweep regenerated today (`scripts/terminal_value_sensitivity.py` →
`outputs/terminal_value_sensitivity.md` / `.xlsx`).

This memo resolves Open Methodology Decision #2 (§9.2): what multiple should the
dividend strip's terminal value carry. It lays out four options, recommends one,
and leaves an owner DECISION block. **No engine change has been made** — the
production constant `dividend_strip.TERMINAL_NAV_MULTIPLE` remains `1.0`. The
recommendation below is to ratify that, so adopting it requires no code; adopting
an alternative is a follow-up.

---

## 1. The mechanism (what the multiple actually controls)

Each name's fair value blends a **NAV leg** (weight `w_nav`) and an **earnings
leg** = the dividend strip's implied price (weight `w_earn`), `w_nav + w_earn = 1`.

The strip = 8 quarters of discounted DPS **plus a discounted terminal at q9**:

```
terminal = TERMINAL_NAV_MULTIPLE × NAV(fleet aged ~9 quarters) , discounted at 11%
```

Two facts decide this memo:

1. **The terminal is built from the tool's *current* vessel marks, aged down the
   depreciation curve but never re-priced** (`_terminal_nav_per_share` ages
   `v.age + years`; the $/vessel mark is held). So at a cycle peak the 1.0×
   terminal silently carries today's firm second-hand prices forward — the
   "peak-forever" outcome §10 warns against; at a trough it carries today's
   depressed prices forward.
2. **`w_earn` and the terminal multiple are orthogonal levers.** `w_earn` sets
   *how much the strip leg counts* (it is cycle-stepped: 0.30 at peak → 0.60
   below mid-cycle, so the strip already matters less at peak). The multiple sets
   *the embedded asset-price level inside the terminal*. Down-weighting a leg
   that contains a too-high number is **not** the same as fixing the number — so
   a terminal multiple is not, by itself, a double-count of `w_earn`.

There is precedent for a multiplier at exactly this layer: the §15
`governance_discount_pct` already applies a haircut to **both** the blend NAV
term and the strip terminal. A terminal-value multiple is architecturally the
same kind of lever.

## 2. How much the decision matters (19-name sweep, today)

FV sensitivity scales with `w_earn`: peak names (`w_earn` 0.30) move only
**3.7–6.8%** across the full ±15% multiple range; below-mid names (`w_earn`
0.60) move **13–14%**. **12 of 19 names never change position.** The most
sensitive name, CCEC (14.4% FV range), does not flip — its BUY survives the whole
sweep. The decision is therefore about a handful of band-edge HOLD/TRIM/BUY
oscillations, all already flagged name-by-name in the decision logs.

The 7 names that flip somewhere in the sweep, and what each option does to them:

| Name | Cycle band | w_earn | 1.0× (status quo) | 0.9× uniform | 1.1× uniform | Cycle-conditional |
|---|---|--:|---|---|---|---|
| DHT | late-cycle/peak | 0.30 | **BUY** | HOLD | BUY | **HOLD** (peak→0.9×) |
| ECO | late-cycle/peak | 0.30 | **HOLD** | TRIM/SHORT | HOLD | **TRIM/SHORT** (peak→0.9×) |
| STNG | late-cycle/peak | 0.30 | HOLD | HOLD | HOLD | HOLD (flips BUY only at 1.15×) |
| ASC | elevated | 0.40 | TRIM/SHORT | TRIM/SHORT | **HOLD** | TRIM/SHORT |
| SBLK | elevated | 0.40 | TRIM/SHORT | TRIM/SHORT | **HOLD** | TRIM/SHORT |
| GNK | mid-cycle | 0.50 | HOLD | HOLD | **BUY** ⚠ | HOLD |
| FLNG | below-mid | 0.60 | HOLD | HOLD | HOLD | HOLD (flips at 0.85/1.15 only) |

⚠ GNK's price is pinned to the live Diana cash tender — its EV/position is
deal-arb noise, not a clean NAV read (see `decisions/gnk_log.md`). Discount its
flip.

**The practical decision today reduces to ~2–3 band-edge names:** moving DHT/ECO
(peak) more bearish (0.9× / cycle-conditional), or moving ASC/SBLK to HOLD (1.1×).
Cycle-conditional and uniform-0.9× produce the **same realized book today** (only
DHT and ECO move) because the book currently holds no trough-band names where
their signs would diverge.

## 3. The four options

**Option 1 — ratify 1.0× (status quo).** Terminal = aged NAV, no cycle view in
the multiple. *For:* simplest and most auditable (terminal is a clean identity);
the marks are already conservative/transaction-anchored and `w_earn` already
down-weights the strip at peak; the at-stake flips are immaterial band-edge
wiggles. *Against:* leaves the forward-mean-reversion-of-asset-values error
uncorrected precisely for the high-conviction peak names — conservative marks are
honest about *today's* level but assert nothing about the forward path, and at a
hot peak transaction-anchored marks track *recent (elevated)* prints, so
"conservative vs broker" ≠ "not peak-level."

**Option 2 — uniform 0.9× (mid-cycle discount).** Assume asset values mean-revert
down by the terminal everywhere. *For:* a single auditable constant; the natural
shrink-toward-long-run-mean prior; corrects the peak embedded-mark error (DHT/ECO
turn more cautious). *Against:* **wrong sign at troughs** — §10 says trough ships
trade *below* replacement cost so the terminal should revert *up*; a uniform 0.9×
haircuts already-depressed trough marks further. Dominated by Option 4, which
does the identical peak correction without breaking troughs.

**Option 3 — uniform 1.1× (structural-undersupply premium).** Assume asset values
stay elevated/rise. *For:* tanker orderbooks are thin and the documented broker
premium (k_broker ~1.12–1.14) says the market pays above tool marks. *Against:*
**this is the weakest option.** Its broker-gap justification is precisely the
"tweak marks toward broker" move §6/§9 forbids (broker consensus is a
*discrimination diagnostic, not a calibration target*), just relocated to the
terminal layer; and it bakes a permanent directional bull bet into a tool whose
philosophy is to not assume peak-forever. (Panel confidence: low.)

**Option 4 — cycle-conditional.** Multiple varies with the cycle band:
late-cycle/peak → 0.9×, elevated → ~0.95×, mid-cycle → 1.0×, below-mid → 1.1×,
trough → 1.15×. *For:* maps one-to-one onto the §10 philosophy verbatim ("the
terminal should not assume peak-forever; at troughs NAV is the floor"); corrects
the embedded-mark level (the thing `w_earn` cannot touch) in the right direction
at each band; architecturally identical to the accepted §15 multiplier mechanism.
*Against:* introduces a **judgmental, unvalidated, discontinuous** knob keyed to
the *same* cycle band that already drives `w_earn` (so peak gets conservatism via
three correlated channels — low `w_earn`, conservative marks, and the 0.9×); a
name crossing a band boundary would jump its terminal multiple, manufacturing
drift; and the thresholds are not validated against disposal data the way the
mark curves are.

## 4. Recommendation

**Ratify Option 1 (1.0×) as the production default now, and adopt Option 4
(cycle-conditional) as the designated successor — to be implemented when its two
preconditions are met.** Reject Options 2 and 3.

Reasoning:

- **Options 2 and 3 are out.** 1.1× violates the no-calibration-to-broker
  doctrine and is a standing bull bet; 0.9×-uniform is strictly dominated by
  cycle-conditional (same peak fix, wrong at troughs) and the book will
  eventually hold trough names (dry bulk / containers cycle hard).
- **The contest is 1.0× vs cycle-conditional, and it is close.** Cycle-conditional
  is the more *principled* answer — it corrects a real error (`w_earn` does not
  touch the embedded mark level) and matches the philosophy and the §15
  precedent. But adopting it *now* buys a ~2-name (DHT/ECO) band-edge effect at
  the cost of a new, unvalidated, discontinuous cycle-timing knob — poor leverage
  for a tool that prizes auditability and empirical grounding and that refuses to
  back-solve marks. The honest engineering call is **don't add the knob until it
  is shown to bind.**
- **Adoption triggers for Option 4** (revisit when either fires): (a) disposal /
  transaction data shows the terminal-horizon mark at a peak is materially
  elevated vs realized values ~2–3 years out (i.e. the embedded-mark error is
  empirically sized, not assumed); or (b) the book gains genuine trough-band
  names, where the cycle-conditional *up*-tilt vs a flat 1.0× changes a
  conviction call (not just a band-edge wiggle).
- **Interim discipline (already in force):** for any name whose call sits at a
  band edge where the §9.2 choice would flip it — currently DHT, ECO, ASC, SBLK
  (and FLNG/STNG at the extremes) — name the 1.0× assumption explicitly in the
  decision log, so the dependence is visible until the decision is locked.

This is a genuine judgment call; an owner who weights principle-fidelity over
knob-parsimony could reasonably choose Option 4 today. The DECISION block records
the pick.

## 5. OWNER DECISION

> _Decision:_ __________________________  (1.0× / 0.9× / 1.1× / cycle-conditional)
>
> _Date:_ __________   _Rationale:_
>
>
> _If cycle-conditional:_ band→multiple table confirmed? ____   thresholds source: ____

On a pick other than 1.0×, the follow-up is: set/parameterize
`dividend_strip.TERMINAL_NAV_MULTIPLE` (or add the cycle-conditional rule keyed to
`cycle.band_label`), re-pin the affected FV-band tests, re-run the pipeline, and
annotate the decision logs of every name whose position flips.

## Reproduce

```
.venv/bin/python scripts/terminal_value_sensitivity.py
```

→ `outputs/terminal_value_sensitivity.md` (per-name tables + summary) and `.xlsx`.
See METHODOLOGY §9 (open decisions), §3.2 (strip / terminal construction), §10
(cycle philosophy), §15 (the precedent multiplier mechanism).
