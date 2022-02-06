#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, List
from itertools import count, tee, product


def parse_input(data: str) -> List[int]:
    """Parses module mass from puzzle input"""
    return [int(n) for n in data.split(',')]


def program(mem: List[int]) -> List[int]:
    """Executes an int list of memory and returns the memory after the program
    finishes. Mutates the memory."""
    for c in count(0, 4):
        op = mem[c]
        if op == 99:
            break
        a = mem[mem[c + 1]]
        b = mem[mem[c + 2]]
        if op == 1:
            mem[mem[c + 3]] = a + b
        elif op == 2:
            mem[mem[c + 3]] = a * b
        else:
            raise ValueError(f"Unknown opcode {op}")
    return mem


def program_init_state(mem: List[int], noun = 12, verb = 2) -> List[int]:
    """Initializes memory with given state. Defaults to the 1202 program alarm
    state (see README part 1)"""
    mem[1] = noun
    mem[2] = verb
    return mem


def solve_puzzle(data: Iterator[str], noun = 12, verb = 2) -> int:
    """Restore state and run program. Return first opcode."""
    mem = parse_input(next(data))
    mem = program_init_state(mem, noun, verb)
    mem = program(mem)
    return mem[0]


def solve_part_2(data: Iterator[str]) -> int:
    for noun, verb in product(range(100), range(100)):
        data, origin = tee(data)
        ans = solve_puzzle(origin, noun, verb)
        if ans == 19690720:
            return 100 * noun + verb
    raise ValueError('Not encountered the correct noun and verb')


if __name__ == '__main__':
    create_cli(2, part1=solve_puzzle, part2=solve_part_2)
