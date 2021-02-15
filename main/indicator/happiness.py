from main.indicator.indicator import Indicator


class Happiness(Indicator):
    NAME = Indicator.HAPPINESS

    def __init__(self):
        super().__init__()
        self.value = 50
