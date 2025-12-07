import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from functools import reduce
from itertools import zip_longest
from operator import add, mul
import re

def parse_input(input: Iterator[str], debug: bool = False) -> Iterator[str]:
    for line in input:
        yield re.split(r'\s+', line.strip())

def grand_total(input: Iterator[str], debug: bool = False) -> int:
    total = 0
    for column in zip(*parse_input(input, debug=debug)):
        problem = reversed(column)
        operant = next(problem)
        numbers = list(map(int, problem))
        if debug:
            print(f'{operant}: {numbers}')
        func = { '+': add, '*': mul }[operant]
        total += reduce(func, numbers)
    return total

def parse_columns(input: Iterator[str], debug: bool = False) -> Iterator[tuple]:
    columns = []
    for column in zip_longest(*input, fillvalue=' '):
        if all(c == ' ' or c == '\n' for c in column):
            yield columns
            columns = []
        else:
            columns.append(column)
    yield columns

def parse_input_part_2(input: Iterator[str], debug: bool = False) -> Iterator[tuple[str,list[int]]]:
    for column in parse_columns(input, debug=debug):
        operant = None
        numbers = []
        for row in reversed(column):
            n = ''.join(row[:-1])
            numbers.append(int(n.strip()))
            if row[-1] != ' ':
                operant = row[-1]
        if operant is not None:
            if debug:
                print(f'{operant}: {numbers}')
            yield operant, numbers

def grand_total_part_2(input: Iterator[str], debug: bool = False) -> int:
    total = 0
    for operant, numbers in parse_input_part_2(input, debug=debug):
        func = { '+': add, '*': mul }[operant]
        total += reduce(func, numbers)
    return total

if __name__ == '__main__':
    create_cli(6, part1=grand_total, part2=grand_total_part_2)
