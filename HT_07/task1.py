# Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100 не включно),
# кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.



my_list = [item for item in range(100) if item % 5 == 0 and item % 3 != 0]
print(my_list)
