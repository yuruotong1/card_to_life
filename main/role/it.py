from main.role.role import Role


class IT(Role):
    def __init__(self):
        super().__init__()
        self.name = "IT"
        self._salary = 10000

