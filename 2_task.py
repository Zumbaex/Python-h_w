class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def weight(self):
        result = self._length * self._width * 25 * 5
        print(f'{self._length} м * {self._width} м * 25 кг * 5 см = {result // 1000} т')


r = Road(1000, 120)
r.weight()
