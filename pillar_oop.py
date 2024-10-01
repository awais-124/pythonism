from abc import ABC, abstractmethod

# Abstraction
# Abstract base class (similar to abstract classes in C++)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Encapsulation
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width  # Private attribute (similar to private in C++)
        self.__height = height  # Double underscore for name mangling

    # Getter methods
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    # Setter methods
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be positive")

    # Implementation of abstract methods
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

# Inheritance
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Call to parent constructor (similar to Rectangle::Rectangle in C++)

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

# Polymorphism
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Demonstrating the use of these classes
def print_shape_info(shape: Shape):  # Polymorphism through method overriding
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Usage
rectangle = Rectangle(5, 4)
square = Square(5)
circle = Circle(3)

print("Rectangle:")
print_shape_info(rectangle)

print("\nSquare:")
print_shape_info(square)

print("\nCircle:")
print_shape_info(circle)

# Demonstrating encapsulation
print("\nDemonstrating encapsulation:")
print(f"Rectangle width: {rectangle.get_width()}")
rectangle.set_width(6)
print(f"New rectangle width: {rectangle.get_width()}")

# This would raise an AttributeError due to name mangling
# print(rectangle.__width)

# Demonstrating inheritance
print("\nDemonstrating inheritance:")
square.set_side(7)
print(f"Square area: {square.area()}")