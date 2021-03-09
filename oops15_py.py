# abstract base class, forces the rectangle class to have a method print_area
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 2
# commenting out the below function will throw error as the function is mandatory as per abstract class

    def print_area(self):
        return self.length * self.breadth


r = Rectangle()
print(r.print_area())
