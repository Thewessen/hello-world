#!/usr/bin/env python3

from argparse import ArgumentParser
from typing import Iterable, Optional
from copy import copy

class Cave:
    def __init__(self, cat: str, spots: tuple):
        self.cat = cat
        self.spots = spots

    @property
    def completed(self) -> bool:
        return all(timid == self.cat for timid in self.spots)

    @property
    def depth(self) -> int:
        return len(self.spots)

    def first_available(self) -> Optional[str]:
        for spot in self.spots:
            if isinstance(spot, str):
                return spot

    def __lt__(self, other):
        return self.cat < other.cat
        

class TimidPuzzle:
    def __init__(self, caves: list[Cave], spots: dict, energy: int):
        self.caves = caves
        self.depth = max(cave.depth for cave in caves)
        self.spots = spots
        self.energy = energy

    @classmethod
    def empty(cls, depth: int):
        caves = [Cave('A', (None,) * depth),
                 Cave('B', (None,) * depth),
                 Cave('C', (None,) * depth),
                 Cave('D', (None,) * depth)]
        spots = { k: '.' for k in range(7) }
        return cls(caves, spots, 0)

    def fill(self, caves: Iterable[Iterable[str]]):
        for i, cave in enumerate(caves):
            self.caves[i].spots = tuple(cave)


    def __repr__(self):
        rpr = f'Score: {self.energy}'
        rpr = '#' * 13 + '\n'
        rpr += (
            f'#{self.spots[0]}{self.spots[1]}'
            f'.{self.spots[2]}.{self.spots[3]}'
            f'.{self.spots[4]}.'
            f'{self.spots[5]}{self.spots[6]}#' + '\n')
        rpr += ('#' * 3 +
                '#'.join([(self.caves[c].spots[self.depth - 1] or '.'
                          if self.depth - 1 < self.caves[c].depth
                          else '.') for c in range(4)]) +
                '#' * 3 + '\n')
        rpr += ('  #' +
                '#'.join([(self.caves[c].spots[self.depth - i - 2] or '.'
                          if self.depth - i - 2 < self.caves[c].depth
                          else '.') for c in range(4) for i in range(self.depth - 1)]) +
                '#  ' + '\n')
        rpr += '  ' + '#' * 9 + '  '
        return rpr

    def can_move(self, s, f):
        if s == f:
            return True
        if abs(s - f) == 1:
            return self.spots[max(s, f) + 1] == '.'
        mn = min(s, f)
        return (self.can_move(mn, mn + 1)
                and self.can_move(mn + 1, max(s, f)))

    def next_available(self):
        for i, cave in enumerate(self.caves):
            timid = cave.first_available()
            if timid is None:
                continue
            for spot in self.spots.keys():
                if self.can_move(i, spot):
                    new_spots = copy(self.spots)
                    new_spots[spot] = timid
                    return 

def main():
    parser = ArgumentParser(description="Day 23 solution")
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
            t = TimidPuzzle.empty(2).fill([
                ['A', 'B'],
                ['D', 'C'],
                ['C', 'B'],
                ['A', 'D'],
            ])
            print(t)


if __name__ == '__main__':
    main()
