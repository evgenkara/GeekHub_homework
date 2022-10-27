# Напишіть функцію,яка приймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора в один рядок.



def shortest_word(some_string):
    result = min([item for item in list(map(len, some_string.split(' ')))])
    return result


print(shortest_word('hello my dear friend'))
