#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from enum import Enum
from typing import Iterator

class ParamMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Memory:
    """Base memory object with read and write methods.
    Includes mode option for reading"""
    def __init__(self, mem: list[str]):
        self.mem = list(mem)

    def read(self, address: int, mode = ParamMode.IMMEDIATE) -> int:
        a = self.mem[address]
        if mode == ParamMode.IMMEDIATE:
            return int(a)
        return int(self.mem[int(a)])

    def write(self, address: int, value: int):
        self.mem[address] = str(value)


class Program:
    """Base program object"""
    def __init__(self, mem: list[str], *args):
        self.mem = Memory(mem)
        self.pointer = 0
        self.args = args
    
    def __iter__(self):
        return self
    
    def __next__(self):
        i = int(self.opcode[-2:])
        if i == 1:
            self.sum()
        if i == 2:
            self.prod()
        if i == 3:
            self.inp()
        if i == 4:
            return self.out()
        if i == 5:
            self.jump_if_true()
        if i == 6:
            self.jump_if_false()
        if i == 7:
            self.less_than()
        if i == 8:
            self.equals()
        if i == 99:
            raise StopIteration("End of program")

    @property
    def opcode(self):
        op = str(self.mem.read(self.pointer))
        return op.rjust(6, '0')

    def sum(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, a + b)
        self.pointer += 4

    def prod(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, a * b)
        self.pointer += 4

    def inp(self):
        [value, *args] = self.args
        self.args = args
        address = self.mem.read(self.pointer + 1)
        self.mem.write(address, value)
        self.pointer += 2

    def out(self):
        output = self._get_param(1)
        self.pointer += 2
        return output

    def jump_if_true(self):
        value = self._get_param(1)
        if value == 0:
            self.pointer += 3
            return
        address = self._get_param(2)
        self.pointer = address

    def jump_if_false(self):
        value = self._get_param(1)
        if value != 0:
            self.pointer += 3
            return
        address = self._get_param(2)
        self.pointer = address

    def less_than(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, int(a < b))
        self.pointer += 4

    def equals(self):
        a = self._get_param(1)
        b = self._get_param(2)
        address = self.mem.read(self.pointer + 3)
        self.mem.write(address, int(a == b))
        self.pointer += 4
    
    def _get_param(self, nr: int) -> int:
        address = self.pointer + nr
        mode = ParamMode(int(self.opcode[-1 * nr - 2]))
        return self.mem.read(address, mode)


def parse_input(data: Iterator[str]) -> list[str]:
    """Returns the given program as memory (list of str)."""
    return next(data).split(',')


def diagnostic_program(data: Iterator[str], *args) -> int:
    """Runs the program for a given input data,
    and checks intermediate results (see Readme)"""
    prog = Program(parse_input(data), *args)
    result = 0
    for inst in prog:
        # check last result
        if type(inst) == int and inst is not None:
            if result != 0:
                raise ValueError(("Intermediate result none zero"
                                  "Test program failed."))
            result = inst
    return result


def part_1(data: Iterator[str]) -> int:
    """Solution part 1 (see Readme)"""
    return diagnostic_program(data, 1)


def part_2(data: Iterator[str]) -> int:
    """Solution part 2 (see Readme)"""
    return diagnostic_program(data, 5)


if __name__ == '__main__':
    create_cli(5, part1=part_1, part2=part_2)
