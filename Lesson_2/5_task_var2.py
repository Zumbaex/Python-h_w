my_list = [7, 5, 3, 3, 2]
print(f'Это программа добавления цифр в рейтинг (ограничение 3 цифры)')
i = 1

while i <= 3:
    print(f'Актуальный рейтинг: {my_list}')
    user = int(input('Введите цифру для добавления в рейтинг: '))
    for v in range(len(my_list)):
        if my_list[v] > user and my_list[v+1]< user:
            my_list.insert(v + 1, user)
        elif my_list[v] == user:
            my_list.insert(v+1, user)
            break
        elif my_list[0] < user:
            my_list.insert(0, user)
        elif my_list[-1] > user:
            my_list.append(user)