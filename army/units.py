from abc import ABC, abstractmethod
from .enums import UnitType

class Unit(ABC):
    TRAINING_COST : int
    def __init__(self, strength: int, unit_type: UnitType, age: int = 18):
        self.age = age
        self.strength = strength
        self.unit_type = unit_type

    def __str__(self):
        return "{0}: Strength points: {1}, Age: {2}".format(self.unit_type.value, self.strength, self.age)
    
    @abstractmethod
    def train(self, army: "Army"):
        return army.remove_gold_coins(self.TRAINING_COST)
        pass

    @abstractmethod
    def transform(self, army: "Army"):
        return army.remove_gold_coins(self.TRAINING_COST)
        pass
    
class Knight(Unit):


    def __init__(self, strength: int = 20, age: int = 18):
        TRAINING_COST: int = 30
        super().__init__(strength, UnitType.KNIGHT, age)
    
    def train(self, army: "Army"):
        if not super().train(army): 
            return False
        self.strength += 10
        return True
    
    def transform(self):
        raise NotImplementedError("Knight cannot be transformed")
            
class Archer(Unit):
    
    TRAINING_COST: int = 20
    TRANSFORMATION_COST: int = 40

    def __init__(self, strength: int = 10, age: int = 18):
        super().__init__(strength, UnitType.ARCHER, age)

    def train(self, army: "Army"):
        if not super().train(army): 
            return False
        self.strength += 7
        return True

    def transform(self, army: "Army") -> Knight:
        if not super().train(army): 
            return None
        return Knight(max(self.strength, 20), self.age)

    
class Pikeman(Unit):

    TRAINING_COST: int = 10
    TRANSFORMATION_COST: int = 30
    
    def __init__(self, strength: int = 5, age: int = 18):
        super().__init__(strength, UnitType.PIKEMAN, age)
    
    def train(self, army: "Army"):
        if not super().train(army): 
            return False
        self.strength += 3
        return True
    
    def transform(self, army: "Army") -> Archer:
        if not super().train(army): 
            return None
        return Archer(max(self.strength, 10), self.age)


    