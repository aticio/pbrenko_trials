import yfinance as yf
import requests
import pandas as pd


class YahooRepoAllStock:
    def get_data(self, symbol, interval, start_date_obj, end_date_obj):
        start_date_str = start_date_obj.strftime("%Y-%m-%d")
        end_date_str = end_date_obj.strftime("%Y-%m-%d")
        data = yf.download(tickers=symbol, interval=interval, start=start_date_str, end=end_date_str, auto_adjust=True, progress=False)['Close']
        return data.values.tolist()

    def list_pairs(self):
        data = pd.read_csv('https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo')
        return data.symbol.tolist()
