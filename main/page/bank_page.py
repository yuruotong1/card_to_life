from main.base import Base
from main.indicator.money import Money


class BankPage:
    INTEREST_RATE = 0.4

    def __init__(self, money: Money):
        Base.draw_text("欢迎来到银行，我行现推出以下业务：")
        # 贷款上限为工资 *10
        # todo：加入资产评估
        from main.context import Context
        self.indicator_money = money
        self.loan_limit = Context.get_profession().get_salary() * 10

    def loan(self, describe):
        """
        银行操作，包括贷款
        :param describe: 描述信息
        :return:
        """
        while True:
            Base.draw_text("根据资产评估，您的贷款上限为：", self.loan_limit, "，贷款时间为： 30 年")
            loan_amount = Base.input_text("当前利率为：4%，请输入贷款金额，* 为取消：")
            if loan_amount == "*":
                continue
            elif int(loan_amount) <= self.loan_limit:
                from main.context import Context
                interest = int(int(loan_amount) * self.INTEREST_RATE)
                Context.get_profession().loan.append(
                    {"describe": describe,
                     "money": (int(loan_amount) + interest) // 30,
                     "time": 30})
                self.indicator_money.change(int(loan_amount))
                Base.draw_text(f"贷款成功！ 您贷款了 {loan_amount} 元，利息为 {interest} 元\n当前余额：{self.indicator_money.value}")
                break
            elif int(loan_amount) > self.loan_limit:
                Base.draw_text("贷款金额超出上限，请重新选择")
