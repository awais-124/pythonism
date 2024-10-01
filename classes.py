class Person:
    def __init__(self, name, age):  #constructor
        self.name = name
        self.age = age
    
    def greet(self):    
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

    @property   
    def birth_year(self):
        return 2024 - self.age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating an instance
person = Person("Alice", 30)
print(person.greet())
print(person.birth_year)

# Using class method
person2 = Person.from_birth_year("Bob", 1990)
print(person2.age)

# Using static method
print(Person.is_adult(20))

# Inheritance
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    
    def greet(self):
        return f"{super().greet()} My employee ID is {self.employee_id}."

employee = Employee("Charlie", 25, "E12345")
print(employee.greet())