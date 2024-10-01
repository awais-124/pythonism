# List functions
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(len(numbers))  # Length
print(max(numbers))  # Maximum value
print(min(numbers))  # Minimum value
print(sum(numbers))  # Sum of all elements
ret=numbers.sort()  # Sort in-place
print(numbers,"Returned : ",type(ret))
numbers.reverse()  # Reverse in-place
print(numbers)

# String functions
text = "Hello, World!"
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.split(','))  # Split string into list
print(' '.join(['Hello', 'World']))  # Join list into string
print(text.strip())  # Remove leading/trailing whitespace
print(text.replace('Hello', 'Hi'))  # Replace substring

# Dictionary functions
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person.keys())  # Get all keys
print(person.values())  # Get all values
print(person.items())  # Get all key-value pairs
person.update({'job': 'Developer'})  # Update dictionary
print(person.pop('age'))  # Remove and return value
print(person.get('salary', 'Not found'))  # Get with default value

# Set functions
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))  # Union of two sets
print(set1.intersection(set2))  # Intersection of two sets
print(set1.difference(set2))  # Difference between two sets
set1.add(6)  # Add an element
set1.remove(1)  # Remove an element
print(set1.issubset(set2))  # Check if set1 is a subset of set2

# Tuple functions (limited as tuples are immutable)
tup = (1, 2, 3, 2, 4, 2)
print(tup.count(2))  # Count occurrences of an element
print(tup.index(3))  # Find index of an element

# Built-in functions for all iterable data structures
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, numbers)))  # Apply function to all elements
print(list(filter(lambda x: x % 2 == 0, numbers)))  # Filter elements
from functools import reduce
print(reduce(lambda x, y: x + y, numbers))  # Reduce list to single value

# Enumerate function
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index: {index}, Value: {value}")

# Zip function
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")