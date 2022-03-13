q = 'y'
result = 0
print('Программа суммирования, введите n, чтобы закончить')
while q == 'y':
    try:
        user_n = input('Введите числа через пробел: ').split()
        int_list = list(map(int, list(filter(str.isdigit, user_n))))
        str_list = list(filter(str.isalpha, user_n))
        result += sum(int_list[:])
        print(result)
        if 'n' in str_list:
            break
        else:
            q = input('Хотите добавить еще? y - да, n - нет: ')
    except ValueError as er:
        print(er)

print('Конец программы')
