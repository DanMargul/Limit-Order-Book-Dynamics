from dataclasses import dataclass, field

from lobd.cash import Cash
from lobd.inventory import Inventory
from lobd.price import PriceProcess
from lobd.trade import Trade
from lobd.trader import Action

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
    inventory: Inventory = field(default_factory=Inventory)
    cash: Cash = field(default_factory=Cash)

    def quote(self, process: PriceProcess) -> Quote:
        return Quote(
            bid=process.value - self.half_spread,
            ask=process.value + self.half_spread,
        )

    def execute(
            self,
            quote: Quote,
            action: Action,
            quantity: float,
    ) -> Trade | None:
        if action is Action.BUY:
            self.inventory.sell(quantity)
            self.cash.receive(quantity * quote.ask)

            return Trade(
                price=quote.ask,
                quantity=quantity,
                aggressor=action,
            )

        if action is Action.SELL:
            self.inventory.buy(quantity)
            self.cash.pay(quantity * quote.bid)

            return Trade(
                price=quote.bid,
                quantity=quantity,
                aggressor=action,
            )

        return None
