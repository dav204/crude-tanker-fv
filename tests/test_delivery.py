from datetime import datetime, timedelta, timezone
from crude_tanker_fv import delivery
from test_notify import FakeSMTP, FAKE_ENV


def test_retry_persists_body_and_message_id_and_stops_after_success(tmp_path):
    FakeSMTP.sent = []
    FakeSMTP.raise_on_send = True
    now = datetime(2026, 9, 22, tzinfo=timezone.utc)
    path = delivery.enqueue('subject', 'exact body', tmp_path, now=now)
    first = delivery.attempt(path, environ=FAKE_ENV, smtp_factory=FakeSMTP, now=now)
    assert first['status'] == 'pending' and first['attempts'] == 1
    assert delivery.attempt(path, environ=FAKE_ENV, smtp_factory=FakeSMTP, now=now)['attempts'] == 1
    FakeSMTP.raise_on_send = False
    done = delivery.attempt(path, environ=FAKE_ENV, smtp_factory=FakeSMTP, now=now + timedelta(minutes=5))
    assert done['status'] == 'accepted' and not delivery.pending(tmp_path)
    assert FakeSMTP.sent[-1]['Message-ID'] == first['message_id']
    delivery.attempt(path, environ=FAKE_ENV, smtp_factory=FakeSMTP, now=now + timedelta(days=1))
    assert len(FakeSMTP.sent) == 1


def test_configuration_failure_blocks_instead_of_retrying(tmp_path):
    p = delivery.enqueue('s', 'b', tmp_path)
    result = delivery.attempt(p, environ={})
    assert result['status'] == 'blocked'
    assert result['last_result']['failure_class'] == 'configuration'
    delivery.retry(tmp_path, p.stem)
    assert delivery.pending(tmp_path)[0]['attempts'] == 0


def test_retry_budget_exhausted(tmp_path):
    now = datetime(2026, 9, 22, tzinfo=timezone.utc)
    FakeSMTP.raise_on_send = True
    p = delivery.enqueue('s', 'b', tmp_path, now=now)
    try:
        for seconds in (0, 300, 900, 3600, 21600):
            result = delivery.attempt(p, environ=FAKE_ENV, smtp_factory=FakeSMTP, now=now + timedelta(seconds=seconds))
        assert result['status'] == 'exhausted' and result['attempts'] == 5
    finally:
        FakeSMTP.raise_on_send = False
