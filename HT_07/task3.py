# Всі ви знаєте таку функцію як <range>.
# Напишіть свою реалізацію цієї функції. 


def my_range(start, stop=None, step=1):

    if not stop:
        stop = start
        start = 0

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


print(list(my_range(25)))
print(list(my_range(-25)))
print(list(my_range(3, 25, 3)))
print(list(my_range(25, 1, -2)))
print(list(my_range(25, 10)))
