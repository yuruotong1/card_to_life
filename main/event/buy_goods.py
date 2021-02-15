from main.event.event import Event
from main.indicator.indicator_factory import IndicatorFactory


class BuyGoods(Event):
    """
    买物品
    """
    NAME = "买房子"
    INFO = "金钱 -1000000，幸福 +5"

    def __init__(self, indicator: IndicatorFactory):
        super().__init__(indicator)
        self.indicator = indicator

    def generate(self):
        """
        购买物品会使金钱减少，幸福增加
        物品包括：奢饰品，汽车
        :return:
        """
        self.change(self.indicator.money, -1000000)
        self.change(self.indicator.happiness, 5)
