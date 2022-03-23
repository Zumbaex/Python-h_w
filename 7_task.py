from itertools import count
from functools import reduce


num = int(input('Введите число: '))


def gen():
    for el in count(1):
        if el == num + 1:
            break
        else:
            yield el


gen = gen()
li_st = [i for i in gen]


def m_fact(i2, i1):
    return i2 * i1


print(f'Факториал вашего числа равен: {reduce(m_fact, li_st)}')
