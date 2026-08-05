from lobd import Action, MarketMaker, PriceProcess, Valuation


def main() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=0.0,
    )

    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(process)

    market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=2,
    )

    valuation = Valuation(
        cash=market_maker.cash,
        inventory=market_maker.inventory,
    )

    print(valuation.wealth(process.value))


if __name__ == "__main__":
    main()
