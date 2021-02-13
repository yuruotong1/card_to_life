from main.context import Context
from main.page.home_page import HomePage


class Main:
    def __init__(self):
        self.context = Context()
        self.home_page = HomePage(self.context)

    def main(self):
        self.home_page.choose_occupation()
        while True:
            # 回合数加 1
            self.context.bout += 1
            # 显示指标
            self.context.indicator.show_indicator()
            break
