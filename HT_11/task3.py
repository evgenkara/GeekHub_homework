# Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
# Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.


import datetime
import sqlite3


con = sqlite3.connect('atm.bd')
cur = con.cursor()


class DataBase(object):
    def __init__(self, username):
        self.username = username

    @staticmethod
    def create_tables():
        cur.execute('''CREATE TABLE IF NOT EXISTS users
                        (id integer PRIMARY KEY, username text, password text,
                        is_incasator BOOLEAN NOT NULL CHECK (is_incasator IN (0,1)), UNIQUE (username)) ''')
        cur.execute('''CREATE TABLE IF NOT EXISTS balance
                        ( id integer PRIMARY KEY,
                        username text,
                        user_balance integer,
                        FOREIGN KEY (id) REFERENCES users(id))''')
        cur.execute('''CREATE TABLE IF NOT EXISTS users_transactions (id integer, username text, operation text, 
                    date_time timestamp, operation_summa integer, balance_after_oper integer, 
                    FOREIGN KEY (id) REFERENCES users(id))''')
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS banknotes (key integer PRIMARY KEY, banknote integer, amount integer )''')
        cur.execute('''CREATE TABLE IF NOT EXISTS atm_transactions (key integer, date_time timestamp, 
                    username text, operation text, amount integer)''')
        con.commit()

    @staticmethod
    def insert_tables():
        cur.execute('''INSERT OR IGNORE INTO users VALUES (1, 'user1', '12345', 0), (2, 'user2', '23456', 0),
                    (3, 'user3', '34567', 0), (4, 'admin', 'admin', 1)''')
        cur.execute('''INSERT OR IGNORE INTO balance VALUES (1, 'user1', 50000), (2, 'user2', 45000),
                    (3, 'user3', 55000), (4, 'admin', 0)''')
        cur.execute('''INSERT OR IGNORE INTO banknotes VALUES (1, 1000, 5), (2, 500, 1), (3, 200, 4), (4, 100, 0),
                    (5, 50, 1), (6, 20, 1), (7, 10, 5)''')
        con.commit()

    def add_transaction(self, username, summa, new_sum, currency):
        if new_sum == currency + summa:
            transaction = 'Пополнение счета'
        else:
            transaction = 'Получение наличных'
        cur.execute('SELECT id FROM users WHERE username = ?', (username,))
        user_id = cur.fetchone()[0]
        date_time = datetime.datetime.now().strftime('%d.%m.%Y, %H:%M')
        cur.execute('INSERT INTO users_transactions VALUES (?, ?, ?, ?, ?, ?)',
                    (user_id, username, transaction, date_time, summa, new_sum))
        con.commit()

    @staticmethod
    def withdraw_balance(summa):
        cur.execute('SELECT banknote, amount FROM banknotes')
        load_banknotes = {bank[0]: bank[1] for bank in cur.fetchall() if bank[1] > 0}

        def map_func(x):
            a = []
            for _ in range(x[1]):
                a.append(x[0])
            return a

        keys = sum(list(map(map_func, load_banknotes.items())), [])
        sums = {0: 0}
        for i in range(1, len(keys) + 1):
            value = keys[i - 1]
            new_sums = {}
            for j in sums.keys():
                new_sum = j + value
                if new_sum > summa:
                    continue
                elif new_sum not in sums.keys():
                    new_sums[new_sum] = value
            sums = sums | new_sums
            if summa in sums.keys():
                break
        given_banknotes = []
        if summa not in sums.keys():
            print('Выдать сумму невозможно')
            raise BankException
        else:
            rem = summa
            while rem > 0:
                given_banknotes.append(sums[rem])
                rem -= sums[rem]

        cash_bd = {}
        for i in given_banknotes:
            cash_bd[i] = given_banknotes.count(i)
        for item in cash_bd.items():
            amount = load_banknotes[item[0]] - item[1]
            cur.execute('UPDATE banknotes SET amount = ? WHERE banknote = ?', (amount, item[0]))
            con.commit()

        return f'Выдано купюры: {given_banknotes}'


class Person(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password


class User(Person):

    def check_balance(self, username):
        cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
        balance = cur.fetchone()[0]
        return f'Ваш баланс: {str(balance)}'

    def replenish(self, username):
        summa = int(input('Сумма пополнения: '))
        cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
        currency = cur.fetchone()[0]
        if summa >= 0:
            new_balance = currency + summa
            cur.execute('UPDATE balance SET user_balance = ? WHERE username = ?', (new_balance, username))
            add_transaction(username, summa, new_balance, currency)
            print(f'Счет пополнен на {summa}')
        else:
            print('Не могу распознать купюры...')

    def withdraw(self, username):
        atm_sum = 0
        cur.execute('SELECT banknote, amount FROM banknotes')
        for bank in cur.fetchall():
            atm_sum += bank[0] * bank[1]
        cur.execute('SELECT user_balance FROM balance WHERE username = ?', (username,))
        currency = cur.fetchone()[0]
        summa = int(input(f'Сумма наличных в банкомате: {atm_sum}\nУкажите сумму для вывода: '))
        while summa > atm_sum:
            print('В банкомате недостаточно денег.')
            print('Для выхода в главное меню нажмите 0 (ноль)')
            summa = int(input(f'Сумма наличных в банкомате: {atm_sum}\nУкажите сумму для вывода: '))

        if summa == 0:
            return
        elif summa > 0 and summa % 10 == 0:

            if summa <= currency:
                new_balance = currency - summa
                cur.execute('UPDATE balance SET user_balance = ? WHERE username = ?', (new_balance, username))
                add_transaction(username, summa, new_balance, currency)
                print(withdraw_balance(summa))

            else:
                w = int(input('На Вашем счету недостаточно денег :(. Введите сумму меньше: '))
                print(withdraw_balance(w))

        else:
            print('Сумма должна быть кратна 10.')
            withdraw(username)
        con.commit()

    def main_screen(self):
        while True:
            action = int(input(
                '''Я Банкомат. Что желаете сделать?\n\n1. Войти в систему\n2. Регистрация нового пользователя\n3. Завершить работу\n> '''))
            if action == 1:
                username = input('Введите имя: ')
                password = input('Введите пароль: ')
                if validate_user(username, password)[1]:
                    while True:
                        action = int(input(
                            '''Выберите операцию:\n1. Показать доступные купюры\n2. Изменить наличие купюр\n3. История операций банкомата\n4. Завершить работу\n> '''))
                        if action == 1:
                            print(check_banknotes())
                        elif action == 2:
                            change_banknotes()
                        elif action == 3:
                            get_atm_history()
                        elif action == 4:
                            break
                        else:
                            print('Что-то пошло не так. Попробуйте ещё раз.\n>')
                elif validate_user(username, password)[0]:
                    while True:
                        action = int(input(
                            '''Выберите операцию:\n1. Баланс на экран\n2. Пополнить счет\n3. Получить наличные\n4. История операций\n5. Завершить работу\n> '''))
                        if action == 1:
                            print(check_balance(username))
                        elif action == 2:
                            replenish(username)
                        elif action == 3:
                            withdraw(username)
                        elif action == 4:
                            get_user_history(username)
                        elif action == 5:
                            break
                        else:
                            print('Что-то пошло не так. Попробуйте ещё раз.\n>')

            elif action == 2:
                register()
            elif action == 3:
                exit()
            else:
                print('1, 2 или 3!!!')


class Incasator(Person):

    @staticmethod
    def check_banknotes(self):
        cur.execute('SELECT banknote, amount FROM banknotes')
        result = {bank[0]: bank[1] for bank in cur.fetchall()}
        return result

    def change_banknotes(self):
        while True:
            print(f'В наличии: {check_banknotes()}')
            print('Для выхода в главное меню нажмите 0 (ноль)')
            choice = input('Выберите номинал: ')
            if choice == '0':
                break
            cur.execute('SELECT * FROM banknotes WHERE banknote = ?', (choice,))
            if cur.fetchone():
                new = int(input('Новое значение: '))
                if new >= 0:
                    cur.execute('UPDATE banknotes SET amount = ? WHERE banknote = ?', (new, choice))
                else:
                    print('Значение не может быть отрицательным\n>')
            else:
                print('Выберите из доступных значений (10, 20, 50, 100, 200, 500, 1000)')

        con.commit()

    def menu(self):
        pass


class Auth(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def register(self):                     # TODO: Бонус при регистрации
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

    def validate_user(self, username, password):
        login_check = False
        is_admin = False
        cur.execute('SELECT is_incasator FROM users WHERE username = ? AND password = ?', (username, password))
        user = cur.fetchone()
        if user:
            login_check = True
            if 1 in user:
                is_admin = True
        return login_check, is_admin

class Atm(object):

    def start(self):
        create_tables()
        insert_tables()
        main_screen()


if __name__ == '__main__':

    username = input("Enter username: ")
    password = input("Enter password: ")
    DataBase.create_tables()
    DataBase.insert_tables()
    ATM().start(username, password)

    con.close()
