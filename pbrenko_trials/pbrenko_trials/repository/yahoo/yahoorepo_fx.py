import yfinance as yf


class YahooRepoFX:
    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d")
        end_date_str = end_date_obj.strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol, interval=interval, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)['Close']
        return data.values.tolist()

    def list_pairs(self):
        return ["EURUSD=X", "JPY=X", "GBPUSD=X", "CHF=X", "AUDUSD=X", "CAD=X", "NZDUSD=X", "EURGBP=X", "EURCHF=X", "EURJPY=X", "GBPJPY=X", "CHFJPY=X", "AUDJPY=X", "CADJPY=X", "NZDJPY=X", "AUDNZD=X", "AUDCHF=X", "GBPCHF=X", "CADCHF=X", "EURTRY=X", "TRY=X", "MXN=X", "ZAR=X", "HKD=X", "SGD=X", "THB=X", "SEK=X", "DKK=X"]
