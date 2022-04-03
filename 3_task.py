class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        res = self.cell - other.cell
        if res >= 0:
            return Cell(res)
        else:
            return 'Ошибка! Не может быть отрицательное число ячеек'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        res = self.cell / other.cell
        return Cell(int(res))

    def __str__(self):
        return f'Результат: {self.cell}'

    def make_order(self, row):
        stars = ''
        rows = self.cell // row # количество рядов *
        for i in range(rows): # для каждого ряда определяем количество *
            stars += f"{'*' * row}\n"
        stars += f'{"*" * (self.cell % row)}' # добавляем оставшиеся  от деления *
        return stars


cell1 = Cell(5)
cell2 = Cell(4)

print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(2))
