# Write a script to check whether a value
# from user input is contained in a group of values.

group_of_values = [1, 2, 'u', 'a', 4, True]
user_value = input()
l = list(map(str, group_of_values))

if user_value in l:
    print('True')
else:
    print('False')
