import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Result:
    symbol: str
    percent: float
    score: float
    start_date: datetime
    end_date: datetime