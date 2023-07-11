from pbrenko_trials.domain.brick import Brick


def test_brick_model_init():
    brick = Brick(
        type="up",
        open=100,
        close=200,
        low=100,
        high=230,
    )

    assert brick.type == "up"
    assert brick.open == 100
    assert brick.close == 200
    assert brick.low == 100
    assert brick.high == 230
