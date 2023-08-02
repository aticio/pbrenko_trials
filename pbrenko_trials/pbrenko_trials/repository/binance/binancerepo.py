import os
import requests


class BinanceRepo:
    def __init__(self) -> None:
        self.binance_kline_url = os.getenv("BINANCE_KLINE_URL")
        self.binance_exchange_info = os.getenv("BINANCE_EXCHANGE_INFO")

    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        params = {"symbol": symbol, "interval": interval, "startTime": int(start_date_obj.timestamp() * 1000), "endTime": int(end_date_obj.timestamp() * 1000), "limit": 1000}
        response = requests.get(url=self.binance_kline_url, params=params)
        data = response.json()
        return [float(d[4]) for d in data]

    def list_pairs(self):
        exchange_info = self.get_exchange_info()
        pairs = self.get_pairs(exchange_info)
        filtered_pairs = self.filter_usdt_pairs(pairs)
        return filtered_pairs

    def filter_usdt_pairs(self, pairs):
        usdt_paris = []
        for pair in pairs:
            if "USDT" in pair and "BUSD" not in pair and "USDC" not in pair and "LUNA" not in pair and "DOWN" not in pair:
                usdt_paris.append(pair)
        return usdt_paris

    def get_pairs(self, exchange_info):
        pairs = []
        for symbol in exchange_info["symbols"]:
            pairs.append(symbol["symbol"])
        return pairs

    def get_exchange_info(self):
        response = requests.get(self.binance_exchange_info)
        exchange_info = response.json()
        return exchange_info
