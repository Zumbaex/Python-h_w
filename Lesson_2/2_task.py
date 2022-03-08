rev_list = []
i = 1
while i <= 5:
    list_el = input(f'Введите {i}-й элемент списка: ')
    rev_list.append(list_el)
    i += 1

print(f'Итоговый список : {rev_list}')

z = 0
x = 1
while z < 5:
    p = rev_list.pop(z)
    rev_list.insert(x, p)
    x += 2
    z += 2

print(f'Меняем местами индексы 0 и 1, 2 и 3, 4 на месте: {rev_list}')
