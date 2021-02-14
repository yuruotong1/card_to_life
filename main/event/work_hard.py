from main.event.event import Event
from main.indicator import Indicator


class WorkHard(Event):
    NAME = "努力工作"
    INFO = "金钱 +1，幸福 -5，权力 +1"

    def __init__(self, indicator: Indicator):
        self.indicator = indicator

    def generate(self):
        """
        努力工作会使金钱增加，权力增加，幸福减少
        资产包括：企业，出租房屋
        :return:
        """
        self.indicator.money += 1
        self.indicator.happiness -= 5
        self.indicator.power += 1
