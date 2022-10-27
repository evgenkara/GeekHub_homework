# Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр, 
# які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих). 
# Реалізуйте обчислення за допомогою генератора в один рядок



def uniq_char_count(some_string):
    chars = set([item for item in some_string.lower() if some_string.lower().count(item) > 1])
    return f'{some_string} -> {len(chars)}'


print(uniq_char_count('DDa'))
print(uniq_char_count('AAbbcdef'))
print(uniq_char_count('aabbCcdefghij'))
print(uniq_char_count('aabbccdDefgh'))
