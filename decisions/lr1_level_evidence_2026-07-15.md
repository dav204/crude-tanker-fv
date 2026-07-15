# P1c — LR1 level evidence + decision packet (STAGED — owner fork, nothing wired)

**2026-07-15. Registered-pending: no numbers move in this step.** Thread-1A registered
LR1's sourcing path ("intermodal weekly … a current issue gives an LR1 5yr mark; the
Resale anchor is NOT tabulated"). The current issue has now landed, and it shows the
wired LR1 curve is stale-low — with an internal inversion no single-node fix can clear.
This packet lays out the dated evidence and the fork; the wiring is owner-gated and, being
FV-moving (INSW), queues post-Stage-A per the 2026-07-15 sequencing principle.

## 0. Why LR1 now matters more than it did

After the MR flip (`decisions/mr_secondhand_resumption_2026-07-15.md`), **LR1 is the
single class keeping TRMD off resale-uniform** — i.e. the last basis blocker on the
book's tightest tool↔broker name (k 1.03, all queues cleared) reaching
**VALIDATED-TIGHT**. It is also INSW's only non-uniform class, and INSW holds the
book's only YOUNG LR1 tonnage (3 hulls, ages 0–1: Alacran/Balboa/Bonita), so the LR1
level is live NAV, not shelf inventory.

## 1. Dated evidence (all in-repo, all current)

| Source | date | mark | note |
|---|---|--:|---|
| intermodal W29 | 2026-07-10 (issue 07-14) | **LR1 (75KT DH) 5yr $60.0M** | unchanged w/w (60.0 on 03-07 too); the registered Thread-1A path delivered |
| xclusiv W29 NB table | 2026-07-13 | **Panamax (LR1) NB contract $61.0M** | new line vs the 06-22 issue; avg-2026 col $59.0M |
| MB Tanker | 2026-06-26 | LR1 NB $64M / 5yr $58M | already in AGE0_BASIS note (cross-check, kept unwired) |
| — | — | LR1 Resale: **no broker tabulates it** | xclusiv/advanced/intermodal/banchero/fearnleys all checked 2026-07-15 |

Wired today: age-0 $59.0M / 5yr $53.5M (static; LR1 is NOT a §9.9 fitted class, so the
static nodes ARE the marks).

## 2. The defect the evidence exposes

1. **Inversion:** the dated 5yr ($60.0M, two houses ~$58–60M) sits ABOVE the wired
   age-0 ($59.0M). A 0-year ship cannot be worth less than a 5-year ship.
2. **Stale 5yr:** wired $53.5M vs dated $60.0M = −10.8%.
3. **Age-0 below dated NB contract** ($59.0M < $61.0M xclusiv, $64M MB) — in this
   market resale ≥ contract (the book-wide invariant), so age-0 is floor-violating too.
4. Consequence: INSW's 3 young LR1 hulls are marked low; TRMD/HAFN/TEN LR1s (ages 12+)
   sit past the 10yr node and are UNAFFECTED by any 0/5-node fix.

Note the monotonicity guard (`test_curve_anchors_monotonic`) means the 5yr cannot be
refreshed alone — 60.0 > 59.0 would red the suite. Any fix moves BOTH nodes.

## 3. The fork (owner)

- **(i) Contract-floor age-0 + dated 5yr** — age-0 → **$61.0M** (xclusiv Panamax-tanker
  NB, contract = prompt-resale FLOOR, conservative; the product-Handysize 2026-07-15
  precedent exactly), 5yr → **$60.0M** (intermodal, dated). LR1 **stays
  `pending-sourceable`** (no broker Resale line — same posture as Handysize).
  Estimated INSW: ~+$2M age-0 effect on 3 young hulls +5yr-node pull-through ≈ +0.3–0.5%
  NAV — sub-bar, surgical, but FV-moving ⇒ **post-Stage-A**.
- **(ii) Uplift-derived age-0** — apply a Resale/5yr uplift (xclusiv MR2 1.10× →
  ~$66M) for a truer prompt-resale level. More accurate, but it is a DERIVED mark —
  tension with the Amendment-B "read straight off the dated curve, never re-derive"
  posture; needs an explicit owner methodology ruling.
- **(iii) Hold everything** — keep the inversion documented. Cheapest, but the curve
  is now KNOWN-wrong internally (§2.1), which is worse than stale: it fails the
  monotone-economics smell test on the book's youngest product hulls.

**Recommendation: (i)** — conservative, citation-clean (two dated broker marks, zero
derivation), reuses the ratified Handysize contract-floor pattern, and fixes the
inversion. Fold into the same post-Stage-A anchor-refresh round as the
mr_secondhand §5 rider (one attributable curve-refresh step, one drift review).

## 4. The taxonomy question (decide once, here)

Even under (i)/(ii), `resale-uniform` as defined (*age-0 == the dated xclusiv Resale
line*) is unreachable for LR1 — no such line exists, at any freshness. If the owner
wants TRMD (and INSW's basis leg) to ever clear on today's broker coverage, the fork is:

- **(a) Taxonomy stands** — LR1 stays pending-sourceable until a broker prints LR1
  Resale; TRMD stays GOVERNED-WIDE·basis-pending indefinitely on a class that is 10
  of its 85 hulls, ages 13–14 (10yr+ segment: the pending class contributes ZERO
  age-0-sensitive NAV). Honest but blunt.
- **(b) A scoped amendment** — e.g. `resale-corroborated`: age-0 on a dated
  broker CONTRACT floor + dated 5yr, both current, for classes where no house prints
  Resale AND the name's holdings in that class are all ≥10yr (age-0-insensitive).
  Under (b), TRMD → resale-uniform-equivalent → **VALIDATED-TIGHT** becomes reachable
  this cycle. This is a governance loosening — it belongs to the owner, pre-registered,
  never back-filled to flatter a name.

No recommendation is embedded in (b)'s availability; the packet only notes that (a)
leaves TRMD's tier pinned by tonnage that cannot mathematically feel the missing mark.

**Owner ruling line:** fork (i)/(ii)/(iii) + taxonomy (a)/(b): ______ (date / verbatim).
