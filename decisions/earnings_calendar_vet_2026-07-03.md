# Q2-2026 earnings-calendar vet — 2026-07-03 (WO2 2.1, owner-ordered)

Full RE-VERIFICATION of all 22 names against primary sources (company financial
calendars, dated press releases, Oslo newsweb/MFN announcements, EDGAR archives)
— not a gap-fill. Executed as a 22-agent parallel research sweep (one name per
agent, primary-source-first discipline, cadence inference only where no
announcement exists) + one inline completion (SB). Full evidence rows preserved
in the session workflow journal; the distilled per-name basis strings live in
the calendar file itself. The file simultaneously moved to the R-5 meta/names
shape with `disclosure_type` + `venue` per entry; the calendar is now read only
via `refresh.load_earnings_calendar`.

## Material changes vs the Jun-11 sweep

| Name | Was | Now | Why |
|---|---|---|---|
| **CAPT** | expected Aug-17..31 | **confirmed Sep-1** | its Oslo Newspoint financial calendar (published 2026-03-12) — the Jun-11 sweep missed it; half-yearly reporter |
| **CMBT** | ABSENT | **confirmed Aug-27** | seeded from CMB.TECH's own PR (GlobeNewswire 2026-06-29) |
| **SB** | ABSENT | expected Jul-28..31 | seeded from Q2-25 cadence (released Tue Jul-29-2025 after close, set-date PR a week prior) |
| **FRO** | expected Aug-26..31 | **confirmed Aug-31** | frontlineplc.cy calendar (announced 2026-05-22) |
| **TNK** | expected ..Jul-31 | expected ..Aug-5 (widened) | Q2-25 actually released Jul-30 (Wed-after-close pattern); also **disclosure-type correction: TNK is a 6-K FPI — zero 10-Qs on CIK 1419945** (the "domestic 10-Q filer" assumption was wrong) |
| **CMDB** | expected ..Aug-10 | expected ..Aug-14 (widened) | young listing, thin cadence history; H1-25 6-K filed Aug-8 |
| **FLNG** | slot Aug-28 | confirmed Aug-28, note kept | 2025 release came a week EARLY (Aug-20) — expect the announced date to move up |

Confirmed-and-unchanged (company calendars validated against their own Q1
adherence where possible): ECO Aug-4, SBLK Aug-5, HAFN Aug-28 (Q1 slot matched),
TRMD Aug-26 (Q1 slot matched), MPCC Aug-26, BRUT Aug-13. Cadence-window names
re-verified unchanged: DHT, INSW, NAT, STNG, ASC, TEN (September H1), GNK, GSL,
CCEC.

## Collateral catches — THREE WRONG CIKs in data_sources.yaml

The vet + the WO2 2.2 CIK sweep (every CIK cross-checked against SEC
`company_tickers.json` + live submissions JSON) caught:

| Name | Wrong CIK (was) | Resolved to | Correct CIK |
|---|---|---|---|
| FLNG | 0001738202 | Carmenta Capital Fund SPV (Form-D filer) | **0001772253** |
| CCEC | 0001736035 | Blackstone Secured Lending Fund (BXSL) | **0001392326** (legacy CPLP root) |
| INSW | 0001650044 | nothing on EDGAR | **0001679049** |

Three of 19 SEC names would have silently missed every filing this season —
the EDGAR poller bootstrapped against phantoms. Fixed in data_sources.yaml
(dated comments), poller state re-bootstrapped against real histories (FLNG 72
relevant filings, INSW 169, CCEC 398), and the full verified ticker→CIK map is
now PINNED in tests/test_edgar_poll.py (a CIK change must re-verify + re-pin —
the two-surfaces rule applied to identifiers).

## Completeness audit (inline)

All 22 names present exactly once; zero not-found verdicts; every confirmed row
carries a citable announcement source; disagreements with the old calendar all
listed above; date plausibility checked (TEN September = its documented H1
pattern; CAPT Sep-1 = its published half-yearly calendar). Owner attention:
none required beyond this record — the SEEDED/expected windows will tighten as
sets-date PRs land (~1-2 weeks ahead of release; the EARNINGS-DUE digest lines
start at T-14d).
