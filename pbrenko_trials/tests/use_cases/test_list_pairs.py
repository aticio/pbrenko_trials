import pytest

from unittest import mock
from pbrenko_trials.use_cases.list_pairs import list_pairs
from pbrenko_trials.responses import ResponseTypes


@pytest.fixture
def exchange_info():
    return ["BTCUSDT", "ETHUSDT", "AVAXUSDT"]


def test_list_pairs(exchange_info):
    repo = mock.Mock()
    repo.list_pairs.return_value = exchange_info

    response = list_pairs(repo)

    repo.list_pairs.assert_called_with()
    assert bool(response) is True
    assert response.value == ["BTCUSDT", "ETHUSDT", "AVAXUSDT"]


def test_list_pairs_invalid_resource():
    repo = mock.Mock()
    repo.list_pairs.return_value = []

    response = list_pairs(repo)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.RESOURCE_ERROR,
        "message": "No data returned from the repository",
    }
