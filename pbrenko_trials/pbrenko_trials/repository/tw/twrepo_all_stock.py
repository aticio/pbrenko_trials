import pandas as pd
from datetime import datetime
from tvDatafeed import TvDatafeed, Interval


class TWRepoAllStock:
    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d %H:%M:%S")
        end_date_str = end_date_obj.strftime("%Y-%m-%d %H:%M:%S")
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
        data = pd.read_csv('https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo')
        symbols = []
        for index, d in data.iterrows():
            if d["exchange"] == "NYSE ARCA" or d["exchange"] == "NYSE MKT":
                symbols.append(f'AMEX:{d["symbol"]}')
            else:
                symbols.append(f'{d["exchange"]}:{d["symbol"]}')
        return symbols
