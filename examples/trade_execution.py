from lobd import Action, MarketMaker, PriceProcess


def main() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=0.25,
    )

    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(process)

    trade = market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=10,
    )

    print(trade)


if __name__ == "__main__":
    main()
