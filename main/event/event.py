from main.indicator.indicator_factory import IndicatorFactory


class Event:
    """
    定义事件
    """
    NAME = ""
    INFO = ""

    def __init__(self, indicator: IndicatorFactory):
        self.indicator = indicator
        # 存放当前事件是什么，比如加钱，减幸福
        self.content = {}

    def generate(self):
        """
        事件发生时，会造成什么影响
        :return:
        """

    def change(self, name, value):
        """
        找到对应指标并修改
        :param name:
        :param value:
        :return:
        """
        # 如果已经有值，不进行处理
        if name in self.content:
            return
            # 从指标列表中找符合要求和指标，进行修改
        for index in self.indicator.tags:
            if index == name:
                self.content.update(index.change(value))

    def __str__(self):
        result = self.NAME + " " + str(self.content)
        return result
