from cmath import sqrt

while True:
    try:
        a = input('Введите первый коэффициент: ')
        a = complex(a)
        break
    except ValueError:
        print('Коэффициент должен быть комплексным числом!')

while True:
    try:
        b = input('Введите второй коэффициент: ')
        b = complex(b)
        break
    except ValueError:
        print('Коэффициент должен быть комплексным числом!')

while True:
    try:
        c = input('Введите третий коэффициент: ')
        c = complex(c)
        break
    except ValueError:
        print('Коэффициент должен быть комплексным числом!')

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
                if b == 0:
                    print(f'x= {sqrt(-c / a)}')
                else:
                    discriminant = b ** 2 - 4 * a * c
                    x1 = (-b + sqrt(discriminant)) / (2 * a)
                    x2 = (-b - sqrt(discriminant)) / (2 * a)
                    print(f'x1: {x1}, x2: {x2}')