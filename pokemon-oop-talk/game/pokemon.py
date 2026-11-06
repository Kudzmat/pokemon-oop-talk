"""
pokemon.py: the class hierarchy from the talk.

All four OOP pillars live in this file. Search for the labels:
    ENCAPSULATION, ABSTRACTION, INHERITANCE, POLYMORPHISM
"""
from abc import ABC, abstractmethod


class Pokemon(ABC):
    # INHERITANCE: neutral defaults that each type overrides
    type_name = "Normal"
    emoji = "⚪"
    move_name = "Tackle"
    base_power = 10
    strong_against = set()
    weak_against = set()

    def __init__(self, name, max_hp):
        self.name = name
        self._max_hp = max_hp      # ENCAPSULATION: internal state, leading underscore
        self._hp = max_hp
        self._power = self.base_power

    # ---- ENCAPSULATION: read-only views of internal data ----
    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def is_fainted(self):
        return self._hp == 0

    # ---- ENCAPSULATION: the only approved ways to change HP ----
    def take_damage(self, amount):
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        """Restore HP (never above max). Returns how much was actually restored."""
        before = self._hp
        self._hp = min(self._max_hp, self._hp + amount)
        return self._hp - before

    # ---- ABSTRACTION: one simple call hides the damage math ----
    def attack(self, target):
        multiplier = self._type_multiplier(target)
        damage = int(self._power * multiplier)
        before = target.hp
        target.take_damage(damage)

        lines = [f"{self.emoji} {self.name} used {self.move_name}!"]
        if multiplier > 1:
            lines.append("   It's super effective!")
        elif multiplier < 1:
            lines.append("   It's not very effective...")
        lines.append(f"   {target.name} HP: {before} -> {target.hp}")
        return "\n".join(lines)

    def _type_multiplier(self, target):
        if target.type_name in self.strong_against:
            return 2.0
        if target.type_name in self.weak_against:
            return 0.5
        return 1.0

    # ---- POLYMORPHISM: every type must evolve in its own way ----
    @abstractmethod
    def evolve(self):
        ...

    def _evolve_into(self, new_name, hp_bonus, power_bonus):
        """Shared evolution mechanics; subclasses supply the specifics."""
        old_name = self.name
        self.name = new_name
        self._max_hp += hp_bonus
        self._hp = self._max_hp
        self._power += power_bonus
        return f"{old_name} evolved into {new_name}!"


# --------------------------------------------------------------------------
# INHERITANCE: each child declares only what makes it different
# --------------------------------------------------------------------------
class FireType(Pokemon):
    type_name = "Fire"
    emoji = "🔥"
    move_name = "Ember"
    strong_against = {"Grass"}
    weak_against = {"Water"}

    def evolve(self):  # POLYMORPHISM: same method name, different behavior
        text = self._evolve_into("Charizard", hp_bonus=40, power_bonus=15)
        return f"{text} 🔥 Wings sprout and the tail flame burns hotter."


class WaterType(Pokemon):
    type_name = "Water"
    emoji = "💧"
    move_name = "Water Gun"
    strong_against = {"Fire"}
    weak_against = {"Grass"}

    def evolve(self):
        text = self._evolve_into("Blastoise", hp_bonus=40, power_bonus=15)
        return f"{text} 💧 Water cannons emerge from its shell."


class GrassType(Pokemon):
    type_name = "Grass"
    emoji = "🌿"
    move_name = "Vine Whip"
    strong_against = {"Water"}
    weak_against = {"Fire"}

    def evolve(self):
        text = self._evolve_into("Venusaur", hp_bonus=40, power_bonus=15)
        return f"{text} 🌿 A huge flower blooms on its back."
