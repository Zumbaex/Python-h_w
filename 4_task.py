with open('4_task_1.txt', 'r', encoding='utf-8') as engl:
    di_ct = {
        'one': 'Один',
        'two': 'Два',
        'three': 'Три',
        'four': 'Четыре'
    }
    i = 0
    n = 1
    keys = list(di_ct.keys())
    val = list(di_ct.values())
    for line in engl:
        lst = line.split(' — ')
        with open('4_task_2.txt', 'a', encoding='utf-8') as russ:
            russ.write(val[i] + ' — ' + lst[1])
        i += 1

    print('Конец записи')
