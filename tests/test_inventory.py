from lobd import Action, MarketMaker, PriceProcess


def test_buy_reduces_inventory() -> None:
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
        quantity=5,
    )

    assert market_maker.inventory.position == -5


def test_sell_increases_inventory() -> None:
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
        quantity=3,
    )

    assert market_maker.inventory.position == 3
