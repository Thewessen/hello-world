#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator, Iterable
from dataclasses import dataclass, field
from functools import wraps, reduce
from operator import attrgetter
from more_itertools import consume
import re

def read(r, regs: dict):
    if r in regs.keys():
        return regs[r]
    if isinstance(r, str):
        return int(r)
    raise ValueError(f'Failed reading {r}')

def write(r, v, regs: dict):
    if not isinstance(v, int) or 9 < v < 1 or r not in regs.keys():
        raise ValueError(f'Failed writing {r}')
    regs[r] = v

def inp_instr(regs, r):
    def instr(inp):
        v = int(next(inp))
        write(r, v, regs)
    return instr

def add_instr(regs, a, b):
    def instr(inp):
        v = read(a, regs) + read(b, regs)
        write(a, v, regs)
    return instr

def mul_instr(regs, a, b):
    def instr(inp):
        v = read(a, regs) * read(b, regs)
        write(a, v, regs)
    return instr

def div_instr(regs, a, b):
    def instr(inp):
        v = int(read(a, regs) / read(b, regs))
        write(a, v, regs)
    return instr

def mod_instr(regs, a, b):
    def instr(inp):
        v = read(a, regs) % read(b, regs)
        write(a, v, regs)
    return instr

def eql_instr(regs, a, b):
    def instr(inp):
        v = int(read(a, regs) == read(b, regs))
        write(a, v, regs)
    return instr

def parse_program(data: Iterable[str], regs):
    for line in data:
        opr, *args = line.strip().split(' ')
        yield {
            'inp': inp_instr,
            'add': add_instr,
            'mul': mul_instr,
            'div': div_instr,
            'mod': mod_instr,
            'eql': eql_instr,
        }[opr](regs, *args)


def exec_program(instr: Iterable[str], inp: str):
    v = iter(inp)
    regs = {"w": 0, "x": 0, "y": 0, "z": 0 }
    consume(fn(v) for fn in parse_program(instr, regs))
    return regs


def largest_valid_number(data: Iterator[str]) -> int:
    instr = list(data)
    for n in range(10 ** 14 - 1, 10 ** 13, -1):
        inp = str(n)
        if '0' in inp:
            continue
        print(inp)
        r = exec_program(instr, inp)
        if r['z'] == 0:
            return int(n)
    raise ValueError('No valid MONAD number found')


def main():
    parser = ArgumentParser(description="Day 24 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open('./input', 'r') as data:
        if args.part2:
            exit(1)
        else:
            n = largest_valid_number(data)
    print(n)


if __name__ == '__main__':
    main()
