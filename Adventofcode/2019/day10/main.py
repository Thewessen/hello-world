#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Optional
from dataclasses import dataclass
from numpy import gcd, arctan, pi
from itertools import zip_longest
from more_itertools import nth
from collections import defaultdict


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

    def direction(self, other):
        a = other.x - self.x
        b = other.y - self.y
        d = gcd(a, b)
        return Coord(a / d, b / d)

    def angle(self, other):
        if self == other:
            return 0
        if self.x == other.x:
            return int(self.y < other.y)
        if self.y == other.y:
            return int(self.x > other.x) + 0.5

        if (self.y > other.y and self.x < other.x
            or self.y < other.y and self.x > other.x):
            a = arctan(abs(self.x - other.x) / abs(self.y - other.y))
            if self.y > other.y:
                return a / pi
            else:
                return 1 + a / pi
        else:
            a = arctan(abs(self.y - other.y) / abs(self.x - other.x))
            if self.y > other.y:
                return 1.5 + a / pi
            else:
                return 0.5 + a / pi


class Matrix:
    def __init__(self, mtrx: list[list[str]]):
        self._mtrx = mtrx

    @classmethod
    def from_iter(cls, data: Iterator[str]):
        return cls([list(d.strip()) for d in data])

    @property
    def height(self):
        return len(self._mtrx)

    @property
    def width(self):
        return max(len(row) for row in self._mtrx)

    def all_coords(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                yield Coord(x, y)

    def get(self, c: Coord) -> Optional[str]:
        if self.in_bound(c):
            return self._mtrx[c.y][c.x]

    def in_bound(self, c: Coord) -> bool:
        return (0 <= c.x < self.width and
                0 <= c.y < self.height)


def visible_astroids(station: Coord, galaxy: Matrix) -> int:
    """Count the number of visible astroids from a given station (astroid)."""
    if galaxy.get(station) != '#':
        raise ValueError('Station should be on a astroid')

    directions = set()
    for astroid in astroids(galaxy):
        if astroid != station:
            directions.add(station.direction(astroid))

    return len(directions)


def astroids(galaxy: Matrix) -> Iterator[Coord]:
    """Get the coords of all astroids on the given map."""
    for coord in galaxy.all_coords():
        if galaxy.get(coord) == '#':
            yield coord


def part_1(data: Iterator[str]) -> int:
    """Solution part 1, maximum visible astroids from any astroid. (see Readme)"""
    galaxy = Matrix.from_iter(data)
    return max(visible_astroids(station, galaxy)
               for station in astroids(galaxy))


def destroy_astroids(station: Coord, galaxy: Matrix) -> Iterator[Coord]:
    """Get the coords of all astroids destroyed by the giant lazer in order."""
    d = defaultdict(list)
    for astroid in astroids(galaxy):
        if astroid != station:
            d[station.angle(astroid)].append(astroid)
    astroids_by_angle = (sorted(astroids, key=lambda s: station.manhattan_distance(s))
                         for _, astroids in sorted(d.items(), key=lambda d: d[0]))
    for poss_astroids in zip_longest(*astroids_by_angle):
        yield from filter(None, poss_astroids)


def best_station(galaxy: Matrix) -> Coord:
    """Get the coords of the best location (astroid) for the space station."""
    return max(astroids(galaxy), key=lambda s: visible_astroids(s, galaxy))
    

def nth_destroyed(data: Iterator[str], n = 200) -> Coord:
    """Get the coords of the nth astroid destroyed by the giant lazer."""
    galaxy = Matrix.from_iter(data)
    station = best_station(galaxy)
    return nth(destroy_astroids(station, galaxy), n - 1, Coord(0, 0))


def part_2(data: Iterator[str]) -> int:
    """Solution part 2, 200th astroid destroyed
    (see Readme part 2)"""
    target = nth_destroyed(data, 200)
    return target.x * 100 + target.y


if __name__ == '__main__':
    create_cli(10, part1=part_1, part2=part_2)
