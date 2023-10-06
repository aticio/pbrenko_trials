import pandas as pd
import yfinance as yf


class YahooRepoTR:
    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d")
        end_date_str = end_date_obj.strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol, interval=interval, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)['Close']
        return data.values.tolist()

    def list_pairs(self):
        tickers = pd.read_html("https://tr.wikipedia.org/wiki/Borsa_%C4%B0stanbul#2023_itibar%C4%B1yla_BIST100'de_i%C5%9Flem_g%C3%B6ren_%C5%9Firketler")[2]
        symbol_list = tickers["Kod [9]"].values.tolist()
        corrected_symbol_list = []
        for symbol in symbol_list:
            corrected_symbol_list.append(symbol + ".IS")
        return corrected_symbol_list
