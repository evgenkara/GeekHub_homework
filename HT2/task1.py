# Write a script which accepts a sequence of comma-separated numbers
# from user and generates a list and a tuple with those numbers.


user_input = input()
list_of_numbers = user_input.split(',')
tuple_of_numbers = tuple(list_of_numbers)
print(list_of_numbers, tuple_of_numbers)
