#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator, Self, Optional, Iterable
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Coord:
    x: int
    y: int

    def surrounding(self) -> Iterator[Self]:
        """Get all surrounding coordinates"""
        yield Coord(self.x - 1, self.y)
        yield Coord(self.x - 1, self.y - 1)
        yield Coord(self.x, self.y - 1)
        yield Coord(self.x + 1, self.y - 1)
        yield Coord(self.x + 1, self.y)
        yield Coord(self.x + 1, self.y + 1)
        yield Coord(self.x, self.y + 1)
        yield Coord(self.x - 1, self.y + 1)

    def __repr__(self) -> str:
        """String representation of the coordinate"""
        return f'({self.x}, {self.y})'

    def __hash__(self) -> int:
        """Hash the coordinate"""
        return hash(repr(self))


@dataclass
class Position:
    coords: list[Coord]

    def __init__(self, coords: Iterable[Coord]):
        """Create a position from a list of coordinates"""
        self.coords = list(coords)

    def surrounding(self) -> Self:
        """Get all surrounding coordinates"""
        return Position(set(c for coord in self.coords
                            for c in coord.surrounding()
                            if c not in self.coords))

    def __iter__(self) -> Iterator[Coord]:
        """Iterate over the coordinates"""
        return iter(self.coords)


@dataclass
class EngineSchematic:
    schematic: list[list[str]]
    debug: bool = False
    
    def number_positions(self) -> Iterator[Position]:
        """Get all positions of numbers"""
        for y, line in enumerate(self.schematic):
            coords = []
            for x, ch in enumerate(line):
                if ch.isdigit():
                    coords.append(Coord(x, y))
                elif len(coords) > 0:
                    yield Position(coords)
                    coords = []
            if len(coords) > 0:
                yield Position(coords)

    def is_engine_part(self, position: Position) -> bool:
        """Check if a position is an engine part"""
        return (position in self
                and all(ch.isdigit() for ch in self[position])
                and any(not ch.isdigit() and ch != '.'
                        for ch in self[position.surrounding()]))

    def engine_part_numbers(self) -> Iterator[int]:
        """Get all numbers of engine parts"""
        for position in self.number_positions():
            if self.debug:
                pos = f'{self[position]} {self[position.surrounding()]}'
                if self.is_engine_part(position):
                    print(f'{pos} (engine part)')
                else:
                    print(pos)
            if self.is_engine_part(position):
                yield int(self[position])

    def gear_part_numbers(self) -> Iterator[list[int, int]]:
        """Get all numbers of gear parts"""
        table = defaultdict(list)
        for position in self.number_positions():
            for coord in position.surrounding():
                if self[coord] == '*':
                    table[coord].append(int(self[position]))

        for numbers in table.values():
            if len(numbers) == 2:
                yield numbers

    def __contains__(self, key: Coord|Position) -> bool:
        """Check if a coordinate or position is in the schematic"""
        if isinstance(key, Position):
            return all(coord in self for coord in key.coords)

        return (key.y >= 0 and key.y < len(self.schematic)
                and key.x >= 0 and key.x < len(self.schematic[key.y]))

    def __getitem__(self, key: Coord|Position) -> Optional[str]:
        """Get the value at a given coordinate"""
        if isinstance(key, Position):
            return ''.join(self[coord] for coord in key.coords
                                       if coord in self)

        if key in self:
            return self.schematic[key.y][key.x]

    def __repr__(self) -> str:
        """String representation of the schematic"""
        return '\n'.join(''.join(line) for line in self.schematic)

    @classmethod
    def from_data(cls, data: Iterator[str], debug: bool) -> Self:
        """Create a schematic from puzzle input"""
        return cls([list(line.strip()) for line in data], debug=debug)


def part_numbers(data: Iterator[str], debug = False) -> int:
    """Sum of all part numbers in puzzle input"""
    engine_schematic = EngineSchematic.from_data(data, debug=debug)
    return sum(engine_schematic.engine_part_numbers())


def gear_parts(data: Iterator[str], debug = False) -> int:
    """Sum of all powers of gear part numbers in puzzle input"""
    engine_schematic = EngineSchematic.from_data(data, debug=debug)
    return sum(a * b for a, b in engine_schematic.gear_part_numbers())


if __name__ == '__main__':
    create_cli(3, part1=part_numbers, part2=gear_parts)
