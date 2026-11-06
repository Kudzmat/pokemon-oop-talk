"""Pillar 1: Encapsulation. An object protects its own data."""


# WITHOUT encapsulation: anyone can set HP to nonsense
class LeakyPokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


charmander = LeakyPokemon("Charmander", 39)
charmander.hp = 9999
charmander.hp = -50
print("Without encapsulation:", charmander.hp)


# WITH encapsulation: the object enforces its own rules
class Pokemon:
    def __init__(self, name, max_hp):
        self.name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def hp(self):
        return self._hp

    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        self._hp = min(self._max_hp, self._hp + amount)


charmander = Pokemon("Charmander", 39)
charmander.take_damage(10)
print("After 10 damage:", charmander.hp)           # 29

charmander.take_damage(500)
print("After 500 damage:", charmander.hp)          # 0, never negative

try:
    charmander.hp = 9999
except AttributeError:
    print("Can't set hp directly. Use take_damage() or heal().")
