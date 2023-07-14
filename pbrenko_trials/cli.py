#!/usr/bin/env python
import sys
import os
import json

from pbrenko_trials.repository.memrepo import MemRepo
from pbrenko_trials.use_cases.analyze import AnalyzeUseCase
from pbrenko_trials.requests.analyze import build_analyze_request

APPLICATION_CONFIG_PATH = "config"


def app():
    repo = MemRepo()

    request = build_analyze_request({"symbol": "BTCUSDT", "interval": "1d", "start_date": "202101010000", "end_date": "202301010000"})

    analyze_use_case = AnalyzeUseCase()
    result = analyze_use_case.analyze(repo, request)
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
    app()
