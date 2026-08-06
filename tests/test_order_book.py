import pytest

from lobd import Order, OrderBook


def test_empty_book():
    book = OrderBook()

    assert book.best_bid is None
    assert book.best_ask is None
    assert book.spread is None
    assert book.midprice is None


def test_single_bid():
    book = OrderBook()

    book.add(
        Order.limit_buy(
            quantity=10,
            price=99.5,
        )
    )

    assert book.best_bid is not None
    assert book.best_bid.price == pytest.approx(99.5)
    assert book.best_ask is None


def test_single_ask():
    book = OrderBook()

    book.add(
        Order.limit_sell(
            quantity=8,
            price=100.5,
        )
    )

    assert book.best_ask is not None
    assert book.best_ask.price == pytest.approx(100.5)


def test_spread():
    book = OrderBook()

    book.add(Order.limit_buy(quantity=5, price=99))
    book.add(Order.limit_sell(quantity=7, price=101))

    assert book.spread == pytest.approx(2.0)
    assert book.midprice == pytest.approx(100.0)


def test_multiple_bid_levels():
    book = OrderBook()

    book.add(Order.limit_buy(quantity=5, price=98))
    book.add(Order.limit_buy(quantity=5, price=99))
    book.add(Order.limit_buy(quantity=5, price=97))

    assert book.best_bid is not None
    assert book.best_bid.price == pytest.approx(99)
