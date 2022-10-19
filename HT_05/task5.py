# Написати функцію <fibonacci>, яка приймає один аргумент
# і виводить всі числа Фібоначчі, що не перевищують його.


def fibonacci(number):
    result = [0, 1, 1]
    if number == 0:
        return [0]
    elif number == 1:
        return result
    else:
        while result[-1] < number:
            new_item = result[-1] + result[-2]
            if new_item < number:
                result.append(new_item)
            else:
                return result


print(fibonacci(500))
        
