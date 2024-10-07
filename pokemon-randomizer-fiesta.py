# Python script for generating random Pokemon teams

import pokebase as pb
import argparse
import random

PARTY_SIZE = 6

def arguments_setup() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("game", help="determines which encounter set is used i.e. 'black-white'")
    # milestones
    parser.add_argument("--no-milestones", help="disables milestones, allowing each team member to come from any milestone", action="store_true")
    # excluding modifiers
    parser.add_argument("--version", help="removes pokemon not obtainable from this version from team i.e. 'white'")
    parser.add_argument("--no-trade", help="removes pokemon which evolve via trade from team", action="store_true")
    parser.add_argument("--no-starter", help="removes pokemon which are gifted at the start from team", action="store_true")
    # including modifiers
    parser.add_argument("--allow-legend", help="allows for legendary pokemon to be included in team", action="store_true")
    parser.add_argument("--allow-event", help="allows for event-only pokemon to be included in team", action="store_true")
    return parser

def parse_game_data(game: str) -> list[int, str]:
    milestones_encounters = []
    f = open("game/" + game + ".txt", "r")
    for l in f:
        s = l.replace("\n", "").split(", ")
        milestones_encounters.append([int(s[1]), s[0]])
    return milestones_encounters

def pick_milestones() -> list[int]:
    rand_milestones = [0] # guaranteed for first milestone to be badge 0
    next = 1
    while len(rand_milestones) < PARTY_SIZE:
        if random.randint(0, 1) == 0:
            next = next + 1
        rand_milestones.append(next)
        next = next + 1
    return rand_milestones

def pick_encounters(milestones: list[int], milestones_encounters: list[int, str]) -> list[pb.APIResource]:
    encounters = []
    for i in milestones:
        temp_encounters_id = []
        for m, e in milestones_encounters:
            if i == m:
                temp_encounters_id.append(e)
        temp_mon_id = random.choice(temp_encounters_id)
        encounters.append(pb.pokemon(temp_mon_id))
    return encounters


def main():
    arguments = arguments_setup().parse_args()

    milestones_encounters = parse_game_data(arguments.game)

    if arguments.no_milestones:
        milestones = None
    else:
        milestones = pick_milestones()
        while milestones[-1] > 8:
            milestones = pick_milestones()

    encounters = pick_encounters(milestones, milestones_encounters)
    print(encounters)

if __name__ == "__main__":
    main()
