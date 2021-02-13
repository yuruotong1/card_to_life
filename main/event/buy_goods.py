from main.event.event import Event
from main.indicator import Indicator


class BuyGoods(Event):
    def __init__(self, indicator: Indicator):
        self.indicator = indicator

    def generate(self):
        """
        购买物品会使金钱减少，幸福增加
        :return:
        """
        self.indicator.money -= 10
        self.indicator.happiness += 5
