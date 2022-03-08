n = input('Введите предложение: ')
my_list = n.split()

for i, v in enumerate(my_list):
    if len(v) <= 10:
        print(f'{i + 1}) {v}')
    else:
        print(f'{i + 1}) {v[0:10]}')
