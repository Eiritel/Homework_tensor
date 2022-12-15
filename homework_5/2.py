def sumAll(*args):
    '''Функцию, принимающую сколько угодно параметров (в том числе и 0) 
    и возвращающую их сумму
    '''
    try:
        sum = None
        for arg in args:
            if sum == None:
                sum = arg
            else:
                sum += arg
        if sum is None:
            sum = 0        
        return sum
    except TypeError:
        print("Введены не числовые значения!")
        return None    

sum=sumAll(22,11111,44444)
if sum is not None:
    print('Sum of arguments: ' + str(sum)) 