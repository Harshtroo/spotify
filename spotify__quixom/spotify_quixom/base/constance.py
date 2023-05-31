from enum import Enum


class Role(Enum):
    licenar = "licenar"
    singer = "singer"

    @classmethod
    def choices(cls):
        return tuple((role.name, role.value) for role in cls)
