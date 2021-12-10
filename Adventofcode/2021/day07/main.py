#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from math import ceil, floor

def calc_cheapest_horz_position(data: Iterator[str]) -> int:
    """Finds a point which requires all points in a given input to travel the
    least amount of distance combined"""
    positions = list(sorted(int(h) for h in next(data).split(',')))
    b = positions[round(len(positions) / 2)] 
    return sum(abs(p - b) for p in positions)


def calc_cheapest_horz_position_crab_engineering(data: Iterator[str]) -> int:
    """Finds a point which requires each point in a given input to travel the
    least amount of distance"""
    positions = list(int(h) for h in next(data).split(','))
    # I would suspect round here ?!?
    low = floor(sum(positions) / len(positions))
    high = ceil(sum(positions) / len(positions))
    return min(sum(int(abs(p - low) * (abs(p - low) + 1) / 2) for p in positions),
               sum(int(abs(p - high) * (abs(p - high) + 1) / 2) for p in positions))
def main():
    parser = ArgumentParser(description="Day 7 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = calc_cheapest_horz_position_crab_engineering(data)
        else:
            r = calc_cheapest_horz_position(data)
        print(r)


if __name__ == '__main__':
    main()
