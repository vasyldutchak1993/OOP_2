import math

from shape import Shape


class Circle(Shape):

    def __init__(self, radius, precision=4):
        self._radius = radius
        self._precision = precision

    def area(self):
        return round(math.pi * self._radius * self._radius,self.precision)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value < 0:
            raise ValueError("Precision must be a non-negative integer")
        self._precision = value

    def __float__(self):
        return self._radius

    def __int__(self):
        return int(self._radius)

    def __add__(self,other):
        if not isinstance(other,Circle):
            raise TypeError("Can only add circles to circles")
        return Circle(self._radius + other._radius,self.precision)

    def __str__(self):
        return f"Circle with radius {str(self._radius)}  and square is  {str(self.area())}"


