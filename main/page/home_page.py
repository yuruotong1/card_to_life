from main.base import Base
from main.context import Context
from main.role.it import IT


class HomePage(Base):
    """
    展示首页
    """
    def __init__(self, context: Context):
        super().__init__()
        self.profession = [IT()]
        self.context = context

    def choose_occupation(self):
        """
        首页选项：
        1. 选择职业：确定当前职业
        :return:
        """
        self.context.set_profession(self.profession[0])
        return
        while True:
            self.draw_text(self.profession)
            # 获取当前职业
            profession = self.profession[int(self.input_text("请选择职业："))]
            sure = self.input_text(f"确定是{profession}吗？ \n0: Yes, 1: No")
            if sure == "0":
                break
        # 将当前职业存入上下文，以便后续使用
        self.context.set_profession(profession)
