from army.units import Pikeman, Archer, Knight
from army.civilization import ChineseArmy, EnglishArmy

pikeman = Pikeman(5)
archer = Archer(10)
knight = Knight(20)
print(archer)
print(pikeman)
print(knight)
archer.train()
print(archer)
new_knight = archer.transform()
print(new_knight)

chinos = ChineseArmy()
ingleses = EnglishArmy()

for t, u in chinos.army_units.items():
    print(f"Type: {t.value}")
    for unit in u:
        print(unit)

ingleses.attack(chinos)

print(ingleses.battle_history[0].winner.civilization_type)