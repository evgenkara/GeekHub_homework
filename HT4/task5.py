# Калькулятор


def calculate(user_input):
    try:
        return eval(user_input)
    except NameError:
        return 'Неможливо вирішити. Перевірте правильність виразу'

print(50 * '#')
print()
print('КАЛЬКУЛЯТОР'.center(50, '-'))
print()
print(50 * '#')
while True:
    print('Для завершення програми введіть "Q".'.center(50, '-'))
    user_input = input('\nВведіть вираз (наприклад 2 + 2): ')
    print()
    if user_input in 'QqЙй':
        break
    else:
        print(f'Це було не складно. {user_input} = {calculate(user_input)}\n')
        


    
