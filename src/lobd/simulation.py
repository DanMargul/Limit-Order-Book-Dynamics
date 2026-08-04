from dataclasses import dataclass

import numpy as np

from lobd.price import PriceProcess


@dataclass(slots=True)
class Simulation:
    process: PriceProcess

    def run(
        self,
        steps: int,
        seed: int | None = None,
    ) -> list[float]:
        rng = np.random.default_rng(seed)

        prices = [self.process.value]

        for _ in range(steps):
            prices.append(self.process.step(rng))

        return prices
