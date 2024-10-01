# 1. Swap Two Variables Without Temp Variable
a, b = 5, 10
a, b = b, a
print(f"Swapped values: a={a}, b={b}\n")  # Output: a=10, b=5

# 2. Use zip() to Loop Over Two Lists Simultaneously
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print()  # Output: Alice: 85, Bob: 90, Charlie: 78

# 3. List Comprehensions for Quick List Creation
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}\n")  # Output: [1, 4, 9, 16, ..., 100]

# 4. Get Both Index and Value with enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
print()  # Output: 1: apple, 2: banana, 3: cherry

# 5. Use collections.Counter for Easy Counting
from collections import Counter
letters = "abracadabra"
counter = Counter(letters)
print(f"Letter count: {counter}\n")  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 6. Multiple Return Values from a Function
def get_user_info():
    return "Alice", 25, "Engineer"
name, age, profession = get_user_info()
print(f"Name: {name}, Age: {age}, Profession: {profession}\n")

# 7. Flexible Functions with *args and **kwargs
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
greet("Alice", "Bob", "Charlie")  # Output: Hello Alice! Hello Bob! Hello Charlie!
print()

def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
user_info(name="Alice", age=25, city="New York")
print()

# 8. Using _ for Ignored Variables
for _ in range(3):
    print("Repeat this message!")
print()

# 9. One-Liner if-else (Ternary Operator)
age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}\n")  # Output: Adult

# 10. Using set for Unique Elements and Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Union: {a | b}")  # Output: {1, 2, 3, 4, 5, 6}
print(f"Intersection: {a & b}")  # Output: {3, 4}
print(f"Difference: {a - b}\n")  # Output: {1, 2}

# 11. Using any() and all() for Conditional Checks
numbers = [0, 1, 2, 3]
print(f"Any non-zero: {any(numbers)}")  # Output: True
print(f"All non-zero: {all(numbers)}\n")  # Output: False

# 12. Get the Most Common Elements with Counter
data = "apple banana apple apple orange banana"
counter = Counter(data.split())
print(f"Most common: {counter.most_common(1)}\n")  # Output: [('apple', 3)]

# 13. defaultdict for Handling Missing Keys
from collections import defaultdict
student_grades = defaultdict(lambda: 'N/A')
student_grades['Alice'] = 'A'
print(f"Alice's grade: {student_grades['Alice']}")  # Output: A
print(f"Bob's grade: {student_grades['Bob']}\n")  # Output: N/A

# 14. Concatenate Strings Efficiently
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(f"Sentence: {sentence}\n")  # Output: Python is awesome

# 15. Lambda Functions for Short Anonymous Functions
add = lambda x, y: x + y
print(f"Sum: {add(5, 3)}")  # Output: 8

fruits = ['banana', 'apple', 'cherry']
fruits.sort(key=lambda x: len(x))
print(f"Sorted fruits by length: {fruits}\n")  # Output: ['apple', 'banana', 'cherry']

# 16. Using map() and filter()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")  # Output: [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}\n")  # Output: [2, 4]

# 17. Using itertools for Infinite Iterations and Combinations
import itertools
counter = itertools.count(start=1, step=2)
print("Counting with step of 2:")
for i in range(5):
    print(next(counter))  # Output: 1, 3, 5, 7, 9
print()

# 18. List Slicing with Steps
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Every second number: {numbers[::2]}")  # Output: [0, 2, 4, 6, 8]
print(f"Reversed list: {numbers[::-1]}\n")  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
