from main.base import Base
from main.indicator.indicator_factory import IndicatorFactory
from main.page.bank_page import BankPage


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

        # 可反复借贷，直到钱够了为止
        while True:
            Base.draw_text("事件：" + self.NAME + " " + str(self.value))
            operation = Base.input_text(f"是否要进行操作：\n0，是，1，否")
            if operation == "1":
                return False
            # 如果钱不够，使用贷款
            if "money" in value and self.indicator.money.value + value.get("money") < 0:
                is_loan = Base.input_text(f"钱不够，是否要：\n0，使用贷款，1，放弃购买")
                if is_loan == "1":
                    return False
                elif is_loan == "0":
                    # 进行贷款
                    BankPage(self.indicator.money).loan(self.NAME)
            else:
                break

        for index_name, index_value in value.items():
            self.change(index_name, index_value)
        return True

    def change(self, index_name, index_value):
        """
        找到对应指标并修改
        :param index_name: 要修改的指标名
        :param index_value: 要修改的指标值
        :return:
        """

        # 从指标列表中找符合要求的指标，进行修改
        for index in self.indicator.tags:
            if index.NAME == index_name:
                index.change(index_value, self.NAME)
        return True
