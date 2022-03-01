n = int(input('Введите число: '))
max = n % 10

while n >= 1:
    n = n // 10

    if max == 9:
        break
    if n % 10 > max:
        max = n % 10
        continue
    if n % 10 < max:
        continue

print(f'Максимальная цифра вашего числа: {max}')
