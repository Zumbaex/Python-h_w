from functools import reduce

li_st = [i for i in range(100, 1001) if i % 2 == 0]


def my_f(i_1, i_2):
    return i_1 * i_2


print(reduce(my_f, li_st))
