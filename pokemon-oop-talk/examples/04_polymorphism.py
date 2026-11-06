"""Pillar 4: Polymorphism. Same method call, different behavior."""
from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def evolve(self):
        ...


class FireType(Pokemon):
    def evolve(self):
        return f"{self.name} evolved into Charizard! 🔥 Wings sprout and the tail flame burns hotter."


class WaterType(Pokemon):
    def evolve(self):
        return f"{self.name} evolved into Blastoise! 💧 Water cannons emerge from its shell."


class GrassType(Pokemon):
    def evolve(self):
        return f"{self.name} evolved into Venusaur! 🌿 A huge flower blooms on its back."


team = [FireType("Charmander"), WaterType("Squirtle"), GrassType("Bulbasaur")]

# One loop. Zero type checks.
for pokemon in team:
    print(pokemon.evolve())


# Python's twist: duck typing. No shared parent needed.
class Pikachu:
    def evolve(self):
        return "Pikachu evolved into Raichu! ⚡"


print("\n-- Duck typing --")
for pokemon in team + [Pikachu()]:
    print(pokemon.evolve())
