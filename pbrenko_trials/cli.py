#!/usr/bin/env python
import sys
import os
import json

from pbrenko_trials.repository.memrepo import MemRepo
from pbrenko_trials.repository.binance.binancerepo import BinanceRepo
from pbrenko_trials.use_cases.analyze import AnalyzeUseCase
from pbrenko_trials.use_cases.backtest import BacktestUseCase
from pbrenko_trials.requests.analyze import build_analyze_request
from pbrenko_trials.requests.backtest import build_backtest_request

APPLICATION_CONFIG_PATH = "config"


def analyze(symbol, repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()

    request = build_analyze_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

    analyze_use_case = AnalyzeUseCase()
    result = analyze_use_case.analyze(repo, request)
    print(result.value)


def backtest(symbol, repo_type, percent, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()

    request = build_backtest_request({"symbol": symbol, "percent": percent, "interval": interval, "start_date": start_date, "end_date": end_date})

    backtest_use_case = BacktestUseCase()
    result = backtest_use_case.backtest(repo, request)
    print(result.value)


def setenv(variable, default):
    os.environ.setdefault(variable, default)


def app_config_file(config):
    return os.path.join(APPLICATION_CONFIG_PATH, f"{config}.json")


def read_json_configuration(config):
    # Read configuration from the relative JSON file
    with open(app_config_file(config)) as f:
        config_data = json.load(f)

    # Convert the config into a usable Python dictionary
    config_data = dict((i["name"], i["value"]) for i in config_data)

    return config_data


def configure_app(config):
    configuration = read_json_configuration(config)

    for key, value in configuration.items():
        setenv(key, value)


if __name__ == "__main__":
    config = sys.argv[1]
    configure_app(config)
    if sys.argv[2] == "analyze":
        symbol = sys.argv[3]
        repo_type = sys.argv[4]
        interval = sys.argv[5]
        start_date = sys.argv[6]
        end_date = sys.argv[7]
        analyze(symbol, repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "backtest":
        symbol = sys.argv[3]
        repo_type = sys.argv[4]
        percent = sys.argv[5]
        interval = sys.argv[6]
        start_date = sys.argv[7]
        end_date = sys.argv[8]
        backtest(symbol, repo_type, percent, interval, start_date, end_date)
