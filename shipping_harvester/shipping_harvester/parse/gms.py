"""GMS (Global Marketing Systems) weekly ship-recycling report parser.

GMS is the largest cash buyer; its weekly quotes USD/LDT per recycling market
(Bangladesh, India, Pakistan, Turkey), split by vessel type:
    Gen Cargo (Dry) / Bulker  ->  dry scrap price
    Tankers (Wet) / Tanker    ->  tanker scrap price
    Containers                ->  container (captured; no class mapping)
Prices are usually ranges ("USD 460-465/LT LDT"); we take the midpoint.

Emits demolition marks keyed by market (note) and type (vessel_class). The
factor adapter's scrap_curve turns these into per-class scrap_25yr via
$/ldt * lightweight, using the tanker price for tanker classes and the dry price
for dry classes.

KEY ROBUSTNESS POINT: a GMS report is full of other dollar figures -- steel
plate (USD 540/ton), oil (USD 62/barrel), currencies. So every price is anchored
to the LDT unit (`... /LT LDT`); a number not followed by LDT is ignored. That
cleanly separates scrap prices from steel/oil/FX.

Built against GMS's canonical demo-rankings format (e.g. "Bangladesh ...
Gen Cargo (Dry): USD 460-465/LT LDT Tankers (Wet): USD 480-485/LT LDT").
Confirm with `cli inspect` on a real issue -- some GMS PDFs render the headline
table as a graphic, in which case only the prose recap is extractable.
"""
from __future__ import annotations

import re

from ..models import KIND_DEMOLITION, Mark
from . import base


_MARKETS = ("Bangladesh", "India", "Pakistan", "Turkey")

# a USD/LDT price (single or range), anchored to the LDT unit
_PRICE = r"(?:USD\s*)?(\d{3}(?:\s*[-\u2013]\s*\d{3})?)\s*/?\s*(?:LT\s*)?LDT"

# vessel-type labels -> canonical type token (used as vessel_class on the mark)
_TYPE_LABELS = {
    "Tanker": r"(?:Tankers?\s*\(?\s*Wet\s*\)?|\bTankers?\b|\bWet\b)",
    "Container": r"\bContainers?\b",
    "Dry": r"(?:Gen\s*Cargo|\bBulkers?\b|Dry\s*Bulk|\(\s*Dry\s*\)|\bDry\b)",
}


def _midpoint(s: str) -> float:
    nums = [float(x) for x in re.findall(r"\d+", s)]
    return round(sum(nums) / len(nums), 2) if nums else 0.0


class GmsParser(base.BrokerParser):
    broker_id = "gms"

    def extract(self, tables, text: str) -> list[Mark]:
        marks: list[Mark] = []
        for market in _MARKETS:
            block = self._market_block(text, market)
            if block is None:
                continue
            for vtype, label in _TYPE_LABELS.items():
                price = self._price_for(block, label)
                if price is not None:
                    marks.append(Mark(
                        kind=KIND_DEMOLITION, vessel_class=vtype, metric="$/ldt",
                        value=price, unit="usd_per_ldt", note=market.lower(),
                    ))
        return marks

    @staticmethod
    def _market_block(text: str, market: str) -> str | None:
        """The first occurrence of the market whose following window yields an
        LDT-anchored price. The window is truncated at the next market name so
        prices don't bleed across markets."""
        for m in re.finditer(rf"\b{market}\b", text):
            nxts = [p for p in (text.find(mk, m.end()) for mk in _MARKETS) if p != -1]
            end = min([*nxts, m.end() + 260])
            window = text[m.end():end]
            if re.search(_PRICE, window, re.I):
                return window
        return None

    @staticmethod
    def _price_for(block: str, label_pat: str) -> float | None:
        m = re.search(label_pat + r"[^\d]{0,18}" + _PRICE, block, re.I)
        return _midpoint(m.group(1)) if m else None
