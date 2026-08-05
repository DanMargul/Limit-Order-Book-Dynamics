from lobd import Action, MarketMaker, PriceProcess


def main() -> None:
    market_maker = MarketMaker(
        half_spread=0.05,
    )

    quote = market_maker.quote(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    market_maker.execute(
        quote=quote,
        action=Action.BUY,
        quantity=3,
    )

    print(f"Inventory: {market_maker.inventory.position}")
    print(f"Cash: {market_maker.cash.balance:.2f}")


if __name__ == "__main__":
    main()
