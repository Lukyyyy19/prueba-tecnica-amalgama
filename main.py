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
#new_knight = archer.transform()
#print(new_knight)

chinos = ChineseArmy()
ingleses = EnglishArmy()

for t, u in chinos.army_units.items():
    print(f"Type: {t.value}")
    for unit in u:
        print(unit)

ingleses.attack(chinos)
# for i in range(1000):
#     ingleses.army_units[UnitType.ARCHER][0].train(ingleses)  
print(ingleses.gold_coins)
ingleses.army_units[UnitType.ARCHER][0].train()
#ingleses.army_units[UnitType.ARCHER][0].transform()
#ingleses.army_units[UnitType.PIKEMAN][0].transform()
print(ingleses.army_units[UnitType.ARCHER][0].strength)
chinos.attack(ingleses)
chinos.remove_strongest_unit()
chinos.remove_weakest_unit()
print(ingleses.gold_coins)
