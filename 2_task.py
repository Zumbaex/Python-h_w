class Division:
    def __init__(self, delim, delit):
        self.delim = delim
        self.delit = delit

    def div(self):
        if self.delit == 0:
            raise ZeroDivisionErr(self.delit)
        return f'Результат деления: {self.delim // self.delit}'


class ZeroDivisionErr(Exception):
    def __init__(self, current, need='число > 0'):
        self.current = current
        self.need = need

    def __str__(self):
        return f'Делить на ноль нельзя! Вы указали: {self.current}, а нужно указать {self.need}'


try:
    m = Division(2, 0)
    print(m.div())
except ZeroDivisionErr as err:
    print(err)
