from abc import ABC, abstractmethod
import json

from task_3.shape_meta import ShapeMeta


class Shape(ABC,metaclass=ShapeMeta):

    db_filename="shapes.txt"

    @abstractmethod
    def show(self):
        pass


    def save(self,filename=db_filename):
        shape_data = self.__dict__
        shape_data['type'] = self.__class__.__name__
        normalized_shape_data = {key.lstrip('_'): value for key, value in shape_data.items()}
        with open(filename, 'a', encoding='utf-8') as file:
            json.dump(normalized_shape_data, file)
            file.write("\n")

    @classmethod
    def load(cls,filename=db_filename):
        shapes = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                shape_data = json.loads(line.strip())
                shape_type = shape_data.pop('type')

                shape_class = ShapeMeta.registry.get(shape_type)
                if shape_class:
                    shapes.append(shape_class(**shape_data))
        return shapes