from .civilization import Army

class Battle:
    
    winner: Army = None
    loser: Army = None

    GOLD_COINS_REWARD = 100
    LOSER_UNITS_REMOVED = 2

    def __init__(self, attacker: Army, defender: Army):
        self.attacker = attacker
        self.defender = defender
        self.resolve_battle()

    def resolve_battle(self):
        attacker_points: int = 0
        defender_points: int = 0

        for unit in self.attacker.army_units.values():
            attacker_points += sum(u.strength for u in unit)

        for unit in self.defender.army_units.values():
            defender_points += sum(u.strength for u in unit)

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
