from abc import ABC, abstractmethod
from enum import Enum

class UnitType(Enum):
    PIKEMAN = "Pikeman"
    ARCHER = "Archer"
    KNIGHT = "Knight"

class Unit(ABC):
    
    def __init__(self, strength: int, unit_type: UnitType, age: int = 18):
        self.age = age
        self.strength = strength
        self.unit_type = unit_type

    def __str__(self):
        return "{0}: Strength points: {1}, Age: {2}".format(self.unit_type.value, self.strength, self.age)

    # def get_age(self) -> int:
    #     return self.age
    
    # def get_strength(self) -> int:
    #     return self.strength
    
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def transform(self):
        pass
    
class Knight(Unit):

    TRAINING_COST: int = 30

    def train(self):
        self.strength += 10
    
    def get_transformation_cost(self):
        return "This unit can't be transformed."
    
    def transform(self):
        return "This unit can't be transformed."
            
class Archer(Unit):
    
    TRAINING_COST: int = 20
    TRANSFORMATION_COST: int = 40

    def train(self):
        self.strength += 7

    def get_transformation_cost(self) -> int:
        return 40
    
    def transform(self) -> Knight:
        return Knight(self.strength if (self.strength > 20) else 20, UnitType.KNIGHT, self.age)

    
class Pikeman(Unit):

    TRAINING_COST: int = 10
    TRANSFORMATION_COST: int = 30

    def get_training_cost(self) -> int:
        return 10
    
    def train(self):
        self.strength += 3

    def get_transformation_cost(self) -> int:
        return 30
    
    def transform(self):
        return Archer(self.strength if (self.strength > 10) else 10, UnitType.ARCHER, self.age)


    