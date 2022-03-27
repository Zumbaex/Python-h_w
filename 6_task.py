from functools import reduce
with open('6_task.txt', 'r', encoding='utf-8') as lessons:
    di_ct = {}

    def red(n1, n2):
        return n1 + n2


    for line in lessons:
        li_st = line.split()
        #СЧИТАЕМ ЦИФРЫ
        numbers = li_st[1:]
        numbers1 = []
        for i in numbers:
            numb = ''.join(n for n in i if n.isdecimal())
            numbers1.append(numb)
        int_list = [int(i) for i in numbers1]
        result = reduce(red, int_list)
        #ВЫТАСКИВАЕМ ПРЕДМЕТ
        less = li_st[0]
        less_clr = less.replace(':', '')
        di_ct[less_clr] = result

    print(di_ct)
