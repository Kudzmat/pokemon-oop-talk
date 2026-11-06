# Gotta Abstract 'Em All 🔥💧🌿

**The four pillars of Object-Oriented Programming in Python, explained with Charmander, Squirtle, and Bulbasaur.**

Companion repository for the talk *"Gotta Abstract 'Em All"* by [Your Name],
presented at [Conference Name, Year]. It contains the slides, a step-by-step
set of code examples, and a small playable game that uses all four pillars.

| Pillar | The idea | The Pokémon version |
|---|---|---|
| **Encapsulation** | Protect the data | You can't set Charmander's HP to 9999 |
| **Abstraction** | Hide the complexity | You press "Fight," not a damage formula |
| **Inheritance** | Share the foundation | Every Pokémon starts from the same base class |
| **Polymorphism** | Same call, different behavior | Charmander, Squirtle, and Bulbasaur each evolve their own way |

No Pokémon knowledge is required. The talk explains everything you need.

## What's in here

```
pokemon-oop-talk/
├── slides/        The slide deck (CC BY 4.0)
├── examples/      One short, runnable script per pillar, matching the slides
├── game/          A finished turn-based game using all four pillars
├── LICENSE            MIT, for the code
├── LICENSE-CONTENT.md CC BY 4.0, for the slides and teaching materials
└── CODE_OF_CONDUCT.md
```

## Quick start

Requires **Python 3.8 or newer**. There are no dependencies to install.

```bash
git clone https://github.com/[your-username]/pokemon-oop-talk.git
cd pokemon-oop-talk

# Walk through the pillars one at a time
python examples/01_encapsulation.py
python examples/02_abstraction.py
python examples/03_inheritance.py
python examples/04_polymorphism.py

# Play the game
python game/play.py
```

## The game

Pick a starter, beat the rival you have the type advantage over, evolve, then
beat the rival who has the advantage over you. Use potions wisely.

```bash
python game/play.py                              # interactive
python game/play.py --starter squirtle           # skip the selection menu
python game/play.py --auto --starter charmander  # watch it play itself
python game/play.py --fast                       # no pauses between lines
```

The game is split so the pillars are easy to spot:

- `game/pokemon.py` holds the class hierarchy. Search for the labels
  `ENCAPSULATION`, `ABSTRACTION`, `INHERITANCE`, and `POLYMORPHISM`.
- `game/play.py` holds the game loop. It never touches a Pokémon's HP directly
  and never checks which type is attacking. It only calls `attack()`, `heal()`,
  and `evolve()`.

**Try this:** add a new type (for example `ElectricType`, strong against Water
and weak against Grass) to `pokemon.py` without changing anything in the game
loop. That is the whole payoff of good OOP design.

## For teachers

You're very welcome to use these materials in your classes. Some ideas:

- Use the `examples/` scripts as live-coding demos, one per lesson
- Ask students to predict each script's output before running it
- Have students add a fourth type, a new move, or a second evolution stage
- Ask students to spot which pillar a given line of `game/` code demonstrates

The only ask is credit. See below.

## Credit and licensing

This is open source, and it is also my work. I'd like it to stay that way.

- **Code** (`examples/` and `game/`) is under the [MIT License](LICENSE).
  Keep the copyright notice with any copy of the code.
- **Slides and written materials** are under
  [CC BY 4.0](LICENSE-CONTENT.md). You may share and adapt them, including for
  teaching and commercial use, as long as you give credit and note any
  changes.

A suggested credit line:

> "Gotta Abstract 'Em All" by [Your Name], originally presented at
> [Conference Name, Year]. https://github.com/[your-username]/pokemon-oop-talk

## Contributing

Issues and pull requests are welcome, especially fixes, clearer explanations,
and translations. By participating you agree to follow the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Disclaimer

This is an unofficial, educational fan project. It is not affiliated with,
endorsed by, or sponsored by Nintendo, Game Freak, Creatures Inc., or The
Pokémon Company. Pokémon and all related names, characters, and artwork are
trademarks and copyrights of their respective owners. The licenses above apply
only to the original work in this repository, not to any third-party
trademarks or artwork.

## Contact

[Your Name] · [your-email@example.com] · [@your-handle]
