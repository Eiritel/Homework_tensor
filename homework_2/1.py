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

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponentiation =a ** b
modulo_operation =a % b
integer_division =a // b

print(f'Введённые числа: {a}, {b}')
print(f'Результат сложения: {addition}')
print(f'Результат вычитания: {subtraction}')
print(f'Результат умножения: {multiplication}')
print(f'Результат деления: {division}')
print(f'Результат возведения в степень: {exponentiation}')
print(f'Результат деления по модулю: {modulo_operation}')
print(f'Результат целочисленного деления: {integer_division}')