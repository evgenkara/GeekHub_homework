# Написати функцію <prime_list>, яка прийматиме 2 аргументи -
# початок і кінець діапазона, і вертатиме список простих чисел всередині
# цього діапазона. Не забудьте про перевірку на валідність введених даних
# та у випадку невідповідності - виведіть повідомлення.


def is_prime(number):
    t = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            t += 1
    if not t:
        return True
    else:
        return False


def prime_list(start, stop):
    return list(filter(is_prime, range(start, stop)))


while True:
    try:
        start = int(input('Початок діапазону: '))
        stop = int(input('Кінець діапазону: '))
    except ValueError:
        print('Помилка! Введіть числове значення.')
        continue
    else:
        print(prime_list(start, stop))
        break

    
