# Створіть функцію, всередині якої будуть записано СПИСОК
# із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій -
# необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна: якщо введено правильну пару ім'я/пароль - вертається True; якщо введено неправильну пару ім'я/пароль:
# якщо silent == True - функція повертає False, якщо silent == False - породжується виключення LoginException (його також треба створити =))


class LoginException(Exception):
    pass

    
def check_user(login, password, silent=False):
    users = [('login_1', 'password_1'),
             ('login_2', 'password_2'),
             ('login_3', 'password_3'),
             ('login_4', 'password_4'),
             ('login_5', 'password_5')]
    
    if (login, password) in users:
        return True
    elif (login, password) not in users and silent:
        return False
    else:
        raise LoginException('No such user')


print(check_user('login_1', 'password_1'))
print(check_user('login_12', 'password_12', True))
print(check_user('login_12', 'password_12'))
    
