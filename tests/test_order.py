from lobd import Order, OrderType, Side


def test_market_buy() -> None:
    order = Order.market_buy(quantity=5)

    assert order.side is Side.BUY
    assert order.order_type is OrderType.MARKET
    assert order.limit_price is None
    assert order.quantity == 5


def test_limit_sell() -> None:
    order = Order.limit_sell(
        quantity=10,
        price=101.25,
    )

    assert order.side is Side.SELL
    assert order.order_type is OrderType.LIMIT
    assert order.limit_price == 101.25


def test_unique_ids() -> None:
    first = Order.market_buy(quantity=1)
    second = Order.market_buy(quantity=1)

    assert first.id != second.id
