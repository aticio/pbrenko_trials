
from pbrenko_trials.repository.yahoo.yahoorepo import YahooRepo
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date


def test_repo_get_data_with_parameters():
    symbol = "AMZN"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    start_date_obj = convert_to_date(start_date)
    end_date_obj = convert_to_date(end_date)

    yahoo_repo = YahooRepo()
    data = yahoo_repo.get_data(symbol, interval, start_date_obj, end_date_obj)

    assert isinstance(data, list) is True


def test_repo_list_pairs():
    yahoo_repo = YahooRepo()
    pairs = yahoo_repo.list_pairs()

    assert isinstance(pairs, list) is True
