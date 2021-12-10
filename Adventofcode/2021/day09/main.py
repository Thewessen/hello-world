#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from functools import reduce

class Cloud:
    """A helper class for easily retrieving data and checking conditions
    from a grid like data structure."""
    def __init__(self, data: Iterator[str]):
        self._cloud = [[int(i) for i in line.strip()]
                       for line in data]

    def in_bound(self, point) -> bool:
        x, y = point
        return x >= 0 and x < len(self._cloud) and y >= 0 and y < len(self._cloud[x])
    
    def get(self, point: tuple[int, int]) -> int:
        x, y = point
        return self._cloud[x][y]

    def all_coords(self):
        for i, row in enumerate(self._cloud):
            for j, _ in enumerate(row):
                yield (i, j)

    def is_low_point(self, coord) -> bool:
        if not self.in_bound(coord):
            raise ValueError("Lowest point coord not in cloud")

        return all((not self.in_bound(surr)
                    or self.get(surr) > self.get(coord)
                    for surr in surrounding_points(coord)))

    def lowest_points(self) -> Iterator[tuple[int, int]]:
        for point in self.all_coords():
            if self.is_low_point(point):
                yield point

    def get_basin(self, coord: tuple[int, int]):
        basin: list[tuple[int, int]] = [coord]
        while True:
            ext = []
            for point in basin:
                surroundings = filter(lambda p: p not in basin and p not in ext,
                                      surrounding_points(point))
                for surr in surroundings:
                    if (self.in_bound(surr) and self.get(surr) != 9):
                        ext.append(surr)
            if len(ext) == 0:
                break
            basin += ext
        return basin


def surrounding_points(point: tuple[int, int]) -> Iterator[tuple[int, int]]:
    """Yields all points (coords) surrounding a given point."""
    x, y = point
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def calc_total_risk(data: Iterator[str]) -> int:
    """Calculates the total risk. (see README part 1)"""
    cloud = Cloud(data)
    return sum(cloud.get(point) + 1 for point in cloud.lowest_points())


def three_largest_basins(data: Iterator[str]):
    """Multiplies the size of the three largest basins. (see README part 2)"""
    cloud = Cloud(data)
    basins = sorted((cloud.get_basin(point)
                     for point in cloud.lowest_points()), key=len)
    return reduce(lambda acc, curr: acc * len(curr), basins[-3:], 1)


def main():
    parser = ArgumentParser(description="Day 9 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = three_largest_basins(data)
        else:
            r = calc_total_risk(data)
    print(r)


if __name__ == '__main__':
    main()
