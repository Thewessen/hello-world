#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
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


if __name__ == '__main__':
    create_cli(1, part1=fuel_requirements, part2=exact_fuel_requirements)
