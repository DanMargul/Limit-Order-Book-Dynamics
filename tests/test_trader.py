from dataclasses import dataclass

from lobd import Action, MarketState, Trader


@dataclass(slots=True)
class AlwaysBuyTrader(Trader):
    def decide(self, state: MarketState) -> Action:
        return Action.BUY


def test_trader_returns_action() -> None:
    trader = AlwaysBuyTrader()

    action = trader.decide(
        MarketState(price=100.0)
    )

    assert action is Action.BUY
