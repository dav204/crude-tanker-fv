# Thread 1A — product/Handy resale sourcing — pre-registration

**Frozen ahead of the wiring.** The live residue of the Thread-1 comparability fix:
the `pending-sourceable` classes (LR1, Handysize, Handymax) on the 5 product/hybrid
names (INSW, STNG, HAFN, TRMD, ASC). Same discipline as the eight already-sourced
classes — source dated, verify the *label* (Resale vs 5yr — the crude-cascade lesson),
register ahead, then wire. **No mark is wired off a stale or proxied value.**

## 0. Sourcing finding (the gating fact)

A multi-broker sweep of every in-repo broker report (xclusiv current to 2026Q2; allied/
intermodal/banchero/fearnleys/advanced stale at 2023) establishes that, of the three
classes, **only Handysize has a CURRENT dated in-repo resale mark.** The "absence isn't
evidence" check paid off — it found an LR1 mark the parser had dropped (intermodal),
and confirmed Handymax is genuinely uncovered.

| Class | Current in-repo source? | Mark (verified) |
|---|---|---|
| **Handysize** | **YES — xclusiv 2026Q2** | **Resale $36.0M** (vs 5yr $29.5M — the Resale line, label-checked) |
| LR1 | No (intermodal covers it, but only to 2023, 5yr-anchor only) | $51.0M 5yr (2023) — stale; no current issue in-repo |
| MR | No current (xclusiv dropped MR secondhand after 2023Q4) | allied/advanced 2023 Resale ~$52.5–53.5M corroborates the repo's $54M |
| Handymax | **No — NO broker tabulates product Handymax secondhand** | — (needs a chem-tanker specialist / issuer mark) |

## 1. The wiring (Handysize only — the one verifiable current mark)

- `vessel_value_curves.yaml` Handysize age-0 **$40M → $36.0M** (xclusiv Resale 2026-06-22).
- `prompt_resale` (newbuild_contract_prices.yaml): add Handysize $36.0M (the resale source/ceiling).
- `basis_status.yaml`: Handysize `pending-sourceable → resale-uniform`.
- `AGE0_BASIS` registry: Handysize `exception → xclusiv-resale` (so the completeness guard now
  asserts Handysize age-0 == xclusiv Resale, and `XCLUSIV_WIRED` includes it).

**Predicted outcome (committed AHEAD; honor a miss):** **NAV-NEUTRAL** — no name moves. Only <5yr
Handysize reprices on an age-0 change, and HAFN's Handysize is age-18, ASC's age-11 (and no other
name holds young Handysize). So:
- No NAV/EV/band move ⇒ **no re-ratify** (drift gate stays clean).
- **basis_status:** Handysize → resale-uniform. **Scorecard:** ASC moves `pending-sourceable →
  unverified-no-current-xclusiv-line` (its only remaining non-uniform class is MR); HAFN/INSW/
  TRMD/STNG stay `pending-sourceable` (LR1/Handymax). **No name reaches resale-uniform** — they
  all hold LR1/Handymax/MR.
- If any name's NAV moves, halt and investigate (a hidden young-Handysize hull).

## 2. Registered sourcing paths — LR1 / Handymax / MR (external-data-gated)

Not wired (no current in-repo mark); registered so the next pull knows exactly what to request:

- **LR1** → **intermodal weekly** (tabulates 75k DH product secondhand, 5yr anchor ~$51M in 2023).
  A current issue gives an LR1 5yr mark; the **Resale** anchor is NOT tabulated, so the age-0 Resale
  would need a Resale-to-5yr uplift from another source or a different broker. Until then LR1 stays
  `pending-sourceable`.
- **MR** → **allied or advanced weekly** (both tabulate MR Resale; ~$52.5–53.5M in 2023, corroborating
  the repo's $54M). A current issue verifies the $54M level and clears the `unverified-no-current-
  xclusiv-line` flag. The repo's $54M is a sound Resale-basis level meanwhile (NOT a mislabel).
- **Handymax** → **no general broker tabulates product-Handymax secondhand** (the hardest gap). Needs
  a chemical-tanker specialist (e.g. a chem-S&P broker) or the issuer's (STNG's) own marks. Stays
  `pending-sourceable`, flagged structurally hard.

## 3. Discipline notes

- Do NOT wire the stale 2023 LR1/MR marks as a current age-0 (stale-mark error). Wire only Handysize.
- The Handysize $36M is the **Resale** line (label-verified vs the 5yr $29.5M) — no repeat of the
  Thread-1 5yr-as-age-0 conflation.
- The completeness guard (`test_every_curve_class_age0_basis_registered`) still passes: Handysize moves
  from a documented exception to `xclusiv-resale`; LR1/Handymax remain documented exceptions (Group A
  pending, now with explicit sourcing paths); MR stays the unverified-no-current-line exception.
