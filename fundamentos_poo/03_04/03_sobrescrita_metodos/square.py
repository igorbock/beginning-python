# TODO: Import Shape class from shape.py
# Use format: from shape import Shape

from shape import Shape

class Square(Shape):
    def __init__(self, color, side_length):
        # TODO: Call parent constructor with color using super()
        # TODO: Store side_length as instance attribute (self.side_length)
        super().__init__(color)
        self.side_length = side_length
    
    def area(self):
        # TODO: Return square area using side_length ** 2
        # TODO: Formula: self.side_length ** 2
        return self.side_length ** 2
    
    def describe(self):
        # TODO: Print a description of the square
        # TODO: Format should be exactly: "This is a {self.color} square with side length {self.side_length}."
        print(f"This is a {self.color} square with side length {self.side_length}.")