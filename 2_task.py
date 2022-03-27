with open('2_task.txt', 'r', encoding='utf-8') as piton:
    i = 1
    for line in piton:
        print(f'Количество букв в {i} строке: {len(line)}')
        words = line.split(' ')
        print(f'Количество слов в {i} строке: {len(words)}')
        print('*' * 30)
        i += 1
