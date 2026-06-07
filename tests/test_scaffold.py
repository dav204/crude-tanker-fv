"""Scaffold smoke test: the package and all modules import cleanly.

No valuation logic exists yet — this only guards the project skeleton.
"""

import importlib

import pytest

MODULES = [
    "crude_tanker_fv",
    "crude_tanker_fv.schemas",
    "crude_tanker_fv.loaders",
    "crude_tanker_fv.vessel_values",
    "crude_tanker_fv.nav",
    "crude_tanker_fv.dividend_strip",
    "crude_tanker_fv.cycle",
    "crude_tanker_fv.blend",
    "crude_tanker_fv.breakeven",
    "crude_tanker_fv.sensitivity",
    "crude_tanker_fv.report",
    "crude_tanker_fv.pipeline",
]


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module):
    importlib.import_module(module)
