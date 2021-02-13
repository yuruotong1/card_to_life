from main.base import Base


class BasicPage(Base):
    """
    展示游戏主体，产生随机事件
    """
    def show_current_info(self):
        self.draw_text("")