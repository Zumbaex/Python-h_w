from abc import abstractmethod


class Clothes:
    def __init__(self, n):
        self.name = n

    @abstractmethod
    def result(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.size = v

    def cloth(self):
        f = self.size / 6.5 + 0.5
        result = round(f, 1)
        return result

    @property
    def result(self):
        return f'Название одежды: {self.name}. \nРасход ткани: {self.cloth()}'


class Costume(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.height = h

    def cloth(self):
        f = 2 * self.height + 0.3
        result = round(f, 1)
        return result

    @property
    def result(self):
        return f'Название одежды: {self.name}. \nРасход ткани: {self.cloth()}'


cl1 = Coat('Red', 5)
print(cl1.result)

cl2 = Costume('Blue', 5)
print(cl2.result)
