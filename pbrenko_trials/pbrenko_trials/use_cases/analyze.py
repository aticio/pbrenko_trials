from pbrenko_trials.use_cases.tools.find_optimum_percent import find_optimum_percent
from pbrenko_trials.use_cases.tools.pbrenko_creator import PBRenkoCreator
from pbrenko_trials.use_cases.tools.score import calculate_score
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date
from pbrenko_trials.domain.result import Result
from pbrenko_trials.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


class AnalyzeUseCase:
    def analyze(self, repo, request):
        if not request:
            return build_response_from_invalid_request(request)

        try:
            start_date_obj = convert_to_date(request.parameters["start_date"])
            end_date_obj = convert_to_date(request.parameters["end_date"])
            symbol = request.parameters["symbol"]

            data = repo.get_data(symbol, start_date_obj, end_date_obj)

            if len(data) == 0:
                return ResponseFailure(ResponseTypes.RESOURCE_ERROR, "No data returned from the repository")

            percent = find_optimum_percent(data)

            pbrenko_creator = PBRenkoCreator()
            pbrenko = pbrenko_creator.create_pbrenko(data, percent)
            score = calculate_score(pbrenko.bricks, len(data))

            result = Result(
                symbol=symbol,
                percent=percent,
                score=score,
                start_date=start_date_obj,
                end_date=end_date_obj,
            )

            return ResponseSuccess(result)
        except Exception as exc:
            return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
