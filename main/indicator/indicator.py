class Indicator:
    """
    指标基类，用于存放指标的公共方法
    """
    NAME = ""
    MONEY = "money"
    HAPPINESS = "happiness"
    POWER = "power"

    def __init__(self):
        self.value = 0

    def change(self, value):
        self.value += value
        return {self.NAME: value}

    def __str__(self):
        return self.NAME + "：" + str(self.value)
