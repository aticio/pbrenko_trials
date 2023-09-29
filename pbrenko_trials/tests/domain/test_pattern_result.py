from pbrenko_trials.domain.pattern_result import PatternResult
from pbrenko_trials.domain.brick import Brick

from datetime import datetime


def test_pattern_result_model_init():
    pattern_result = PatternResult(
        symbol="BTCUSDT",
        percent=2.6,
        start_date=datetime(2022, 1, 1, 0, 0, 0),
        end_date=datetime(2023, 1, 1, 0, 0, 0),
        bricks=[Brick(type="up", open=100, close=200, low=100, high=230)],
        found_pattern="one-back pattern"
    )

    assert pattern_result.symbol == "BTCUSDT"
    assert pattern_result.percent == 2.6
    assert pattern_result.start_date == datetime(2022, 1, 1, 0, 0, 0)
    assert pattern_result.end_date == datetime(2023, 1, 1, 0, 0, 0)
    assert pattern_result.bricks == [Brick(type="up", open=100, close=200, low=100, high=230)]
    assert pattern_result.found_pattern == "one-back pattern"
