# Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр, 
# які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих). 
# Реалізуйте обчислення за допомогою генератора в один рядок



def uniq_char_count(some_string):
    chars = {item for item in some_string if some_string.lower().count(item) > 1}
    return f'{some_string} -> {len(chars)}'


print(uniq_char_count('dDfghjk'))
print(uniq_char_count('dsfsdrdDtryfjkgk'))
print(uniq_char_count('bvgv5fd74igfhj45dy5'))
print(uniq_char_count('wfekfnnjefnn778fi'))
