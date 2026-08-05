import pytest

from lobd import Order, PriceLevel


def test_empty_level() -> None:
    level = PriceLevel(price=100.0)

    assert len(level) == 0
    assert level.volume == 0.0
    assert not level


def test_add_order() -> None:
    level = PriceLevel(price=100.0)

    level.add(
        Order.limit_buy(
            quantity=5,
            price=100.0,
        )
    )

    assert len(level) == 1
    assert level.volume == pytest.approx(5.0)
    assert level


def test_multiple_orders() -> None:
    level = PriceLevel(price=100.0)

    level.add(Order.limit_buy(quantity=3, price=100.0))
    level.add(Order.limit_buy(quantity=7, price=100.0))

    assert len(level) == 2
    assert level.volume == pytest.approx(10.0)


def test_remove_order() -> None:
    level = PriceLevel(price=100.0)

    order = Order.limit_buy(
        quantity=3,
        price=100.0,
    )

    level.add(order)
    level.remove(order)

    assert len(level) == 0
    assert level.volume == 0.0
