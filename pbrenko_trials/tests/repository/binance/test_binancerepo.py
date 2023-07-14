from pbrenko_trials.repository.binance.binancerepo import BinanceRepo
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date


def test_repo_get_data_with_parameters():
    symbol = "BTCUSDT"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    start_date_obj = convert_to_date(start_date)
    end_date_obj = convert_to_date(end_date)

    binance_repo = BinanceRepo()
    data = binance_repo.get_data(symbol, interval, start_date_obj, end_date_obj)

    assert isinstance(data, list) is True
    assert binance_repo.symbol == symbol
    assert binance_repo.interval == interval
    assert binance_repo.start_date_obj == start_date_obj
    assert binance_repo.end_date_obj == end_date_obj
