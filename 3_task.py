class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self.wage = w
        self.bonus = b


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        self._income = {'wage': self.wage, 'bonus': self.bonus}
        print(self._income)


ceo = Position('James', 'William', 'CEO', 7000, 500)
ceo.get_full_name()
ceo.get_total_income()
