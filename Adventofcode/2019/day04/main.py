#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Iterable
from itertools import pairwise, groupby

class Validator:
    def __init__(self):
        self.rules = []

    def addRule(self, fn):
        self.rules.append(fn)

    def validate(self, n: int) -> bool:
        return all(fn(n) for fn in self.rules)

    @classmethod
    def part1(cls):
        validator = cls()
        validator.addRule(never_decreases)
        validator.addRule(atleast_one_pair)
        return validator

    @classmethod
    def part2(cls):
        validator = cls()
        validator.addRule(never_decreases)
        validator.addRule(atleast_one_exact_pair)
        return validator

def parse_input(data: Iterator[str]) -> Iterable[int]:
    """Returns a range of numbers from a given input."""
    [start, end] = next(data).split('-')
    return range(int(start), int(end) + 1)


def never_decreases(n: int) -> bool:
    for a, b in pairwise(str(n)):
        if int(a) > int(b):
            return False
    return True

def atleast_one_pair(n: int) -> bool:
    for a, b in pairwise(str(n)):
        if a == b:
            return True
    return False

def atleast_one_exact_pair(n: int) -> bool:
    return any(sum(1 for _ in g) == 2
               for _, g in groupby(str(n)))

def count_valid_numbers(data: Iterator[str]) -> int:
    validator = Validator.part1()
    return sum(int(validator.validate(n)) for n in parse_input(data))

def count_valid_numbers_part2(data: Iterator[str]) -> int:
    validator = Validator.part2()
    return sum(int(validator.validate(n)) for n in parse_input(data))

if __name__ == '__main__':
    create_cli(4, part1=count_valid_numbers, part2=count_valid_numbers_part2)
