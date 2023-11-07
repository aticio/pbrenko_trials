#!/usr/bin/env python
import sys
import os
import json

from pbrenko_trials.repository.memrepo import MemRepo
from pbrenko_trials.repository.binance.binancerepo import BinanceRepo
from pbrenko_trials.repository.yahoo.yahoorepo import YahooRepo
from pbrenko_trials.repository.yahoo.yahoorepo_tr import YahooRepoTR
from pbrenko_trials.repository.yahoo.yahoorepo_fx import YahooRepoFX
from pbrenko_trials.repository.yahoo.yahoorepo_all_stock import YahooRepoAllStock
from pbrenko_trials.repository.tw.twrepo_all_stock import TWRepoAllStock
from pbrenko_trials.repository.tw.twrepo_tr import TWRepoTR
from pbrenko_trials.use_cases.analyze import AnalyzeUseCase
from pbrenko_trials.use_cases.backtest import BacktestUseCase
from pbrenko_trials.use_cases.find_patterns import FindPatternsUseCase
from pbrenko_trials.use_cases.analyze_best import AnalyzeBestUseCase
from pbrenko_trials.use_cases.list_pairs import list_pairs
from pbrenko_trials.requests.analyze import build_analyze_request
from pbrenko_trials.requests.backtest import build_backtest_request
from pbrenko_trials.requests.analyze_best import build_analyze_best_request
import pandas as pd

APPLICATION_CONFIG_PATH = "config"


def analyze(symbol, repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    request = build_analyze_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

    analyze_use_case = AnalyzeUseCase(drawing_enabled=True)
    result = analyze_use_case.analyze(repo, request)
    print("symbol:", result.value.symbol, "percent:", result.value.percent, "score:", result.value.score)

    for b in result.value.bricks:
        print(b)


def analyze_best(symbol, repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = TWRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()
    elif repo_type == "stock-all":
        repo = TWRepoAllStock()

    request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

    analyze_best_use_case = AnalyzeBestUseCase(drawing_enabled=True)
    result = analyze_best_use_case.analyze_best(repo, request)
    print("symbol:", result.value.symbol, "percent:", result.value.percent, "score:", result.value.score)
    for b in result.value.bricks:
        print(b)


def backtest(symbol, repo_type, percent, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = TWRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()
    elif repo_type == "stock-all":
        repo = TWRepoAllStock()

    request = build_backtest_request({"symbol": symbol, "percent": percent, "interval": interval, "start_date": start_date, "end_date": end_date})

    backtest_use_case = BacktestUseCase(drawing_enabled=True)
    result = backtest_use_case.backtest(repo, request)

    for b in result.value.bricks:
        print(b)
    print("------------")
    print("symbol:", result.value.symbol, "percent:", result.value.percent, "score:", result.value.score)


def analyze_all(repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    response = list_pairs(repo)
    list_of_results = []
    for symbol in response.value:
        request = build_analyze_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

        analyze_use_case = AnalyzeUseCase()
        response = analyze_use_case.analyze(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.score > 0:
                list_of_results.append(result_object)
    list_of_results.sort(key=lambda x: x.score, reverse=True)
    for res in list_of_results:
        print(res.symbol, res.percent, res.score)


def analyze_all_best(repo_type, interval, start_date, end_date, write_to_file=False):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = TWRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()
    elif repo_type == "stock-all":
        repo = TWRepoAllStock()

    pairs_response = list_pairs(repo)
    list_of_results = []
    
    for symbol in pairs_response.value:
        request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

        analyze_best_use_case = AnalyzeBestUseCase()
        response = analyze_best_use_case.analyze_best(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.score > 0:
                with open(f'results/{repo_type}-{interval}-{start_date}-{end_date}.txt', 'a+') as f:
                    f.write(f'{result_object.symbol} - {result_object.percent} - {result_object.score}' + '\n')


def find_patterns(repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    response = list_pairs(repo)
    list_of_results = []
    for symbol in response.value:
        request = build_analyze_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

        find_patterns_use_case = FindPatternsUseCase(drawing_enabled=True)
        response = find_patterns_use_case.find_patterns(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.found_pattern is not None:
                list_of_results.append(result_object)
    
    for res in list_of_results:
        print(res.symbol, res.percent, res.found_pattern)


def find_bulls_from_file(repo_type, file, min_score, interval, start_date, end_date):
    if repo_type == "stock-all":
        repo = TWRepoAllStock()
    elif repo_type == "stock-tr":
        repo = TWRepoTR()

    result_file = open(file, 'r')
    lines = result_file.readlines()
    for line in lines:
        line = line.strip()
        info = line.split(" - ")
        
        if float(info[2]) < float(min_score):
            continue
        request = build_backtest_request({"symbol": info[0], "percent": float(info[1]), "interval": interval, "start_date": start_date, "end_date": end_date})

        backtest_use_case = BacktestUseCase(drawing_enabled=False)
        result = backtest_use_case.backtest(repo, request)

        if result.value.bricks[-1].type == "up":
            with open(f'results/{repo_type}-{interval}-{start_date}-{end_date}-bulls.txt', 'a') as f:
                f.write(f'{info[0]} {info[1]} {info[2]}' + '\n')



def get_pairs_open_for_position(repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = YahooRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()

    response = list_pairs(repo)
    list_of_results = []
    for symbol in response.value:
        request = build_analyze_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

        analyze_use_case = AnalyzeUseCase()
        response = analyze_use_case.analyze(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.score > 0:
                if result_object.bricks[-2].type == "down" and result_object.bricks[-1].type == "up":
                    list_of_results.append(result_object)

    list_of_results.sort(key=lambda x: x.score, reverse=True)
    for res in list_of_results:
        print(res.symbol, res.percent, res.score)


def get_pairs_open_for_position_best(repo_type, interval, start_date, end_date):
    if repo_type == "test":
        repo = MemRepo()
    elif repo_type == "crypto":
        repo = BinanceRepo()
    elif repo_type == "stock":
        repo = YahooRepo()
    elif repo_type == "stock-tr":
        repo = TWRepoTR()
    elif repo_type == "fx":
        repo = YahooRepoFX()
    elif repo_type == "stock-all":
        repo = TWRepoAllStock()

    response = list_pairs(repo)
    list_of_results = []
    for symbol in response.value:
        request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})

        analyze_best_use_case = AnalyzeBestUseCase()
        response = analyze_best_use_case.analyze_best(repo, request)
        if bool(response) is True:
            result_object = response.value
            if result_object.score > 6:
                if result_object.bricks[-2].type == "down" and result_object.bricks[-1].type == "up":
                    list_of_results.append(result_object)
                    print(result_object.symbol, result_object.percent, result_object.score)
    print("-----")
    list_of_results.sort(key=lambda x: x.score, reverse=True)
    for res in list_of_results:
        print(res.symbol, res.percent, res.score)


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
    elif sys.argv[2] == "analyze_best":
        symbol = sys.argv[3]
        repo_type = sys.argv[4]
        interval = sys.argv[5]
        start_date = sys.argv[6]
        end_date = sys.argv[7]
        analyze_best(symbol, repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "backtest":
        symbol = sys.argv[3]
        repo_type = sys.argv[4]
        percent = float(sys.argv[5])
        interval = sys.argv[6]
        start_date = sys.argv[7]
        end_date = sys.argv[8]
        backtest(symbol, repo_type, percent, interval, start_date, end_date)
    elif sys.argv[2] == "analyze_all":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        analyze_all(repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "analyze_all_best":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        if len(sys.argv) > 7:
            write_to_file = sys.argv[7]
        else:
            write_to_file = False
        analyze_all_best(repo_type, interval, start_date, end_date, write_to_file)
    elif sys.argv[2] == "open_position":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        get_pairs_open_for_position(repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "open_position_best":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        get_pairs_open_for_position_best(repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "find_patterns":
        repo_type = sys.argv[3]
        interval = sys.argv[4]
        start_date = sys.argv[5]
        end_date = sys.argv[6]
        find_patterns(repo_type, interval, start_date, end_date)
    elif sys.argv[2] == "find_bulls_from_file":
        repo_type = sys.argv[3]
        file = sys.argv[4]
        min_score = sys.argv[5]
        interval = sys.argv[6]
        start_date = sys.argv[7]
        end_date = sys.argv[8]
        find_bulls_from_file(repo_type, file, min_score, interval, start_date, end_date)
    else:
        print("Command not found.")
