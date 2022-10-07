# Write a script which accepts a <number> from user
# and then <number> times asks user for string input.
# At the end script must print out result of concatenating all <number> strings.


num = int(input())
s = ''
for i in range(num):
    s += input()

print(s)
