from task_3.shape import Shape


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self.width = width
        self.height = height

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
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be positive")
        self._height = value

    def show(self):
        print(f"Ellipse: x {self._x},y {self._y},width {self.width},height {self.height}")

