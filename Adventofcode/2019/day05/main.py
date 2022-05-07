#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from typing import Iterator


def solve(data: Iterator[str], *args) -> int:
    return Program.from_str(next(data), *args).run()


def part_1(data: Iterator[str]) -> int:
    """Solution part 1 (see Readme)"""
    return solve(data, 1)


def part_2(data: Iterator[str]) -> int:
    """Solution part 2 (see Readme)"""
    return solve(data, 5)


if __name__ == '__main__':
    create_cli(5, part1=part_1, part2=part_2)
