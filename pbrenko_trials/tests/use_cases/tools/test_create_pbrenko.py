from pbrenko_trials.domain.brick import Brick
from pbrenko_trials.domain.pbrenko import PBRenko
from pbrenko_trials.use_cases.tools.pbrenko_creator import PBRenkoCreator


def test_create_pbrenko():
    data = [100, 110, 125, 130, 150, 140, 120, 110, 105, 115, 135, 145]
    percent = 10
    number_of_leaks = 0

    brick_0 = Brick(
        type="first",
        open=100,
        close=100,
        high=100,
        low=100,
    )

    brick_1 = Brick(
        type="up",
        open=100,
        close=110,
        high=110,
        low=100,
    )

    brick_2 = Brick(
        type="up",
        open=110,
        close=121,
        high=121,
        low=110,
    )

    brick_3 = Brick(
        type="up",
        open=121,
        close=133.5,
        high=133.5,
        low=121,
    )

    brick_4 = Brick(
        type="up",
        open=133.5,
        close=146,
        high=146,
        low=133.5,
    )

    brick_5 = Brick(
        type="down",
        open=133.5,
        close=118.5,
        high=133.5,
        low=118.5,
    )

    brick_6 = Brick(
        type="down",
        open=118.5,
        close=107.5,
        high=118.5,
        low=107.5,
    )

    brick_7 = Brick(
        type="up",
        open=118.5,
        close=129,
        high=129,
        low=118.5,
    )

    brick_8 = Brick(
        type="up",
        open=129,
        close=142.5,
        high=142.5,
        low=129,
    )

    bricks = [brick_0, brick_1, brick_2, brick_3, brick_4, brick_5, brick_6, brick_7, brick_8]

    pb_renko = PBRenko(
        bricks=bricks,
        percent=percent,
        number_of_leaks=0,
    )

    pbrenko_creator = PBRenkoCreator()
    result = pbrenko_creator.create_pbrenko(data, percent)

    assert pb_renko == result
