# Write a script to concatenate all elements in a list into a string and print it.
# List must include both strings and integers and must be hardcoded.


l = ['a', 2, 'd', 3, 'www']
l2 = list(map(str, l))
print(''.join(l2))
