from dataclasses import dataclass, field

from lobd.order import Order, Side
from lobd.price_level import PriceLevel


@dataclass(slots=True)
class OrderBook:
    bids: dict[float, PriceLevel] = field(default_factory=dict)
    asks: dict[float, PriceLevel] = field(default_factory=dict)

    def add(self, order: Order) -> None:
        if order.limit_price is None:
            raise ValueError("Only limit orders may rest in the order book.")

        levels = self.bids if order.side is Side.BUY else self.asks

        level = levels.get(order.limit_price)

        if level is None:
            level = PriceLevel(price=order.limit_price)
            levels[order.limit_price] = level

        level.add(order)

    def remove(self, order: Order) -> None:
        if order.limit_price is None:
            raise ValueError("Market orders are never stored in the order book.")

        levels = self.bids if order.side is Side.BUY else self.asks

        level = levels[order.limit_price]
        level.remove(order)

        if not level:
            del levels[order.limit_price]

    @property
    def best_bid(self) -> PriceLevel | None:
        if not self.bids:
            return None

        return self.bids[max(self.bids)]

    @property
    def best_ask(self) -> PriceLevel | None:
        if not self.asks:
            return None

        return self.asks[min(self.asks)]

    @property
    def spread(self) -> float | None:
        if self.best_bid is None or self.best_ask is None:
            return None

        return self.best_ask.price - self.best_bid.price

    @property
    def midprice(self) -> float | None:
        if self.best_bid is None or self.best_ask is None:
            return None

        return 0.5 * (
            self.best_bid.price
            + self.best_ask.price
        )