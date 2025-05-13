from task_3.rectangle import Rectangle
from task_3.shape import Shape
from task_3.сircle import Circle


class Square(Shape):

    def __init__(self, x, y, side_length):
        self._x = x
        self._y = y
        self.side_length = side_length

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def x(self, y):
        self._y = y

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, side_length):
        if side_length < 0:
            raise ValueError("side_length cannot be negative")
        self._side_length = side_length

    def show(self):
        print(f"The side length is {self._side_length} x coordinate {self._x} y coordinate {self._y}")



