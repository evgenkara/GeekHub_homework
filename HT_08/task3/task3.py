# Програма-банкомат.
#    Використовуючи функції створити програму з наступним функціоналом:
#       - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
#       - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій
#       (файл <{username_transactions.JSON>);
#       - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
#       (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
#    Особливості реалізації:
#       - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#       - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#       - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання
#       нового користувача - не стримуйте себе :)
#    Особливості функціонала:
#       - за кожен функціонал відповідає окрема функція;
#       - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#       - на початку роботи - логін користувача (програма запитує ім'я/пароль).
#       Якщо вони неправильні - вивести повідомлення про це і закінчити роботу
#       (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
#       - потім - елементарне меню типн:
#         Введіть дію:
#            1. Подивитись баланс
#            2. Поповнити баланс
#            3. Вихід



import csv
import json
import datetime



def validate_user(username, password):
    user_info = [username, password]
    login_check = False
    with open('users.csv', 'r') as users_data:
        data = csv.reader(users_data)
        for user in data:
            if user_info == user:
                login_check = True
                break
    return login_check


def add_transaction(username, summa, new_sum):
    if new_sum > new_sum - summa:
        transaction = 'Пополнение счета'
    else:
        transaction = 'Получение наличных'
    date_time = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M')
    data = {'Дата, время': date_time, 'Операция': transaction, 'Сумма операции': summa, 'Баланс после операции': new_sum}
    with open(f'{username}_transactions.json', 'a', encoding='utf-8') as transactions:
        json.dump(data, transactions, ensure_ascii=False)
        transactions.write('\n')


def check_balance(username):
    with open(f'{username}_balance.txt', 'r') as balance:
        currency = int(balance.readline())
        return f'У Вас на счету: {currency}'


def replenish(username):
    with open(f'{username}_balance.txt', 'r') as balance:
        currency = int(balance.readline())
    summa = int(input('Сумма пополнения: '))
    if summa >= 0:
        new_balance = currency + summa
        with open(f'{username}_balance.txt', 'w') as balance:
            balance.write(str(new_balance))
        add_transaction(username, summa, new_balance)
        print(f'Счет пополнен на {summa}')
    else:
        print('Не могу распознать купюры...')


def withdraw(username):
    with open(f'{username}_balance.txt', 'r') as balance:
        currency = int(balance.readline())
    summa = int(input('Укажите сумму для вывода: '))
    if summa > 0:
        if summa <= currency:
            new_balance = currency - summa
            with open(f'{username}_balance.txt', 'w') as balance:
                balance.write(str(new_balance))
            add_transaction(username, summa, new_balance)
            print(f'Вы сняли со счета {summa}')
        else:
            print('На Вашем счету недостаточно денег :(')
            withdraw(username)
    else:
        print('Проверьте сумму')


def back():
    choose = int(input('1. На главный экран\n2. Завершить работу\n> '))
    if choose == 1:
        start()
    elif choose == 2:
        exit()


def start():
    if validate_user(login, password):
        action = int(input('Выберите операцию:\n1. Баланс на экран\n2. Пополнить счет\n3. Получить наличные\n4. Завершить работу\n> '))
        if action == 1:
            print(check_balance(login))
            back()
        elif action == 2:
            replenish(login)
            back()
        elif action == 3:
            withdraw(login)
            back()
        elif action == 4:
            exit()
        else:
            print('Что-то пошло не так. Попробуйте ещё раз.\n')
            start()
    else:
        print('Неверный логин или пароль.')



if __name__ == '__main__':
    login = input('Введите имя: ')
    password = input('Enter password: ')
    try:
        start()
    except ValueError:
        print('Что-то пошло не так. Попробуйте ещё раз.')
        start()
