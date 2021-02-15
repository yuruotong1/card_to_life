from main.indicator.indicator_factory import IndicatorFactory


class Event:
    """
    定义事件
    """
    NAME = ""
    INFO = ""

    def __init__(self, indicator: IndicatorFactory, name, value):
        """
        :param indicator:
        :param name: 操作名称，比如买房子
        :param value: 要修改的指标，比如 {"money": -1000000, "happiness": 5}
        """
        self.indicator = indicator
        # 存放当前事件是什么，比如加钱，减幸福
        self.content = {}
        self.NAME = name
        self.value = value

    def change_from_dict(self, value=None):
        """
        从字典中提取数据，进行指标修改
        :param value: 要修改的数据值，格式 {"money": -1000000, "happiness": 5}
        :return:
        """
        if value is None:
            value = self.value
        for index_name, index_value in value.items():
            self.change(index_name, index_value)

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

        # 从指标列表中找符合要求的指标，进行修改
        for index in self.indicator.tags:
            if index.NAME == name:
                self.content.update(index.change(value))

    def __str__(self):
        result = self.NAME + " " + str(self.content)
        return result
