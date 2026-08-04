from lobd import MarketMaker, PriceProcess


def main() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=0.25,
    )

    dealer = MarketMaker(
        half_spread=0.05,
    )

    quote = dealer.quote(process)

    print(f"Bid : {quote.bid:.2f}")
    print(f"Ask : {quote.ask:.2f}")
    print(f"Spread : {quote.spread:.2f}")


if __name__ == "__main__":
    main()
