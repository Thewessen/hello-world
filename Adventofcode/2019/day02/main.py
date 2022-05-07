#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from typing import Iterator
from itertools import tee, product
from more_itertools import consume


def program_init_state(program: Program, noun = 12, verb = 2) -> None:
    """Initializes memory with given state. Defaults to the 1202 program alarm
    state (see README part 1)"""
    program.mem.write(1, noun)
    program.mem.write(2, verb)


def solve_puzzle(data: Iterator[str], noun = 12, verb = 2) -> int:
    """Restore state and run program. Return first opcode."""
    program = Program.from_str(next(data))
    program_init_state(program, noun, verb)
    consume(program)
    return program.mem.read(0)


def solve_part_2(data: Iterator[str]) -> int:
    for noun, verb in product(range(100), range(100)):
        data, origin = tee(data)
        ans = solve_puzzle(origin, noun, verb)
        if ans == 19690720:
            return 100 * noun + verb
    raise ValueError('Not encountered the correct noun and verb')


if __name__ == '__main__':
    create_cli(2, part1=solve_puzzle, part2=solve_part_2)
