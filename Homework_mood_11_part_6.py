# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур.
# Визначте методи:
# ■ Show() — виведення на екран інформації про фігуру;
# ■ Save() — збереження фігури у файл;
# ■ Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# ■ Square — квадрат із заданими з координатами лівого
# верхнього кута та довжиною сторони.
# ■ Rectangle — прямокутник із заданими координатами
# верхнього лівого кута та розмірами.
# Домашнє завдання
# 1
# ■ Circle — коло із заданими координатами центру та радіусом.
# ■ Ellipse — еліпс із заданими координатами верхнього кута
# описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
# фігуру.
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates:", self.x, self.y)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Coordinates: {self.x}, {self.y}")

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            data = f.read().split(': ')[1].split(', ')
            x, y = map(int, data)
            return cls(x, y)

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def show(self):
        super().show()
        print("Side:", self.side)

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as f:
            f.write(f"\nSide: {self.side}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print("Width:", self.width)
        print("Height:", self.height)

    def save(self, filename):
        super().save(filename)
        with open(filename, 'a') as f:
            f.write(f"\nWidth: {self.width}\nHeight: {self.height}")

square = Square(0, 0, 5)
square.show()
square.save("square.txt")

rectangle = Rectangle(1, 1, 4, 3)
rectangle.show()
rectangle.save("rectangle.txt")

loaded_square = Shape.load("square.txt")
loaded_rectangle = Shape.load("rectangle.txt")

print("\nLoaded square:")
loaded_square.show()

print("\nLoaded rectangle:")
loaded_rectangle.show()

