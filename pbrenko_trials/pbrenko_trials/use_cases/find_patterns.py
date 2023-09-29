from pbrenko_trials.use_cases.tools.find_optimum_percent import find_optimum_percent
from pbrenko_trials.use_cases.tools.pbrenko_creator import PBRenkoCreator
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date
from pbrenko_trials.use_cases.tools.draw_chart import draw_chart
from pbrenko_trials.domain.pattern_result import PatternResult
from pbrenko_trials.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


class FindPatternsUseCase:
    def __init__(self, drawing_enabled=False):
        self.drawing_enabled = drawing_enabled

    def find_patterns(self, repo, request):
        if not request:
            print("burda")
            return build_response_from_invalid_request(request)

        try:
            start_date_obj = convert_to_date(request.parameters["start_date"])
            end_date_obj = convert_to_date(request.parameters["end_date"])
            symbol = request.parameters["symbol"]
            interval = request.parameters["interval"]

            data = repo.get_data(symbol, interval, start_date_obj, end_date_obj)
            if len(data) == 0:
                return ResponseFailure(ResponseTypes.RESOURCE_ERROR, "No data returned from the repository")

            if len(data) * 2 < (end_date_obj - start_date_obj).days:
                return ResponseFailure(ResponseTypes.RESOURCE_ERROR, "Not enough data point.")

            percent = find_optimum_percent(data)
            if percent is None:
                pattern_result = PatternResult(
                    symbol=symbol,
                    percent=-1,
                    start_date=start_date_obj,
                    end_date=end_date_obj,
                    found_pattern=""
                )
                return ResponseSuccess(pattern_result)
            pbrenko_creator = PBRenkoCreator()
            pbrenko = pbrenko_creator.create_pbrenko(data, percent)

            found_pattern = "test_pattern"

            pattern_result = PatternResult(
                symbol=symbol,
                percent=percent,
                start_date=start_date_obj,
                end_date=end_date_obj,
                bricks=pbrenko.bricks,
                found_pattern=found_pattern
            )

            if self.drawing_enabled is True:
                draw_chart(pbrenko.bricks, percent, symbol + "-" + request.parameters["interval"] + "-" + request.parameters["start_date"] + "-" + request.parameters["end_date"])

            return ResponseSuccess(pattern_result)
        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
