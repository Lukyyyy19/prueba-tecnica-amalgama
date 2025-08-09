from abc import ABC, abstractmethod
from .units import Unit, Pikeman, Archer, Knight
from .enums import CivilizationType, UnitType


class Army(ABC):
    
    def __init__(self, civilization_type: CivilizationType):
        self.gold_coins = 1000
        self.civilization_type = civilization_type
        self.battle_history: list["BattleInfo"] = []
        self.army_units: dict[UnitType, list[Unit]] = {
            UnitType.PIKEMAN: [],
            UnitType.ARCHER: [],
            UnitType.KNIGHT: []
        }

    def attack(self, other: 'Army'):
        from .battle import Battle
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

class ChineseArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.CHINESE)
        self.army_units[UnitType.PIKEMAN] += [Pikeman() for _ in range(2)]
        self.army_units[UnitType.ARCHER] += [Archer() for _ in range(25)]
        self.army_units[UnitType.KNIGHT] += [Knight() for _ in range(2)]

class EnglishArmy(Army):
    
    def __init__(self):
        super().__init__(CivilizationType.ENGLISH)
        self.army_units[UnitType.PIKEMAN] += [Pikeman() for _ in range(10)]
        self.army_units[UnitType.ARCHER] += [Archer() for _ in range(10)]
        self.army_units[UnitType.KNIGHT] += [Knight() for _ in range(10)]

class ByzantineArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.BYZANTINE)
        self.army_units[UnitType.PIKEMAN] += [Pikeman() for _ in range(5)]
        self.army_units[UnitType.ARCHER] += [Archer() for _ in range(8)]
        self.army_units[UnitType.KNIGHT] += [Knight() for _ in range(15)]
