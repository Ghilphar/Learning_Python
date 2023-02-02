import math

class Shape:
    """This is a Shape"""
    def area(self):
        return "Area of the Shape"

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * math.pow(self.r, 2)

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.length * self.width

shape = Shape()
circle = Circle(2)
rectangle = Rectangle(2, 4)

print(shape.area())
print(circle.area())
print(rectangle.area())