from dataclasses import dataclass
from abc import ABC,ABCMeta
from .db import DB

class MetaDataClass(ABCMeta):
    def __new__(cls, name, bases, namespace):
        cls_obj = super().__new__(cls, name, bases, namespace)
        return dataclass(cls_obj)

@dataclass
class Model(ABC, metaclass=MetaDataClass):
    def save(self):
        class_type = type(self)
        if class_type in DB.keys():
            DB[class_type].append(self)
        else:
            DB[class_type] = [self]