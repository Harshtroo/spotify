from enum import Enum


class Role(Enum):
    licenar = "Licenar"
    singer = "Singer"

    @classmethod
    def choices(cls):
        return tuple((role.name, role.value) for role in cls)
