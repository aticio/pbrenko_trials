import dataclasses
from typing import List
from pbrenko_trials.domain.brick import Brick


@dataclasses.dataclass
class PBRenko:
    bricks: List[Brick]
    percent: float
    number_of_leaks: int
