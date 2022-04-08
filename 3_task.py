class ListIter:
    def __init__(self, *args):
        self.li_st = []

    def iterat(self):
        print('Введите числа через enter. Чтобы закончить ввод напишите "stop"')
        while True:
            try:
                data = input('Введите число: ')
                if data == 'stop':
                    break
                else:
                    n = int(data)
                    self.li_st.append(n)
            except ValueError:
                #raise ValueErr()
                print('Недопустимо введение других данных, кроме чисел!')
        print(f'Итоговый результат: {self.li_st}')


#class ValueErr(Exception):
    #def __str__(self):
        #return f'Не допустимо введение других данных, кроме чисел!'


t = ListIter()
t.iterat()
