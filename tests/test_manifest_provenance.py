"""General manifest-claim provenance guard.

The DHT catch (2026-06-30) was the existence proof: a manifest line said the fleet was
"100% scrubber-fitted **(confirmed)**" while the cited 6-K says "scrubber" zero times — a claim
carrying the word *confirmed* that the filing did not confirm. "(confirmed)" ≠ confirmed. The
annotation was load-bearing (a future reader, or a guard that trusted the word, would read it as
"done, don't re-check") and it was hollow.

So the clearance bar for any verification CLAIM in a manifest / balance sheet is a *resolvable
citation* — a specific filing, note, broker source, owner attestation, or dated verification —
never the bare word. This guard is field-GENERAL (the defect is "manifest claims lack enforced
provenance", of which scrubber was only the instance under the light): it reds any "confirmed"/
"verified"/"confirms" assertion that does not reference a source. Honest forms — imperative TODOs
("confirm at H1", "VERIFY at…") and negations ("unconfirmed", "unverified") — are not claims and
are exempt. The value-moving FLAGS themselves are covered by the field-specific provenance guards
(test_scrubber_provenance, test_newbuild_convention, AGE0_BASIS); this layer catches hollow
verification CLAIMS in any field.
"""

import glob
import re

import pytest

# Asserting forms (past / 3rd-person). NOT "confirm"/"verify" (imperative TODO) and NOT
# "unconfirmed"/"unverified" (negations) — \b... \b means the "un"-prefixed words don't match.
CLAIM_RE = re.compile(r"\b(confirmed|verified|confirms)\b", re.IGNORECASE)

# A resolvable source reference. A confirmation claim must cite at least one of these — a primary
# filing, a note/accession, a named broker/independent source, an owner/issuer attestation, an
# adversarial-verification marker, or a dated/vintage reference (yyyy-mm-dd or a 4-digit year).
CITATION_RE = re.compile(
    r"6-?k|10-?[qk]|20-?f|note\s*\d|accession|\bpareto\b|xclusiv|clarksons|compass|\bvie\b|"
    r"euronext|newsweb|\bledger\b|\bissuer\b|owner-confirmed|adversarial|\bmb\b|gmail|"
    r"\d{4}-\d{2}-\d{2}|\b(?:19|20)\d{2}\b",
    re.IGNORECASE,
)

_FILES = sorted(
    glob.glob("inputs/fleet_manifests/*.yaml") + glob.glob("inputs/balance_sheets/*.yaml")
)


def test_no_unbacked_verification_claims():
    """Every 'confirmed'/'verified'/'confirms' assertion in a manifest or balance sheet must carry
    a resolvable citation on the same line. A bare claim (the DHT '(confirmed)' case) hard-fails —
    so the word can never again stand in for the source."""
    violations = []
    for path in _FILES:
        if "_template" in path:
            continue
        for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
            if CLAIM_RE.search(line) and not CITATION_RE.search(line):
                violations.append(f"{path}:{lineno}: {line.strip()}")
    assert not violations, (
        "Unbacked verification claim(s) — a 'confirmed'/'verified' assertion with no resolvable "
        "citation (filing / note / broker / owner / date). '(confirmed)' is not a source; add the "
        "reference or rephrase as an explicit pending TODO:\n  " + "\n  ".join(violations)
    )


def test_guard_actually_discriminates():
    """The guard must reject a bare claim and accept a cited one (so it can't silently pass all)."""
    assert CLAIM_RE.search("100% scrubber-fitted (confirmed)")
    assert not CITATION_RE.search("100% scrubber-fitted (confirmed)")          # bare -> would fail
    assert CITATION_RE.search("scrubber-fitted, confirmed per Q1-2026 6-K Note 5")  # cited -> passes


# ---------------------------------------------------------------------------
# NAV-FIGURE provenance (the NAT instance, 2026-06-30). The principle is field-general:
# any manifest figure that MOVES NAV must resolve to a citation; a figure flagged as an
# ESTIMATE (a tilde, "approx", "[ESTIMATE]", "typical", "assumed") is a red regardless of
# whether it is populated — "present but uncited" fails identically to "absent", because for
# a NAV-driver an uncited number is worse than a missing one (the missing one fails loudly,
# the uncited one silently drives a move). Applied first to the §9.6-driving newbuild
# commitment/advance figures, where NAT exposed it and where the convention queue acts.
import glob as _glob  # noqa: E402
import re as _re  # noqa: E402

import yaml as _yaml  # noqa: E402

# Every term in the NAV equation (nav.py compute_nav): NAV = fleet − debt − leases − commitment
# + advances + cash + working_capital − preferred + shuttle. "NAV-moving" is the guard's scope
# criterion (the owner's clean line: in the NAV equation -> must trace; not in it -> benign).
_NAV_FIELDS = (
    "total_debt", "cash_and_equivalents", "working_capital_net", "lease_liabilities",
    "newbuild_capex_commitments", "newbuild_advances_paid", "preferred_equity",
    "shuttle_contracted_book",
)
# Context for each half of the equation. Newbuild lines are scanned with a broad estimate marker
# (bare "~" included — validated clean there); the OTHER NAV fields (debt/cash/leases/preferred/
# working-capital/shuttle) use an EXPLICIT keyword only, because their comments carry derivations
# and asides where a bare "~" is not an admission of non-provenance (e.g. "~$34.2M gain" next to an
# exactly-derived working-capital figure).
_NB_CTX_RE = _re.compile(r"newbuild|under construction|commitment|advance|instal|capex|\bnb\b", _re.IGNORECASE)
_OTHER_NAV_CTX_RE = _re.compile(
    r"\bdebt\b|\bcash\b|working capital|\blease|preferred|shuttle|\bNIBD\b|liquidit|"
    r"liabilit|payable|receivable|deposit",
    _re.IGNORECASE,
)
_ESTIMATE_RE = _re.compile(r"~|\bapprox\b|\[est|estimate|\bassumed\b|\btypical\b|placeholder|~equal", _re.IGNORECASE)
_KEYWORD_RE = _re.compile(r"\bapprox\b|\[est|\bestimated\b|\bassumed\b|placeholder|\bguess\b", _re.IGNORECASE)
_MONEY_RE = _re.compile(r"\$\s?[\d,]+|\b\d+(?:\.\d+)?\s?(?:M\b|bn\b|million|billion)|\b\d{6,}\b")

# Names with an estimate-flagged, uncited NAV-equation figure — the figure-provenance audit queue.
# Each clears ONLY by sourcing the figure (estimate marker gone, citation present). xfail-strict so
# a name can't leave by deleting the figure. THIS GATES THE CONVENTION QUEUE: a name here has an
# uncited NAV-driver, so wiring its newbuilds on-curve (§9.6) would build the move on sand.
NAV_FIGURE_ESTIMATE_QUEUE = {
    "brut", "cmbt", "flng", "hafn", "ten",
}  # nat/asc/stng left; trmd left 2026-07-02 (all six [ESTIMATE] figures sourced to the Q1-2026 6-K, workflow-verified)


def _nav_figure_estimate_flagged(path: str) -> bool:
    """A NAV-equation figure declared an estimate without a resolvable citation. Newbuild context:
    any estimate marker (incl. bare "~"). Other NAV fields (debt/cash/…): EXPLICIT keyword only
    (APPROX/[ESTIMATE]/estimated/assumed) — precise against derivations/asides."""
    doc = _yaml.safe_load(open(path))
    has_nb = bool(doc.get("newbuild_capex_commitments") or doc.get("newbuild_advances_paid"))
    for line in open(path, encoding="utf-8"):
        if _MONEY_RE.search(line) and not CITATION_RE.search(line):
            if has_nb and _NB_CTX_RE.search(line) and _ESTIMATE_RE.search(line):
                return True
            if _OTHER_NAV_CTX_RE.search(line) and _KEYWORD_RE.search(line):
                return True
    return False


def _nav_balance_sheets():
    return {p.split("/")[-1].replace("_2026-Q1.yaml", ""): p for p in sorted(_glob.glob("inputs/balance_sheets/*.yaml"))}


def test_every_estimate_flagged_nav_figure_is_queued():
    """Enumeration: a name with an uncited estimate on ANY NAV-equation field (commitment, advance,
    debt, cash, working capital, …) must be in the queue. A NEW such name (the next NAT) hard-fails
    until placed — so an uncited NAV-driver can never silently enter the model."""
    for name, path in _nav_balance_sheets().items():
        if _nav_figure_estimate_flagged(path):
            assert name in NAV_FIGURE_ESTIMATE_QUEUE, (
                f"{name}: a NAV-equation figure is an uncited estimate (APPROX/[ESTIMATE]/tilde) but "
                f"is not in NAV_FIGURE_ESTIMATE_QUEUE — source it to a citation, or queue it. A figure "
                f"in the NAV equation may not rest on an estimate marker."
            )


def _figq_param(name: str):
    return pytest.param(name, marks=pytest.mark.xfail(strict=True, reason=f"{name}: NAV figure uncited estimate"))


@pytest.mark.parametrize("name", [_figq_param(n) for n in sorted(NAV_FIGURE_ESTIMATE_QUEUE)])
def test_nav_figure_sourced(name):
    """xfail-strict figure-provenance queue. Clears ONLY by sourcing the figure (estimate marker
    gone, citation present) — a strict xpass if cleared by removing the marker or the figure, so
    the queue can't be emptied by hiding the tilde."""
    bs = _nav_balance_sheets()
    assert name in bs and not _nav_figure_estimate_flagged(bs[name]), (
        f"{name}: a NAV-equation figure is still an uncited estimate (figure-provenance queue)."
    )
