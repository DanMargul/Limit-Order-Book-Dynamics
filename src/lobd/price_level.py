from dataclasses import dataclass, field

from lobd.order import Order


@dataclass(slots=True)
class PriceLevel:
    price: float
    orders: list[Order] = field(default_factory=list)

    def add(self, order: Order) -> None:
        self.orders.append(order)

    def remove(self, order: Order) -> None:
        self.orders.remove(order)

    @property
    def volume(self) -> float:
        return sum(order.quantity for order in self.orders)

    def __len__(self) -> int:
        return len(self.orders)

    def __bool__(self) -> bool:
        return bool(self.orders)
