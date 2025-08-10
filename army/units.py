from abc import ABC
from .enums import UnitType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .civilization import Army


class Unit(ABC):

    TRAINING_COST: int
    TRAINING_STRENGTH: int

    def __init__(self, strength: int, unit_type: UnitType, army: "Army", age: int = 18):
        self.age = age
        self.army = army
        self.strength = strength
        self.unit_type = unit_type

    def __str__(self):
        return "{0}: Strength points: {1}, Age: {2}".format(self.unit_type.value, self.strength, self.age)

    def train(self):
        return self.army.remove_gold_coins(self.TRAINING_COST)


class TransformableUnit(Unit):

    TRANSFORMATION_COST: int

    def transform(self):
        return self.army.remove_gold_coins(self.TRANSFORMATION_COST)


class Knight(Unit):

    TRAINING_COST = 30
    TRAINING_STRENGTH = 10

    def __init__(self, army: "Army", strength: int = 20, age: int = 18):
        super().__init__(strength, UnitType.KNIGHT, army, age)

    def train(self):
        if not super().train():
            return False
        self.strength += self.TRAINING_STRENGTH
        return True


class Archer(TransformableUnit):

    TRAINING_COST = 20
    TRANSFORMATION_COST = 40
    TRAINING_STRENGTH = 7

    def __init__(self, army: "Army", strength: int = 10, age: int = 18):
        super().__init__(strength, UnitType.ARCHER, army, age)

    def train(self):
        if not super().train():
            return False
        self.strength += self.TRAINING_STRENGTH
        return True

    def transform(self) -> Knight:
        if not super().transform():
            return None
        knight: Knight = Knight(self.army, max(self.strength, 20), self.age)
        self.army.remove_unit(self)
        self.army.add_unit_to_army(knight)
        return knight


class Pikeman(TransformableUnit):

    TRAINING_COST = 10
    TRANSFORMATION_COST = 30
    TRAINING_STRENGTH = 3

    def __init__(self, army: "Army", strength: int = 5, age: int = 18):
        super().__init__(strength, UnitType.PIKEMAN, army, age)

    def train(self):
        if not super().train():
            return False
        self.strength += self.TRAINING_STRENGTH
        return True

    def transform(self) -> Archer:
        if not super().transform():
            return None
        archer = Archer(self.army, max(self.strength, 10), self.age)
        self.army.remove_unit(self)
        self.army.add_unit_to_army(archer)
        return archer
