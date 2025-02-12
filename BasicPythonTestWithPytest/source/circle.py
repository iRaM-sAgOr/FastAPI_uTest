from .shape import Shape


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        if self.radius <= 0:
            raise ValueError("Radius should be greater than 0")
        return 3.14159 * self.radius**2

    def perimeter(self):
        if self.radius <= 0:
            raise ValueError("Radius should be greater than 0")
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"{self.name} with radius {self.radius}"
