from itertools import count

num = int(input('Введите число с которого начать счет: '))

for el in count(num):
    if el > num + 10:
        break
    else:
        print(el)
