from abc import ABC
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

    def get_all_units(self):
        for units in self.army_units.values():
            for unit in units:
                yield unit

    def attack(self, other: "Army"):
        Battle(self, other)

    def remove_strongest_unit(self):
        self.remove_unit_by_strength(strongest=True)

    def remove_weakest_unit(self):
        self.remove_unit_by_strength(strongest=False)

    def remove_unit_by_strength(self, strongest: bool = True):
        aux_unit: Unit = list(self.get_all_units())[0]
        for _, units in self.army_units.items():
            for unit in units:
                if strongest:
                    if unit.strength > aux_unit.strength:
                        aux_unit = unit
                else:
                    if unit.strength < aux_unit.strength:
                        aux_unit = unit
        self.army_units[aux_unit.unit_type].remove(aux_unit)

    def remove_unit(self, unit: Unit):
        if unit in self.army_units[unit.unit_type]:
            self.army_units[unit.unit_type].remove(unit)

    def add_gold_coins(self, amount: int):
        self.gold_coins += amount

    def remove_gold_coins(self, amount: int) -> bool:
        if amount > self.gold_coins:
            return False
        self.gold_coins -= amount
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

    def add_unit_to_army(self, unit: Unit):
        if unit not in self.get_all_units():
            self.army_units[unit.unit_type].append(unit)

    def get_total_strength(self) -> int:
        return sum(unit.strength for unit in self.get_all_units())


class ChineseArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.CHINESE)
        self.create_units(UnitType.PIKEMAN, 2)
        self.create_units(UnitType.ARCHER, 25)
        self.create_units(UnitType.KNIGHT, 2)


class EnglishArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.ENGLISH)
        self.create_units(UnitType.PIKEMAN, 10)
        self.create_units(UnitType.ARCHER, 10)
        self.create_units(UnitType.KNIGHT, 10)


class ByzantineArmy(Army):

    def __init__(self):
        super().__init__(CivilizationType.BYZANTINE)
        self.create_units(UnitType.PIKEMAN, 5)
        self.create_units(UnitType.ARCHER, 8)
        self.create_units(UnitType.KNIGHT, 15)
