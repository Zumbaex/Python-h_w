from functools import reduce
with open('3_task.txt', 'r', encoding='utf-8') as surnames:
    less_20k = []
    salary = []
    staff = []
    for line in surnames:
        li_st = line.split(' ')
        salary.append(float(li_st[1]))
        staff.append(li_st[0])
        if float(li_st[1]) < 20000:
            less = li_st[0]
            less_20k.append(less)

    print(f'Сотрудники имеющие оклад менее 20к: {less_20k}')

    def sum_sal(sal_1, sal_2):
        return sal_1 + sal_2

    red = reduce(sum_sal, salary)
    average = red / len(staff)

    print(f'Средняя величина дохода сотрудников: {round(average, 2)}')
