from army.units import Pikeman, Archer, Knight, UnitType

pikeman = Pikeman(5, UnitType.PIKEMAN)
archer = Archer(10, UnitType.ARCHER)
knight = Knight(20, UnitType.KNIGHT)
print(archer)
print(pikeman)
print(knight)
archer.train()
print(archer)
new_knight = archer.transform()
print(new_knight)