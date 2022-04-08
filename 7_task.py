class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение равно: z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'


z_1 = ComplexNumbers(4, -7)
z_2 = ComplexNumbers(2, 9)
print(z_1 + z_2)
print(z_1 * z_2)
