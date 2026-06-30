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
