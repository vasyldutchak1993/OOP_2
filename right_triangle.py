from shape import Shape

class Right_Triangle(Shape):

    def __init__(self, base_width,height,precision=4):
        self._base_width = base_width
        self._height = height
        self._precision = precision

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
