
from pbrenko_trials.repository.tw.twrepo_all_stock import TWRepoAllStock
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date


def test_repo_get_data_with_parameters():
    symbol = "NASDAQ:AMZN"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    start_date_obj = convert_to_date(start_date)
    end_date_obj = convert_to_date(end_date)

    tw_repo_all_stock = TWRepoAllStock()
    data = tw_repo_all_stock.get_data(symbol, interval, start_date_obj, end_date_obj)
    assert isinstance(data, list) is True


def test_repo_list_pairs():
    tw_repo_all_stock = TWRepoAllStock()
    pairs = tw_repo_all_stock.list_pairs()

    assert isinstance(pairs, list) is True
