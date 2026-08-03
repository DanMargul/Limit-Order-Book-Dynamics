from lobd import PriceProcess, Simulation


def test_simulation_returns_steps_plus_initial_value() -> None:
    process = PriceProcess(
        value=100.0,
        volatility=1.0,
    )

    simulation = Simulation(process)

    prices = simulation.run(
        steps=10,
        seed=1,
    )

    assert len(prices) == 11


def test_simulation_is_reproducible() -> None:
    simulation_a = Simulation(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    simulation_b = Simulation(
        PriceProcess(
            value=100.0,
            volatility=1.0,
        )
    )

    prices_a = simulation_a.run(
        steps=50,
        seed=7,
    )

    prices_b = simulation_b.run(
        steps=50,
        seed=7,
    )

    assert prices_a == prices_b
