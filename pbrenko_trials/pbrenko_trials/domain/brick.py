import dataclasses


@dataclasses.dataclass
class Brick:
    type: str
    open: float
    close: float
    low: float
    high: float
