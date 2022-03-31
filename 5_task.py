class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка чернилами...')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка графитом...')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка цветом...')


hand1 = Handle('Blue handle')
hand1.draw()
print(hand1.title)

pencil1 = Pencil('Standart pencil')
pencil1.draw()
print(pencil1.title)

pen1 = Pen('Black pen')
pen1.draw()
print(pen1.title)
