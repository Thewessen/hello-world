#!/usr/bin/env python3

import re
from argparse import ArgumentParser
from typing import Iterator, Generator, Optional
from itertools import groupby


class BingoCard:
    def __init__(self, card):
        if len(card) != 5 or any(len(row) != 5 for row in card):
            print('Invalid bingo card', card)
            exit(1)
        self._card = card

    def get_rows(self):
        for row in self._card:
            yield row

    def get_columns(self) -> Iterator[tuple[int]]:
        for column in zip(*self._card):
            yield column

    def get_numbers(self):
        for row in self.get_rows():
            for number in row:
                yield number


class FilledBingoCard(BingoCard):
    def __init__(self, card, numbers: list[int]):
        super().__init__(card)
        self._numbers = []
        bingo = self._bingo()
        bingo.send(None)
        for n in numbers:
            if bingo.send(n):
                break

    def _bingo(self) -> Generator[bool, Optional[int], None]:
        while True:
            n = yield self.has_bingo()
            self._numbers.append(n)

    def turns(self):
        return len(self._numbers)

    def has_bingo(self) -> bool:
        def can_fill(line):
            return all(map(lambda i: i in self._numbers, line))

        return (any(can_fill(row) for row in self.get_rows())
                or any(can_fill(column) for column in self.get_columns()))

    def score(self):
        return (sum(filter(lambda n: n not in self._numbers,
                           self.get_numbers()))
                * self._numbers[-1])



def chunk(pred, it):
    l = []
    for value in it:
        if pred(value):
            yield l
            l = []
        else:
            l.append(value)


def get_cards(data: Iterator[str]) -> Iterator[list[list[int]]]:
    for card in (g for k, g in groupby(data, lambda line: line != '\n') if k):
        num_card = []
        for row in card:
            num_card.append([int(d) for d in re.findall(r'\d+', row)])
        yield num_card
        

def parse_input(data: Iterator[str])\
-> tuple[list[int], Iterator[list[list[int]]]]:
    numbers = list(map(lambda x: int(x), next(data).split(',')))
    next(data)
    return numbers, get_cards(data)


def get_best_card(data: Iterator[str]) -> FilledBingoCard:
    numbers, cards = parse_input(data)
    best = min(map(lambda card: FilledBingoCard(card, numbers), cards),
                key=lambda c: c.turns())
    return best


def get_least_best_card(data: Iterator[str]) -> FilledBingoCard:
    numbers, cards = parse_input(data)
    least = max(map(lambda card: FilledBingoCard(card, numbers), cards),
                key=lambda c: c.turns())
    return least


def main():
    parser = ArgumentParser(description="Day 2 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            card = get_least_best_card(data)
        else:
            card = get_best_card(data)
    print(card.score())


if __name__ == '__main__':
    main()
