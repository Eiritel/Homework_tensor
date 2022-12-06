x=0
y=0
print('Для выхода из программы введите e')
while True:
    while True:
        try:
            direction_of_movement = input('Введите направление (f, b, r, l): ')
            direction_of_movement = str(direction_of_movement)
            if direction_of_movement == 'r' or direction_of_movement == 'l' or direction_of_movement == 'f' or direction_of_movement == 'b' or direction_of_movement == 'e':
                break
            else:
                raise ValueError
        except ValueError:
            print('Направление движения может быть только  f, b, r или l  - вперёд (f), назад(b), вправо (r) или влево (l)')
    if direction_of_movement == 'e':
        exit()

    while True:
        try:
            distance = input('Пройденная дистанция: ')
            distance = float(distance)
            if (distance < 0):
                raise ValueError
            break
        except ValueError:
            print('Введите положительное и численное значение дистанции!')


    if (direction_of_movement == 'f'):
        y += distance
    elif (direction_of_movement == 'b'):
        y -= distance
    elif (direction_of_movement =='r'):
        x += distance
    elif (direction_of_movement == 'l'):
        x -= distance

    print(f'Текущая позиция по x: {x}, по y: {y}')   