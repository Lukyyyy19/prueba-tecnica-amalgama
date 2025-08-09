from abc import ABC, abstractmethod
from .enums import UnitType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .civilization import Army

class Unit(ABC):
    TRAINING_COST : int
    TRANSFORMATION_COST: int
    def __init__(self, strength: int, unit_type: UnitType, army: "Army", age: int = 18):
        self.age = age
        self.army = army
        self.strength = strength
        self.unit_type = unit_type

    def __str__(self):
        return "{0}: Strength points: {1}, Age: {2}".format(self.unit_type.value, self.strength, self.age)
    
    @abstractmethod
    def train(self):
        return self.army.remove_gold_coins(self.TRAINING_COST)
        pass

class TransformableUnit(Unit):
    
    @abstractmethod
    def transform(self):
        return self.army.remove_gold_coins(self.TRANSFORMATION_COST)
        pass


class Knight(Unit):


    def __init__(self, army: "Army", strength: int = 20, age: int = 18):
        TRAINING_COST: int = 30
        super().__init__(strength, UnitType.KNIGHT, army ,age)
    
    def train(self):
        if not super().train(): 
            return False
        self.strength += 10
        return True
            
class Archer(TransformableUnit):
    
    TRAINING_COST: int = 20
    TRANSFORMATION_COST: int = 40

    def __init__(self, army: "Army", strength: int = 10, age: int = 18):
        super().__init__(strength, UnitType.ARCHER, army ,age)

    def train(self):
        if not super().train(): 
            return False
        self.strength += 7
        return True

    def transform(self) -> Knight:
        if not super().transform(): 
            return None
        knight: Knight = Knight(max(self.strength, 20), self.age)
        self.army.army_units[UnitType.ARCHER].remove(self)
        self.army.army_units[UnitType.KNIGHT].append(knight)
        return knight


    
class Pikeman(TransformableUnit):

    TRAINING_COST: int = 10
    TRANSFORMATION_COST: int = 30
    
    def __init__(self, army: "Army" ,strength: int = 5, age: int = 18):
        super().__init__(strength, UnitType.PIKEMAN, army, age)
    
    def train(self):
        if not super().train(): 
            return False
        self.strength += 3
        return True
    
    def transform(self) -> Archer:
        if not super().train(): 
            return None
        archer = Archer(max(self.strength, 10), self.age)
        self.army.army_units[UnitType.PIKEMAN].remove(self)
        self.army.army_units[UnitType.ARCHER].append(archer)
        return archer


    