#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Callable, Optional
from collections.abc import Iterable


def create_filter_incr() -> Callable[[str], bool]:
    """Filter function for increasing data"""
    mem: Optional[int] = None
    def increasing(data):
        nonlocal mem
        prev = mem
        mem = int(data)
        return prev is not None and prev < int(data)
    return increasing


def count_increasing(measurements: Iterable) -> int:
    """Count the number of times the measurement is increasing
    (see README part 1)"""
    data = filter(create_filter_incr(), measurements)
    return sum(1 for _ in data)


def window_sum(data: list[str], size=1):
    """Sum the data for a given window"""
    for i in range(0, len(data) - size + 1):
        yield sum(int(d) for d in data[i:i+size])


def count_windowed_increasing(measurements: list[str]) -> int:
    """Count the number of times the sanitized measurement is increasing
    (see README part 2)"""
    return count_increasing(window_sum(measurements, 3))


def main():
    parser = ArgumentParser(description="Day 1 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 " +
                              "(default: part 1 is printed)"))
    args = parser.parse_args()
    with open(args.path, 'r') as data:
        if args.part2:
            print(count_windowed_increasing(data.readlines()))
        else:
            print(count_increasing(data.readlines()))


if __name__ == '__main__':
    main()
