class BinanceRepo:
    def __init__(self) -> None:
        


    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        self.symbol = symbol
        self.interval = interval
        self.start_date_obj = start_date_obj
        self.end_date_obj = end_date_obj