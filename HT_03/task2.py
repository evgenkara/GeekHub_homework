# Write a script to remove empty elements from a list.


test_list = [(), ('hey'), (''), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

print(list(filter(len, test_list)))
