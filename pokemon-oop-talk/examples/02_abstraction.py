"""Pillar 2: Abstraction. Hide the complexity behind a simple interface."""


class Pokemon:
    strong_against = set()
    weak_against = set()
    type_name = "Normal"

    def __init__(self, name, max_hp):
        self.name = name
        self._hp = max_hp

    @property
    def hp(self):
        return self._hp

    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)

    # The simple public interface...
    def attack(self, target):
        damage = self._calculate_damage(target)
        target.take_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage}!")

    # ...hides the complexity underneath.
    def _calculate_damage(self, target):
        return int(10 * self._type_multiplier(target))

    def _type_multiplier(self, target):
        if target.type_name in self.strong_against:
            return 2.0
        if target.type_name in self.weak_against:
            return 0.5
        return 1.0


class FireType(Pokemon):
    type_name = "Fire"
    strong_against = {"Grass"}
    weak_against = {"Water"}


class WaterType(Pokemon):
    type_name = "Water"
    strong_against = {"Fire"}
    weak_against = {"Grass"}


charmander = FireType("Charmander", 39)
squirtle = WaterType("Squirtle", 44)

# BEFORE abstraction, the trainer would do all this by hand:
damage = 10
if squirtle.type_name in charmander.weak_against:
    damage *= 0.5
squirtle.take_damage(int(damage))

# AFTER abstraction, the trainer just asks:
charmander.attack(squirtle)
