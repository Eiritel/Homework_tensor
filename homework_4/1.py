from random import randint
while True:
    try:
        length = input('Введите желаемую длину массива: ')
        length = int(length)
        break
    except ValueError:
        print('Введите число!')

array = []
for i in range(length):
    array.append(randint(-50, 50))
print(f'Изначальный массив: {array}')
 
 
for i in range(length-1):
    for j in range(length-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
 
print(f'Отсортированный массив: {array}')