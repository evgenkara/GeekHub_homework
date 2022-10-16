# Створіть ф-цiю, яка буде отримувати довільні рядки та обробляє наступні випадки:
# -  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
# -  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)


def make_a_magic(some_chars):
    if len(some_chars) < 30:
        summa = 0
        output_string = ''
        for char in some_chars:
            if char.isdigit():
                summa += int(char)
            elif char.isalpha():
                output_string += char
            else:
                continue
        return f'Сума числових символів: {summa}\nА тут лише букви: {output_string}' 
    elif len(some_chars) > 50:
        return make_a_magic(some_chars[10:50])
    else:
        digit_count = 0
        letter_count = 0
        for char in some_chars:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():
                letter_count += 1
        return f'Довжина рядка: {len(some_chars)}\nУ рядку {digit_count} цифр та {letter_count} літер'


some_chars = input('Введіть рядок: ')
print(make_a_magic(some_chars))



            
