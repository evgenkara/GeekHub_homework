# Банкомат 2.0
#     - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
#     - на старті додати можливість залогінитися або створити нового користувача (при створенні нового користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
#     - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор, який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
#     - банкомат має власний баланс
#     - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість). Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
#     - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
#     - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
#     - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
#     - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (невірний логін/пароль, недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
#     - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій, що б ми могли його використати



import sqlite3
import datetime



class BankException(Exception):
    pass


con = sqlite3.connect('atm.db')
cur = con.cursor()


def create_tables():
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (id integer PRIMARY KEY, username text, password text,
                    is_incasator BOOLEAN NOT NULL CHECK (is_incasator IN (0,1)), UNIQUE (username)) ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS balance
                    ( id integer PRIMARY KEY,
                    username text,
                    user_balance integer,
                    FOREIGN KEY (id) REFERENCES users(id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users_transactions (id integer, username text, operation text, date_time timestamp, operation_summa integer, balance_after_oper integer, FOREIGN KEY (id) REFERENCES users(id))''')
    cur.execute('''CREATE TABLE IF NOT EXISTS banknotes (key integer PRIMARY KEY, banknote integer, amount integer )''')
    con.commit()


def insert_tables():
    cur.execute('''INSERT OR IGNORE INTO users VALUES (1, 'user1', '12345', 0), (2, 'user2', '23456', 0), (3, 'user3', '34567', 0), (4, 'admin', 'admin', 1)''')
    cur.execute('''INSERT OR IGNORE INTO balance VALUES (1, 'user1', 50000), (2, 'user2', 45000), (3, 'user3', 55000), (4, 'admin', 75000)''')
    cur.execute('''INSERT OR IGNORE INTO banknotes VALUES (1, 1000, 50), (2, 500, 50), (3, 200, 100), (4, 100, 100), (5, 50, 200), (6, 20, 200), (7, 10, 200)''')
    con.commit()


def validate_user(username, password):
    login_check = False
    is_admin = False
    cur.execute('SELECT is_incasator FROM users WHERE username = ? AND password = ?', (username, password))
    user = cur.fetchone()
    if user:
        login_check = True
        if 1 in user:
            is_admin = True
    return login_check, is_admin


def add_transaction(username, summa, new_sum):
    if new_sum > new_sum - summa:
        transaction = 'Пополнение счета'
    else:
        transaction = 'Получение наличных'
    cur.execute('SELECT id FROM users WHERE username = ?', (username,))
    user_id = cur.fetchone()[0]
    date_time = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M')
    cur.execute(f'INSERT INTO users_transactions VALUES (?, ?, ?, ?, ?, ?)', (user_id, username, transaction, date_time, summa, new_sum))
    con.commit()


def check_balance(username):
    cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
    balance = cur.fetchone()[0]
    return f'Ваш баланс: {str(balance)}'


def replenish(username):
    summa = int(input('Сумма пополнения: '))
    cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
    currency = cur.fetchone()[0]
    if summa >= 0:
        new_balance = currency + summa
        cur.execute('UPDATE balance SET user_balance = ? WHERE username = ?', (new_balance, username))
        add_transaction(username, summa, new_balance)
        print(f'Счет пополнен на {summa}')
    else:
        print('Не могу распознать купюры...')


def withdraw_balance(num):
    cur.execute('SELECT banknote, amount FROM banknotes')
    load_banknotes = {bank[0]: bank[1] for bank in cur.fetchall()}
    keys = list(map(int, load_banknotes.keys()))
    wit_banknotes = []
    counter = 0
    while sum(wit_banknotes) < num:
        skip = False
        if counter + 1 > len(keys):
            raise BankException
        for key in keys:
            if skip:
                break
            elif key + sum(wit_banknotes) <= num and load_banknotes[key] > 0:
                for k in keys:
                    if (num - sum(wit_banknotes) - key) % k == 0 and load_banknotes[k] > 0:
                        wit_banknotes.append(key)
                        load_banknotes[key] -= 1
                        skip = True
                        break
        counter += 1
    for key, val in zip(load_banknotes.keys(), load_banknotes.values()):
        cur.execute('UPDATE banknotes SET amount = ? WHERE banknote = ?', (val, key))
        con.commit()
    return f'Выдано купюры: {wit_banknotes}'


def withdraw(username):
    atm_sum = 0
    cur.execute('SELECT banknote, amount FROM banknotes')
    for bank in cur.fetchall():
        atm_sum += bank[0] * bank[1]
    cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
    currency = cur.fetchone()[0]

    summa = int(input(f'Сумма наличных в банкомате: {atm_sum}\nУкажите сумму для вывода: '))
    if summa > 0 and summa % 10 == 0:
        if summa <= currency:
            new_balance = currency - summa
            cur.execute('UPDATE balance SET user_balance = ? WHERE username = ?', (new_balance, username))
            add_transaction(username, currency, new_balance)
            try:
                print(withdraw_balance(summa))
            except BankException:
                w = int(input(f'В банкомате недостаточно денег. Доступно: {atm_sum}'))
                print(withdraw_balance(w))
        else:
            w = int(input('На Вашем счету недостаточно денег :(. Введите сумму меньше: '))
            print(withdraw_balance(w))

    else:
        print('Сумма должна быть кратна 10.')
        withdraw(username)
    con.commit()


def register():
    new_user = input('Имя пользователя: ')
    new_password = input('Пароль: ')
    not_occupied = True
    cur.execute('SELECT * FROM users WHERE username = ?', (new_user,))
    user = cur.fetchall()
    cur.execute('SELECT max(id) FROM users')
    last_id = cur.fetchone()[0]
    if user:
        not_occupied = False
    if not_occupied:
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (last_id + 1, new_user, new_password, 0))
        cur.execute('INSERT INTO balance VALUES (?, ?, ?)', (last_id + 1, new_user, 0))
        con.commit()
    else:
        print('Имя пользователя занято.')


def check_banknotes():
    cur.execute('SELECT banknote, amount FROM banknotes')
    result = {bank[0]: bank[1] for bank in cur.fetchall()}
    return result


def change_banknotes():
    choice = input('Выберите номинал: ')
    cur.execute('SELECT * FROM banknotes WHERE banknote = ?', (choice,))
    if cur.fetchone():
        new = int(input('Новое значение: '))
        if new >= 0:
            cur.execute('UPDATE banknotes SET amount = ? WHERE banknote = ?', (new, choice))
        else:
            print('Значение не может быть отрицательным\n>')
            change_banknotes()
    else:
        print('Выберите из доступных значений (10, 20, 50, 100, 200, 500, 1000)')
        change_banknotes()
    con.commit()


def start(username, password):
    create_tables()
    insert_tables()
    if validate_user(username, password)[0]:
        while True:
            if validate_user(username, password)[1]:
                while True:
                    action = int(input('Выберите операцию:\n1. Показать доступные купюры\n2. Изменить наличие купюр\n3. Завершить работу\n> '))
                    if action == 1:
                        print(check_banknotes())
                    elif action == 2:
                        change_banknotes()
                    elif action == 3:
                        exit()
                    else:
                        print('Что-то пошло не так. Попробуйте ещё раз.\n>')
            action = int(input('Выберите операцию:\n1. Баланс на экран\n2. Пополнить счет\n3. Получить наличные\n4. Завершить работу\n> '))
            if action == 1:
                print(check_balance(username))
            elif action == 2:
                replenish(username)
            elif action == 3:
                withdraw(username)
            elif action == 4:
                exit()
            else:
                print('Что-то пошло не так. Попробуйте ещё раз.\n>')
    else:
        reg = int(input('Вы не зарегистрированы. Пройти регистрацию\n1. Да\n2. Нет\n> '))
        if reg == 1:
            register()
        else:
            exit()



if __name__ == '__main__':
    username = input('Введите имя: ')
    password = input('Введите пароль: ')

    start(username, password)

    con.close()
