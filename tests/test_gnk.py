"""GNK tests — fill in data, then remove the skip marker.

When the four YAMLs under inputs/ are populated, delete the `pytestmark` line
below to activate the loads-cleanly assertion. Add per-name assertions
(fleet counts, NAV reconciliation band, position) as you understand the name."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs

pytestmark = pytest.mark.skip(
    reason="GNK scaffolded by /add-ticker; data not yet filled in. "
           "Remove this marker when the four YAMLs are populated."
)


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("GNK", "2026-Q1")
    assert ci is not None
