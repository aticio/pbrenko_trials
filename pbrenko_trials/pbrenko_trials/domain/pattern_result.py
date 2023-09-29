import dataclasses
from datetime import datetime
from typing import List
from pbrenko_trials.domain.brick import Brick


@dataclasses.dataclass
class PatternResult:
    symbol: str
    percent: float
    start_date: datetime
    end_date: datetime
    bricks: List[Brick]
    found_pattern: str
