import pytest

from lobd import Action, MarketMaker, PriceProcess


def test_buy_increases_cash() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=2,
    )

    assert market_maker.cash.balance == pytest.approx(200.10)


def test_sell_decreases_cash() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    market_maker.execute(
        quote=quote,
        action=Action.SELL,
        quantity=2,
    )

    assert market_maker.cash.balance == pytest.approx(-199.90)
