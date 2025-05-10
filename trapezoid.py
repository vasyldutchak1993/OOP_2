from shape import Shape

class Trapezoid(Shape):
    def __init__(self, a, b, height, precision=4):
        self._a = a
        self._b = b
        self._height = height
        self._precision = precision

    def area(self):
        return round(0.5 * (self._a + self._b) * self._height, self._precision)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value < 0:
            raise ValueError("Precision must be a non-negative integer")
        self._precision = value
