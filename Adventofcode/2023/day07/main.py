#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Iterable
from functools import cached_property, partial
from collections import Counter
from dataclasses import dataclass
from enum import Enum

class Card:
    def __init__(self, value: str, part2 = False):
        """Create a card from a string"""
        self.value = value
        if part2:
            self._v = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'].index(value)
        else:
            self._v = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'].index(value)

    def __repr__(self):
        """Return the string representation of a card"""
        return self.value

    def __lt__(self, other: Self):
        """Compare cards less than"""
        return self._v < other._v

    def __gt__(self, other: Self):
        """Compare cards greater than"""
        return self._v > other._v

    def __eq__(self, other: Self|str):
        """Compare cards equal"""
        if isinstance(other, str):
            return self.value == other
        return self.value == other.value

    def __hash__(self):
        """Hash a card"""
        return hash(self.value)


class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand:
    cards: list[Card]
    part2: bool = False

    @cached_property
    def hand_type(self) -> HandType:
        """Return the type of hand"""
        if self.is_five_of_a_kind():
            return HandType.FIVE_OF_A_KIND
        if self.is_four_of_a_kind():
            return HandType.FOUR_OF_A_KIND
        if self.is_full_house():
            return HandType.FULL_HOUSE
        if self.is_three_of_a_kind():
            return HandType.THREE_OF_A_KIND
        if self.is_two_pair():
            return HandType.TWO_PAIR
        if self.is_pair():
            return HandType.PAIR
        return HandType.HIGH_CARD

    def is_five_of_a_kind(self) -> bool:
        """Check if hand is five of a kind"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']
            if len(c) == 0:
                # account for all jokers
                return jokers == 5

        most_common = c.most_common(1)[0][1]
        return most_common + jokers == 5

    def is_four_of_a_kind(self) -> bool:
        """Check if hand is four of a kind"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']
        most_common = c.most_common(1)[0][1]
        return most_common + jokers == 4

    def is_full_house(self) -> bool:
        """Check if hand is full house"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']

        (_, first), (_, second) = c.most_common(2)
        if self.part2:
            return first + second + jokers == 5

        return first == 3 and second == 2

    def is_three_of_a_kind(self) -> bool:
        """Check if hand is full house"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']
        most_common = c.most_common(1)[0][1]
        return most_common + jokers == 3

    def is_two_pair(self) -> bool:
        """Check if hand is two pair"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']

        (_, first), (_, second) = c.most_common(2)
        if self.part2:
            return first + second + jokers == 4
        return first == 2 and second == 2

    def is_pair(self) -> bool:
        """Check if hand is pair"""
        c = Counter(self.cards)
        jokers = 0
        if self.part2:
            jokers = c['J']
            del c['J']
        most_common = c.most_common(1)[0][1]
        return most_common + jokers == 2

    def __lt__(self, other: Self):
        """Compare hands less than"""
        if self.hand_type != other.hand_type:
            return self.hand_type.value < other.hand_type.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue
            return self_card < other_card

    def __gt__(self, other: Self):
        """Compare hands greater than"""
        if self.hand_type != other.hand_type:
            return self.hand_type.value > other.hand_type.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue
            return self_card > other_card

    def __eq__(self, other: Self):
        """Compare hands equal"""
        return (self.hand_type == other.hand_type and
                all(self_card == other_card
                    for self_card, other_card in
                    zip(self.cards, other.cards)))


def parse_input(data: Iterable[str], part2 = False) -> Iterator[[Hand, int]]:
    """Parse input data"""
    for line in data:
        if line.strip() == '':
            continue
        hand, bid = line.split(' ')
        yield Hand([Card(h, part2) for h in hand], part2), int(bid)


def total_winnings(data: Iterable[str], debug = False, part2 = False) -> int:
    """Calculate total winings from input data"""
    game = sorted(parse_input(data, part2), key=lambda x: x[0])

    if debug:
        total = 0
        for rank, (hand, bid) in enumerate(game):
            print(f'{rank + 1}: {hand} {bid}')
            total += (rank + 1) * bid
        return total

    return sum((rank + 1) * bid for rank, bid in enumerate(g[1] for g in game))


if __name__ == '__main__':
    create_cli(7, part1=total_winnings, part2=partial(total_winnings, part2=True))
