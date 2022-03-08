my_list = [7, 5, 3, 3, 2]
i = 1
print(f'Это программа добавления цифр в рейтинг {my_list} (ограничение 3 цифры)')
while i <= 3:
    user = int(input('Введите цифру для добавления в рейтинг: '))
    my_list.append(user)
    my_list.sort()
    my_list.reverse()
    print(f'Актуальный рейтинг: {my_list}')
    i += 1

print('Спасибо за работу!')
