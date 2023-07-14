import os
import requests


class BinanceRepo:
    def __init__(self) -> None:
        self.binance_kline_url = os.getenv("BINANCE_KLINE_URL")

    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        params = {"symbol": symbol, "interval": interval, "startTime": int(start_date_obj.timestamp() * 1000), "endTime": int(end_date_obj.timestamp() * 1000)}
        response = requests.get(url=self.binance_kline_url, params=params)
        data = response.json()
        return [float(d[4]) for d in data]
