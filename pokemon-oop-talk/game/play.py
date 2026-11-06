"""
play.py: a small turn-based game built on the classes in pokemon.py.

    python game/play.py                            # interactive
    python game/play.py --auto --starter squirtle  # watch it play itself
    python game/play.py --fast                     # no pauses between lines

The rules: pick a starter, beat the rival you have the type advantage over,
evolve, then beat the rival who has the advantage over you.

Notice that this file never touches a Pokémon's HP directly, and never checks
which type is attacking. It just calls attack(), heal(), and evolve().
"""
import argparse
import sys
import time

from pokemon import FireType, GrassType, WaterType

STARTERS = {
    "charmander": (FireType, "Charmander", 39),
    "squirtle": (WaterType, "Squirtle", 44),
    "bulbasaur": (GrassType, "Bulbasaur", 45),
}
STARTING_POTIONS = 2
POTION_HEAL = 20

pause = 0.7


def say(text=""):
    print(text)
    sys.stdout.flush()
    time.sleep(pause)


def hp_bar(p, width=20):
    filled = round(width * p.hp / p.max_hp)
    return f"[{'█' * filled}{'░' * (width - filled)}] {p.hp}/{p.max_hp}"


def ask(prompt, valid):
    while True:
        try:
            answer = input(prompt).strip().lower()
        except EOFError:
            print("\nInput closed. Goodbye!")
            sys.exit(0)
        if answer in valid:
            return answer
        print(f"  Please enter one of: {', '.join(sorted(valid))}")


def build(key):
    cls, name, hp = STARTERS[key]
    return cls(name, hp)


def pick_starter(choice):
    if choice:
        return build(choice)
    say("Choose your starter Pokémon!")
    keys = list(STARTERS)
    for i, key in enumerate(keys, 1):
        cls = STARTERS[key][0]
        say(f"  {i}) {cls.emoji} {STARTERS[key][1]} ({cls.type_name}-type)")
    pick = ask("> ", {"1", "2", "3"})
    return build(keys[int(pick) - 1])


def choose_rivals(player):
    """First rival: one you beat. Second rival: the one that beats you."""
    others = [k for k in STARTERS if STARTERS[k][1] != player.name]
    easy = next(k for k in others if STARTERS[k][0].type_name in player.strong_against)
    hard = next(k for k in others if k != easy)
    return build(easy), build(hard)


def battle(player, foe, potions, auto):
    say(f"\n⚔️  {foe.name} ({foe.type_name}-type) wants to battle!\n")
    while True:
        say(f"{foe.name:<12} {hp_bar(foe)}")
        say(f"{player.name:<12} {hp_bar(player)}")
        if auto:
            action = "1"
        else:
            print(f"\nYour turn!  1) Fight ({player.move_name})   "
                  f"2) Potion ({potions} left)   3) Run")
            action = ask("> ", {"1", "2", "3"})
        say()

        if action == "3":
            say("You ran away... Game over.")
            sys.exit(0)
        if action == "2":
            if potions == 0:
                say("You're out of potions!")
                continue
            potions -= 1
            restored = player.heal(POTION_HEAL)
            say(f"🧪 {player.name} recovered {restored} HP!")
        else:
            say(player.attack(foe))

        if foe.is_fainted:
            say(f"\n{foe.name} fainted. You win this round! 🎉")
            return True, potions

        say(foe.attack(player))
        if player.is_fainted:
            say(f"\n{player.name} fainted... You lose. Better luck next time!")
            return False, potions
        say()


def main():
    global pause
    parser = argparse.ArgumentParser(description="A tiny Pokémon-style battle game.")
    parser.add_argument("--auto", action="store_true", help="always choose Fight")
    parser.add_argument("--fast", action="store_true", help="no pauses")
    parser.add_argument("--starter", choices=STARTERS, help="skip the selection menu")
    args = parser.parse_args()
    if args.fast or args.auto:
        pause = 0

    say("=== The Starter Tournament ===\n")
    player = pick_starter(args.starter)
    say(f"\nYou chose {player.name}!")
    rival1, rival2 = choose_rivals(player)
    potions = STARTING_POTIONS

    won, potions = battle(player, rival1, potions, args.auto)
    if not won:
        return

    say("\n✨ What's this? Your Pokémon is evolving!")
    say(player.evolve())
    say(f"HP fully restored: {hp_bar(player)}")

    won, potions = battle(player, rival2, potions, args.auto)
    if won:
        say(f"\n🏆 {player.name} is the champion! Thanks for playing.")


if __name__ == "__main__":
    main()
