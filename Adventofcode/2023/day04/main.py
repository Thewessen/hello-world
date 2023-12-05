#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Iterable
from dataclasses import dataclass
import re

@dataclass
class Scratchcard:
    id: int
    winning_numbers: list[int]
    available_numbers: list[int]

    def score(self) -> int:
        """Calculate the score of the scratchcard"""
        count = self.count_winning_numbers()
        if count == 0:
             return 0
        return 2 ** (count - 1)

    def count_winning_numbers(self) -> int:
        """Count the number of winning numbers on the scratchcard"""
        return sum(1 for number in self.available_numbers
                     if number in self.winning_numbers)

    def __repr__(self) -> str:
        """String representation of the coordinate"""
        return (f'Card {str(self.id)}: {" ".join(str(n) for n in self.winning_numbers)} | ' +
                f'{" ".join(str(n) for n in self.available_numbers)}')

    @classmethod
    def from_data(cls, data: str) -> Self:
        """Create a scratchcard from a string"""
        id = re.search(r'^Card +(\d+):', data).group(1)
        winning_numbers, available_numbers = data.split(' | ')
        winning_numbers = winning_numbers.split(':')[1].strip()
        return cls(int(id), [int(number) for number in re.split(' +', winning_numbers.strip())],
                            [int(number) for number in re.split(' +', available_numbers.strip())])


def parse_input(data: Iterator[str]) -> Iterator[Scratchcard]:
    """Parse puzzle input into scratchcards"""
    for line in data:
        if len(line.strip()) > 0:
            yield Scratchcard.from_data(line.strip())


def score_scratchcards(data: Iterator[str], debug = False) -> int:
    """Sum all the scores of each scratchcard in puzzle input"""
    if debug:
        for scratchcard in parse_input(data):
            print(scratchcard)
            print(scratchcard.score())
    return sum(scratchcard.score() for scratchcard in parse_input(data))


def number_of_scratchcards(data: Iterator[str], debug = False) -> int:
    """Count the number of scratchcards after copying in puzzle input"""
    number_of_scratchcards = []
    for scratchcard in parse_input(data):
        # keep max id for later use
        max_id = scratchcard.id

        if len(number_of_scratchcards) == scratchcard.id - 1:
            number_of_scratchcards.append(1)
        else:
            number_of_scratchcards[scratchcard.id - 1] += 1

        score = scratchcard.count_winning_numbers()
        count = number_of_scratchcards[scratchcard.id - 1]
        for i in range(score):
            id = scratchcard.id + i
            if len(number_of_scratchcards) == id:
                number_of_scratchcards.append(count)
            else:
                number_of_scratchcards[id] += count

    if debug:
        print(number_of_scratchcards)

    return sum(number_of_scratchcards[:max_id])

if __name__ == '__main__':
    create_cli(4, part1=score_scratchcards, part2=number_of_scratchcards)
