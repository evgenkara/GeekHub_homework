# Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж)
# і повертає генератор, який буде повертати значення з цієї послідовності, при цьому, якщо було повернено
# останній елемент із послідовності - ітерація починається знову.



def my_generator(iterable):

    while True:
        for item in iterable:
            yield item


l = 'qwertyuiooppljhggfdsaAVXNM'
for item in my_generator(l):
    print(item)
