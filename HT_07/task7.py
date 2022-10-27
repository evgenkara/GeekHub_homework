# Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, в якому знаходяться елементи першого списку,
# яких немає в другому. Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному) списку.
# Реалізуйте обчислення за допомогою генератора в один рядок.



def list_diff(first_list, second_list):
    return [item for item in first_list if item not in second_list]


first_list = [1, 2, 3, 4, 5]
second_list = [1, 2, 3]
print(list_diff(first_list, second_list))
