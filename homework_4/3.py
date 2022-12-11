from random import randint
array_1 = []
array_2 = []
while True:
    try:
        length = input('Введите желаемую длину массивов: ')
        length = int(length)
        break
    except ValueError:
        print('Введите число!')
for i in range(length):
    array_1.append(randint(-100, 100))
    array_2.append(randint(-100, 100))

print(f'Первый массив: {array_1}')
print(f'Первый массив: {array_2}')
set_array1=set(array_1)
set_array2=set(array_2)
print(f'Элементы, входящие одновременно в оба множества: {str(set_array1.intersection(set_array2))}')
print(f'Элементы, входящие только в первое, но не входят во второе множнство: {str(set_array1.difference(set_array2))}')
print(f'Элементы, входящие только в первое, но не входят во второе множнство: {str(set_array2.difference(set_array1))}')
print(f'Элементы, входящие в первое или во второе множество, но не в оба из них одновременно: {str(set_array1.symmetric_difference(set_array2))}')