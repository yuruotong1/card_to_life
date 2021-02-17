from typing import Dict


class Role:
    def __init__(self):
        self.name = ""
        # 表示年收入，比如程序员年收入 10 万（税后 + 奖金）
        self._salary = 0
        # 个人贷款，每年偿还数额，比如
        # {"describe": 买手机, "money": 3000, "time": 30} 表示买手机每年贷款 3000 ，要还 30 年
        self.loan: [Dict] = []

    def __str__(self):
        return "职业：" + self.name + \
               " 工资： " + str(self._salary)

    def get_salary(self):
        return self._salary

    def get_event(self):
        """
        选择一个事件
        :return:
        """
        pass
