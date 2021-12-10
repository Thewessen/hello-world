#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterator
from itertools import permutations


def parse_input(data: Iterator[str]) -> Iterator[tuple[list[str], list[str]]]:
    """Data is split into input and output, each containing a list of
    corresponding segments"""
    for line in data:
        inp, out = line.split(' | ')
        yield ([i.strip() for i in inp.split(' ')],
               [o.strip() for o in out.split(' ')])


def count_easy_digits(data: Iterator[str]) -> int:
    """Count how many entries in data are easy digits to recognize.
    Considering only the unique segment counts for digit 1, 4, 7 and 8.
    (see README part 1)"""
    one = 'cf'
    four = 'bcdf' 
    seven = 'acf'
    eight = 'abcdefg'
    lengths = (len(one), len(four), len(seven), len(eight))
    count = 0
    for _, output in parse_input(data):
        count += sum(len(o) in lengths for o in output)
    return count


def solution_part_2(data: Iterator[str]) -> int:
    """Sums all digits for output in data.
    (see README part 2)"""
    return sum(decipher_output(inp, out)
               for inp, out in parse_input(data))


def decipher_output(inp: list[str], out: list[str]) -> int:
    """Tries to find a fitting translation wichs translates all segments in
    data-input to corresponding valid digits, returns the translation of the
    output"""
    for p in permutations('abcdefg'):
        trans = ''.maketrans(''.join(p), 'abcdefg')
        if all(parse_digits(i.translate(trans) for i in inp)):
            return int(''.join(parse_digits(o.translate(trans) for o in out)))
    print('No translation found!')
    exit(1)


def parse_digits(data: Iterator[str]) -> Iterator[str]:
    """All digits have a unique combination of active segments.
    Returns the corresponding digit if found, else an empty string is
    returned."""
    digits = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }
    for line in data:
        yield digits.get(''.join(sorted(line)), '')


def main():
    parser = ArgumentParser(description="Day 8 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            r = solution_part_2(data)
        else:
            r = count_easy_digits(data)
    print(r)


if __name__ == '__main__':
    main()
