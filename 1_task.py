import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    time = [7, 2, 7]

    def turn_light(self):
        i = 0
        for z in self.__color:
            print(f'Работает {self.__color[i]} свет')
            time.sleep(self.time[i])
            i += 1

        print('Выключение светофора...')


tr_li = TrafficLight()
tr_li.turn_light()
