# На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
#   а) створити список із парами ім'я/пароль різноманітних видів
#      (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
#      перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення


class LoginException(Exception):
    def __init__(self, message=None):
        self.message = message
        

def validate_user(username, password):
    if len(username) <= 3:
        raise LoginException('Username is too short')
    elif len(username) >= 50:
        raise LoginException('Username is too long')
    elif len(password) <= 8:
        raise LoginException('Password is too short')
    elif password.isalpha():
        raise LoginException('Password must contain at least one number')
    elif not any(i.isupper() for i in password):
        raise LoginException('Password must contain at least one uppercase letter')


def check_user(login, password, ex='OK'):
    try:
        validate_user(login, password)
    except LoginException as err:
        ex = err
    print(f'Name: {login}\nPassword: {password}\nStatus: {ex}\n-----')


users = [['user1', 'password555'], ['user2', 'Ppassword'], ['u3', 'Password777'], ['user4', 'Pass3'], ['useruser31361115146461513514894946156146441516146494', 'Password777']]
for user in users:
    check_user(user[0], user[1])
