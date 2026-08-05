from dataclasses import dataclass, field
from enum import Enum, auto
from uuid import UUID, uuid4


class Side(Enum):
    BUY = auto()
    SELL = auto()


class OrderType(Enum):
    MARKET = auto()
    LIMIT = auto()


class TimeInForce(Enum):
    GTC = auto()


@dataclass(frozen=True, slots=True)
class Order:
    id: UUID = field(default_factory=uuid4)
    side: Side = Side.BUY
    quantity: float = 0.0
    order_type: OrderType = OrderType.MARKET
    time_in_force: TimeInForce = TimeInForce.GTC
    limit_price: float | None = None

    @classmethod
    def market_buy(cls, quantity: float) -> "Order":
        return cls(
            side=Side.BUY,
            quantity=quantity,
            order_type=OrderType.MARKET,
        )

    @classmethod
    def market_sell(cls, quantity: float) -> "Order":
        return cls(
            side=Side.SELL,
            quantity=quantity,
            order_type=OrderType.MARKET,
        )

    @classmethod
    def limit_buy(cls, quantity: float, price: float) -> "Order":
        return cls(
            side=Side.BUY,
            quantity=quantity,
            order_type=OrderType.LIMIT,
            limit_price=price,
        )

    @classmethod
    def limit_sell(cls, quantity: float, price: float) -> "Order":
        return cls(
            side=Side.SELL,
            quantity=quantity,
            order_type=OrderType.LIMIT,
            limit_price=price,
        )
