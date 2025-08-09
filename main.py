from army.units import Pikeman, Archer, Knight
from army.civilization import ChineseArmy, EnglishArmy
from army.enums import *
pikeman = Pikeman(5)
archer = Archer(10)
knight = Knight(20)
print(archer)
print(pikeman)
print(knight)
#archer.train()
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
for i in range(1000):
    ingleses.army_units[UnitType.ARCHER][0].train(ingleses)  
  
print(ingleses.army_units[UnitType.ARCHER][0].strength)
print(ingleses.gold_coins)