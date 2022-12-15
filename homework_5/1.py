import re

'''Программа проверяет пароль с заданными критериями. 
Если они были пройдены - будет выведено True, иначе False
    '''
def passwdCheck(passwd):
    try:
        passwd=str(passwd)
        if ((len(passwd) < 6) or 
        (re.search('\d',passwd) == None) or 
        (passwd.isdigit())) or (passwd.lower().find('password') != -1):
            raise ValueError
    except ValueError:
        return False
    return True    

passwd = input('Введите пароль: ')
print(passwdCheck())