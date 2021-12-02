#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Callable, Optional
from collections.abc import Iterator
from functools import reduce
from more_itertools import take


def sum_increasing() -> Callable[[int, str], int]:
    """Counts when data is increasing"""
    mem: Optional[int] = None
    def increasing(acc, curr):
        nonlocal mem
        prev = mem
        mem = int(curr)
        return acc + int(prev is not None and prev < int(curr))
    return increasing


def count_increasing(measurements: Iterator) -> int:
    """Count the number of times the measurement is increasing
    (see README part 1)"""
    return reduce(sum_increasing(), measurements, 0)


def window_sum(data: Iterator[str], size=1) -> Iterator[int]:
    """Sum the data for a given window"""
    window = take(size, data) 
    lines = enumerate(data) 

    if len(window) == size:
        yield sum(int(d) for d in window)

    for index, line in lines:
        window[index % size] = line
        yield sum(int(d) for d in window)


def count_windowed_increasing(measurements: Iterator[str], window_size: int) -> int:
    """Count the number of times the sanitized measurement is increasing
    (see README part 2)"""
    return count_increasing(window_sum(measurements, window_size))


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
            print(count_windowed_increasing(data, 3))
        else:
            print(count_increasing(data))


if __name__ == '__main__':
    main()
