from pbrenko_trials.requests.backtest import build_backtest_request


def test_build_backtest_request_without_parameters():
    request = build_backtest_request()

    assert request.has_errors()
    assert bool(request) is False


def test_build_backtest_request_missing_parameters():
    request = build_backtest_request({"symbol": "BTCUSDT", "percent": 6.3, "interval": "1d", "start_date": "202101010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_backtest_request_with_invalid_keys():
    request = build_backtest_request({"sybol": "BTCUSDT", "percent": 6.3, "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_backtest_request_with_invalid_parameters():
    request = build_backtest_request("test")

    assert request.has_errors()
    assert bool(request) is False


def test_build_backtest_request_with_valid_parameters():
    request = build_backtest_request({"symbol": "BTCUSDT", "percent": 6.3, "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert bool(request) is True
