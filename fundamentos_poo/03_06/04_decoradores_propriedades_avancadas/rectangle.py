class Rectangle:
    def __init__(self, width, height):
        # NOTE: Set initial values to 0 before using the property setters
        self._width = 0
        self._height = 0

        # Use property setters to set width and height (for validation)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def dimensions(self):
        return (self.width, self.height)

    @dimensions.setter
    def dimensions(self, dimensions):
        width, height = dimensions
        self.width = width
        self.height = height

    @dimensions.deleter
    def dimensions(self):
        self.width = 1
        self.height = 1