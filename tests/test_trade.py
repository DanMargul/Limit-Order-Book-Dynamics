from lobd import Action, MarketMaker, PriceProcess


def test_buy_executes_at_ask() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    trade = market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=5,
    )

    assert trade is not None
    assert trade.price == 100.05
    assert trade.quantity == 5
    assert trade.aggressor is Action.BUY


def test_wait_does_not_trade() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    trade = market_maker.execute(
        quote=quote,
        action=Action.WAIT,
        quantity=5,
    )

    assert trade is None
