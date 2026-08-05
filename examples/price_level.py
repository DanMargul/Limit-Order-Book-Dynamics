from lobd import Order, PriceLevel


def main() -> None:
    level = PriceLevel(price=100.0)

    level.add(Order.limit_buy(quantity=10, price=100.0))
    level.add(Order.limit_buy(quantity=5, price=100.0))

    print(level)
    print(level.volume)


if __name__ == "__main__":
    main()
