#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Iterable
from dataclasses import dataclass, field
from itertools import chain


@dataclass
class Mapping:
    tar: int
    dest: int
    length: int

    def __contains__(self, item: int):
        """Check if item is in range"""
        return self.tar <= item < self.tar + self.length

    def __getitem__(self, key):
        """Get item from range"""
        if key in self:
            return self.dest + key - self.tar
        else:
            raise IndexError

    def __repr__(self):
        """Get string representation"""
        return f"{self.dest} {self.tar} {self.length}"


@dataclass
class Map:
    type: str
    ranges: list[Mapping] = field(default_factory=list)

    def add_range(self, mapping: Mapping):
        """Add a range to the map"""
        self.ranges.append(mapping)

    def __getitem__(self, key: int):
        """Get corresponding destination number"""
        for mapping in self.ranges:
            if key in mapping:
                return mapping[key]
        return key
    
    def __repr__(self):
        """Get string representation"""
        return f"<Map type={self.type} ranges={self.ranges}>"


@dataclass
class GardingPlan:
    seeds: list[int]
    maps: list[Map]

    def find_location(self, seed: int) -> int:
        """Find the location of the seed"""
        for m in self.maps:
            seed = m[seed]
        return seed

    def __repr__(self):
        """Get string representation"""
        return f"<GardingPlan seeds={self.seeds} maps={self.maps}>"

    @classmethod
    def from_data(cls, data: Iterator[str]):
        seeds = []
        maps = []
        for line in data:
            if line.startswith('seeds'):
                seeds = [int(c) for c in line.split(':')[1].strip().split(' ')]
            elif line.strip().endswith('map:'):
                t = line.split(' ')[0]
                maps.append(Map(t))
            elif line.strip() == '':
                continue
            else:
                dest, tar, length = [int(c) for c in line.strip().split(' ')]
                maps[-1].add_range(Mapping(tar, dest, length))

        return cls(seeds, maps)


def lowest_seed_location(data: Iterator[str], debug = False) -> int:
    """Find the lowest seed location for the puzzle input"""
    plan = GardingPlan.from_data(data)
    if debug:
        print(plan)

    return min(plan.find_location(s) for s in plan.seeds)

def ranged_seed_lowest_location(data: Iterator[str], debug = False) -> int:
    """Find the lowest seed location for the puzzle input"""
    plan = GardingPlan.from_data(data)
    if debug:
        print(plan)

    seeds = []
    for start, length in zip(plan.seeds[::2], plan.seeds[1::2]):
        seeds.append(range(start, start + length))

    return min(chain(*seeds), key=lambda s: plan.find_location(s))


if __name__ == '__main__':
    create_cli(5, part1=lowest_seed_location, part2=ranged_seed_lowest_location)
