---
description: Draft a filing-reconciliation packet (prereg-style) from a staged EDGAR filing — drafts only, never live YAMLs
argument-hint: <TICKER> [accession]
---

Draft a **reconciliation packet** for $ARGUMENTS from its newest staged filing
(`inputs/filings/<ticker>/`, arrivals in `state/edgar_manifest.jsonl` — pick
the named accession if given, else the newest quarterly form). The packet is
the machine-readable-plus-narrative INPUT to a human reconciliation; it is
NEVER a reconciliation itself.

**Template of record: `decisions/trmd_reconciliation_prereg_2026-07-01.md` —
mirror it section for section:**

1. **Header** — ticker, filing form + accession + exhibit, which note numbers
   carry the balance sheet and contractual obligations, what the prior model
   state was (count the `[ESTIMATE]` figures being replaced).
2. **The subsequent-events audit FIRST** (the ASC/HAFN/TRMD pattern, now
   thrice-caught): read the subsequent-events note before anything else; list
   every post-quarter event and mark each IN or OUT of the as-of snapshot,
   with the exact quote that dates it.
3. **Sourced-figures table** — one row per balance-sheet field: model value
   (flag `[EST]` where estimated), sourced value, citation down to the line
   item / note. Every NAV-moving figure must resolve to a citation
   (CLAUDE.md provenance rule — a `~` or `[ESTIMATE]` is a RED, not data).
4. **Issuer cross-checks** — any NAV/share, fleet value, or NIBD the issuer
   itself discloses.
5. **PRE-REGISTERED PREDICTION** — per-field deltas, predicted NAV/sh with a
   band, predicted position change, predicted queue/tier movements.
6. **OPEN FORKS** — each judgment call as an explicit owner decision with
   both branches quantified. **Anything ambiguous, uncited, or contradictory
   goes here under "requires human — do not auto-promote", never silently
   resolved.** Scrubber counts, WC basis, §9.6 on/off-curve are the
   recurring forks.
7. **HALT criteria** — the band, SANITY, guard expectations.

**Hard rules:**
- Write ONLY: the packet to `decisions/<ticker>_reconciliation_prereg_<date>.md`
  and any candidate YAML as `inputs/balance_sheets/<t>_<q>.yaml.draft`
  (`.draft` suffix mandatory — pipeline-loaded YAMLs are promoted by the
  human reconciliation, never by this skill).
- Numbers come from the filing text you actually read — quote the line item.
  If a figure isn't in the filing, it goes to the forks section, not the table.
- Fleet counts: trust the report tables, not IR pages; the snapshot is AS-OF
  the balance-sheet date (subsequent events are OUT).
- End by listing the packet path + draft paths and the one-line SANITY
  expectation. Do NOT run the pipeline, reconcile, or edit live inputs.
