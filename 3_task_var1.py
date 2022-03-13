def my_func(a, b, c):
    magic_list = [a, b, c]
    magic_list.sort(reverse=True)
    result = magic_list[0] + magic_list[1]
    print(f'Сумма двух наибольших чисел равна: {result}')


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

my_func(num_1, num_2, num_3)
