# Write a script to remove empty elements from a list.


test_list = [(), ('hey'), (''), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

result = [element for element in test_list if element]

print(result)
