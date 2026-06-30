# §18.5 gates — data contract (Threads 3 & 5)

The §18.5a mean-reversion gate and §18.5b orderbook cross-check are **registered**
(`PRE_REGISTRATION_NORMAL_RATES.md` §5a/§5b) and the **machinery is built**
(`normal_rates.py`, `tests/test_normal_rate_gates.py`) — but both are **DATA-GATED**.
Until the inputs below are provided, every class returns **`pending`** (no crash, no
proxy). This contract states EXACTLY what each gate needs so it can run unchanged the
day the data lands.

**Hard rule (both gates):** never fabricate, never proxy, never scale. The in-repo
`baltic_indexes_daily.csv` is **index-point** (§11.7.2), not $/day — it must NOT be
scaled into the §5a series. Orderbook ratios must NOT be estimated from memory.

---

## Thread 3 / §18.5a — Baltic $/day TC series

**File (provide):** `inputs/market_data/baltic_tce_series.yaml`

```yaml
# Real (inflation-adjusted, current $) quarterly time-charter-equivalent, $/day,
# oldest-first. ~15yr (≥ ~60 quarters) per class so the anchor is a true 15yr median
# and the gate clears ≥12 observations after the 4q horizon. Each value is a quarter's
# realized TC average. Source + as-of date in the header; public, no look-ahead.
report_source: "Baltic Exchange / Clarksons TC assessments"
units: usd_per_day_real
series:
  Cape:        [ ... ~60 quarterly $/day values, oldest-first ... ]
  Pana:        [ ... ]
  # ...
```

**Per-class series (route to provide):**

| Repo class | Baltic / route series ($/day TCE) |
|---|---|
| VLCC | Baltic VLCC TCE (TD3C) |
| Suezmax | Suezmax TCE (TD20) |
| Aframax | Aframax TCE (TD25 / TD7) |
| LR2 | LR2 clean TCE (TC1 / TC15) |
| MR | MR clean TCE basket (TC2 / TC7) |
| Cape | **BCI 5TC** |
| Pana | **BPI 4TC** |
| Supra-Ultra | **BSI 10TC** |
| Handysize | **BHSI 7TC** |
| Ctr-* | **New ConTex / HARPEX** ($/day) |

Confirm the exact route per crude/product class with the provider; the dry-bulk /
container codes (bold) are the registered ones (PRE_REGISTRATION §7).

**Registered gate parameters** (in `normal_rates.py`, do not tune to fit a result):
horizon **4 quarters**, **≥12** observations (else `insufficient`), pass at **≥70%**
sign-consistency, anchor = **5/95-winsorized median** of the (already real) series.

**What the gate does on the data:** per class, `ratio = TC_t / anchor` predicts the SIGN
of the forward (`t+4q`) realized change (ratio>1 ⇒ falls). **Pass** ⇒ the
`historical_mean` anchor is validated. **Reject** ⇒ the anchor is dropped (`None`) and
that class's historical-basis reads are flagged unvalidated. Report the per-class
pass/reject table book-wide when it runs.

---

## Thread 5 / §18.5b — orderbook-to-fleet ratios

**File (provide):** `inputs/market_data/orderbook_ratios.yaml`

```yaml
# Orderbook-to-fleet ratio per class, INDEPENDENT of the parity computation (sourced
# from a broker orderbook report, NOT back-derived from the divergence). `neutral` is
# the balanced / replacement-rate orderbook level for that class (fleet renewal at the
# economic-life rate). date + source per class; public, dated.
orderbook:
  Cape:   { ratio: 0.00, neutral: 0.00, date: "YYYY-MM-DD", source: "Clarksons orderbook" }
  Pana:   { ratio: 0.00, neutral: 0.00, date: "YYYY-MM-DD", source: "..." }
  VLCC:   { ratio: 0.00, neutral: 0.00, date: "YYYY-MM-DD", source: "..." }
  # ...
```

- `ratio` = orderbook ÷ on-the-water fleet (as a fraction, e.g. 0.08 = 8%).
- `neutral` = the balanced level (≈ the renewal rate implied by the economic life; the
  orderbook level that just replaces scrappings). The gate calls a book **thin** below
  `neutral·(1−0.20)`, **thick** above `neutral·(1+0.20)`, else **balanced**.

**Registered parameters:** balanced band **±20%** around `neutral`; a divergence is
"balanced" when `|historical−parity| / parity < 5%`.

**What the gate does on the data:** per class, the SIGN of `(historical_mean − parity)`
must coincide with the orderbook signal — under-ordered (divergence < 0) ⇒ thin book;
over-ordered ⇒ thick. **Coincide** ⇒ the §18 under-/over-ordered read is independently
confirmed (breaks the circularity). **Contradict** ⇒ flags the **parity INPUT**, not the
output. Apply to all sectors (crude's "collapse" should coincide with a balanced/not-thin
book; dry-bulk's under-ordering with a thin book).

---

## Out of scope (no source ⇒ stays pending)

- Synthesising the §5a series from `baltic_indexes_daily.csv` (index points, not $/day).
- Estimating orderbook ratios from memory or back-solving them from the divergence.
- Migrating cycle position onto a validated historical basis — `cycle.py` is **frozen**
  (owner decision D1); that is a separate, pre-registered, re-ratified change, NOT this.
