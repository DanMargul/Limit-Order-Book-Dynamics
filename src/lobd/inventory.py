from dataclasses import dataclass


@dataclass(slots=True)
class Inventory:
    position: float = 0.0

    def buy(self, quantity: float) -> None:
        self.position += quantity

    def sell(self, quantity: float) -> None:
        self.position -= quantity
