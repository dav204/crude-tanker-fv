"""iter_history's client-side oldest bound (the 2026-07-27 wedge fix).

The RC API silently ignores an ``oldest`` param it can't parse (hand-typed
second-precision ISO without ms/Z), which made a bounded --since walk
unbounded: it hit the WO2 1.1 sanity cap, exited 3 without persisting the
new lane's cursor, and every scheduled run after tripped the CURSOR-RESET
guard (2026-07-24 -> 27). The bound is now enforced client-side too.
"""

from crude_tanker_fv import rocketchat_api as rc


def test_iso_key_orders_api_and_cli_forms_together():
    api = rc._iso_key("2026-07-24T12:36:09.768Z")
    cli = rc._iso_key("2026-07-26T00:00:00")  # naive → UTC
    assert api < cli
    assert rc._iso_key("2026-07-26T00:00:00.000Z") == cli


def test_iter_history_stops_at_oldest_client_side(monkeypatch):
    pages = [
        {"success": True, "messages": [
            {"ts": "2026-07-27T10:00:00.000Z", "msg": "new-1"},
            {"ts": "2026-07-26T09:00:00.000Z", "msg": "new-2"},
            # older than the bound — the walk must stop HERE even though the
            # (fake) server ignored the oldest param and kept paginating:
            {"ts": "2026-07-25T08:00:00.000Z", "msg": "too-old"},
        ]},
        {"success": True, "messages": [
            {"ts": "2026-07-20T08:00:00.000Z", "msg": "never-reached"},
        ]},
    ]
    calls = []

    class _Resp:
        def __init__(self, payload):
            self._payload = payload
        def raise_for_status(self):
            pass
        def json(self):
            return self._payload

    def fake_get(url, params=None, headers=None, timeout=None):
        calls.append(params)
        return _Resp(pages[min(len(calls) - 1, len(pages) - 1)])

    monkeypatch.setattr(rc, "_get", fake_get)
    monkeypatch.setattr(rc, "BATCH_SIZE", 3)

    got = [m["msg"] for m in rc.iter_history("h", "room", {}, "2026-07-26T00:00:00")]
    assert got == ["new-1", "new-2"]   # stops strictly before the bound
    assert len(calls) == 1             # never paginated past the stop


def test_decide_oldest_since_binds_even_with_missing_cursor():
    from crude_tanker_fv.ingest_rocketchat import _decide_oldest
    # the 2026-07-27 wedge: cursor-less source + --since must use the bound
    assert _decide_oldest("2026-07-24T13:00:00", False, [None]) == "2026-07-24T13:00:00"
    assert _decide_oldest(None, True, ["2026-07-24T12:36:09.768Z"]) is None
    assert _decide_oldest(None, False, [None]) is None  # guard upstream refuses this case
    assert _decide_oldest(None, False, ["2026-07-20T00:00:00.000Z",
                                        "2026-07-24T12:36:09.768Z"]) == "2026-07-20T00:00:00.000Z"
