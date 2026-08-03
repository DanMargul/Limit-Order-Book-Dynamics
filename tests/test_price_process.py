import numpy as np

from lobd import PriceProcess


def test_step_changes_value() -> None:
    rng = np.random.default_rng(1)

    process = PriceProcess(
        value=100.0,
        volatility=1.0,
    )

    initial = process.value

    process.step(rng)

    assert process.value != initial


def test_zero_volatility_keeps_price_constant() -> None:
    rng = np.random.default_rng(1)

    process = PriceProcess(
        value=100.0,
        volatility=0.0,
    )

    process.step(rng)

    assert process.value == 100.0
