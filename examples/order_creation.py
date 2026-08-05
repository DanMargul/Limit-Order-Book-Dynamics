from lobd import Order


def main() -> None:
    market = Order.market_buy(quantity=100)
    limit = Order.limit_sell(
        quantity=50,
        price=101.75,
    )

    print(market)
    print(limit)


if __name__ == "__main__":
    main()
