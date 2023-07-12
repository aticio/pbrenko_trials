from pbrenko_trials.use_cases.tools.date_converter import convert_to_date
from datetime import datetime


def test_date_converter():
    start_date = "202101010000"
    start_date_obj = datetime(2021, 1, 1, 0, 0, 0)

    result = convert_to_date(start_date)

    assert result == start_date_obj
