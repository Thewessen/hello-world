#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterable

class BaseSubState:
    """Basic submarine state
    horiz: int
        horizontal position of the submarine
    depth: int
        depth of the submarine
    inc. some instruction for moving forward, up and down
    (see. README part 1)
    """
    def __init__(self, horiz: int, depth: int):
        self.horiz = horiz
        self.depth = depth

    def __eq__(self, p):
        return self.horiz == p.horiz and self.depth == p.depth

    def __repr__(self):
        return f'BaseSubState {{ horiz: {self.horiz}, depth: {self.depth} }}'

    def forward(self, s: int):
        """Increases horizontal position by s"""
        self.horiz += s

    def up(self, s: int):
        """Decreases depth by s"""
        self.depth -= s

    def down(self, s: int):
        """Increases depth by s"""
        self.depth += s

    def process_instructions(self, instructions: Iterable):
        """Calls corresponding class method for each instruction"""
        for instr in instructions:
            d, s = instr.split(' ')
            if hasattr(self, d):
                getattr(self, d)(int(s))
            else:
                print(f'Unknown instruction {d}. Terminating...')
                exit(1)

    def sol(self) -> int:
        """Returns the solution of the current state"""
        return self.horiz * self.depth


class AdvSubState(BaseSubState):
    """Advanced submarine state
    ...all props from basic submarine state
    aim: int
        the aim of the submarine
    the instruction for forward, up and down are changed
    (see. README part 2)
    """
    def __init__(self, horiz: int, depth: int, aim: int):
        super().__init__(horiz, depth)
        self.aim = aim

    def __repr__(self):
        return ('AdvSubState {'
                f' horiz: {self.horiz},'
                f' depth: {self.depth},'
                f' aim: {self.aim} }}')

    def forward(self, s: int):
        """Increases forward position by s and depth my aim * s"""
        self.horiz += s
        self.depth += s * self.aim

    def up(self, s: int):
        """Decreases aim by s"""
        self.aim -= s

    def down(self, s: int):
        """Increases aim by s"""
        self.aim += s



def main():
    parser = ArgumentParser(description="Day 2 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    parser.add_argument('-v', '--verbose', action='store_true',
                        help=("Also prints the last state of the submarine"
                              "(default: False)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            state = AdvSubState(0, 0, 0)
            state.process_instructions(data.readlines())
        else:
            state = BaseSubState(0, 0)
            state.process_instructions(data.readlines())

    if args.verbose:
        print(state)
    print(state.sol())


if __name__ == '__main__':
    main()
