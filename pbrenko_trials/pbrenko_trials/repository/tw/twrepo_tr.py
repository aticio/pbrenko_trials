import pandas as pd
from datetime import datetime
from tvDatafeed import TvDatafeed, Interval


class TWRepoTR:
    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d %H:%M:%S")
        end_date_str = end_date_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(start_date_obj, end_date_str)
        delta = datetime.now() - start_date_obj
        if delta.days < 0:
            return []

        tv = TvDatafeed()

        if interval == "1d":
            interval_param = Interval.in_daily
        elif interval == "1h":
            interval_param = Interval.in_1_hour

        symbol_info = symbol.split(":")

        data = tv.get_hist(symbol=symbol_info[1], exchange=symbol_info[0], interval=interval_param,n_bars=delta.days)
        selected_data = data.loc[start_date_str:end_date_str]
        return selected_data["close"].tolist()

    def list_pairs(self):
        tickers = pd.read_html("https://tr.wikipedia.org/wiki/Borsa_%C4%B0stanbul#2023_itibar%C4%B1yla_BIST100'de_i%C5%9Flem_g%C3%B6ren_%C5%9Firketler")[1]
        symbol_list = tickers["Kod [9]"].values.tolist()
        corrected_symbol_list = []
        for symbol in symbol_list:
            corrected_symbol_list.append(f'BIST:{symbol}')
        return corrected_symbol_list
