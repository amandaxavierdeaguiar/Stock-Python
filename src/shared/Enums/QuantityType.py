from enum import Enum


class QuantityType(Enum):
    weight = "weight"
    unit = "unit"

    @classmethod
    def return_types(cls):
        return [f"{cls.weight.value}", f"{cls.unit.value}"]
