# КАЛЬКУЛЯТОР


def calculate(x, y, operator):
    operators = ('+', '-', '*', '**', '/', '%', '//')
    if operator in operators[4:] and not y:
        return 'На ноль делить нельзя'
    elif operator == '+':
        return f'{x} + {y} = {x + y}'
    elif operator == '-':
        return f'{x} - {y} = {x - y}'
    elif operator == '*':
        return f'{x} * {y} = {x * y}'
    elif operator == '**':
        return f'{x} ** {y} = {x ** y}'
    elif operator == '/':
        return f'{x} / {y} = {x / y}'
    elif operator == '//':
        return f'{x} // {y} = {x // y}'
    elif operator == '%':
        return f'{x} % {y} = {x % y}'


while True:
    try:
        x = float(input('Введите первый операнд: '))
        operator = input('Введите знак операции: ')
        y = float(input('Введите второй операнд: '))
    except ValueError:
        print('Проверте значение операнда')
    else:
        print(calculate(x, y, operator))
    exit_calc = input('Вы хотите завершить программу? (Y/N)')
    if exit_calc in 'YyНн':
        break
    elif exit_calc in 'NnТт':
        continue


