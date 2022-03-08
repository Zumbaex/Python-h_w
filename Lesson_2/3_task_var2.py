s_num = int(input('Введите номер месяца: '))
seasons = {
    1: 'зиме',
    2: 'весне',
    3: 'лету',
    4: 'осени',

}

if s_num <= 2 or s_num == 12:
    print(f'Ваш номер месяца соответствует {seasons[1]}')

elif s_num >= 3 and s_num <= 5:
    print(f'Ваш номер месяца соответствует {seasons[2]}')

elif s_num >= 6 and s_num <= 8:
    print(f'Ваш номер месяца соответствует {seasons[3]}')

elif s_num >= 9 and s_num <= 1:
    print(f'Ваш номер месяца соответствует {seasons[4]}')
