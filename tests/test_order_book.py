import pytest

from lobd import Order, OrderBook


def test_empty_book() -> None:
    book = OrderBook()

    assert book.best_bid is None
    assert book.best_ask is None
    assert book.spread is None
    assert book.midprice is None


def test_single_bid() -> None:
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


def test_single_ask() -> None:
    book = OrderBook()

    book.add(
        Order.limit_sell(
            quantity=8,
            price=100.5,
        )
    )

    assert book.best_ask is not None
    assert book.best_ask.price == pytest.approx(100.5)


def test_spread() -> None:
    book = OrderBook()

    book.add(Order.limit_buy(quantity=5, price=99))
    book.add(Order.limit_sell(quantity=7, price=101))

    assert book.spread == pytest.approx(2.0)
    assert book.midprice == pytest.approx(100.0)


def test_multiple_bid_levels() -> None:
    book = OrderBook()

    book.add(Order.limit_buy(quantity=5, price=98))
    book.add(Order.limit_buy(quantity=5, price=99))
    book.add(Order.limit_buy(quantity=5, price=97))

    assert book.best_bid is not None
    assert book.best_bid.price == pytest.approx(99)


def test_remove_order() -> None:
    book = OrderBook()

    order = Order.limit_buy(
        quantity=5,
        price=99,
    )

    book.add(order)

    assert book.best_bid is not None

    book.remove(order)

    assert book.best_bid is None


def test_remove_one_of_two_orders() -> None:
    book = OrderBook()

    first = Order.limit_buy(
        quantity=5,
        price=99,
    )

    second = Order.limit_buy(
        quantity=3,
        price=99,
    )

    book.add(first)
    book.add(second)

    book.remove(first)

    assert book.best_bid is not None
    assert len(book.best_bid) == 1
    assert book.best_bid.volume == pytest.approx(3)