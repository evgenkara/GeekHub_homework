# Write a script that will run through a list of tuples
# and replace the last value for each tuple.
# The list of tuples can be hardcoded.
# The "replacement" value is entered by user.
# The number of elements in the tuples must be different.

list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), ()]
user_input = int(input('Enter value: '))
for i in range(len(list_of_tuples)):
    if not list_of_tuples[i]:
        continue
    t = list(list_of_tuples[i])
    t[-1] = user_input
    list_of_tuples[i] = tuple(t)

print(list_of_tuples)

    
