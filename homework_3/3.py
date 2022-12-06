from math import sqrt

while True:
    try:
        a = input('Введите первый коэффициент: ')
        a = float(a)
        break
    except ValueError:
        print('Введите числовой коэффициент!')

while True:
    try:
        b = input('Введите второй коэффициент: ')
        b = float(b)
        break
    except ValueError:
        print('Введите числовой коэффициент!')

while True:
    try:
        c = input('Введите третий коэффициент: ')
        c = float(c)
        break
    except ValueError:
        print('Введите числовой коэффициент!')

if a == 0 and b == 0 and c == 0:
    print('Ответ - любое число')
else:
    if a == 0 and b == 0:
        print('Корней нет')
    else:
        if a == 0 and c == 0:
            print(f'x = 0')
        else:
            if a == 0:
                x = (-c / b)
                print(f'x = {x}')
            else:
                discriminant = b ** 2 - 4 * a * c
                if discriminant > 0:
                    x1 = (-b + sqrt(discriminant)) / (2 * a)
                    x2 = (-b - sqrt(discriminant)) / (2 * a)
                    print(f'x1: {x1}, x2: {x2}')
                elif (discriminant == 0):
                    x = -b / (2 * a)
                    print(f'x: {x}')
                else:
                    print('Корней нет')