inventory=dict()

while True:
        try:
            weight = input('Введите ограничение инвентаря по весу: ')
            weight = float(weight)
            if (weight < 0):
                raise ValueError
            break
        except ValueError:
            print('Вес инвентаря должен быть положительным числом!')
print('Игровой инвентарь') 
while True: 
    while True:
        try:
            command = input('Для добавления предмета - введите "a", для удаления предмета - введите "d", для просмотра инвентаря - "w", для выхода - "e": ')
            if command == 'e' or command == 'w' or command == 'a' or command == 'd' :
                break
            else:
                raise ValueError
        except ValueError:
            print('Некорректная команда!') 


    if (command == 'a'):
        name=input('Введите название предмета: ')
        while True:
            try:
                item_weight = input('Введите вес предмета: ')
                item_weight = float(item_weight)
                if (item_weight < 0):
                    raise ValueError
                break
            except ValueError:
                print('Вес предмета должен быть положительным числом!')    
        if ( (sum(inventory.values())) + item_weight ) <= weight:
            inventory[name] = item_weight   
        else:
            print('Превышен лимит инвентаря!')
    elif (command == 'w'):
        print(inventory)
    elif (command == 'd'):
        print('Какой предмет удаляем?')
        print(inventory)
        item = str(input('Введите название предмета из списка выше: '))
        if item in inventory:
            del inventory[item]
            print(f'Удалили {item}')
        else:
            print('Такого предмета нет')
    else:
        break
