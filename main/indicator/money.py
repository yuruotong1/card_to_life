from main.indicator.indicator import Indicator


class Money(Indicator):
    NAME = Indicator.MONEY

    def __init__(self):
        super().__init__()
        self.value = 10000
