class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def __str__(self):
        return self.name
