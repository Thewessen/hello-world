#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from typing import Iterator


def parse_input(data: Iterator[str]) -> str:
    return next(data).strip()


def validate_and_run(program: Program) -> int:
    output = list(program)
    if len(output) > 1:
        raise ValueError('Intcode computer not ready for BOOST program')
    return output[0]


def part_1(data: Iterator[str]) -> int:
    """Solution part 1, running the given program in test mode. (see Readme)"""
    p = Program.from_str(parse_input(data), 1)
    return validate_and_run(p)


def part_2(data: Iterator[str]) -> int:
    """Solution part 2, running the given program in sensor boost mode
    (see Readme part 2)"""
    p = Program.from_str(parse_input(data), 2)
    return validate_and_run(p)


if __name__ == '__main__':
    create_cli(9, part1=part_1, part2=part_2)
