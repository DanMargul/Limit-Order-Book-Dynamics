from dataclasses import dataclass

from lobd.cash import Cash
from lobd.inventory import Inventory


@dataclass(frozen=True, slots=True)
class Valuation:
    cash: Cash
    inventory: Inventory

    def wealth(self, reference_price: float) -> float:
        return (
            self.cash.balance
            + self.inventory.position * reference_price
        )
