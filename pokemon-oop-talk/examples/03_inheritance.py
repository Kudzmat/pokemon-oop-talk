"""Pillar 3: Inheritance. Write shared code once, specialize in the children."""


class Pokemon:
    type_name = "Normal"
    strong_against = set()
    weak_against = set()

    def __init__(self, name, max_hp):
        self.name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def hp(self):
        return self._hp

    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)


# Each child declares only what makes it different.
class FireType(Pokemon):
    type_name = "Fire"
    strong_against = {"Grass"}
    weak_against = {"Water"}


class WaterType(Pokemon):
    type_name = "Water"
    strong_against = {"Fire"}
    weak_against = {"Grass"}


class GrassType(Pokemon):
    type_name = "Grass"
    strong_against = {"Water"}
    weak_against = {"Fire"}


charmander = FireType("Charmander", 39)
squirtle = WaterType("Squirtle", 44)
bulbasaur = GrassType("Bulbasaur", 45)

charmander.take_damage(10)            # inherited: never written in FireType
print(charmander.name, charmander.hp)  # Charmander 29
print(charmander.type_name)            # Fire: unique to this child

# The "is-a" relationship
print(isinstance(charmander, FireType))    # True
print(isinstance(charmander, Pokemon))     # True: it's both!
print(isinstance(charmander, WaterType))   # False
