#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from dataclasses import dataclass
from more_itertools import nth
from itertools import product
from numpy import prod


@dataclass
class TreeContext:
    size: int
    top: list[int]
    right: list[int]
    bottom: list[int]
    left: list[int]

    @property
    def visible(self):
        return any([self.is_visible('top'),
                    self.is_visible('right'),
                    self.is_visible('bottom'),
                    self.is_visible('left')])

    def is_visible(self, direction: str):
        return all(t < self.size for t in getattr(self, direction))

    @property
    def scenic_score(self):
        return prod([self.visible_trees('top'),
                     self.visible_trees('right'),
                     self.visible_trees('bottom'),
                     self.visible_trees('left')])

    def visible_trees(self, direction: str):
        if direction == 'top' or direction == 'left':
            trees = list(reversed(getattr(self, direction)))
        else:
            trees = getattr(self, direction)

        count = 0
        for t in trees:
            count += 1
            if t >= self.size:
                break
        return count

    def __eq__(self, o):
        return hash(self) == hash(o)

    def __hash__(self):
        return hash((self.size,
                     tuple(self.top),
                     tuple(self.right),
                     tuple(self.bottom),
                     tuple(self.left)))


@dataclass
class Coord:
    x: int
    y: int
    
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"C({self.x}, {self.y})"


@dataclass
class Grid:
    rows: list[list[int]]

    @property
    def columns(self):
        return zip(*self.rows)

    def get_tree_context(self, coord: Coord):
        row = self.rows[coord.y]
        column = nth(self.columns, coord.x)
        return TreeContext(size=row[coord.x],
                           left=row[:coord.x],
                           right=row[coord.x+1:],
                           top=column[:coord.y],
                           bottom=column[coord.y+1:])

    @property
    def width(self):
        return max(len(row) for row in self.rows)

    @property
    def height(self):
        return len(self.rows)


def parse_input(data: Iterator[str]) -> Grid:
    """Return the tree grid contained in the puzzle input"""
    return Grid([[int(s) for s in line.strip()] for line in data
                                                if line.strip() != ''])


def count_visible_trees(data: Iterator[str]) -> int:
    """Count all trees which are visible from the outside (part 1)"""
    grid = parse_input(data)
    perimeter = 2 * grid.width + 2 * grid.height
    # edges are counted twice
    perimeter -= 4
    return perimeter + sum(int(grid.get_tree_context(Coord(x, y)).visible)
                               for x, y in product(range(1, grid.width - 1),
                                                   range(1, grid.height - 1)))


def max_scenic_score(data: Iterator[str]) -> int:
    """Calc max scenic score of all trees (part 2)"""
    grid = parse_input(data)
    return max(grid.get_tree_context(Coord(x, y)).scenic_score
               for x, y in product(range(grid.width), range(grid.height)))


if __name__ == '__main__':
    create_cli(8, part1=count_visible_trees, part2=max_scenic_score)
