from .shape import Shape


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        if self.length == 0 or self.width == 0:
            raise ValueError("Length and width should be greater than 0")
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"{self.name} with length {self.length} and width {self.width}"
