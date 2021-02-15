from main.base import Base
from main.indicator.happiness import Happiness
from main.indicator.money import Money
from main.indicator.power import Power


class IndicatorFactory:
    """
    记录当前的数据信息
    """

    def __init__(self):
        # todo： 多项指标相互影响相互制约
        self.money = Money()
        self.happiness = Happiness()
        self.power = Power()
        self.tags = [self.money, self.happiness, self.power]

    def show_indicator(self):
        """
        展示指标信息
        :return:
        """
        Base.draw_text(self.money, " | ", self.happiness, " | ", self.power)
