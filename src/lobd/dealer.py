from dataclasses import dataclass

from lobd.price import PriceProcess


@dataclass(frozen=True, slots=True)
class Quote:
    bid: float
    ask: float

    @property
    def midpoint(self) -> float:
        return (self.bid + self.ask) / 2.0

    @property
    def spread(self) -> float:
        return self.ask - self.bid


@dataclass(slots=True)
class MarketMaker:
    half_spread: float

    def quote(self, process: PriceProcess) -> Quote:
        return Quote(
            bid=process.value - self.half_spread,
            ask=process.value + self.half_spread,
        )
