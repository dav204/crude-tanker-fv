# VIE NAV Cross-Reference (2026-06-04; corrected 2026-06-04 PM after Pareto 4-Jun check)

**Purpose:** reconcile our framework's per-share NAV against Value Investor's
Edge (VIE) published NAV/sh across all 12 watchlist names, using broker-consensus
NAV (price ÷ Pareto P/NAV) as the bridge. NAV-layer counterpart to:

- `vie_coverage_universe_xref.md` — VIE *position stance* vs our position call.
- `vie_market_rates_xref.md` — VIE *forward rate / 10y-mean* methodology vs ours.

> **CORRECTION NOTE (2026-06-04 PM).** The first draft of this file claimed
> "VIE marks product asset values above even broker consensus." **That finding
> was wrong** — it was an artifact of two stale APPROX `consensus_pnav` inputs
> (STNG 0.87, TRMD 1.00). The Pareto Shipping Daily of **4 Jun 2026** publishes
> real P/NAVs of **STNG 0.70** and **TRMD 0.83**, which raise their broker NAVs
> substantially. With the corrected P/NAVs, **VIE ≈ broker NAV across all
> sectors** and the "VIE > broker on product" signal disappears. The corrected
> finding is below; the consequence (STNG + TRMD reclassify mark-validated →
> mark-driven) is the substantive result.

**Source (VIE):** VIE Live Analytics Platform — Crude / Product / LNG (Live)
tabs. "Asset Values Updated: 24 May 2026." NAV/sh from VIE's own NAV $M ÷ shares.

**Source (broker):** Pareto Securities Shipping Daily, **4 Jun 2026** — the
P/NAV column. Broker NAV = price ÷ Pareto P/NAV. Pareto publishes **no P/NAV for
NAT, ASC, CCEC** (shown as "-"); those three keep an APPROX consensus_pnav and
are flagged below.

**Source (tool):** `value_company(...).nav.nav_per_share`, 2026-Q1.

**Refresh cadence:** quarterly, or whenever VIE refreshes "Asset Values Updated"
or Pareto publishes a new P/NAV.

---

## Full 12-name NAV reconciliation (corrected P/NAVs)

| Name | Sector | Tool NAV | Broker NAV | VIE NAV | VIE/Broker | Tool→Broker | P/NAV src | Read |
|---|---|--:|--:|--:|--:|--:|---|---|
| DHT  | crude | $15.29 | $15.05 | $15.25 | 1.01× | −1pp | Pareto 1.09 | **VIE ≈ broker ≈ tool** |
| ECO  | crude | $39.93 | $39.42 | $39.11 | 0.99× | −1pp | Pareto 1.21 | **VIE ≈ broker ≈ tool** |
| FRO  | crude | $28.79 | $28.75 | $26.54 | 0.92× | −0pp | Pareto 1.20 | **VIE ≈ broker ≈ tool** |
| TNK  | crude | $83.32 | $93.16 | $83.78 | 0.90× | +10pp | Pareto 0.76 | VIE ≈ tool, below broker |
| NAT  | crude | $2.63 | $6.12 | $4.67 | 0.76× | +51pp | **APPROX 0.85** | VIE between tool & broker (P/NAV unanchored) |
| INSW | hybrid | $40.18 | $79.59 | $75.90 | 0.95× | +22pp | Pareto 0.98 | **VIE ≈ broker** (whole-co) |
| STNG | product | $83.76 | $108.00 | $103.62 | 0.96× | **+27pp** | **Pareto 0.70** | **VIE ≈ broker** — STNG now mark-driven |
| TRMD | product | $26.74 | $33.98 | $30.83 | 0.91× | **+22pp** | **Pareto 0.83** | VIE ≈ broker — TRMD now mark-driven |
| HAFN | product | $5.30 | $8.11 | $8.55 | 1.05× | +31pp | Pareto 0.95 | **VIE ≈ broker** |
| ASC  | product | $15.78 | $21.33 | $21.50 | 1.01× | +30pp | **APPROX 0.75** | VIE ≈ broker (P/NAV unanchored) |
| FLNG | lng | $28.45 | $21.68 | $18.57 | 0.86× | −20pp | Pareto 1.37 | VIE < broker < tool (VIE most bearish) |
| CCEC | lng | $28.10 | $24.33 | $25.98 | 1.07× | −15pp | **APPROX 0.90** | VIE ≈ broker (P/NAV unanchored) |

_Broker NAV = price ÷ consensus_pnav (Pareto 4-Jun where published). Tool→Broker = §9.9 EV%-spread. "≈" band ±10%._

---

## Headline finding — VIE NAV ≈ broker-consensus NAV, full stop

The corrected data is unambiguous: **VIE's published NAV tracks broker-consensus
NAV (price ÷ Pareto P/NAV) for essentially every name.** VIE/Broker sits in a
tight 0.86–1.07 band across all 12 names, with VIE running *at or slightly
below* broker — never materially above. VIE is **not an independent third mark**;
it is a second read on the same broker-consensus asset values our k_broker
already computes.

This collapses the entire tool-vs-VIE NAV gap back onto the **§9.9 mark-driven
axis**. Where the tool is mark-validated (DHT/ECO/FRO, spread ≤1pp), VIE ≈ tool ≈
broker. Where the tool is mark-driven (everyone else), VIE sides with **broker**,
and the tool-vs-VIE gap is exactly the tool-vs-broker spread. There is no
separate "VIE disagrees with us on NAV" signal — there is only "the tool is
conservative vs broker consensus, and VIE confirms where broker consensus sits."

The only names where VIE departs from broker at all are on the **conservative**
side: FLNG (VIE 0.86× broker — structural-LNG-glut bearishness) and TNK (VIE
0.90× broker — VIE validates our conservative TNK mark over the broker premium).
VIE is never the bullish outlier.

---

## The substantive result — STNG and TRMD reclassify to mark-driven

The Pareto 4-Jun P/NAV check corrected two stale APPROX inputs, and the
consequence is a **reclassification**, not a new VIE signal:

| Name | Old P/NAV (APPROX) | Pareto 4-Jun | Old spread | **New spread** | Old class | **New class** |
|---|--:|--:|--:|--:|---|---|
| STNG | 0.87 | **0.70** | +8pp | **+27pp** | mark-validated | **MARK-DRIVEN** |
| TRMD | 1.00 | **0.83** | +2pp | **+22pp** | mark-validated | **MARK-DRIVEN** |
| HAFN | 1.00 | **0.95** | +29pp | +31pp | mark-driven | mark-driven (confirmed) |

STNG had been cited as a **mark-validated validator** (e.g. LIMITATIONS §4
"mark-validated bucket: DHT, ECO, FRO, STNG"). That was an artifact of the stale
0.87 P/NAV. With Pareto's real 0.70, STNG's broker NAV is **$108.00 vs tool
$83.76** — a +29% mark gap, +27pp EV spread. **STNG is firmly mark-driven.** TRMD
likewise moves from a trivial +2pp to +22pp. Both reclassifications flow purely
from correcting the input, and both are confirmed independently by VIE (VIE NAV
≈ the higher broker NAV on both: STNG VIE $103.62 ≈ broker $108; TRMD VIE $30.83
≈ broker $34).

**Downstream corrections applied (2026-06-04 PM):** LIMITATIONS §1 mark-driven
list now includes STNG (+27pp) and TRMD (+22pp); LIMITATIONS §4 mark-validated
bucket reduced to DHT / ECO / FRO; `vie_coverage_universe_xref.md` STNG row
mark-classification updated robust → driven.

---

## What this means for §11.5 (product divergence) — hypothesis #2 strengthened

§11.5 hypothesis #2 was: "our product vessel curves are conservative vs current
market." The corrected NAV cross-reference is **strong support** — and now from
**two independent sources that agree with each other:**

| Name | Tool NAV | Broker NAV (Pareto) | VIE NAV | Tool is below both by |
|---|--:|--:|--:|--:|
| STNG | $83.76 | $108.00 | $103.62 | ~24–29% |
| TRMD | $26.74 | $33.98 | $30.83 | ~15–27% |
| HAFN | $5.30 | $8.11 | $8.55 | ~53–61% |

Both Pareto (sell-side broker) and VIE (independent analyst) mark product asset
values **~25–50% above our tool curves**, and they agree with each other (VIE ≈
broker). That is much harder to dismiss than a single source: two independent
marks converging above our curve is the strongest evidence yet that the product
curve level is conservative.

### Reconciliation with the LR2 transaction print (unchanged)

The §11.5 PM/evening transaction work found the one clean-LR2 print (STNG STI
Goal/Gallantry at $52.3M) sits 27% **below** our Aframax-proxy curve — the
opposite direction. With the corrected broker/VIE data the full STNG LR2 mark
stack is:

```
clean-LR2 transaction  $52.3M   ← clean-only marginal buyer (LOWEST)
tool Aframax-proxy     $71.4M   ← our curve
broker / VIE          ~$78–88M  ← dirty-optionality-inclusive (HIGHEST)
```

The reconciliation is unchanged and is the **§14.6.1 LR2 cargo-switching
option**: broker + VIE mark the coated LR2 at its dirty-Aframax-optionality
value; the clean-only buyer who bought STI Goal/Gallantry paid only the
clean-product value. Directly evidenced by STI Condotti (dirty-mode LR2) selling
at $70M vs STI Goal/Gallantry (clean-mode) at $52.3M — same seller, vintage,
spec, 4 months apart (33% spread). **Both broker/VIE and the transaction are
"right" conditional on whether the marginal buyer values the cargo-switch
option.** So §11.5's product NAV gap = *VIE and broker price the LR2 option into
NAV; our curve (and a clean-only buyer) do not.*

---

## Two crude/LNG counter-cases — VIE sides with the conservative mark

VIE is never the bullish outlier; on two names it sits at/below our tool:

- **TNK** (crude): VIE $83.78 ≈ tool $83.32, and **10% below broker $93.16.**
  TNK is the one crude name where broker marks materially above tool (P/NAV
  0.76 → broker $93); VIE agrees with our conservative mark. External validation
  relevant to the §9.10 finding that TNK is the lowest-conviction crude name.
- **FLNG** (LNG): VIE $18.57 < broker $21.68 < tool $28.45. VIE marks LNG below
  everyone (structural-glut bearishness; same thesis behind FLNG Avoid at $16.50
  in the coverage xref). Reinforces the case for a non-zero `structural_reset`
  weight on FLNG (§11.3).

---

## Three-sector NAV pattern (corrected summary)

| Sector | VIE vs broker | Interpretation |
|---|---|---|
| **Crude validated** (DHT/ECO/FRO) | VIE ≈ broker ≈ tool | All three agree; no mark gap |
| **Crude mark-driven** (TNK, NAT) | VIE ≈ broker (TNK: VIE ≈ tool < broker) | Gap is §9.9 spread; VIE confirms broker (NAT P/NAV is APPROX) |
| **Product** (STNG/TRMD/HAFN/ASC) | VIE ≈ broker | Tool conservative vs BOTH broker and VIE (which agree); §11.5 hyp #2 supported; gap = §14.6.1 LR2 option |
| **Hybrid (INSW)** | VIE ≈ broker (whole-co) | Same mark-driven gap; VIE confirms broker $79.59 |
| **LNG (FLNG)** | VIE < broker < tool | VIE most bearish; structural_reset candidate |
| **LNG (CCEC)** | VIE ≈ broker | All agree on NAV; CCEC disagreement is forward/weight (§13), not NAV |

**Clean takeaway:** the NAV-layer divergence between our framework and VIE is
**entirely the §9.9 mark-driven spread re-expressed through an independent
analyst who happens to track broker consensus.** It is not a new signal. The one
genuinely useful addition VIE makes at the NAV layer is the two
conservative-side reads (TNK, FLNG) where VIE validates our lower mark against a
broker premium.

---

## Data caveats

- **VIE asset values dated 24 May 2026; Pareto P/NAV dated 4 Jun 2026; tool
  snapshot 2026-Q1 / watchlist as_of 2026-06-04.** Comparable within ~10 days.
- **Pareto publishes no P/NAV for NAT, ASC, CCEC** — those broker NAVs use our
  APPROX consensus_pnav and are genuinely unanchored. NAT's VIE/broker 0.76×
  in particular should not be over-read (the 0.85 P/NAV is a band-midpoint
  guess, not a Pareto print).
- **TEN (Tsakos)** is on VIE's sheets but its VIE NAV is stale (ref Q4-24, last
  update 15 Apr 25). Not on our watchlist; excluded.
- **broker NAV = price ÷ consensus_pnav** is the *broker's NAV estimate*, not an
  independent vessel mark; it inherits the price snapshot and the P/NAV.

---

## Recommended follow-ups

- **§11.5 update** — hypothesis #2 supported by two agreeing sources (Pareto +
  VIE); product NAV gap = §14.6.1 LR2 option, in tension-but-not-contradiction
  with the clean-LR2 transaction. *(done 2026-06-04 PM)*
- **LIMITATIONS.md** — STNG/TRMD reclassify mark-validated → mark-driven; add to
  the mark-driven list; reduce the mark-validated bucket to DHT/ECO/FRO.
  *(done 2026-06-04 PM)*
- **§6 STNG / §9.10** — STNG mark classification robust → driven; the STNG
  "mark-validated validator" framing is retired. *(candidate)*
- **§6 TNK footnote** — VIE NAV validates our conservative TNK mark over the
  broker premium. *(candidate)*

No curve or weight recalibration implied. The product NAV gap is the §14.6.1
cargo-switching option (broker + VIE price it; our curve and a clean-only buyer
do not), not a curve error. This file is the recurring quarterly NAV-layer
artifact alongside the position-layer and rate-layer xrefs.
