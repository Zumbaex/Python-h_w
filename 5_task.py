try:
    user_n = input('Введите числа через пробел: ')
    user_list = list(map(int, user_n.split()))
    result = sum(user_list[:])
    print(result)
except ValueError as er:
    print(er)
    user_n = input('Введите числа через пробел: ')
    user_list = list(map(int, user_n.split()))
    result = sum(user_list[:])
    print(result)

q = input('Хотите добавить еще? y - да, n - нет: ')

while q == 'y':
    user_n = input('Пожалуйста, добавляйте: ')
    li_st = user_n.split()
    try:
        li_st = list(map(int, user_n.split()))
        result = result + sum(li_st[:])
        print(result)
    except ValueError as er:
        print(er)
        li_st.pop(-1)
        li_st = list(map(int, user_n.split()))
        result = result + sum(li_st[:])
        print(result)

    q = input('Хотите добавить еще? y - да, n - нет: ')

print('Конец программы')


