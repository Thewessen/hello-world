#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Optional, Callable
from more_itertools import consume

class Grid:
    """A helper class for easy access to internal grid points and their
    surrounding points, with eq-comparison and a nice representation
    of the internal grid."""
    def __init__(self, grid: list[list[int]]):
        self._grid = grid
    
    def __eq__(self, other) -> bool:
        return all(all(self.get((i, j)) == other.get((i, j))
                   for j, _ in enumerate(row))
                   for i, row in enumerate(self._grid))

    def __repr__(self):
        return '\n'.join(''.join(str(d) for d in row)
                         for row in self._grid)

    def get(self, point: tuple[int, int]) -> int:
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

    def get_surrounding(self, point: tuple[int, int]):
        for p in surrounding_points(point):
            if self.in_bound(p):
                yield p

    def count_when(self, fn: Callable[[int], bool]):
        return sum(sum(int(fn(d)) for d in row)
                   for row in self._grid)


class OctopusSchool(Grid):
    """A school of octopus which flashes over time. This class is an iterator
    which iterates over an initial state and keeps count of all flashes during
    its progression (see README part 1).
    It can also tell when the school synces (see README part 2)."""
    def __init__(self, school: Iterator[str]):
        grid = [[int(d) for d in row.strip()]
                for row in school]
        if (len(grid) != 10
            or any(len(row) != 10 for row in grid)):
               raise ValueError('Invalid school size')
        super().__init__(grid)
        self.flashes = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.update(lambda point: self.get(point) + 1)
        flashes = self.count_when(lambda d: d >= 10)
        while flashes > 0:
            self.flashes += flashes
            self.update(lambda point: 0 if (self.get(point) == 0 or self.get(point) >= 10)
                                        else (self.get(point) +
                                              sum(int(self.get(p) >= 10)
                                                  for p in self.get_surrounding(point))))
            flashes = self.count_when(lambda d: d >= 10)

    def update(self, fn: Callable[[tuple[int, int]], int]):
        self._grid = [[fn((i, j)) for j, _ in enumerate(row)]
                      for i, row in enumerate(self._grid)]

    def is_synced(self):
        return all(all(d == 0 for d in row)
                   for row in self._grid)


def count_flashes(data: Iterator[str], steps: int) -> int:
    """Returns the number of flashes after `steps` from an intitial state of
    a school of octopus (see README part 1)."""
    school = OctopusSchool(data)
    consume(school, steps)
    return school.flashes


def surrounding_points(point: tuple[int, int]) -> Iterator[tuple[int, int]]:
    """Returns the coords of surrounding points, given a single `point`."""
    x, y = point
    yield x + 1, y + 1
    yield x + 1, y
    yield x + 1, y - 1
    yield x, y + 1
    yield x, y - 1
    yield x - 1, y + 1
    yield x - 1, y
    yield x - 1, y - 1


def first_step_synced(data: Iterator[str]) -> Optional[int]:
    """Returns the first step when an intitial state of a school
    of octopus sync for the first time (see README part 2)."""
    school = OctopusSchool(data)
    step = 0
    for _ in school: 
        step += 1
        if school.is_synced():
            return step

def main():
    parser = ArgumentParser(description="Day 11 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = first_step_synced(data)
        else:
            r = count_flashes(data, 100)
    print(r)


if __name__ == '__main__':
    main()
