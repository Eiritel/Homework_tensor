from math import pi
while True:
    try:
        r = input('Введите радиус круга: ')
        r = float(r)
        break
    except ValueError:
        print('Введённый радиус не является числом!')
print(f'Площадь круга: {str(pi*r**2)}')