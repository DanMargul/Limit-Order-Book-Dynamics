from dataclasses import dataclass


@dataclass(slots=True)
class Cash:
    balance: float = 0.0

    def receive(self, amount: float) -> None:
        self.balance += amount

    def pay(self, amount: float) -> None:
        self.balance -= amount
