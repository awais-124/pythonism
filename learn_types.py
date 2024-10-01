# 1. NoneType
none_value = None

# 2. Numeric Types
# 2.1 int (integer)
integer = 42

# 2.2 float (floating-point)
float_number = 3.14

# 2.3 complex
complex_number = 1 + 2j

# 3. Sequence Types
# 3.1 list
my_list = [1, 2, 3]

# 3.2 tuple
my_tuple = (1, 2, 3)

# 3.3 range
my_range = range(5)

# 4. Text Sequence Type
# 4.1 str (string)
my_string = "Hello, World!"

# 5. Binary Sequence Types
# 5.1 bytes
my_bytes = b"hello"

# 5.2 bytearray
my_bytearray = bytearray(b"hello")

# 5.3 memoryview
my_memoryview = memoryview(b"hello")

# 6. Set Types
# 6.1 set
my_set = {1, 2, 3}

# 6.2 frozenset (immutable set)
my_frozenset = frozenset([1, 2, 3])

# 7. Mapping Type
# 7.1 dict (dictionary)
my_dict = {"key": "value"}

# 8. Boolean Type
# 8.1 bool
my_bool = True

# 9. Callable Types
# 9.1 function
def my_function():
    pass

# 9.2 method
class MyClass:
    def my_method(self):
        pass

# 9.3 lambda
my_lambda = lambda x: x * 2

# 10. Module Type
import math
# math is a module

# 11. Class and Instance Types
class MyClass:
    pass

my_instance = MyClass()
# MyClass is a type, my_instance is an instance

# 12. File Type
with open("example.txt", "w") as f:
    # f is a file object
    pass

# 13. Ellipsis Type
my_ellipsis = ...

# 14. Slice Type
my_slice = slice(1, 5, 2)

# Checking types
print(type(none_value))    # <class 'NoneType'>
print(type(integer))       # <class 'int'>
print(type(float_number))  # <class 'float'>
print(type(my_list))       # <class 'list'>
print(type(my_dict))       # <class 'dict'>
print(type(my_function))   # <class 'function'>
print(type(MyClass))       # <class 'type'>
print(type(my_instance))   # <class 'MyClass'>
print(type(my_ellipsis))   # <class 'ellipsis'>
print(type(my_slice))      # <class 'slice'>