import random
from typing import List

from main.base import Base
from main.event.event import Event
from main.indicator.indicator_factory import IndicatorFactory


class EventFactory:
    def __init__(self, indicator: IndicatorFactory):
        self.events: List[Event] = []
        self.indicator = indicator

    def register(self, event):
        self.events.append(event(self.indicator))

    def get_event(self):
        """
        随机获取一个事件
        :return:
        """
        event = random.choice(self.events)
        result = event.generate()
        Base.draw_text(event)
        return result
