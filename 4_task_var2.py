def my_f(x, y):
    i = 1
    while i != y:
        x = x * y
        i += 1
    result = 1 / x
    print(f'Результат: {result}')


n_1 = int(input('Введите положительное число: '))

while n_1 < 0:
    print('Введите положительное число!')
    n_1 = int(input('Попробуйте еще раз: '))

n_2 = int(input('Введите отрицательную степень: '))

while n_2 > 0:
    print('Введите отрицательную степень!')
    n_2 = int(input('Попробуйте еще раз: '))

my_f(n_1, abs(n_2))
