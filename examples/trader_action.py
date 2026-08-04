from dataclasses import dataclass

from lobd import Action, MarketState, Trader


@dataclass(slots=True)
class MomentumTrader(Trader):
    threshold: float

    def decide(self, state: MarketState) -> Action:
        if state.price > self.threshold:
            return Action.BUY

        if state.price < self.threshold:
            return Action.SELL

        return Action.WAIT


def main() -> None:
    trader = MomentumTrader(
        threshold=100.0,
    )

    state = MarketState(
        price=100.25,
    )

    print(trader.decide(state))


if __name__ == "__main__":
    main()
