from main.base import Base


class Indicator:
    """
    记录当前的数据信息
    """

    def __init__(self):
        # todo： 多项指标相互影响相互制约
        self.money = 0
        self.happiness = 50
        self.power = 0

    def show_indicator(self):
        """
        展示指标信息
        :return:
        """
        Base.draw_text("money : ", self.money,
                       " | happiness : ", self.happiness,
                       " | power : ", self.power)

