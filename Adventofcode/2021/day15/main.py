#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Iterable
from operator import attrgetter
import math


class Grid:
    """A helper class for easy access to internal grid points and their
    surrounding points, with eq-comparison and a nice representation
    of the internal grid."""
    def __init__(self, grid: list[list]):
        self._grid = grid
    
    def __eq__(self, other) -> bool:
        return all(all(self.get((i, j)) == other.get((i, j))
                   for j, _ in enumerate(row))
                   for i, row in enumerate(self._grid))

    def __repr__(self):
        return '\n'.join(''.join(str(d) for d in row)
                         for row in self._grid)

    @classmethod
    def from_iter(cls, data: Iterator[Iterable]):
        return cls([[int(d) for d in line]
                   for line in data])

    @property
    def size(self):
        return (len(self._grid), len(max(self._grid, key=len)))

    def get(self, point):
        if not self.in_bound(point):
            raise ValueError((f'Point {point} out in bound in grid size' +
                              f'{len(self._grid)}x{max(self._grid, key=len)}'))
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        x, y = point
        return self._grid[x][y]

    def set(self, point, value: int):
        if not self.in_bound(point):
            raise ValueError((f'Point {point} out in bound in grid size' +
                              f'{len(self._grid)}x{max(self._grid, key=len)}'))
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        x, y = point
        self._grid[x][y] = value

    def in_bound(self, point) -> bool:
        if not isinstance(point, tuple):
            raise TypeError(f'Wrong point type: {point}')
        x, y = point
        height, width = self.size
        return 0 <= x < width and 0 <= y < height

    def all_coords(self):
        for i, row in enumerate(self._grid):
            for j, _ in enumerate(row):
                yield (i, j)

    def get_surrounding(self, coord: tuple[int, int]) -> Iterator[tuple[int, int]]:
        x, y = coord
        for coord in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if self.in_bound(coord):
                yield coord


class Node:
    """A single point in the density map, containing the lowest possible risk
    value to get to this point and the corresponding coords in the cloud."""
    def __init__(self, coord: tuple[int, int]):
        self.value = math.inf
        self.coord = coord

    def __repr__(self):
        x, y = self.coord
        return f'Node({{ coord: ({x}, {y}), value: {self.value} }})'

    def is_finish(self, grid: Grid) -> bool:
        height, width = grid.size
        return self.coord == (width - 1, height - 1)


def find_shortest_path(grid: Grid) -> int:
    """An implementatio of Dijkstra's algoritm."""
    height, width = grid.size
    nodes = Grid([[Node((i, j)) for j in range(width)]
                      for i in range(height)])
    curr_node = nodes.get((0, 0))
    curr_node.value = 0
    unvisited = set(nodes.get(coord) for coord in nodes.all_coords()
                    if coord != (0, 0))

    while len(unvisited) > 0:
        for coord in grid.get_surrounding(curr_node.coord):
            v = grid.get(coord)
            surr_node = nodes.get(coord)
            if surr_node.value > curr_node.value + v:
                surr_node.value = curr_node.value + v

        if curr_node.is_finish(grid):
            return curr_node.value

        unvisited.discard(curr_node)
        curr_node = min(unvisited, key=attrgetter('value'))

    return int(math.inf)


def enhance_data(data: Iterator[str]) -> Iterator[Iterator[int]]:
    """Enhance the given tile in data five times: 5x5 (see README part 2)."""
    dat = list(data)
    for i in range(5):
        for line in dat:
            yield ((int(d) + i + j) % 9
                   if int(d) + i + j != 9
                   else 9
                   for j in range(5)
                   for d in line.strip())


def main():
    parser = ArgumentParser(description="Day 15 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            grid = Grid.from_iter(enhance_data(data))
        else:
            grid = Grid.from_iter(line.strip() for line in data)
    print(find_shortest_path(grid))


if __name__ == '__main__':
    main()

