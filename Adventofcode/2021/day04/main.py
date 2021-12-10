#!/usr/bin/env python3

import re
from argparse import ArgumentParser
from typing import Iterator, Generator, Optional, Callable
from itertools import groupby


class BingoCard:
    """A 5x5 card containing some given numbers."""
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
            for n in row:
                yield n


class FilledBingoCard(BingoCard):
    """A 5x5 card where bingo is reach after x numbers are drawn."""
    def __init__(self, card, numbers: list[int]):
        super().__init__(card)
        self._filled = []
        bingo = self._bingo()
        bingo.send(None)
        for n in numbers:
            if bingo.send(n):
                break

    def _bingo(self) -> Generator[bool, Optional[int], None]:
        while True:
            n = yield self.has_bingo()
            self._filled.append(n)

    def turns(self):
        return len(self._filled)

    def has_bingo(self) -> bool:
        def is_filled(line):
            return all(map(lambda i: i in self._filled, line))

        return (any(is_filled(row) for row in self.get_rows())
                or any(is_filled(column) for column in self.get_columns()))

    def score(self):
        unfilled = filter(lambda n: n not in self._filled, self.get_numbers())
        return sum(unfilled) * self._filled[-1]



def get_cards(data: Iterator[str]) -> Iterator[list[list[int]]]:
    """Yields all containing 5x5 bingo cards in given data.
    Assumes the data contains only bingo cards."""
    for card in (g for k, g in groupby(data, lambda line: line != '\n') if k):
        yield [[int(d) for d in re.findall(r'\d+', row)] for row in card]
        

def parse_input(data: Iterator[str])\
-> tuple[list[int], Iterator[list[list[int]]]]:
    """Splits data in drawn numbers and bingo cards"""
    numbers = [int(x) for x in next(data).split(',')]
    next(data)
    return numbers, get_cards(data)


def get_card(data: Iterator[str], pred: Callable) -> FilledBingoCard:
    """Pick a filled bingo card by min (best) or max (least best) turns until
    bingo. (see README)"""
    numbers, cards = parse_input(data)
    return pred((FilledBingoCard(card, numbers) for card in cards),
                key=lambda c: c.turns())


def main():
    parser = ArgumentParser(description="Day 4 solution")
    parser.add_argument('path', nargs='?', type=str, default='./input',
                        help="The path to the input file (default: ./input)")
    parser.add_argument('-2', '--part2', action='store_true',
                        help=("Print the solution for part 2 "
                              "(default: part 1 is printed)"))
    args = parser.parse_args()

    with open(args.path, 'r') as data:
        if args.part2:
            card = get_card(data, max)
        else:
            card = get_card(data, min)
    print(card.score())


if __name__ == '__main__':
    main()
