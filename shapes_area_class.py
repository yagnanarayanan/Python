import math


class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def calc_area(self):
        raise NotImplementedError('Area Calculator is not implemented!')


class Circle(Shape):
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.__r = r

    def get_radius(self):
        return self.__r

    def calc_area(self):
        return math.pi * (self.__r ** 2)


class Square(Shape):
    def __init__(self, x, y, s):
        Shape.__init__(self, x, y)
        self.__s = s

    def get_side(self):
        return self.__s

    def calc_area(self):
        return self.__s ** 2


radius = int(input('Enter any radius for a circle: '))
side = int(input('Enter any side length for a square: '))
circle = Circle(0, 0, radius)
print(f"Area of circle with radius {circle.get_radius()} is {circle.calc_area()} sq. units")
square = Square(0, 0, side)
print(f"Area of square with side {square.get_side()} is {square.calc_area()} sq. units")
if circle.calc_area() == square.calc_area():
    print('The area of the circle and square are the same.')
elif circle.calc_area() > square.calc_area():
    print(f"The circle's area is greater than the square's area by {circle.calc_area() - square.calc_area()} sq. units")
else:
    print(f"The square's area is greater than the circle's area by {square.calc_area() - circle.calc_area()} sq. units")
