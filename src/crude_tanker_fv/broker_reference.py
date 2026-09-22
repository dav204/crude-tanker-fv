"""Broker ratios belong to their quoted price vintage, never the current tape."""


def broker_reference(entry):
    price = entry.get("as_of_price", entry.get("current_price"))
    ratio = entry.get("consensus_pnav")
    if price is None or ratio is None or price <= 0 or ratio <= 0:
        return {"nav": None, "price": price, "pnav": ratio, "as_of": str(entry.get("as_of") or "") or None}
    return {"nav": price / ratio, "price": price, "pnav": ratio,
            "as_of": str(entry.get("as_of") or "") or None}
