from pbrenko_trials.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes
)


def list_pairs(repo):
    pairs = repo.list_pairs()

    if len(pairs) == 0:
        return ResponseFailure(ResponseTypes.RESOURCE_ERROR, "No data returned from the repository")

    response = ResponseSuccess()
    response.value = pairs

    return response
