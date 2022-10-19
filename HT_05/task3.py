# Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
# и яка вертатиме True, якщо це число просте і False - якщо ні.


def is_prime(number):
    t = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            t += 1
    if not t:
        return True
    else:
        return False


number = int(input('number: '))
print(is_prime(number))
