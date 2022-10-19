# Write a script which accepts a <number>(int) from user
# and generates dictionary in range <number> where key is <number>
# and value is <number>*<number>


user_input = int(input('Enter a number: '))
d = {}


for i in range(user_input + 1):
    d[i] = i * i


print(d)
