#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from typing import Iterator, Optional
from itertools import permutations, cycle


def pipe_amplifiers(p: str, settings: tuple[int, ...]) -> int:
    out = 0
    for s in settings:
        out = Program.from_str(p, s, out).run()
        if out is None:
            raise ValueError('Unexpected output from amplifier')
    return out


def part_1(data: Iterator[str]) -> int:
    """Solution part 1 (see Readme)"""
    p = next(data)
    return max(pipe_amplifiers(p, settings)
               for settings in permutations(range(5)))


def create_feedback_loop(program: str, settings: tuple[int, ...]) -> Optional[int]:
    amplifiers = list()
    out = 0
    for s in settings:
        a = Program.from_str(program, s, out)
        amplifiers.append(a)
        out = a.jump()
    for amplifier in cycle(amplifiers):
        amplifier.args.append(out)
        try:
            out = amplifier.jump()
        except StopIteration:
            return out


def part_2(data: Iterator[str]) -> int:
    """Solution part 2 (see Readme)"""
    p = next(data)
    return max(create_feedback_loop(p, settings) or 0
               for settings in permutations(range(5, 10)))


if __name__ == '__main__':
    create_cli(7, part1=part_1, part2=part_2)
