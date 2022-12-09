#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from dataclasses import dataclass
from enum import Enum
from functools import reduce


@dataclass
class Coord:
    x: int
    y: int
    
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"C({self.x}, {self.y})"

    def is_neighbour(self, o):
        return abs(self.x - o.x) <= 1 and abs(self.y - o.y) <= 1

    def is_diagonal(self, o):
        return self.x != o.x and self.y != o.y


class Direction(Enum):
    R = Coord(1, 0)
    L = Coord(-1, 0)
    U = Coord(0, -1)
    D = Coord(0, 1)


def parse_input(data: Iterator[str]) -> Iterator[tuple[Direction, int]]:
    """Get instructions found in data"""
    start = Coord(0, 0)
    yield start
    for line in data:
        if line.strip() == '':
            break
        d, i = line.strip().split(' ')
        for _ in range(int(i)):
            start += getattr(Direction, d).value
            yield start


def cmp(a: int, b: int) -> int:
    """Returns -1 if a < b, 0 if a == b and 1 if a > b"""
    return (a > b) - (a < b)


def follow(coords: Iterator[Coord]) -> Iterator[Coord]:
    """All coords following a stream of coords one step at the time"""
    first_coord = next(coords)
    T = first_coord
    yield T
    for c in coords:
        if not T.is_neighbour(c):
            # tail should follow by one step
            T = Coord(T.x + cmp(c.x, T.x),
                      T.y + cmp(c.y, T.y))
        if not T.is_neighbour(c):
            # oopsie
            raise ValueError('Rope snaps!!!')
        yield T


def count_tail_visited(data: Iterator[str], knots: int) -> int:
    """Count the unique positions tail visited following head"""
    coords = parse_input(data)
    for _ in range(knots - 1):
        coords = follow(coords)
        next(coords)
    return len(set(coords))


def count_tail_small_rope(data: Iterator[str]) -> int:
    """Count the unique positions tail visited following head with 2 knots (part 1)"""
    return count_tail_visited(data, 2)


def count_tail_larger_rope(data: Iterator[str]) -> int:
    """Count the unique positions tail visited following head with 10 knots (part 2)"""
    return count_tail_visited(data, 10)


if __name__ == '__main__':
    create_cli(9, part1=count_tail_small_rope, part2=count_tail_larger_rope)
