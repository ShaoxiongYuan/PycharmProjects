from math import pi


class ShapeManager:
    def __init__(self):
        self.__list_shapes = []

    def add_shapes(self, shape):
        self.__list_shapes.append(shape)

    def get_area(self):
        result = 0
        for i in self.__list_shapes:
            result += i.calculate()
        return result


class Shape:
    def calculate(self):
        pass


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def calculate(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width


s1 = ShapeManager()
s1.add_shapes(Circle(5))
s1.add_shapes(Rectangle(5, 3))
print(s1.get_area())
