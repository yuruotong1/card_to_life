class Event:
    """
    定义事件
    """
    NAME = ""
    INFO = ""

    def generate(self):
        """
        事件发生时，会造成什么影响
        :return:
        """

    def __str__(self):
        content = self.NAME + "：" + self.INFO
        return content
