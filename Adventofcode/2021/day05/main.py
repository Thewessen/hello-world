#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from functools import reduce
from numpy import sign

class Field:
    """A simple field (or grid) for drawing lines and accumelating overlapping
    coords. With a method `add` for adding a range of points."""
    def __init__(self, max_x: int, max_y: int):
        self.grid = [[0 for _ in range(max_x + 1)]
                      for _ in range(max_y + 1)] 

    def add(self, r: Iterator[tuple[int, int]]):
        for x, y in r:
            self.grid[y][x] += 1

    def overlapping(self):
         return sum(1 for row in self.grid for i in row if i >= 2)


def parse_input(data: Iterator[str])\
-> Iterator[tuple[tuple[int, int], tuple[int, int]]]:
    """Each line in data has a start and end seperated by ->. Returns an
    iterator which yields these points as tuples."""
    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        yield (int(x1), int(y1)), (int(x2), int(y2))


def grid_limit_reducer(acc, curr) -> tuple[int, int]:
    """Can be used to reduce an (start, end) iterator of points to calculate the
    max x and y coords of the field."""
    xa, ya = acc
    start, end = curr
    x1, y1 = start
    x2, y2 = end
    return max(xa, x1, x2), max(ya, y1, y2)


def count_overlapping_coords(data: Iterator[str], diagonal = False) -> int:
    """Count each point in the grid (or field) where lines are overlapping.
    (see README)"""
    coords = list(parse_input(data))
    max_x, max_y = reduce(grid_limit_reducer, coords, (0, 0))
    field = Field(max_x, max_y)
    for start, end in coords:
        x1, y1 = start
        x2, y2 = end
        x_sign = sign(x2 - x1)
        y_sign = sign(y2 - y1)

        if y1 == y2 and x1 != x2:
            field.add((x, y1) for x in range(x1, x2 + x_sign, x_sign))
        elif x1 == x2 and y1 != y2:
            field.add((x1, y) for y in range(y1, y2 + y_sign, y_sign))

        if diagonal and x1 != x2 and y1 != y2:
            field.add(zip(range(x1, x2 + x_sign, x_sign),
                          range(y1, y2 + y_sign, y_sign)))

    return field.overlapping()


def main():
    parser = ArgumentParser(description="Day 5 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            result = count_overlapping_coords(data, True)
        else:
            result = count_overlapping_coords(data)
    print(result)


if __name__ == '__main__':
    main()

