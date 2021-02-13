from main.base import Base
from main.indicator import Indicator
from main.role.role import Role


class Context:
    """
    定义上下文环境，多个场景变量等
    """
    # 如果输入 # ,则重新显示上次内容
    K_REAPPEAR = "#"
    ROUND_CYCLE = 5

    def __init__(self):
        # 当前角色
        self.profession = Role()
        self.indicator = Indicator()
        # 回合数，每 5 回合完成一个周期（一岁）
        self.bout = self.ROUND_CYCLE
        # 年龄
        self.age = 0

    def set_profession(self, professtion):
        """
        设置当前职业
        :param professtion:
        :return:
        """
        Base.draw_text(professtion)
        self.profession = professtion

    def get_profession(self):
        return self.profession

    def iteration_bout(self):
        """
        回合数增加，年龄增加
        :return:
        """
        # 如果到达一个周期，年龄加一，回合清零
        if self.bout == 0:
            self.age += 1
            self.bout = self.ROUND_CYCLE
        else:
            self.bout -= 1
