#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Iterable, Self, Optional
from itertools import cycle, takewhile
from functools import reduce
# from collections import Counter
# from dataclasses import dataclass
from enum import Enum

class Instruction(Enum):
    LEFT = 'L'
    RIGHT = 'R'

class Node:
    def __init__(self, value: str):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def set_left(self, node: Self):
        self.left = node

    def set_right(self, node: Self):
        self.right = node

    def __getitem__(self, key: Instruction):
        """Get node for given instruction"""
        if key == Instruction.LEFT:
            return self.left
        else:
            return self.right

    def __repr__(self):
        return f'Node({self.value}, left={self.left.value}, right={self.right.value})'

    def __hash__(self):
        return hash(self.value)


def parse_input(data: Iterable[str]) -> [Iterator[Instruction], Iterator[Node]]:
    """Parse input data"""
    instructions = next(data).strip()
    #skip blank line
    next(data)

    nodes = []
    for line in data:
        if line.strip() == '':
            break
        node, leftright = line.strip().split(' = ')
        left, right = leftright.replace('(', '').replace(')', '').split(', ')
        nodes.append((Node(node), left, right))

    for node, left, right in nodes:
        node.set_left(next(n[0] for n in nodes if n[0].value == left))
        node.set_right(next(n[0] for n in nodes if n[0].value == right))

    return (Instruction(i) for i in instructions), (n[0] for n in nodes)


def count_steps(data: Iterable[str], dedug = True) -> int:
    """Count steps for a given input"""
    instructions, nodes = parse_input(data)
    node = next(n for n in nodes if n.value == 'AAA')
    count = 0
    for instruction in cycle(instructions):
        count += 1
        if dedug:
            print(f'{instruction}: {node}')
        node = node[instruction]
        if node.value == 'ZZZ':
            break
    return count


def count_ghost_steps(data: Iterable[str], debug = False) -> int:
    """Count steps for a given input"""
    instructions, nodes = parse_input(data)
    nodes = list(n for n in nodes if n.value.endswith('A'))
    count = 0
    for instruction in cycle(instructions):
        count += 1
        if debug:
            print(f'{instruction}: {nodes}')
        nodes = [n[instruction] for n in nodes]
        if all(n.value.endswith('Z') for n in nodes):
            break
    return count


if __name__ == '__main__':
    create_cli(8, part1=count_steps, part2=count_ghost_steps)
