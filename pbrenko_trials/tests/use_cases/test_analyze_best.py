import pytest

from unittest import mock
from pbrenko_trials.use_cases.analyze_best import AnalyzeBestUseCase
from pbrenko_trials.requests.analyze_best import build_analyze_best_request
from datetime import datetime
from pbrenko_trials.responses import ResponseTypes


@pytest.fixture
def market_data():
    return [42373.73, 42217.87, 42053.66, 42535.94, 44544.86, 43873.56, 40515.7, 39974.44, 40079.17, 38386.89, 37008.16, 38230.33, 37250.01, 38327.21, 39219.17, 39116.72, 37699.07, 43160.0, 44421.2, 43892.98, 42454.0, 39148.66, 39397.96, 38420.81, 37988.0, 38730.63, 41941.71, 39422.0, 38729.57, 38807.36, 37777.34, 39671.37, 39280.33, 41114.0, 40917.9, 41757.51, 42201.13, 41262.11, 41002.25, 42364.13, 42882.76, 43991.46, 44313.16, 44511.27, 46827.76, 47122.21, 47434.8, 47067.99, 45510.34, 46283.49, 45811.0, 46407.35, 46580.51, 45497.55, 43170.47, 43444.19, 42252.01, 42753.97, 42158.85, 39530.45, 40074.94, 41147.79, 39942.38, 40551.9, 40378.71, 39678.12, 40801.13, 41493.18, 41358.19, 40480.01, 39709.18, 39441.6, 39450.13, 40426.08, 38112.65, 39235.72, 39742.07, 38596.11, 37630.8, 38468.35, 38525.16, 37728.95, 39690.0, 36552.97, 36013.77, 35472.39, 34038.4, 30076.31, 31017.1, 29103.94, 29029.75, 29287.05, 30086.74, 31328.89, 29874.01, 30444.93, 28715.32, 30319.23, 29201.01, 29445.06, 30293.94, 29109.15, 29654.58, 29542.15, 29201.35, 28629.8, 29031.33, 29468.1, 31734.22, 31801.04, 29805.83, 30452.62, 29700.21, 29864.04, 29919.21, 31373.1, 31125.33, 30204.77, 30109.93, 29091.88, 28424.7, 26574.53, 22487.41, 22136.41, 22583.72, 20401.31, 20468.81, 18970.79, 20574.0, 20573.89, 20723.52, 19987.99, 21110.13, 21237.69, 21491.19, 21038.07, 20742.56, 20281.29, 20123.01, 19942.21, 19279.8, 19252.81, 19315.83, 20236.71, 20175.83, 20564.51, 21624.98, 21594.75, 21591.83, 20862.47, 19963.61, 19328.75, 20234.87, 20588.84, 20830.04, 21195.6, 20798.16, 22432.58, 23396.62, 23223.3, 23152.19, 22684.83, 22451.07, 22579.68, 21310.9, 21254.67, 22952.45, 23842.93, 23773.75, 23643.51, 23293.32, 23268.01, 22987.79, 22818.37, 22622.98, 23312.42, 22954.21, 23174.39, 23810.0, 23149.95, 23954.05, 23934.39, 24403.68, 24441.38, 24305.24, 24094.82, 23854.74, 23342.66, 23191.2, 20834.39, 21140.07, 21515.61, 21399.83, 21529.12, 21368.08, 21559.04, 20241.05, 20037.6, 19555.61, 20285.73, 19811.66, 20050.02, 20131.46, 19951.86, 19831.9, 20000.3, 19796.84, 18790.61, 19292.84, 19319.77, 21360.11, 21648.34, 21826.87, 22395.74, 20173.57, 20226.71, 19701.88, 19803.3, 20113.62, 19416.18, 19537.02, 18875.0, 18461.36, 19401.63, 19289.91, 18920.5, 18807.38, 19227.82, 19079.13, 19412.82, 19591.51, 19422.61, 19310.95, 19056.8, 19629.08, 20337.82, 20158.26, 19960.67, 19530.09, 19417.96, 19439.02, 19131.87, 19060.0, 19155.53, 19375.13, 19176.93, 19069.39, 19262.98, 19549.86, 19327.44, 19123.97, 19041.92, 19164.37, 19204.35, 19570.4, 19329.72, 20080.07, 20771.59, 20295.11, 20591.84, 20809.67, 20627.48, 20490.74, 20483.62, 20151.84, 20207.82, 21148.52, 21299.37, 20905.58, 20591.13, 18547.23, 15922.81, 17601.15, 17070.31, 16812.08, 16329.85, 16619.46, 16900.57, 16662.76, 16692.56, 16700.45, 16700.68, 16280.23, 15781.29, 16226.94, 16603.11, 16598.95, 16522.14, 16458.57, 16428.78, 16212.91, 16442.53, 17163.64, 16977.37, 17092.74, 16885.2, 17105.7, 16966.35, 17088.96, 16836.64, 17224.1, 17128.56, 17127.49, 17085.05, 17209.83, 17774.7, 17803.15, 17356.34, 16632.12, 16776.52, 16738.21, 16438.88, 16895.56, 16824.67, 16821.43, 16778.5, 16836.12, 16832.11, 16919.39, 16706.36, 16547.31, 16633.47, 16607.48, 16542.4, 16616.75, 16672.87, 16675.18, 16850.36, 16831.85, 16950.65, 16943.57, 17127.83, 17178.26, 17440.66, 17943.26, 18846.62, 19930.01, 20954.92, 20871.5, 21185.65, 21134.81, 20677.47, 21071.59, 22667.21, 22783.55, 22707.88, 22916.45, 22632.89, 23060.94, 23009.65, 23074.16, 23022.6, 23742.3, 22826.15, 23125.13, 23732.66, 23488.94, 23431.9, 23326.84, 22932.91, 22762.52, 23240.46, 22963.0, 21796.35, 21625.19, 21862.55, 21783.54, 21773.97, 22199.84, 24324.05, 23517.72, 24569.97, 24631.95, 24271.76, 24842.2, 24452.16, 24182.21, 23940.2, 23185.29, 23157.07, 23554.85, 23492.09, 23141.57, 23628.97, 23465.32, 22354.34, 22346.57, 22430.24, 22410.0, 22197.96, 21705.44, 20362.22, 20150.69, 20455.73, 21997.11, 24113.48, 24670.41, 24285.66, 24998.78, 27395.13, 26907.49, 27972.87, 27717.01, 28105.47, 27250.97, 28295.41, 27454.47, 27462.95, 27968.05, 27124.91, 27261.07, 28348.6, 28028.53, 28465.36, 28452.73, 28171.87, 27800.0, 28165.47, 28170.01, 28033.82, 27906.33, 27938.38, 28323.76, 29637.34, 30200.42, 29888.07, 30373.84, 30466.93, 30295.09, 30304.65, 29430.27, 30380.01, 28797.1, 28243.65, 27262.84, 27816.85, 27590.6, 27510.93, 28300.79, 28415.29, 29472.77, 29311.7, 29230.45, 29233.21, 28068.26, 28669.86, 29026.16, 28838.16, 29505.61, 28848.2, 28430.1, 27668.79, 27628.27, 27598.75, 26968.62, 26795.01, 26775.28, 26917.62, 27162.14, 27033.84, 27405.61, 26821.28, 26880.26, 27102.43, 26747.78, 26849.27, 27219.61, 26329.01, 26473.79, 26705.92, 26854.27, 28065.0, 27736.4, 27694.4, 27210.35, 26817.93, 27242.59, 27069.22, 27115.21, 25728.2, 27230.08, 26339.34, 26498.61, 26477.81, 25841.21, 25925.55, 25905.19, 25934.25, 25128.6, 25598.49, 26345.0, 26516.99, 26339.97, 26844.35, 28307.99, 29993.89, 29884.92, 30688.5, 30527.43, 30700.5]


def test_analyze_best_with_parameters(market_data):
    symbol = "BTCUSDT"
    # repo_type = "crypto"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    repo = mock.Mock()
    repo.get_data.return_value = market_data

    request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})
    analyze_use_case = AnalyzeBestUseCase()

    response = analyze_use_case.analyze_best(repo, request)

    repo.get_data.assert_called_with(symbol, interval, datetime(2021, 1, 1, 0, 0, 0), datetime(2023, 1, 1, 0, 0, 0))
    assert response.value.symbol == "BTCUSDT"
    assert response.value.percent == 9.6
    assert response.value.score == 2.3438042403489647
    assert response.value.start_date == datetime(2021, 1, 1, 0, 0, 0)
    assert response.value.end_date == datetime(2023, 1, 1, 0, 0, 0)


def test_analyze_best_with_invalid_request():
    repo = mock.Mock()

    # creating an invalid request
    request = build_analyze_best_request()
    analyze_best_use_case = AnalyzeBestUseCase()

    response = analyze_best_use_case.analyze_best(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "parameters: Need 4 parameters: symbol, interval, start_date, end_date. Got 0.",
    }


def test_analyze_best_with_invalid_resource():
    symbol = "BTCUSDT"
    # repo_type = "crypto"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    repo = mock.Mock()
    repo.get_data.return_value = []

    request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})
    analyze_best_use_case = AnalyzeBestUseCase()

    response = analyze_best_use_case.analyze_best(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.RESOURCE_ERROR,
        "message": "No data returned from the repository",
    }


def test_analyze_best_with_generic_error():
    symbol = "BTCUSDT"
    # repo_type = "crypto"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202301010000"

    repo = mock.Mock()
    repo.get_data.side_effect = Exception("Just an error message")

    request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})
    analyze_best_use_case = AnalyzeBestUseCase()

    response = analyze_best_use_case.analyze_best(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_analyze_best_with_insufficient_data():
    symbol = "BTCUSDT"
    # repo_type = "crypto"
    interval = "1d"
    start_date = "202101010000"
    end_date = "202307260000"

    repo = mock.Mock()
    repo.get_data.return_value = [42373.73, 42217.87, 42053.66, 42535.94, 44544.86, 43873.56, 40515.7, 39974.44, 40079.17, 38386.89, 37008.16, 38230.33, 37250.01]

    request = build_analyze_best_request({"symbol": symbol, "interval": interval, "start_date": start_date, "end_date": end_date})
    analyze_best_use_case = AnalyzeBestUseCase()

    response = analyze_best_use_case.analyze_best(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.RESOURCE_ERROR,
        "message": "Not enough data point.",
    }
