from pbrenko_trials.requests.analyze_best import build_analyze_best_request


def test_build_analyze_best_request_without_parameters():
    request = build_analyze_best_request()

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_best_request_missing_parameters():
    request = build_analyze_best_request({"symbol": "BTCUSDT", "interval": "1d", "start_date": "202101010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_best_request_with_invalid_keys():
    request = build_analyze_best_request({"sybol": "BTCUSDT", "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_best_request_with_invalid_parameters():
    request = build_analyze_best_request("test")

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_best_request_with_valid_parameters():
    request = build_analyze_best_request({"symbol": "BTCUSDT", "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert bool(request) is True
