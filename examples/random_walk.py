from lobd import PriceProcess, Simulation


def main() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=0.25,
    )

    simulation = Simulation(process)

    prices = simulation.run(
        steps=20,
        seed=42,
    )

    for price in prices:
        print(f"{price:.2f}")


if __name__ == "__main__":
    main()
