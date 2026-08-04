from dataclasses import dataclass

from lobd.trader import Action


@dataclass(frozen=True, slots=True)
class Trade:
    price: float
    quantity: float
    aggressor: Action
