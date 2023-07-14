class BacktestCreateInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, param, message):
        self.errors.append({"parameter": param, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False


class BacktestCreateValidRequest:
    def __init__(self, parameters=None):
        self.parameters = parameters

    def __bool__(self):
        return True


def build_backtest_request(parameters=None):
    accepted_parameters = ["symbol", "percent", "interval", "start_date", "end_date"]
    invalid_req = BacktestCreateInvalidRequest()

    if parameters is not None:
        if not isinstance(parameters, dict):
            invalid_req.add_error("parameters", "Is not iterable")
            return invalid_req

        if len(parameters) != 5:
            for key in accepted_parameters:
                if key not in parameters:
                    invalid_req.add_error("parameters", "Missing parameter. Key {} is mandatory".format(key))
                    return invalid_req

        for key, value in parameters.items():
            if key not in accepted_parameters:
                invalid_req.add_error("parameters", "Key {} cannot be used".format(key))
                return invalid_req

    else:
        invalid_req.add_error("parameters", "Need 5 parameters: symbol, start_date, end_date. Got 0.")
        return invalid_req

    return BacktestCreateValidRequest(parameters=parameters)
