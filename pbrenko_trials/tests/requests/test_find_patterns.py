from pbrenko_trials.requests.find_patterns import build_find_patterns_request


def test_build_find_patterns_request_without_parameters():
    request = build_find_patterns_request()

    assert request.has_errors()
    assert bool(request) is False


def test_build_find_patterns_request_missing_parameters():
    request = build_find_patterns_request({"symbol": "BTCUSDT", "interval": "1d", "start_date": "202101010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_find_patterns_request_with_invalid_keys():
    request = build_find_patterns_request({"sybol": "BTCUSDT", "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_find_patterns_request_with_invalid_parameters():
    request = build_find_patterns_request("test")

    assert request.has_errors()
    assert bool(request) is False


def test_build_find_patterns_request_with_valid_parameters():
    request = build_find_patterns_request({"symbol": "BTCUSDT", "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    assert bool(request) is True
