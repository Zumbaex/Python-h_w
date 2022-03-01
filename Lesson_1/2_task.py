user_sec = int(input('Введите количество секунд: '))

hours = user_sec // 3600
min = (user_sec - hours * 3600) // 60
sec = user_sec - (hours * 3600 + min * 60)

print(f'Введенному количеству секунд соответствует чч:мм:сс : {hours}:{min}:{sec}')
