import pytest

from lobd import (
    Action,
    MarketMaker,
    PriceProcess,
    Valuation,
)


def test_buy_trade_generates_half_spread_profit() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=0.0,
    )

    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(process)

    market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=2,
    )

    valuation = Valuation(
        cash=market_maker.cash,
        inventory=market_maker.inventory,
    )

    assert valuation.wealth(process.value) == pytest.approx(0.10)
