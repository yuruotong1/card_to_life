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

    def change(self, value, describe=""):
        """
        修改指标
        :param describe: 操作描述，比如买手机
        :param value:
        :return:
        """
        self.value += value
        return True

    def __str__(self):
        return self.NAME + "：" + str(self.value)
