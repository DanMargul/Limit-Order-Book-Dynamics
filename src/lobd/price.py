from dataclasses import dataclass

import numpy as np
from numpy.random import Generator


@dataclass(slots=True)
class PriceProcess:
    value: float
    volatility: float

    def step(self, rng: Generator) -> float:
        shock = rng.normal(0.0, self.volatility)
        self.value += float(shock)
        return self.value
