from shape import Shape

class Right_Triangle(Shape):

    def __init__(self, base_width,height,precision=4):
        self.base_width = base_width
        self.height = height
        self.precision = precision

    def area(self):
        return round(1/2*self._base_width * self._height, self._precision)

    @property
    def base_width(self):
        return self._base_width

    @base_width.setter
    def base_width(self, value):
        self._base_width = value

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
        if not isinstance(other, Right_Triangle):
            raise TypeError("Can only add right triangle to Right Triangle")
        new_base_width = self._base_width+ other._base_width
        new_height = self._height + other._height
        return Right_Triangle(new_base_width, new_height, self.precision)

    def __str__(self):
        return f"Right Triangle with  {str(self._base_width)}  and height {str(self._height)} area is  {str(self.area())}"