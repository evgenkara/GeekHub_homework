# Write a script to remove values duplicates from dictionary.


my_dict = {'foo': 'bar', 'one': 'two', 'three': 'bar'}
new_dict = {}

for key, value in my_dict.items():
    if value not in new_dict.values():
        new_dict[key]  = value
print(new_dict)


