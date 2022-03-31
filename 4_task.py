import random


class Car:
    def __init__(self, s, c, n, i_p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    def car_go(self):
        print('Машина поехала')

    def car_stop(self):
        print('Машина остановилась')

    def car_direction(self):
        self.dir = ['прямо', 'назад', 'налево', 'направо']
        rand = random.randint(0, 3)
        print(f'Машина поехала {self.dir[rand]}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля: {self.speed}')
            print('Вы превышаете скорость!')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля: {self.speed}')
            print('Вы превышаете скорость!')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


def pr_int(car_mod):
    print(f'Данные машины: {car_mod.speed} км/ч, цвет по ПТС: {car_mod.color}, марка: {car_mod.name}, служебная машина: {car_mod.is_police}')


my_car = SportCar(70, 'red', 'Audi')
my_car.show_speed()
pr_int(my_car)
