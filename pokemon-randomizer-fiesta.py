# Python script for generating random Pokemon teams

import pokebase as pb
import argparse

def arguments_setup() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("game", help="determines which encounter set is used i.e. 'black-white'")
    
    # milestones
    parser.add_argument("--milestones", help="sets custom milestone markers. by default, these are set to badges 0, 1, 2, 4, 6, 8, requiring each team member to be obtainable before their respective milestone. ex: '0 2 4 5 6 8'", nargs='+', type=int)
    parser.add_argument("--no-milestones", help="disables milestones, allowing each team member to come from any milestone", action="store_true")

    # excluding modifiers
    parser.add_argument("--version", help="removes pokemon not obtainable from this version from team i.e. 'white'")
    parser.add_argument("--no-trade", help="removes pokemon which evolve via trade from team", action="store_true")
    parser.add_argument("--no-starter", help="removes pokemon which are gifted at the start from team", action="store_true")
    parser.add_argument("--no-legend", help="removes pokemon which are labeled as legendaries from team", action="store_true")

    # including modifiers
    parser.add_argument("--allow-event", help="allows for event-only pokemon to be included in team", action="store_true")

    return parser

def parse_game_data(game: str) -> list[str, int]:
    encounters_milestones = []
    f = open("game/" + game + ".txt", "r")
    for l in f:
        s = l.replace("\n", "").split(", ")
        encounters_milestones.append([s[0], int(s[1])])


def main():
    arguments = arguments_setup().parse_args()
    print(arguments.game)
    print(arguments.milestones)

    encounters_milestones = parse_game_data(arguments.game)
    print(encounters_milestones)

if __name__ == "__main__":
    main()
