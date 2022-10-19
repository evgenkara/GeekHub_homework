# Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
# та яка буде повертати пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь).
# У випадку некоректного введеного значення - виводити відповідне повідомлення.


def season(month):
    '''Функція приймає номер місяця та повертає пору року'''
    if month in (1, 2, 12):
        return 'Winter'
    elif month in (3, 4, 5):
        return 'Spring'
    elif month in (6, 7, 8):
        return 'Summer'
    elif month in (9, 10, 11):
        return 'Autumn'
    else:
        return 'Incorrect value'


print(season(3))
