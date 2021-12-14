#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from more_itertools import sliding_window
from collections import Counter
from functools import wraps

def cached(fn):
    """A cache decorator specially designed for the count_elements function."""
    cache = dict()
    @wraps(fn)
    def counter(*args):
        a, b = args[0]
        cache_key = a + b + str(args[2])
        if cache.get(cache_key) is None:
            cache[cache_key] = fn(*args)
        return cache[cache_key]
    return counter

@cached
def count_elements(polymer_pair: tuple[str, str], rules: dict, steps: int) -> Counter:
    """Returns a Counter for a single polymer pair after n `steps`."""
    a, b = polymer_pair
    if steps == 0:
        return Counter(a)
    return (count_elements((a, rules[a + b]), rules, steps - 1) +
            count_elements((rules[a + b], b), rules, steps - 1))


def count_polymer(polymer: str, rules: dict, steps: int) -> Counter:
    """Returns a Counter for all elements in the polymer after n `steps`."""
    c = Counter(polymer[-1])
    for a, b in sliding_window(polymer, 2):
        c += count_elements((a, b), rules, steps)
    return c


def parse_input(data: Iterator[str]) -> tuple[str, dict]:
    """Splits the given input-data into a starting polymer and a rules dict."""
    polymer = next(data).strip()
    next(data)
    rules = dict(line.strip().split(' -> ') for line in data)
    return polymer, rules


def score_polymer(data: Iterator[str], steps: int) -> int:
    """Returns the different between the max occuring elements and min occuring
    elements in a polymer (see README)."""
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
