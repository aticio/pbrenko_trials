from pbrenko_trials.domain.result import Result

from datetime import datetime


def test_result_model_init():
    result = Result(
        symbol="BTCUSDT",
        percent=2.6,
        score=4.2,
        start_date=datetime(2022, 1, 1, 0, 0, 0),
        end_date=datetime(2023, 1, 1, 0, 0, 0)
    )

    assert result.symbol == "BTCUSDT"
    assert result.percent == 2.6
    assert result.score == 4.2
    assert result.start_date == datetime(2022, 1, 1, 0, 0, 0)
    assert result.end_date == datetime(2023, 1, 1, 0, 0, 0)