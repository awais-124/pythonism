# Lists
my_list = [1, 2, 3, 'four', 5.0]
my_list.append(6)  # Add an element
my_list[0] = 'one'  # Modify an element
print(my_list[2])  # Access an element
print(my_list[1:4])  # Slicing [start(inclusive) : end(exclusive) : gap]

# Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['job'] = 'Developer'  # Add a key-value pair
print(my_dict['name'])  # Access a value
print(my_dict.get('name', 'Not found'))  # Get with default value, if not found, will give second parameter
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values

# Tuples (immutable)
my_tuple = (1, 2, 3, 'four', 5.0)
print(my_tuple[0])  # Access an element
# my_tuple[0] = 'one'  # This would raise an error

# Sets
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # Add an element
my_set.remove(3)  # Remove an element
print(2 in my_set)  # Check membership

# List comprehension
squares = [x**2 for x in range(10)]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}