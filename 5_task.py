from functools import reduce
with open('5_task.txt', 'w+') as num_1:
    num = input('Введите числа через пробел: ')
    num_1.write(num)
    num_1.seek(0)
    li_st = num_1.read().split()
    int_list = [int(i) for i in li_st]

    def red(n1, n2):
        return n1 + n2

    result = reduce(red, int_list)
    print(f'Сумма чисел равна: {result}')
