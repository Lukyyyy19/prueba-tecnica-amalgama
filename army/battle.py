from .civilization import Army
from dataclasses import dataclass

class Battle:
    
    winner: Army = None
    loser: Army = None

    GOLD_COINS_REWARD = 100
    LOSER_UNITS_REMOVED = 2

    def __init__(self, attacker: Army, defender: Army):
        self.attacker = attacker
        self.defender = defender
        self.resolve_battle()

    def calculate_points(self, army: Army) -> int:
        points: int = 0
        for unit in army.army_units.values():
            points += sum(u.strength for u in unit)
        return points

    def resolve_battle(self):
        attacker_points: int = 0
        defender_points: int = 0

        attacker_points = self.calculate_points(self.attacker)
        defender_points = self.calculate_points(self.defender)

        if attacker_points > defender_points:
            self.winner = self.attacker
            self.loser = self.defender
        elif attacker_points < defender_points:
            self.winner = self.defender
            self.loser = self.attacker
        else:
            self.attacker.remove_weakest_unit()
            self.defender.remove_weakest_unit()
            return

        for _ in range(self.LOSER_UNITS_REMOVED):
            self.loser.remove_strongest_unit()
        self.winner.add_gold_coins(self.GOLD_COINS_REWARD)
        battle_info = BattleInfo(self.attacker, self.defender, attacker_points, defender_points, self.winner)
        self.attacker.add_battle_info(battle_info)
        self.loser.add_battle_info(battle_info)

@dataclass
class BattleInfo:
    attacker: Army
    defender: Army
    attacker_points: int
    defender_points: int
    winner: Army
    