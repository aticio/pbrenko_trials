import yfinance as yf
import requests


class YahooRepoAllStock:
    def __init__(self, exchange) -> None:
        self.exchange = exchange

    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d")
        end_date_str = end_date_obj.strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol, interval=interval, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)['Close']
        return data.values.tolist()

    def list_pairs(self):
        response = requests.get("https://dumbstockapi.com/stock?format=tickers-only&exchange=" + self.exchange)
        exchange_info = response.json()
        new_exchange_info = []
        for stock in exchange_info:
            if "^" in stock:
                new_stock = stock.split("^", 1)[0]
                new_exchange_info.append(new_stock)
            elif "." in stock:
                new_stock = stock.replace(".", "-")
                new_exchange_info.append(new_stock)
            else:
                new_exchange_info.append(stock)
        return new_exchange_info
