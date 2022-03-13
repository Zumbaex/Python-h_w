def int_func(a):
    li_st = a.split()
    for i in li_st:
        i = str.capitalize(i)
        print(i, end=' ')


user_text = input('Введите строчно несколько латинских слов: ')
int_func(user_text)
