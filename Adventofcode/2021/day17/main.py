#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from itertools import product
import re


def parse_input(data: Iterator[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns the area mark from given input data."""
    min_x, max_x, min_y, max_y = re.findall(r'[-]?\d+', next(data))
    r = (int(min_x), int(max_x)), (int(min_y), int(max_y))
    return r


def max_y_velocity(y_range: tuple[int, int]) -> int:
    """Calculate the max velocity at which the probe can be shot upwards while
    still 'landing' in a given vertical range."""
    min_y, _ = y_range
    return abs(min_y) - 1


def calc_max_height(data: Iterator[str]) -> int:
    """Calculate the max height the probe can be shot while hitting the mark
    given in data (see README part 1)"""
    _, y_range = parse_input(data)
    max_y_velo = max_y_velocity(y_range)
    return tran(max_y_velo)


def tran(size: int) -> int:
    """Calculates the triangle number from a given size."""
    return int(size * (size + 1) / 2)


def steps(velocity: tuple[int, int]) -> Iterator[tuple[int, int]]:
    """Returns each step from coord 0, 0 launching with a given velocity.
    See README for the step rules."""
    x, y = (0, 0)
    xv, yv = velocity
    while True:
        x, y = (x + xv, y + yv)
        yield x, y
        xv = max(0, xv - 1)
        yv -= 1

def hits_mark(x_range: tuple[int, int], y_range: tuple[int, int]):
    """Ditermens if a progression of coords hits the mark. Will return false is
    the mark is 'overshot'."""
    min_x, max_x = x_range
    min_y, max_y = y_range

    def hit(steps: Iterator[tuple[int, int]]):
        for coord in steps:
            x, y = coord
            if (min_x <= x <= max_x) and (min_y <= y <= max_y):
                return True
            if x > max_x or y < min_y:
                return False

    return hit

def valid_velocity_values(data: Iterator[str]) -> Iterator[tuple[int, int]]:
    """Iterates through all possible velocity to see which one hits the
    mark and yields those who does."""
    x_range, y_range = parse_input(data)
    _, max_x = x_range
    min_y, _ = y_range
    hits = hits_mark(x_range, y_range)
    for coord in product(range(1, max_x + 1),
                         range(max_y_velocity(y_range), min_y - 1, -1)):
        if hits(steps(coord)):
            yield coord


def main():
    parser = ArgumentParser(description="Day 17 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = len(set(valid_velocity_values(data)))
        else:
            r = calc_max_height(data)
    print(r)


if __name__ == '__main__':
    main()
