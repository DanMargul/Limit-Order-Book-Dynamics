import pytest

from lobd import MarketMaker, PriceProcess


def test_quotes_are_symmetric() -> None:
    market_maker = MarketMaker(
        half_spread=0.10,
    )

    process = PriceProcess(
        value=100.0,
        volatility=1.0,
    )

    quote = market_maker.quote(process)

    assert quote.bid == pytest.approx(99.9)
    assert quote.ask == pytest.approx(100.1)


def test_spread() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    process = PriceProcess(
        value=10.0,
        volatility=1.0,
    )

    quote = market_maker.quote(process)

    assert quote.spread == pytest.approx(0.10)
