#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from dataclasses import dataclass


@dataclass
class Range:
    minus: int
    maxus: int

    def __eq__(self, other):
        return (self.minus == other.minus
                and self.maxus == other.maxus)

    def __len__(self):
        return abs(self.maxus - self.minus) + 1

    def contains(self, other):
        return (self.minus <= other.minus
                and self.maxus >= other.maxus)

    def overlapping(self, other):
        return (self.contains(other)
                or other.minus <= self.minus <= other.maxus
                or other.minus <= self.maxus <= other.maxus)



def parse_input(data: Iterator[str]) -> tuple[Range, Range]:
    """Split elve pairs into ranges for given input"""
    for line in data:
        elve1, elve2 = line.strip().split(',')
        x1, y1 = elve1.split('-')
        x2, y2 = elve2.split('-')
        yield Range(int(x1), int(y1)), Range(int(x2), int(y2)) 


def supersets(range1: Range, range2: Range) -> bool:
    """Check if one range is a superset of the other range"""
    return range1.contains(range2) or range2.contains(range1)


def count_superfluous_elves(data: Iterator[str]) -> int:
    """Count the number of elves which are in need of reconsideration (part 1)"""
    return sum(int(supersets(range1, range2))
               for range1, range2 in parse_input(data))


def count_overlapping_sections(data: Iterator[str]) -> int:
    """Count the number of elve-pairs with overlapping section (part 2)"""
    return sum(int(range1.overlapping(range2))
               for range1, range2 in parse_input(data))


if __name__ == '__main__':
    create_cli(4, part1=count_superfluous_elves, part2=count_overlapping_sections)
