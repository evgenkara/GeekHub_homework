# Написати функцію <square>, яка прийматиме один аргумент -
# сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
# периметр квадрата, площа квадрата та його діагональ.



def square(side):
    perimeter = 4 * side
    square = side ** 2
    diagonal = round(side * 2 ** 0.5, 2)
    return perimeter, square, diagonal


side = int(input('Введіть сторону квадрата: '))
f = square(side)
print(f'Периметр: {f[0]}, площа: {f[1]}, діагональ: {f[2]}')
