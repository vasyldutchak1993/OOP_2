from abc import ABCMeta

class ShapeMeta(ABCMeta):

    registry = {}

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if name != 'Shape':
            ShapeMeta.registry[new_cls.__name__] = new_cls
        return new_cls