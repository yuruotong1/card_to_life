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
    INTIAL_AGE = 20

    def __init__(self):
        # 当前角色
        self.profession = Role()
        self.indicator = Indicator()
        # 回合数，每 5 回合完成一个周期（一岁）
        self.bout = self.ROUND_CYCLE
        # 年龄
        self.age = self.INTIAL_AGE

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
        回合数介绍，每次从指定回合数开始倒计时，直到 1 。年龄增加
        :return:
        """
        # 如果到达一个周期，年龄加一，回合清零
        if self.bout == 0:
            self.age += 1
            self.bout = self.ROUND_CYCLE
        else:
            self.bout -= 1
        self._show_bout()


    def _show_bout(self):
        """
        展示回合信息
        :return:
        """
        Base.draw_text("当前回合：", self.bout, " 年龄：", self.age)
