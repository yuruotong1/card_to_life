import os
import platform


class Base:
    # 记录已经输出的所有文字
    all_out = []

    @classmethod
    def draw_text(cls, content, *args):
        """
        print word
        :param content:
        :return:
        """
        # 如果是列表，换行打印
        if isinstance(content, list):
            content = [str(i) + "," + str(j) for i, j in enumerate(content)]
            content = "\n".join(content)
        elif not isinstance(content, str):
            content = str(content)
        # 如果存在位置参数，与　content 合并
        if args:
            args = [str(i) for i in args]
            content += "".join(args)
        # 将当前内容存入上下文
        cls.all_out.append(content)
        print(content)

    @classmethod
    def input_text(cls, hint: str = None):
        """
        获取用户输入，并打印
        :param hint:
        :return:
        """
        if hint is not None:
            cls.draw_text(hint)
        in_content = input()
        cls.all_out.append(in_content)
        return in_content

    @classmethod
    def clear_screen(cls):
        """
        清空所有输入
        :return:
        """
        if platform.platform().startswith("Windows"):
            os.system("cls")
        elif platform.platform().startswith("Mac") or platform.platform().startswith("Linux"):
            os.system("clear")
