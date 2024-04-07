# Завдання 1
# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі.
# Завдання 2
# Для класів із першого завдання перевизначте магічні
# методи int (повертає площу) та str (повертає інформацію
# про фігуру).

import math

class Shape:
    def area(self):
        pass

    def __int__(self):
        return self.area()

    def __str__(self):
        return "This is a generic shape."

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Rectangle: width = {self.width}, height = {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Circle: radius = {self.radius}"

class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Right Triangle: base = {self.base}, height = {self.height}"

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __int__(self):
        return self.area()

    def __str__(self):
        return f"Trapezoid: base1 = {self.base1}, base2 = {self.base2}, height = {self.height}"

# Приклад використання
rectangle = Rectangle(5, 4)
print(rectangle)
print("Rectangle area:", int(rectangle))

circle = Circle(3)
print(circle)
print("Circle area:", int(circle))

triangle = RightTriangle(4, 3)
print(triangle)
print("Triangle area:", int(triangle))

trapezoid = Trapezoid(3, 6, 4)
print(trapezoid)
print("Trapezoid area:", int(trapezoid))
