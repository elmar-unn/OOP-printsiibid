from shape import Shape

class Square(Shape):
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def area(self):
        return self._size * self._size

    def __str__(self):
        return f"Size: {self._size}"