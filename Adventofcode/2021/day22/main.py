#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Generator, Optional
from dataclasses import dataclass
from functools import reduce
from itertools import product
from math import inf
import re


@dataclass
class Range:
    minus: int
    maxus: int

    def __repr__(self):
        return f'Range({self.minus}, {self.maxus})'

    def __eq__(self, other):
        return (self.minus == other.minus
                and self.maxus == other.maxus)

    def __len__(self):
        return abs(self.maxus - self.minus) + 1

    def overlapping(self, other):
        return (other.minus <= self.minus <= other.maxus
                or other.minus <= self.maxus <= other.maxus
                or (self.minus < other.minus and other.maxus < self.maxus))

    def parts(self, other):
        if not self.overlapping(other):
            yield self
            yield other
        if self == other:
            yield self
        elif self.minus == other.minus:
            yield Range(self.minus, min(self.maxus, other.maxus))
            yield Range(min(self.maxus, other.maxus) + 1, max(self.maxus, other.maxus))
        elif self.maxus == other.maxus:
            yield Range(min(self.minus, other.minus), max(self.minus, other.minus) - 1)
            yield Range(max(self.minus, other.minus), self.maxus)
        else:
            yield Range(min(self.minus, other.minus), max(self.minus, other.minus) - 1)
            yield Range(max(self.minus, other.minus), min(self.maxus, other.maxus))
            yield Range(min(self.maxus, other.maxus) + 1, max(self.maxus, other.maxus))

    def subset(self, other):
        return self.minus >= other.minus and self.maxus <= other.maxus


@dataclass
class Cuboid:
    x: Range
    y: Range
    z: Range

    @classmethod
    def cube(cls, mn, mx):
        r = Range(mn, mx)
        return cls(r, r, r)

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y
                and self.z == other.z)
    
    def __len__(self):
        return len(self.x) * len(self.y) * len(self.z)

    def __sub__(self, other):
        if not self.overlapping(other):
            return [self]
        if self.subset(other):
            return []
        return list(self.distinct(other))

    def distinct(self, other):
        for x, y, z in product(self.x.parts(other.x),
                               self.y.parts(other.y),
                               self.z.parts(other.z)):
            cuboid = Cuboid(x, y, z)
            if (cuboid.subset(self)
                and not cuboid.subset(other)):
                yield cuboid

    def overlapping(self, other):
        return (self.x.overlapping(other.x)
                and self.y.overlapping(other.y)
                and self.z.overlapping(other.z))

    def subset(self, other):
        return (self.x.subset(other.x)
                and self.y.subset(other.y)
                and self.z.subset(other.z))


class BootSystem:
    def __init__(self):
        self.active_cuboids = []
        self.process = self._process()
        self.process.send(None)

    def __len__(self):
        return sum(len(c) for c in self.active_cuboids)

    def _process(self) -> Generator[None, Optional[tuple[bool, Cuboid]], None]:
        while True:
            instr = (yield)
            if instr is None:
                continue
            add, cuboid = instr
            if add and any(cuboid.subset(c) for c in self.active_cuboids):
                continue
            self.active_cuboids = reduce(lambda acc, cb: acc + (cb - cuboid),
                                         self.active_cuboids, [])
            if add:
                self.active_cuboids.append(cuboid)

    def read(self, add: bool, cuboid: Cuboid):
        self.process.send((add, cuboid))


def parse_input(data: Iterator[str]) -> Iterator[tuple[bool, Cuboid]]:
    digits = r'-?\d+'
    for line in data:
        toggle, ranges = line.strip().split(' ')
        min_max = (re.findall(digits, n) for n in ranges.split(','))
        range_sets = (Range(int(mn), int(mx)) for mn, mx in min_max)
        yield (toggle == 'on', Cuboid(*range_sets))


def count_active_cubes(data: Iterator[str], boundry = Cuboid.cube(-inf, inf)) -> int:
    system = BootSystem()
    for add, cub in parse_input(data):
        if cub.subset(boundry):
            system.read(add, cub)
    return len(system)


def main():
    parser = ArgumentParser(description="Day 22 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open('./input', 'r') as data:
        if args.part2:
            r = count_active_cubes(data)
        else:
            r = count_active_cubes(data, Cuboid.cube(-50, 50))
    print(r)


if __name__ == '__main__':
    main()
