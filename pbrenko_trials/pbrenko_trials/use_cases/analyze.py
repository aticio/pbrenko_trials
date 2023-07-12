from pbrenko_trials.use_cases.tools.find_optimum_percent import find_optimum_percent
from pbrenko_trials.use_cases.tools.pbrenko_creator import PBRenkoCreator
from pbrenko_trials.use_cases.tools.score import calculate_score
from pbrenko_trials.use_cases.tools.date_converter import convert_to_date
from pbrenko_trials.domain.result import Result


class AnalyzeUseCase:
    def analyze(self, repo, symbol, start_date, end_date):
        start_date_obj = convert_to_date(start_date)
        end_date_obj = convert_to_date(end_date)
        
        data = repo.get_data(symbol, start_date_obj, end_date_obj)

        percent = find_optimum_percent(data)

        pbrenko_creator = PBRenkoCreator()
        pbrenko = pbrenko_creator.create_pbrenko(data, percent)
        score = calculate_score(pbrenko.bricks, len(data))

        result = Result(
            symbol = symbol,
            percent = percent,
            score = score,
            start_date = start_date_obj,
            end_date = end_date_obj,
        )

        return result
