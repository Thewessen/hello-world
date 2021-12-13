#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from itertools import takewhile
from enum import Enum


class Grid:
    """A helper class for representing a grid like structure from different
    data types, with eq-comparison."""
    def __init__(self, grid: list[list[str]]):
        self._grid = grid
    
    def __eq__(self, other) -> bool:
        return all(all(self.get((i, j)) == other.get((i, j))
                   for j, _ in enumerate(row))
                   for i, row in enumerate(self._grid))

    def __repr__(self):
        return '\n'.join(''.join(str(d) for d in row)
                         for row in self._grid)

    @classmethod
    def from_str(cls, data: list[str]):
        return cls([list(row) for row in data])

    @classmethod
    def from_coords(cls, coords: set[tuple[int, int]]):
        max_x = max(coords, key=lambda c: c[0])[0]
        max_y = max(coords, key=lambda c: c[1])[1]
        return cls([['#' if (i, j) in coords else '.'
                     for i in range(0, max_x + 1)]
                    for j in range(0, max_y + 1)])

    def get(self, point: tuple[int, int]) -> str:
        if not self.in_bound(point):
            raise ValueError((f'Point {point} out in bound in grid size' +
                              f'{len(self._grid)}x{max(self._grid, key=len)}'))
        x, y = point
        return self._grid[x][y]

    def in_bound(self, point: tuple[int, int]) -> bool:
        x, y = point
        return (x >= 0 and y >= 0
                and x < len(self._grid)
                and y < len(self._grid[x]))


class Direction(Enum):
    UP = 'y'
    LEFT = 'x'


class Fold:
    """A representation class for a fold instruction. Consists of a direction
    and a value. Can `fold` a specific coord."""
    def __init__(self, d: Direction, v: int):
        self.direction = d
        self.value = v

    def __repr__(self):
        return f'Fold({self.direction}={self.value})'

    def fold(self, x: int, y: int) -> tuple[int, int]:
        if self.direction == Direction.UP and y > self.value:
            return x, 2 * self.value - y
        elif self.direction == Direction.LEFT and x > self.value:
            return 2 * self.value - x, y
        else:
            return x, y


def parse_input(data: Iterator[str]) -> tuple[set[tuple[int, int]], Iterator[Fold]]:
    """Splits input into a set of initial coords and a fold-instructions
    iterator."""
    coords = (line.strip().split(',')
                   for line in takewhile(lambda line: line != '\n', data))
    instructs = (line.strip().split(' ')[-1].split('=') for line in data)
    return (set((int(x), int(y)) for x, y in coords),
            (Fold(Direction(d), int(v)) for d, v in instructs))


def count_dots_first_fold(data: Iterator[str]) -> int:
    """Count the number of dots after the first fold instruction from input
    data (see README part 1)."""
    coords, instructs = parse_input(data)
    instr = next(instructs)
    new_coords = set(instr.fold(*coord) for coord in coords)
    return len(new_coords)


def get_code(data: Iterator[str]) -> Grid:
    """Return a representable grid after applying all fold instructions to
    initial cords from input data (see README part 2)."""
    coords, instructs = parse_input(data)
    for instr in instructs:
        coords = set(instr.fold(*coord) for coord in coords)
    return Grid.from_coords(coords)


def main():
    parser = ArgumentParser(description="Day 13 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = get_code(data)
        else:
            r = count_dots_first_fold(data)
    print(r)


if __name__ == '__main__':
    main()
