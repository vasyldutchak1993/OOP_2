from task_3.shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle top x coord {self._x},top y coord {self._y},width {self._width},height {self._height}")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be positive")
        self._height = value