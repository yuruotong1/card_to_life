from main.base import Base
from main.context import Context
from main.event.event_factory import EventFactory
from main.page.home_page import HomePage


class Main:
    def __init__(self):
        self.context = Context()
        self.home_page = HomePage(self.context)
        self.event_factory = EventFactory(self.context.indicator)

    def main(self):
        self.home_page.choose_occupation()
        # 注册事件
        self.event_factory.register_from_file("../resource/events.yaml")
        while True:
            # 显示指标
            self.context.indicator.show_indicator()
            self.event_factory.get_event()
            # 回合数加 1
            self.context.iteration_bout()
            # 如果到达 100 岁，结束游戏
            if self.context.age == 100:
                return
            # 每回合结束，发工资
            elif self.context.bout == 0:
                salary = self.context.profession.get_salary()
                Base.draw_text("发工资：" + str(salary))
                self.context.indicator.money.change(self.context.profession.get_salary())
            Base.draw_text("-" * 40)


if __name__ == 'main':
    Main().main()
