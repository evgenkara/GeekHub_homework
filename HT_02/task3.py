# Write a script which accepts a <number> from user and print out
# a sum of the first <number> positive integers.


result = 0
user_input = int(input())


while user_input > 0:
    result += user_input
    user_input -= 1


print(result)
