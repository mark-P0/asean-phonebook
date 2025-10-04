from enum import Enum


class EnumValues(Enum):
    @classmethod
    def values(cls):
        return [item.value for item in cls]
