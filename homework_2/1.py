while True:
    try:
        a = input('Введите первое число: ')
        a = float(a)
        break
    except ValueError:
        print('Введённый символ не является числом!')

while True:
    try:
        b = input('Введите второе число: ')
        b = float(b)
        break
    except ValueError:
        print('Введённый символ не является числом!')
        
print(f'Введённые числа: {a}, {b}')
print(f'Результат сложения: {a+b}')
print(f'Результат вычитания: {a-b}')
print(f'Результат умножения: {a*b}')
print(f'Результат деления: {a/b}')
print(f'Результат возведения в степень: {a**b}')
print(f'Результат деления по модулю: {a%b}')
print(f'Результат целочисленного деления: {a//b}')