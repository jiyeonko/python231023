# Lists
my_list = [1, 2, 3, 4, 5]
print("List:")
print("Elements:", my_list)
print("Length:", len(my_list))
print("Access Element 0:", my_list[0])
print("Slicing [1:3]:", my_list[1:3])
print("Append 6:", my_list + [6])
print()

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:")
print("Elements:", my_tuple)
print("Length:", len(my_tuple))
print("Access Element 0:", my_tuple[0])
print("Slicing [1:3]:", my_tuple[1:3])
print()

# Sets
my_set = {1, 2, 3, 4, 5}
print("Set:")
print("Elements:", my_set)
print("Cardinality:", len(my_set))
my_set.add(6)
print("Add 6:", my_set)
print("Union with {5, 6, 7}:", my_set.union({5, 6, 7}))
print()

# Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Dictionary:")
print("Elements:", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Get 'name':", my_dict.get('name'))
print("Add 'country': 'USA'", my_dict.update({'country': 'USA'}))
print("Updated Dictionary:", my_dict)

