#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from math import floor, ceil
from functools import reduce
from itertools import permutations
from operator import add


class SnailfishNumber:
    """Represent a SnailfishNumber with addition."""
    def __init__(self, value: tuple):
        self.value = value
        self.exploded = False

    def __repr__(self):
        a, b = self.value
        return f'[{a},{b}]'

    def __add__(self, other):
        return SnailfishNumber((
            SnailfishNumber.from_other(self),
            SnailfishNumber.from_other(other)
        )).reduce()

    def __eq__(self, other):
        return (isinstance(other, SnailfishNumber)
                and self.value == other.value)

    @property
    def magnitude(self):
        a, b = self.value
        if isinstance(a, SnailfishNumber):
            a = a.magnitude
        if isinstance(b, SnailfishNumber):
            b = b.magnitude
        return 3 * a + 2 * b

    def add_left(self, n: int):
        a, b = self.value
        if isinstance(a, SnailfishNumber):
            a.add_left(n)
        else:
            self.value = (a + n, b)
        return self

    def add_right(self, n: int): 
        a, b = self.value
        if isinstance(b, SnailfishNumber):
            b.add_right(n)
        else:
            self.value = (a, b + n)
        return self

    def explode(self, nested = 0):
        a, b = self.value
        if isinstance(a, int) and isinstance(b, int):
            # maybe self explode?
            if nested >= 4:
                self.exploded = True
                return a, b
            else:
                return None

        if isinstance(a, SnailfishNumber):
            new_value = a.explode(nested + 1)
            if new_value is not None:
                # explode happend
                new_a, new_b = new_value
                if a.exploded:
                    a = 0
                if isinstance(b, SnailfishNumber):
                    self.value = (a, b.add_left(new_b))
                else:
                    self.value = (a, b + new_b)
                return new_a, 0

        if isinstance(b, SnailfishNumber):
            new_value = b.explode(nested + 1)
            if new_value is not None:
                # explode happend
                new_a, new_b = new_value
                if b.exploded:
                    b = 0
                if isinstance(a, SnailfishNumber):
                    self.value = (a.add_right(new_a), b)
                else:
                    self.value = (a + new_a, b)
                return 0, new_b

    def split(self):
        a, b = self.value
        if isinstance(a, int) and a >= 10:
            self.value = (SnailfishNumber((floor(a / 2), ceil(a / 2))), b)
            return True
        if isinstance(a, SnailfishNumber) and a.split():
            return True
        if isinstance(b, int) and b >= 10:
            self.value = (a, SnailfishNumber((floor(b / 2), ceil(b / 2))))
            return True
        if isinstance(b, SnailfishNumber) and b.split():
            return True
        return False

    def reduce(self):
        while True:
            if self.explode() is None and not self.split():
                break
        return self

    @classmethod
    def from_str(cls, snailfish_number: str):
        a, b = eval(snailfish_number)
        if isinstance(a, int) and isinstance(b, int):
            return cls((a, b))
        if isinstance(a, int) and not isinstance(b, int):
            return cls((a, cls.from_str(str(b))))
        if not isinstance(a, int) and isinstance(b, int):
            return cls((cls.from_str(str(a)), b))
        if not isinstance(a, int) and not isinstance(b, int):
            return cls((cls.from_str(str(a)), cls.from_str(str(b))))
        raise ValueError(f'Invalid snailfish number {snailfish_number}')

    @classmethod
    def from_other(cls, other):
        a, b = other.value
        if isinstance(a, SnailfishNumber):
            a = cls.from_other(a)
        if isinstance(b, SnailfishNumber):
            b = cls.from_other(b)
        return cls((a, b))
                

def final_sum(data: Iterator[str]) -> SnailfishNumber:
    """Adds all SnailfishNumber from given input data together and returns the
    result as SnailfishNumber"""
    return reduce(add, parse_input(data))


def addition_homework(data: Iterator[str]) -> int:
    """Adds all SnailfishNumber from given input data together and returns the
    magnitude of the total sum (see README part 1)"""
    n = final_sum(data)
    return n.magnitude


def possible_sums(numbers: Iterator[SnailfishNumber]) -> Iterator[SnailfishNumber]:
    """Iterates through the results of all posible sums given the
    SnailfishNumbers."""
    yield from (a + b for a, b in permutations(numbers, 2))


def largest_sum(data: Iterator[str]) -> int:
    """Check which numbers in the given input data compute the largest sum
    based on the results magnitude and return the magnitude.
    (see README part 2)"""
    numbers = parse_input(data)
    return max(n.magnitude for n in possible_sums(numbers))


def parse_input(data: Iterator[str]) -> Iterator[SnailfishNumber]:
    """Parses all lines in data as SnailfishNumbers."""
    yield from (SnailfishNumber.from_str(line.strip())
                for line in data)


def main():
    parser = ArgumentParser(description="Day 18 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = largest_sum(data)
        else:
            r = addition_homework(data)
    print(r)


if __name__ == '__main__':
    main()
