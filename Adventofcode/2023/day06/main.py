#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Iterable
from dataclasses import dataclass
from functools import reduce
from math import sqrt, ceil, floor
import re

def parse_input(data: Iterable[str]) -> (int, int):
    """Parse input data"""
    times = (int(t) for t in  next(data).replace('Time:', '').split(' ')
                    if t != '')
    distances = (int(d) for d in next(data).replace('Distance:', '').split(' ')
                        if d != '')
    for time, distance in zip(times, distances):
        yield time, distance


def calculate_marge_of_error(time: int, record: int) -> int:
    """Calculate marge of error for a given time and record"""
    # a(time - a) = record
    # a * time - a^2 = record
    # a^2 - a * time + record = 0
    # a = (-b +- sqrt(b^2 - 4ac)) / 2a

    x1 = (-time + sqrt(time ** 2 - 4 * record)) / 2
    x2 = (-time - sqrt(time ** 2 - 4 * record)) / 2
    return ceil(max(x1, x2)) - floor(min(x1, x2)) - 1


def product_margins_of_error(data: Iterable[str], debug = False) -> int:
    """Product margins of error for all records in data"""
    return reduce(lambda x, y: x * y, (calculate_marge_of_error(time, distance)
                                       for time, distance in parse_input(data)))


def single_race(data: Iterable[str], debug = False) -> int:
    """Product margins of error for a single race from input data"""
    records = parse_input(data)
    time, distance = (''.join(str(n) for n in data) for data in zip(*records))
    return calculate_marge_of_error(int(time), int(distance))


if __name__ == '__main__':
    create_cli(6, part1=product_margins_of_error, part2=single_race)
