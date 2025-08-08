from abc import ABC, abstractmethod
from .enums import UnitType

class Unit(ABC):
    
    def __init__(self, strength: int, unit_type: UnitType, age: int = 18):
        self.age = age
        self.strength = strength
        self.unit_type = unit_type

    def __str__(self):
        return "{0}: Strength points: {1}, Age: {2}".format(self.unit_type.value, self.strength, self.age)
    
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def transform(self):
        pass
    
class Knight(Unit):

    TRAINING_COST: int = 30

    def __init__(self, strength: int = 20, age: int = 18):
        super().__init__(strength, UnitType.KNIGHT, age)
    
    def train(self):
        self.strength += 10
    
    def transform(self):
        raise NotImplementedError("Knight cannot be transformed")
            
class Archer(Unit):
    
    TRAINING_COST: int = 20
    TRANSFORMATION_COST: int = 40

    def __init__(self, strength: int = 10, age: int = 18):
        super().__init__(strength, UnitType.ARCHER, age)

    def train(self):
        self.strength += 7

    def transform(self) -> Knight:
        return Knight(max(self.strength, 20), self.age)

    
class Pikeman(Unit):

    TRAINING_COST: int = 10
    TRANSFORMATION_COST: int = 30
    
    def __init__(self, strength: int = 5, age: int = 18):
        super().__init__(strength, UnitType.PIKEMAN, age)
    
    def train(self):
        self.strength += 3
    
    def transform(self):
        return Archer(max(self.strength, 10), self.age)


    