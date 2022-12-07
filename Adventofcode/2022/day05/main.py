#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import takewhile, zip_longest
from more_itertools import chunked
from dataclasses import dataclass
import re


@dataclass
class Instruction:
    move: int
    targ: int
    dest: int

    @classmethod
    def from_str(cls, line: str):
        move, targ, dest = re.findall(r"\d+", line)
        return cls(int(move), int(targ), int(dest))


@dataclass
class Cargo:
    setup: dict

    def __repr__(self):
        return '\n'.join(f"{key}: {' '.join(stack)}"
                         for key, stack in self.setup.items())

    def move(self, instruct):
        crate = self.setup[instruct.targ].pop()
        self.setup[instruct.dest].append(crate)

    def move_at_once(self, instruct):
        stack = self.setup[instruct.targ]
        self.setup[instruct.targ] = stack[:-1 * instruct.move]
        self.setup[instruct.dest] += stack[-1 * instruct.move:]

    def top_boxes(self):
        return ''.join(stack[-1] for stack in self.setup.values())


def parse_input(data: Iterator[str]) -> tuple[Cargo, Iterator[Instruction]]:
    """Get initial setup and instruction from input"""
    setup_data = list(takewhile(lambda line: line.strip() != '', data))
    indexes = (int(char) for char in setup_data.pop().strip()
                         if char != ' ')
    lines = ([''.join(crate)
                .strip()
                .replace('[', '')
                .replace(']', '')
              for crate in chunked(line, 4)]
             for line in setup_data)

    stacks = zip_longest(indexes, *lines, fillvalue='')
    setup = {
        index: list(reversed([crate for crate in stack if crate != '']))
        for [index, *stack] in stacks
    }

    return Cargo(setup), (Instruction.from_str(line.strip())
                          for line in data
                          if line.strip() != '')


def top_boxes_9000_instructions(data: Iterator[str]) -> str:
    """Read the top boxes of each stack after moving with CrateMove 9000 (part 1)"""
    cargo, instructions = parse_input(data)
    for instruct in instructions:
        for i in range(instruct.move):
            cargo.move(instruct)
    return cargo.top_boxes()


def top_boxes_9001_instructions(data: Iterator[str]) -> str:
    """Read the top boxes of each stack after moving with CrateMove 9001 (part 2)"""
    cargo, instructions = parse_input(data)
    for instruct in instructions:
        cargo.move_at_once(instruct)
    return cargo.top_boxes()


if __name__ == '__main__':
    create_cli(5, part1=top_boxes_9000_instructions, part2=top_boxes_9001_instructions)
