# Завдання 1
# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі.
import math

class Shape:
    def area(self):
        return f"{self.__dict__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(5, 4)
print("Rectangle area:", rectangle.area())

circle = Circle(3)
print("Circle area:", circle.area())

triangle = RightTriangle(4, 3)
print("Triangle area:", triangle.area())

trapezoid = Trapezoid(3, 6, 4)
print("Trapezoid area:", trapezoid.area())
