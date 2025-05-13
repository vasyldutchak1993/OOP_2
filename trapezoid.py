from shape import Shape

class Trapezoid(Shape):
    def __init__(self, a, b, height, precision=4):
        self.a = a
        self.b = b
        self.height = height
        self.precision = precision

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

    def __float__(self):
        return self.area()

    def __int__(self):
        return int(self.area())

    def __add__(self, other):
        if not isinstance(other, Trapezoid):
            raise TypeError("Can only add trapezoid to Trapezoid")
        new_a = self._a+ other._a
        new_b = self._b + other._b
        new_height = self._height + other._height
        return Trapezoid(new_a,new_b,new_height, self.precision)

    def __str__(self):
        return f"Trapezoid with a side  {str(self._a)} b side {str(self._b)}  and height {str(self._height)} area is  {str(self.area())}"