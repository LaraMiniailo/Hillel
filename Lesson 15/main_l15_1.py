# HW 15.1. Клас "Прямокутник"

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        total_square = self.get_square() + other.get_square()
        return Rectangle(1, total_square)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        if n <= 0:
            raise ValueError("Множник має бути додатнім")

        new_square = self.get_square() * n
        return Rectangle(1, new_square)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height}), square={self.get_square()}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print(r1)
print(r2)

r3 = r1 + r2
print(r3)

r4 = r1 * 4
print(r4)

