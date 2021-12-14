#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from more_itertools import sliding_window
from collections import Counter

def count_elements(polymer: tuple[str, str], rules: dict, steps: int) -> Counter:
    a, b = polymer
    if steps == 0:
        return Counter(a)
    return (count_elements((a, rules[a + b]), rules, steps - 1) +
            count_elements((rules[a + b], b), rules, steps - 1))


def count_polymer(polymer: str, rules: dict, steps: int) -> Counter:
    c = Counter(polymer[-1])
    for a, b in sliding_window(polymer, 2):
        c += count_elements((a, b), rules, steps)
    return c


def parse_input(data: Iterator[str]) -> tuple[str, dict]:
    polymer = next(data).strip()
    next(data)
    rules = dict()
    for line in data:
        k, v = line.strip().split(' -> ')
        rules[k] = v
    return polymer, rules


# def apply_pair_insertion(p: Iterator[str], rules: dict) -> Iterator[str]:
#     inc_first = True
#     for a, b in sliding_window(p, 2):
#         if inc_first:
#             yield a
#         yield rules[a + b]
#         yield b
#         inc_first = False
    

# def pair_insertion(data: Iterator[str], steps: int) -> Iterator[str]:
#     polymer, rules = parse_input(data)
#     for _ in range(steps):
#         polymer = apply_pair_insertion(polymer, rules)
#     return polymer
    
def score_polymer(data: Iterator[str], steps: int) -> int:
    polymer, rules = parse_input(data)
    c = count_polymer(polymer, rules, steps)
    return max(c.values()) - min(c.values())


def main():
    parser = ArgumentParser(description="Day 14 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = score_polymer(data, 40)
        else:
            r = score_polymer(data, 10)
        print(r)


if __name__ == '__main__':
    main()
