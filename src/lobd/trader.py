from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    BUY = "buy"
    SELL = "sell"
    WAIT = "wait"


@dataclass(frozen=True, slots=True)
class MarketState:
    price: float


class Trader(ABC):
    @abstractmethod
    def decide(self, state: MarketState) -> Action:
        pass
