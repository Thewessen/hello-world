#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator


def parse_input(data: Iterator[str]) -> Iterator[int]:
    """Parses module mass from puzzle input"""
    return (int(line.strip()) for line in data)


def calc_fuel(mass: int) -> int:
    """Required fuel for module mass"""
    return int(mass / 3 - 2)


def fuel_requirements(data: Iterator[str]) -> int:
    """Fuel requirements for puzzle input (part 1)"""
    return sum(calc_fuel(mass) for mass in parse_input(data))


def calc_fuel_inc_fuel(mass: int) -> Iterator[int]:
    """Yield's fuel for mass until no fuel is needed"""
    while mass > 0:
        mass = calc_fuel(mass)
        yield max(mass, 0)

def calc_exact_fuel(mass: int) -> int:
    """Required fuel for module mass inc. the extra mass for fuel"""
    return sum(calc_fuel_inc_fuel(mass))


def exact_fuel_requirements(data: Iterator[str]) -> int:
    """Fuel requirements for puzzle input (part 2)"""
    return sum(calc_exact_fuel(mass) for mass in parse_input(data))


def main():
    parser = ArgumentParser(description="Day 1 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 " +
                              "(default: part 1 is printed)"))
    parser.add_argument('-p', '--post', action='store_true',
                        help=("Print the solution for part 2 " +
                              "(default: part 1 is printed)"))
    args = parser.parse_args()
    with open(args.path, 'r') as data:
        if args.part2:
            r = exact_fuel_requirements(data)
        else:
            r = fuel_requirements(data)
    print(r)


if __name__ == '__main__':
    main()
