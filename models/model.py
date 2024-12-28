from dataclasses import dataclass, InitVar,field
from abc import ABC,ABCMeta
from .db import DB

class MetaDataClass(ABCMeta):
    def __new__(cls, name, bases, namespace):
        cls_obj = super().__new__(cls, name, bases, namespace)
        return dataclass(cls_obj,kw_only=True)

@dataclass
class Model(ABC, metaclass=MetaDataClass):
    id: int = field(repr=False,default=0)

    def save(self):
        class_type = type(self)
        if class_type in DB.keys():
            self.id = DB[class_type][-1].id + 1
            DB[class_type].append(self)
        else:
            self.id = 1
            DB[class_type] = [self]