# Source assessment — 2026-09-24

Decision: retain VIE temporarily. No matching licensed replacement has been
confirmed; the observed trial has not started. Quotes are unknown, not zero.

| Source | Confirmed capability | Not established |
|---|---|---|
| Baltic | Daily 17:00 London assessed mid forward curves; Cape 5TC, Pana 5TC, Supra 10TC/11TC listed | Exact widget match, individual eligibility, all-in price, licensed automated/derived use, 20-day access |
| SSY | Bespoke data/API and Navigator; research includes FFA prices | Matching daily basket/tenors, eligibility, price and usage rights |
| Direct MB | Four independent local weekly archives, through September 17/18 | Extraction completeness and future unattended Gmail harvesting |
| Independent harvested PDFs | Advanced, Banchero, Fearnleys, Intermodal and Xclusiv current archives | Complete field coverage; repeated reports are not independent transaction corroboration |

Primary sources checked:
- https://www.balticexchange.com/en/data-services/freight-derivatives-/Baltic-Forward-Assessments.html
- https://www.balticexchange.com/en/free-trial.html (one week, not the required full trial)
- https://www.balticexchange.com/en/data-services/Non-Display.html
- https://www.ssyglobal.com/research
- https://mbshipbrokers.com/research/

An old 2017 Baltic price notice is not a current quote. Do not treat its pricing
as available today. A broker report carrying spot indexes is not an FFA curve.
The Baltic now lists Handy 7TC forwards, whereas historical project notes say no
Handy FFA exists. That does not authorize changing the ruled Supra*0.90 mapping.

## Remaining VIE-linked dependencies

| Dependency | Current use | Exit treatment |
|---|---|---|
| Rocket.Chat screenshots | Dry-bulk forward curve and 12M proxy; downstream cycle/valuation | Requires matched licensed replacement |
| Pareto daily P/NAV | Matched-vintage broker NAV, SANITY, broker sweep, k_broker drift | Trial unavailable state; current gates retained until replacement controls approved |
| Pareto daily research | Transaction/fixture candidates, company context, linked reports | Independent archives plus issuer filings; measure missed coverage |
| Pareto forward P/E/targets | Consensus diagnostics and comparison headers | Explicit unavailable/stale diagnostics; not silently replaced by ship valuations |
| VIE Live Analytics market rates | Historical cross-check and documented rate-source references | Retain dated historical evidence; no automatic historical-mean changes |
| VIE Coverage Universe/NAV cross-reference | Discrimination and coverage diagnostic | Retain dated archive; exclude from live-source claims |
| Historical Pareto/VIE citations | Prior rulings and research provenance | Check retention rights; do not relabel independent or current |
| Issuer filings and independent prices | Fleet/balance-sheet/price inputs | Already independent; continued queue health required |

The independent harvester and transaction scanner were disconnected: the latter
reads the Pareto manifest. The new local document queue connects independent
PDFs to cited review candidates without making assessments valuation inputs.

## Cancellation evidence

User-confirmed annual renewal: March 9; next renewal assumed March 9, 2027.
Seeking Alpha's published policy says subscriptions auto-renew unless cancelled,
and cancellation takes effect at the end of the current billing period. Fees
are generally non-refundable. This is platform policy, not verification of this
account's contract or renewal cutoff.
https://help.seekingalpha.com/basic/seeking-alpha-subscriptions-cancellation-and-refund-policy

Provisional review target: February 7, 2027 (30 days before assumed renewal),
subject to an earlier contractual cancellation cutoff. Account-specific cutoff,
billing channel and archive retention rights remain unverified. No cancellation
or subscription change has been made.


Visual check of MB Dry Bulk Weekly 38 (September 18), page 2: the Baltic FFA
chart labels Handy 7TC, Ultramax 11TC and Kamsarmax 5TC, with monthly/quarterly/
annual tenors. It has no Capesize series or numeric quote table on that page.
This is useful corroboration, not a matched daily replacement; no chart
digitisation or speculative contract mapping is permitted.
