from task_3.ellipse import Ellipse
from task_3.rectangle import Rectangle
from task_3.shape import Shape
from task_3.square import Square
from task_3.circle import Circle

shapes = [
    Rectangle(110, 20, 50, 100),
    Circle(10, 50, 200),
    Rectangle(310, 420, 50, 100),
    Square(100, 500, 20),
    Ellipse(210, 150, 200,100),
    Circle(105, 50, 200),
    Square(10, 50, 200),
]

for shape in shapes:
    shape.save()

loaded_shapes=Shape.load()

for shape in loaded_shapes:
    shape.show()