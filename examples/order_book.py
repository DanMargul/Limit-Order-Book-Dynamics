from lobd import Order, OrderBook


def main():
    book = OrderBook()

    book.add(Order.limit_buy(quantity=10, price=99.5))
    book.add(Order.limit_buy(quantity=4, price=99.0))

    book.add(Order.limit_sell(quantity=6, price=100.5))
    book.add(Order.limit_sell(quantity=2, price=101.0))

    print(book.best_bid)
    print(book.best_ask)
    print(book.spread)
    print(book.midprice)


if __name__ == "__main__":
    main()
