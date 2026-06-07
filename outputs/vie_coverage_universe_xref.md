# VIE Coverage Universe Cross-Reference (2026-06-03)

**Purpose:** independent-analyst cross-reference of our framework's
position-recommendation and fair-value output against Value Investor's Edge
(VIE) "Shipping Coverage Universe" — the J Mintzmyer / James Catlin
subscription product. Used as an external counter-signal layer alongside
the broker-NAV sweep (§9.9 — mark robustness) and the weight-robustness
diagnostic (§9.10).

**Source:** VIE Live Analytics Platform, Shipping Coverage Universe tab
(gid 301279871), accessed via the Claude in Chrome MCP on 2026-06-03.

**Refresh cadence:** quarterly alongside the refresh checklist
(`refresh.py`), or whenever VIE publishes a sector-level coverage update
that materially changes any watchlist name's stance.

---

## Full 10-name overlap (every watchlist name is in VIE's universe)

| Ticker | Sector | VIE Stance | VIE FV | VIE Price | Our PW FV | Our Price | Our Position | Verdict |
|---|---|---|---:|---:|---:|---:|---|---|
| DHT  | crude | Watch | $16.00 | $16.25 | $13.34 | $16.40 | TRIM/SHORT | Direction differs (VIE neutral, we −19%); small magnitude |
| ECO  | crude | Watch | $45.00 | $47.30 | $32.53 | $48.10 | TRIM/SHORT | Direction differs (VIE near fair, we −32%) |
| FRO  | crude | Avoid | $30.50 | $34.01 | $23.87 | $34.50 | TRIM/SHORT | ✓ Agree TRIM (we more bearish) |
| **INSW** | crude+product (hybrid) | **Watch** | **$79.50** | $78.69 | **$52.08** | $76.80 | TRIM/SHORT | **MAJOR — $27/sh gap; mark-driven hybrid (§9.9, §6 INSW)** |
| TNK  | crude | Watch (+6.5%) | $75.00 | $70.44 | $69.31 | $70.50 | HOLD | ✓ Agree HOLD — strong confirmation of §9.10 weight-driven HOLD |
| NAT  | crude | Avoid (−24%) | $4.00 | $5.26 | $2.28 | $5.40 | TRIM/SHORT | ✓ Agree direction; we deeper (§12 case) |
| FLNG | lng | Avoid (−45%) | $16.50 | $29.85 | $28.04 | $30.23 | TRIM/SHORT | ✓ Agree TRIM; VIE *much* more bearish than even broker NAV |
| **CCEC** | lng | **Avoid** (−26%) | **$17.50** | $23.76 | **$26.45** | $23.18 | **BUY** | **OPPOSITE — direct counter-signal to weight-driven BUY (§13)** |
| **ASC** | product | **Bullish** (+35%) | **$21.50** | $15.91 | **$14.24** | $18.50 | TRIM/SHORT | **OPPOSITE — VIE bullish on product; §11.5 framework gap on Handysize sleeve relevant** |
| STNG | product | Watch (+3%) | $77.50 | $75.45 | $73.58 | $79.00 | TRIM/SHORT | ✓ Near-agreement; both at HOLD/TRIM boundary |

**Coverage overlap: 10 of 10.** VIE covers every name on our watchlist.

**Agreement summary:**
- ✓ **6 of 10 in directional agreement** (FRO, TNK, NAT, FLNG, STNG, + DHT/ECO marginal)
- ⚑ **2 of 10 OPPOSITE direction** (CCEC, ASC) — high-leverage external counter-signals
- ⚑ **1 of 10 MAJOR magnitude divergence** without direction flip (INSW — mark-driven gap)

---

## Four divergences worth documenting

### 1. CCEC — VIE Avoid (−26%) vs Our BUY (+14%)

**Direct opposite call on the only BUY in our watchlist.** Our `outputs/ccec_buy_diagnostic.md` already classified this as a **weight-driven BUY** (survives Set B-revised only; HOLD under Set A / Set B; TRIM/SHORT under bearish stress). The §6 CCEC position-sizing recommendation was: "size smaller than a weight-robust BUY would warrant."

**VIE's Avoid is the strongest external counter-signal possible** — sharpens the §13 limitation overlay materially. Per §13.3 ("when to re-evaluate") trigger criteria, independent-analyst opposite-direction signals are explicitly one of the items the methodology owner should treat as a re-evaluation prompt.

**Operational implication:** the position-sizing language in §6 CCEC entry should harden from "smaller than weight-robust BUY would warrant" to **"neutral / small allocation pending Q2 confirmation or independent corroboration of the BUY thesis."** The framework discipline isn't to disregard the BUY signal but to recognize a weight-driven BUY contradicted by VIE has materially less conviction than a weight-driven BUY VIE corroborates.

### 2. ASC — VIE Bullish (+35%) vs Our TRIM (−23%)

**Two methodological factors partially explain the gap:**

- **Price snapshot drift:** VIE $15.91 vs our $18.50 — VIE has the fresher, lower print. Worth refreshing our watchlist `as_of` for ASC (flagged for next refresh checklist run). Even adjusting our price to $15.91: our PW FV $14.24 would imply EV −10.6%, still TRIM/SHORT.
- **Off-curve Handysize sleeve (§11.5 framework gap):** ASC's 6 hulls valued at $91M in `working_capital_net` likely conservative if vintage handy/chem prices have moved per Catlin's data. A $10-20M upward adjustment to the off-curve sleeve would add $0.25-0.50/sh to NAV — still doesn't close the gap to VIE Bullish but narrows it. **[Update 2026-06-05: the 2 clean-product Handies were moved on-curve via the new Handysize class, realizing +$0.18/sh — within the estimated range, confirming "narrows but doesn't close" (ASC PW FV now $14.50 vs VIE $21.50). The 4× 25k stainless-chem hulls remain off-curve. This 2026-06-03 snapshot is otherwise preserved as-authored.]**
- **Product Set B v2 (locked 2026-06-03 PM):** added +$0.65 to our ASC FV already. VIE's view implies the product-sector tightness goes materially beyond what Set B captures.

**This is the first watchlist name where VIE materially overrules our framework on direction.** Worth a §6 ASC footnote noting the divergence and the qualitative VIE-Bullish overlay. The Catlin product-sector thesis (the basis for Product Set B v2) is visibly more pronounced in VIE's own ASC call than in our framework's per-name output — consistent with VIE having access to richer per-name fleet / employment / forward-curve data than we model.

### 3. INSW — VIE Watch ($79.50 ≈ price) vs Our TRIM ($52.08)

**The $27/sh gap is structurally the mark-driven hybrid issue we already documented.** k_broker 1.37 / +22pp tool→broker spread classifies INSW as mark-driven per §9.9. VIE's $79.50 is essentially the broker-NAV-implied value at consensus marks (price $78.69 / consensus_pnav 0.97 ≈ $81 implied broker NAV — close to VIE's $79.50).

**Three-way ordering: VIE $79.50 ≈ broker $81 >> tool $52.** Consistent and internally coherent — VIE matches broker consensus, tool is conservative.

**The discrimination IS the call.** If you trust broker NAVs, INSW is fair (VIE Watch); if you trust tool NAVs, INSW is deeply TRIM (us). The framework's §9.9 mark-driven flag already captures this. Nothing to fix — INSW is an explicitly-marked "trust the marks you trust" name. VIE's view is external validation that the broker-NAV anchor for INSW is mainstream sell-side consensus, not an outlier mark.

### 4. FLNG — VIE Avoid ($16.50, −45%) vs Our TRIM ($28.04, −7.2%)

**Direction agrees but VIE is deeper bearish than even broker consensus.** Our FLNG is already flagged "tool above broker" (k_broker 0.87, −21pp spread): tool $28 > broker ~$21 (implied at consensus_pnav 1.42).

**Three-way ordering: VIE $16.50 < broker $21 < tool $28.** VIE's view extends the "tool > broker" classification to "tool > broker > VIE." Coherent.

**Why VIE more bearish than broker:** likely the LNG glut thesis (orderbook through 2028, structural demand uncertainty) weighted more heavily by VIE than by the sell-side consensus. Our framework partially captures this via §11.3's `structural_reset` scenario (curated but inactive at weight 0.0) — applying VIE-style structural-tail weighting would activate `structural_reset` at perhaps 0.05-0.10 and bring our FLNG closer to VIE.

**Operationally:** add §6 FLNG footnote documenting the tool > broker > VIE three-way ordering and the implied case for considering a non-zero `structural_reset` weight on FLNG specifically (vs the sector-wide weight 0.0 currently).

---

## Three onboarding candidates (VIE covers, we don't)

| Ticker | Firm | Sector | VIE Stance | VIE FV | VIE Yield | Framework value |
|---|---|---|---|---:|---:|---|
| **TRMD** | Torm Plc | Product Tankers | **Bullish** | $34.00 | 17.0% (100% FCF) | First name to exercise full MR + LR1 + LR2 product class map; lr1_clean rate forwards used outside INSW for first time |
| **HAFN** | Hafnia (Oslo) | Product Tankers | **Bullish** | $9.00 | 8.1% (80% EPS) | First non-US-reporting product name (IFRS schema test); large diversified product fleet |
| **TEN** ⚠️ DEFERRED | Tsakos Energy Navigation | Crude/Product/LNG/**Shuttle** hybrid | **Bullish** | $51.50 | 4.1% (Fixed) | **Assessed + deferred 2026-06-04** — 4-asset-type hybrid; ~15-20% DP2 shuttle tankers can't be spot-valued (LIMITATIONS §2), + ~$287M preferreds + $2.0B newbuild book. Blockers in `decisions/ten_log.md` |

All three were already in our "unlocked for templated-mode onboarding" list (METHODOLOGY §1, §11.5). **VIE's strongly Bullish stance on all three product/hybrid names is the strongest external corroboration yet that Catlin-driven product-sector tightness is mainstream sell-side consensus, not just our framework's call.**

**Recommended onboarding order:**
1. **TRMD first** (highest framework value: full product class map exercise + 17% FCF yield is a §12-archetype-like high-payout test case)
2. **HAFN second** (IFRS schema variation; would surface input-loader robustness issues if any)
3. ~~**TEN third** (hybrid carve-out architecture stress test)~~ — **assessed 2026-06-04 and DEFERRED.** The "architecture stress test" turned out to be a hard blocker, not a stretch: TEN is a 4-asset-type hybrid whose NAV is dominated by DP2 shuttle tankers the framework can't spot-value (no `Shuttle` class). See `decisions/ten_log.md` + LIMITATIONS §2.

---

## What this cross-reference confirms about the framework

1. **Mark-driven discrimination (§9.9) is the dominant interpretive axis for the divergences.** INSW (+22pp spread → VIE matches broker), FLNG (−21pp spread → VIE matches/exceeds tool-above-broker direction), NAT (+53pp spread + §12). The framework's mark-validated vs mark-driven bucket is the right primary read for understanding where we and external analysts diverge.

2. **TNK HOLD is externally confirmed.** VIE Watch + our HOLD. Our §9.10 flagged TNK as both mark-driven AND weight-driven (the only crude name where both judgemental dimensions matter); VIE's independent Watch validates the call but doesn't resolve which weight set is "right." Conviction stays "moderate" per the §9.10 matrix. **Worth noting:** TNK is the cleanest validation that our framework's most-uncertain crude name is also externally read as uncertain.

3. **CCEC BUY signal has serious external pushback.** VIE Avoid is precisely the kind of evidence §13's quarterly re-evaluation discipline is designed to catch. The framework's response should be to soften the sizing recommendation in §6 CCEC, not to silently change weights or override the BUY signal.

4. **ASC's TRIM call is the framework's most defensible-only-on-tool-marks position.** VIE Bullish + Catlin product tightness + our +40pp mark-driven spread says the framework's product-sector valuation may be too conservative on Handysize handling. The Product Set B v2 reweighting (locked same day) closed part of the gap but not all of it.

5. **Three product/hybrid onboarding candidates had strong external corroboration.** TRMD / HAFN / TEN all VIE Bullish. **TRMD and HAFN onboarded** (2026-06-03 / -04). **TEN assessed and deferred** (2026-06-04) — the shuttle-tanker sleeve is a hard coverage gap, not a stretch goal; we can't form a tool view to compare against VIE's Bullish until a shuttle module exists (`decisions/ten_log.md`).

---

## Mark robustness × Weight robustness × VIE classification — combined conviction matrix

Building on §9.10's combined mark + weight robustness framework, adding the VIE third dimension:

| Ticker | Mark | Weight | VIE Direction | Combined conviction |
|---|---|---|---|---|
| DHT  | robust | robust | agrees-ish (Watch) | **HIGHEST** — TRIM survives all three dimensions |
| ECO  | robust | robust | agrees-ish (Watch) | **HIGHEST** — TRIM survives all three dimensions |
| FRO  | robust | robust | ✓ agrees (Avoid) | **HIGHEST** — TRIM corroborated externally |
| NAT  | driven | robust | ✓ agrees (Avoid) | **§12-archetype** — direction confirmed, tool magnitude per §12 |
| FLNG | driven | robust | ✓ agrees deeper (Avoid) | **strong external bearish corroboration** — consider structural_reset activation |
| STNG | **driven** (+27pp) | robust | ✓ agrees marginal (Watch) | **MIXED** — reclassified mark-driven after Pareto 4-Jun P/NAV check (0.87→0.70); broker NAV $108 ≈ VIE $104, both well above tool $84 |
| INSW | driven | robust | ⚑ VIE matches broker (Watch) | **MIXED — tool says TRIM, broker+VIE say fair**; trust the marks you trust |
| TNK  | driven | driven | ✓ agrees (Watch) | **MODERATE** — both judgemental dims, but VIE Watch validates HOLD |
| **CCEC** | validated | driven | ⚑ **VIE Avoid (opposite)** | **WEAKEST BUY** — weight-driven AND externally contradicted; **size neutral** |
| **ASC**  | driven | robust | ⚑ **VIE Bullish (opposite)** | **WEAKEST TRIM** — mark-driven AND externally contradicted; **soften TRIM signal** |

**Two operational rules implied:**
- A weight-driven BUY contradicted by VIE → reduce sizing to neutral (CCEC)
- A mark-driven TRIM contradicted by VIE → soften the signal and look for §11.5 framework-gap items to validate (ASC)

---

## Recommended follow-ups

Documentation-only (no weight or curve changes):

- **§6 CCEC footnote** documenting VIE Avoid as §13 external counter-signal
- **§6 INSW footnote** documenting VIE Watch ($79.50) as broker-consensus corroboration
- **§6 FLNG footnote** documenting VIE Avoid ($16.50) extending tool > broker > VIE ordering; flag structural_reset activation as candidate weight for FLNG specifically
- **§6 ASC footnote** documenting VIE Bullish ($21.50) and §11.5 Handysize-sleeve gap as partial explanation

Onboarding work (incremental but adds material framework value):

- **TRMD onboarding** — Q1 2026 data fetch, inputs build, watchlist add, pipeline run, tests, §6 entry, §11.5 update to note first 3-class product name

This file becomes the recurring quarterly external-counter-signal artifact, updated each time VIE publishes a sector coverage refresh or a stance change on any watchlist name.
