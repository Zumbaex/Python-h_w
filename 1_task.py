class Date:
    def __init__(self, d1='2-2-2022'):
        self.date1 = d1

    @classmethod
    def take_int(cls, obj):
        result = obj.date1.split('-')
        return f'1 число - {result[0]}, 2 число - {result[1]}, 3 число - {result[2]}'

    @staticmethod
    def validation(d, m, y):
        if 1 <= d <= 31 and 1 <= m <= 12 and 2000 <= y <= 2022:
            return 'Дата введена корректно'

        else:
            return f'Дата введена некорректно'


t = Date()
print(t.take_int(Date('1-1-1001')))
f = input('Введите дату формата «день-месяц-год»: ')
f = f.split('-')
print(Date.validation(int(f[0]), int(f[1]), int(f[2])))
