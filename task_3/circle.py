from task_3.shape import Shape


class Circle(Shape):

    def __init__(self, x, y, radius):
        self._x = x
        self._y= y
        self.radius = radius

    def show(self):
        print(f"Circle x {self._x} y {self._y} radius {self._radius}")

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
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value