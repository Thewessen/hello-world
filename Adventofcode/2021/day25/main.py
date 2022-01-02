#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterable
from more_itertools import consume


class SeaCucumbers:
    def __init__(self, school = list[list[str]]):
        self.school = school
        self.width = max(len(row) for row in self.school);
        self.height = len(self.school)
        self.moves = 0

    @classmethod
    def from_iter(cls, data: Iterable[str]):
        return cls([list(line.strip()) for line in data])

    def get(self, x, y):
        return self.school[y % self.height][x % self.width]

    def set(self, x, y, ch):
        self.school[y % self.height][x % self.width] = ch

    def __repr__(self):
        return ''.join([''.join(row) + '\n' for row in self.school])

    def __iter__(self):
        return self

    def __next__(self):
        new_school = SeaCucumbers.from_iter(['.' * self.width] * self.height)
        moved = 0
        self.moves += 1
        for y in range(self.height):
            for x in range(self.width):
                d = self.get(x, y)
                if d == '>' and self.get(x + 1, y) == '.':
                    moved += 1
                    new_school.set(x + 1, y, '>')
                elif d == '>':
                    new_school.set(x, y, '>')

        for y in range(self.height):
            for x in range(self.width):
                d = self.get(x, y)
                if (d == 'v'
                    and self.get(x, y + 1) != 'v'
                    and new_school.get(x, y + 1) == '.'):
                    moved += 1
                    new_school.set(x, y + 1, 'v')
                elif d == 'v':
                    new_school.set(x, y, 'v')

        if moved == 0:
            raise StopIteration('school finished moving')
        self.school = new_school.school


def main():
    parser = ArgumentParser(description="Day 25 solution")
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
            r = SeaCucumbers.from_iter(data)
    consume(r)
    print(r.moves)


if __name__ == '__main__':
    main()
