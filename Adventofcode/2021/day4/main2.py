#!/usr/bin/env python3

import re
from argparse import ArgumentParser
from typing import Iterator, Optional, Callable
from itertools import groupby
from functools import partial

BingoCard = list[list[int]] 

def has_bingo(card: BingoCard, filled: list[int]) -> bool:
    """Calculates if a bingocard has bingo given the numbers filled"""
    def is_filled(line):
        return all(map(lambda i: i in filled, line))

    return (any(is_filled(row) for row in card)
            or any(is_filled(column) for column in zip(*card)))

def unfilled(card: BingoCard, filled: list[int]) -> Iterator[int]:
    """Yields the unfilled numbers of a bingo card."""
    for row in card:
        for n in row:
            if n not in filled:
                yield n

def calc_turns_score(card: BingoCard, numbers: list[int]) -> Optional[tuple[int, int]]:
    """Calculates the given number of turns until a bingo card gives bingo,
    followed by the score needed for the solution (see README)."""
    filled = []
    for n in numbers:
        filled.append(n)
        if has_bingo(card, filled):
            return len(filled), sum(unfilled(card, filled)) * filled[-1]

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


def get_card_score(data: Iterator[str], pred: Callable) -> Optional[tuple[int, int]]:
    """Pick a filled bingo card by min (best) or max (least best) turns until
    bingo. (see README)"""
    numbers, cards = parse_input(data)
    fn = partial(calc_turns_score, numbers=numbers)
    _, score = pred((fn(card) for card in cards),
                    key=lambda c: c[0])
    return score


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
            r = get_card_score(data, max)
        else:
            r = get_card_score(data, min)
    print(r)


if __name__ == '__main__':
    main()
