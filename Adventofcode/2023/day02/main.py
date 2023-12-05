#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self
from dataclasses import dataclass
import re

@dataclass
class Set:
    """A hand full of cubes"""
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_valid(self) -> bool:
        """Check if the set is valid"""
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    @classmethod
    def from_str(cls, line: str) -> Self:
        """Create a set from a string"""
        red_search = re.search('(\d+) red', line)
        green_search = re.search('(\d+) green', line)
        blue_search = re.search('(\d+) blue', line)
        red = int(red_search.group(1)) if red_search is not None else 0
        green = int(green_search.group(1)) if green_search is not None else 0
        blue = int(blue_search.group(1)) if blue_search is not None else 0
        return cls(red, green, blue)

    def power(self) -> int:
        """Calculate the power of the set"""
        return self.red * self.green * self.blue

    def __repr__(self) -> str:
        """String representation of the set"""
        return f'(red: {self.red}, green: {self.green}, blue: {self.blue})'


@dataclass
class Game:
    id: int
    sets: list[Set]

    def is_valid(self) -> bool:
        """Check if the game is valid"""
        return all(set.is_valid() for set in self.sets)
    
    @classmethod
    def from_data(cls, line: str) -> Self:
        """Create a game from puzzle input"""
        search_id = re.search('Game (\d+)', line)
        if search_id is None:
            raise ValueError('Invalid game data')

        id = int(search_id.group(1))

        sets = []
        for s in line.split(';'):
            sets.append(Set.from_str(s))

        return cls(id, sets)

    def least_valid(self) -> Set:
        """Find the least valid set"""
        red = max(s.red for s in self.sets)
        green = max(s.green for s in self.sets)
        blue = max(s.blue for s in self.sets)
        return Set(red, green, blue)

    def __repr__(self) -> str:
        """String representation of the game"""
        return f'Game {self.id}: {self.sets}'


def parse_input(data: Iterator[str]) -> Iterator[Game]:
    """Parse Games from puzzle input"""
    for line in data:
        if len(line.strip()) == 0:
            continue
        yield Game.from_data(line.strip())


def valid_games(data: Iterator[str]) -> int:
    """Filter out invalid games"""
    return sum(game.id for game in parse_input(data)
                       if game.is_valid())


def power_of_games(data: Iterator[str]) -> int:
    """Calculate the power of valid games"""
    return sum(game.least_valid().power() for game in parse_input(data))
                                          

if __name__ == '__main__':
    create_cli(2, part1=valid_games, part2=power_of_games)
