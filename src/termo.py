class Termo:
    # TODO: docstring
    def __init__(self, strike_price, spot_price):
        # TODO: regras de validação
        self.strike_price = strike_price
        self.spot_price = spot_price

    def payoff(self, position_is_long: bool = True):
        if position_is_long:
            return self.spot_price - self.strike_price
        else:
            return self.strike_price - self.spot_price


if __name__ == "__main__":
    termo = Termo(strike_price=1.5532, spot_price=1.6)
    print(f"{termo.payoff():.4f}")
    # TODO: teste unitário
