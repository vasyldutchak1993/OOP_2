from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def __float__(self):
        return self.area()

    def __int__(self):
        return int(self.area())

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Can only add rectangle to Rectangle")
        new_width = self._width + other._width
        new_height = self._height + other._height
        return Rectangle(new_width,new_height, self.precision)

    def __str__(self):
        return f"Rectangle with  {str(self._width)}  and height {str(self._height)} area is  {str(self.area())}"