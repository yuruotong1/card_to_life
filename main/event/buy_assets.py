from main.event.event import Event
from main.indicator.indicator_factory import IndicatorFactory


class BuyAssets(Event):
    NAME = "创建企业"
    INFO = "金钱 +10，幸福 -5"

    def __init__(self, indicator: IndicatorFactory):
        super().__init__(indicator)
        self.indicator = indicator

    def generate(self):
        """
        购买资产会使金钱增加，幸福减少
        资产包括：企业，出租房屋
        :return:
        """
        self.change(self.indicator.money, 10)
        self.change(self.indicator.happiness, -5)
