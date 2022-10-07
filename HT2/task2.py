# Write a script which accepts two sequences of comma-separated colors from user.
# Then print out a set containing all the colors from color_list_1
# which are not present in color_list_2.

# red, blue, yellow
# green, black, red, blue


color_list_1 = set(input().replace(' ', '').split(','))
color_list_2 = set(input().replace(' ', '').split(','))

result = color_list_1.difference(color_list_2)

print(result)
