class AnalyzeUseCase:
    def analyze(self, repo, symbol, start_date, end_date):
        data = repo.get_data(symbol)
        
        
