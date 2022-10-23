# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - якесь власне додаткове правило :)
#   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.


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
    elif password.isalpha() == True:
        raise LoginException('Password must contain at least one number')
    elif not any(i.isupper() for i in password):
        raise LoginException('Password must contain at least one uppercase letter')

    
validate_user('user1', 'password555')
