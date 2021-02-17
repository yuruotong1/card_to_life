import random
from typing import List

import yaml

from main.base import Base
from main.event.event import Event
from main.indicator.indicator_factory import IndicatorFactory


class EventFactory:
    def __init__(self, indicator: IndicatorFactory):
        self.events: List[Event] = []
        self.indicator = indicator

    def register(self, event):
        self.events.append(event)

    def register_from_file(self, path):
        """
        从文件中提取事件
        :param path:
        :return:
        """
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for i in data:
            event = Event(self.indicator, i.get("name"), i.get("change"))
            self.register(event)

    def get_event(self):
        """
        随机获取一个事件
        :return:
        """
        event = random.choice(self.events)
        result = event.change_from_dict()
        return result
