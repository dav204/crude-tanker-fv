# TNK — Stage-A void disposition: RETIRED, destination cycle-relabel (WO5/R4 Phase 4, 2026-09-18)

**RULING: RETIRE the void, and route TNK to `POSITION_CYCLE_RELABEL`** — not to a bare raw read.
The verdict cell prints `rich · cycle position (not a short)`. The book's name-specific-shorts line
is unchanged at ten names.

Ruled 2026-09-18 from the owner's chat on the Phase-3 frozen evidence, per
`WO5_R4_DECK_REEXPRESSION.md` Phase 4 and its pre-ruled item 6.

## The ground, and why it is resolved

TNK's membership in `POSITION_UNRELIABLE` had exactly one ground, the 2026-08-10 Stage-A
deck-incoherence void. It is the only one of the three names with no second leg: TNK is
`VALIDATED-TIGHT` with a null tier sub-reason, SANITY OK, handoff ready, and was **never**
`read_blocked`. Nothing outside the deck held this void up.

The ground named its own retire condition — the deck re-expression against the landed base — which
was re-venued from the 8/16 toll cliff to this work order and landed 2026-09-18 (49e0fb9 /
c5ce304). The artifact is gone: **TNK reads TRIM/SHORT at EV −12.9, 7.9pp from the nearest band
edge**, and TRIM/SHORT across **all eight weight sets** (−12.9% to −22.4%, `weight_sign_stable`
true). In price terms TNK re-enters HOLD only at $92.20 (−8.3%) and BUY at $83.42 (−17.0%). There
is no BUY-ward read left to be untrustworthy.

**One correction to the work order's own citation.** It says wf_8b0d1184 found TNK's BUY-ward print
was "a stale-static sim artifact". What that record actually corrected is narrower: the stale-static
object was the C2 blast-radius SIMULATION, which priced TNK off the watchlist static. The 2026-08-10
production print that grounds the void was real at that day's live tape (price $77.25, PW FV $83.72,
EV +8.4%, BUY). So what was refuted is the claim of PERSISTENCE, not the original print: TNK's BUY
was a genuine deck-driven crossing of the +5 edge by 3.4pp that never recurred on any later tape —
the smallest and most fragile of the three flips. That reading strengthens the retirement rather
than weakening it, and it is recorded here so the register does not carry a wrong reason.

## The destination, and why not a bare raw read

Retiring the void without a destination would publish TNK's raw `TRIM/SHORT (overvalued)` as a
NAME-SPECIFIC short, taking the book's named-shorts line from ten names to eleven. The work order
pre-ruled against that at ratification (item 6) and the reasoning holds on the evidence: TNK reads
**rich on parity and rich on history** at VALIDATED-TIGHT — the same late-cycle shape as the crude
peers already in `POSITION_CYCLE_RELABEL` (DHT, FRO, ECO, INSW, NAT), not a name-specific short
thesis. A genuine short call is a governance-side decision, never a rendering default. Cycle-relabel
is the honest cell.

## The rider that the destination makes necessary

`_verdict_position` rewrites a relabelled name's cell **unconditionally**. So a cycle-relabelled name
that later turns raw-BUY would publish as `rich · cycle position (not a short)` and the BUY tripwire
this book runs on would never fire. Nothing guarded that before TNK was routed here — the relabel
registry had only ever held names that were deeply rich.

`tests/test_tier_semantics_amendment.py::test_a_cycle_relabelled_name_may_not_print_a_raw_buy` now
reds if any member of the registry publishes an EV above the +5% edge on the committed surface. It
is not vacuous: it checks nine names today, and BRUT (+5.2), TEN (+24.8) or CCEC (+50.8) would trip
it immediately if any were routed here. **This rider is part of the ruling, not a nicety** — without
it, the destination that makes TNK's cell honest would also make it silent.

## The strongest case against, and why it does not carry

The correction ran BUY-ward: the re-expression lifted every crude name's fair value, TNK by +5.23%.
One could argue an honest deck that is systematically kinder than the broken one deserves seasoning
before a void comes off. The magnitude answers it — +4.3pp of EV against a 7.9pp margin to the
nearest edge and a −22.4pp worst weight set does not approach a flip on any path — and the direction
is an artifact of where the old absolute curves happened to sit under a base that had walked, which
is the defect being repaired, not a new bias.

## What moves, and what re-arms

- Verdict cell: `unreliable read (not actionable)` → `rich · cycle position (not a short)`. Tier,
  read_flag, read_par, handoff and W-frag all unchanged. Named-shorts line unchanged at ten.
- `tests/test_tier_semantics_amendment.py` B1 anchor: the pin that asserted `TNK in
  POSITION_UNRELIABLE` moves with TNK. **The B1 docket RE-ARMS and is not ruled** — per the work
  order's ratification record, its trigger is the day a registry name reads robust-cheap, which no
  member does today. What the pin still holds is B1's actual reason: TNK is robust and raw-BUY
  eligible on agreement alone, and only the DIRECTIONAL read keeps it out of the actionable set.
- Edge-cleared stays `{SB}` — TNK is excluded by `read_par == "rich"`, not by this registry.

## What this ruling does not do

No capital, no position, no tier change, no read-machinery change (TNK was never read_blocked and
its read_flag state is live and governed already).
