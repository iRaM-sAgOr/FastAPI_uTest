from .shape import Shape


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"{self.name} with side {self.side}"
