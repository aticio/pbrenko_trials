import dataclasses
from datetime import datetime
from typing import List
from pbrenko_trials.domain.brick import Brick


@dataclasses.dataclass
class Result:
    symbol: str
    percent: float
    score: float
    start_date: datetime
    end_date: datetime
    bricks: List[Brick]