import time


class OrgTechStock:
    s_stock = []

    def stock(self):
        try:
            mod = input('Введите модель: ')
            col = input('Введите цвет: ')
            pr = int(input('Введите цену за штуку: '))
            am = int(input('Введите количество: '))
            li_st = [mod, col, pr]
            res = {am: li_st}
            self.s_stock.append(res)
            return self.s_stock

        except:
            print('Данные введены неверно!')


class OrgTech:
    def __init__(self, a, m, c, s):
        self.amount = a
        self.model = m
        self.color = c
        self.speed = s


class Printer(OrgTech, OrgTechStock):
    def __init__(self, a, m, c, s, pc):
        self.printcolor = pc
        super().__init__(a, m, c, s)

    def func(self):
        print(f'Принтер модели {self.model} цвета {self.color} печатает со скоростью {self.speed} '
              f'страниц в минуту в цвете {self.printcolor}!')
        i = 1
        zzz = 60 // int(self.speed)
        while i <= 10:
            print(f'Печать {i} страницы...')
            time.sleep(zzz)
            i += 1
        print('Печать 10 страниц окончена!')


class Skanner(OrgTech, OrgTechStock):
    def __init__(self, a, m, c, s, ff):
        self.file_format = ff
        super().__init__(a, m, c, s)

    def func(self):
        print(f'Сканер модели {self.model} цвета {self.color} сканирует со скоростью {self.speed} '
              f'страниц в минуту в формате {self.file_format}!')
        i = 1
        zzz = 60 // int(self.speed)
        while i <= 10:
            print(f'Сканирование {i} страницы...')
            time.sleep(zzz)
            i += 1
        print('Сканирование 10 страниц окончено!')


class Xerox(OrgTech, OrgTechStock):
    def __init__(self, a, m, c, s, qy):
        self.quality = qy
        super().__init__(a, m, c, s)

    def func(self):
        print(f'Ксерокс модели {self.model} цвета {self.color} ксерокопирует со скоростью {self.speed} '
              f'страниц в минуту с уровнем качества: {self.quality}!')
        i = 1
        zzz = 60 // int(self.speed)
        while i <= 10:
            print(f'Ксерокопирование {i} страницы...')
            time.sleep(zzz)
            i += 1
        print('Ксерокопия 10 страниц сделана!')


obj = Xerox(5, 'Samsung', 'black', 40, 'high quality')
obj1 = Printer(7, 'Xiaomi', 'white', 35, 'black/white')
print(obj.stock())
print(obj1.stock())
