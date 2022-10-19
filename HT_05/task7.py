# Написати функцію, яка приймає на вхід список (через кому), підраховує кількість
# однакових елементів у ньому і виводить результат. Елементами списку можуть бути
# дані будь-яких типів.     Наприклад:
# 1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"



def counter(my_list):
    str_list = list(map(str, my_list))
    result = []
    used_items = []
    for item in my_list:
        if str(item) not in used_items:
            x = str_list.count(str(item))
            result.append((item, x))
            used_items.append(str(item))
        else:
            continue
            
    return result
        


my_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]
print(counter(my_list))





