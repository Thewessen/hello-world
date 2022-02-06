#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import takewhile
from dataclasses import dataclass

@dataclass
class Movement:
    direction: str
    steps: int
    
    @property
    def delta(self):
        return {
            "U": Coord(0, 1),
            "D": Coord(0, -1),
            "L": Coord(-1, 0),
            "R": Coord(1, 0)
        }[self.direction]

    @classmethod
    def from_str(cls, m: str):
        direction = m[0]
        steps = int(m[1:])
        return cls(direction, steps)


@dataclass
class Coord:
    x: int
    y: int
    
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def create_movements(line: str) -> Iterator[Movement]:
    """Creates Movement iterator from ',' separated line."""
    for d in line.split(','):
        yield Movement.from_str(d)


def parse_input(data: Iterator[str]) -> tuple[Iterator[Movement], Iterator[Movement]]:
    """Parse two lines (Movement iterators) from given data."""
    line1 = next(data).strip()
    line2 = next(data).strip()
    return create_movements(line1), create_movements(line2)


def create_path(line: Iterator[Movement]) -> Iterator[Coord]:
    """From Movement iterator to Coord iterator."""
    start = Coord(0, 0)
    for m in line:
        for _ in range(m.steps):
            start += m.delta
            yield start


def closest_crossing(data: Iterator[str]) -> int:
    """Calculate the lowest manhattan distance for all crossings to Coord(0, 0)."""
    line1, line2 = parse_input(data)
    path1 = create_path(line1)
    path2 = create_path(line2)
    crossings = set(path1).intersection(set(path2))
    return min(c.manhattan_distance(Coord(0, 0)) for c in crossings)


def dst(path: list[Coord], dest: Coord) -> int:
    """Calculate the number of steps to take on path until dest Coord is
    reached."""
    return len(list(takewhile(lambda c: c != dest, path))) + 1


def least_steps(data: Iterator[str]) -> int:
    """Calculate the least amount of steps walking both paths until they
    cross (see README part 2)."""
    line1, line2 = parse_input(data)
    path1 = list(create_path(line1))
    path2 = list(create_path(line2))
    crossings = set(path1).intersection(set(path2))
    return min(dst(path1, c) + dst(path2, c) for c in crossings)


if __name__ == '__main__':
    create_cli(3, part1=closest_crossing, part2=least_steps)
