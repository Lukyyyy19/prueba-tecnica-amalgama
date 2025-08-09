from abc import ABC, abstractmethod
from .units import Unit, Pikeman, Archer, Knight
from .enums import CivilizationType, UnitType
from .battle import Battle, BattleInfo

class Army(ABC):
    
    def __init__(self, civilization_type: CivilizationType):
        self.gold_coins = 1000
        self.civilization_type = civilization_type
        self.battle_history: list[BattleInfo] = []
        self.army_units: dict[UnitType, list[Unit]] = {
            UnitType.PIKEMAN: [],
            UnitType.ARCHER: [],
            UnitType.KNIGHT: []
        }

    def attack(self, other: "Army"):
        battle: Battle = Battle(self, other)

    def remove_strongest_unit(self):
        strongest_unit: Unit = self.army_units[UnitType.PIKEMAN][0]
        for unit_type, units in self.army_units.items():
            for unit in units:
                if unit.strength > strongest_unit.strength:
                    strongest_unit = unit
        self.army_units[strongest_unit.unit_type].remove(strongest_unit)

    def remove_weakest_unit(self):
        weakest_unit: Unit = self.army_units[UnitType.PIKEMAN][0]
        for unit_type, units in self.army_units.items():
            for unit in units:
                if unit.strength < weakest_unit.strength:
                    weakest_unit = unit
        self.army_units[weakest_unit.unit_type].remove(weakest_unit)

    def add_gold_coins(self, amount: int):
        self.gold_coins += amount
    
    def remove_gold_coins(self, amount: int)->bool:
        if(amount>self.gold_coins):
            return False
        self.gold_coins-=amount
        return True
    
    def add_battle_info(self, battle_info):
        self.battle_history.append(battle_info)

    def create_units(self, unit_type: UnitType, quantity: int):
        match unit_type:
            case UnitType.PIKEMAN:
                self.army_units[UnitType.PIKEMAN] += [Pikeman(self) for _ in range(quantity)]
            case UnitType.ARCHER:
                self.army_units[UnitType.ARCHER] += [Archer(self) for _ in range(quantity)]
            case UnitType.KNIGHT:
                self.army_units[UnitType.KNIGHT] += [Knight(self) for _ in range(quantity)]



class ChineseArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.CHINESE)
        self.create_units(UnitType.PIKEMAN,2)
        self.create_units(UnitType.ARCHER,25)
        self.create_units(UnitType.KNIGHT,2)

class EnglishArmy(Army):
    
    def __init__(self):
        super().__init__(CivilizationType.ENGLISH)
        self.create_units(UnitType.PIKEMAN,10)
        self.create_units(UnitType.ARCHER,10)
        self.create_units(UnitType.KNIGHT,10)

class ByzantineArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.BYZANTINE)
        self.create_units(UnitType.PIKEMAN,5)
        self.create_units(UnitType.ARCHER,8)
        self.create_units(UnitType.KNIGHT,15)