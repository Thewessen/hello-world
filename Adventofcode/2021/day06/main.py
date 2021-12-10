#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from more_itertools import consume
from collections import deque, Counter


class LanternfishSchool:
    """A school of Lanternfish. Iterable by days to get a total lantern fish
    each succesive day."""
    def __init__(self, school: Iterator[int]):
        count = Counter(school)
        self._school = deque(count.get(timer, 0)
                             for timer in range(9))

    def __iter__(self):
        return self

    def __next__(self):
        self._school.rotate(-1)
        self._school[6] += self._school[8]

    def total(self):
        return sum(self._school)


def progress_days(data: Iterator[str], days):
    """Progress a school of latern fish based on initial data x days"""
    school = LanternfishSchool(int(timer)
                               for timer in next(data).split(','))
    consume(school, days)
    return school.total()


def main():
    parser = ArgumentParser(description="Day 6 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            print(progress_days(data, 256))
        else:
            print(progress_days(data, 80))


if __name__ == '__main__':
    main()
