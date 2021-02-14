from main.event.event import Event
from main.indicator import Indicator


class BuyGoods(Event):
    """
    买物品
    """
    NAME = "买手机"
    INFO = "金钱 -10，幸福 +5"

    def __init__(self, indicator: Indicator):
        self.indicator = indicator

    def generate(self):
        """
        购买物品会使金钱减少，幸福增加
        物品包括：奢饰品，汽车
        :return:
        """
        self.indicator.money -= 10
        self.indicator.happiness += 5
