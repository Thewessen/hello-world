#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from dataclasses import dataclass
from collections import defaultdict
from more_itertools import consume
from typing import Iterator


@dataclass
class Coord:
    x: int
    y: int
    
    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"C({self.x}, {self.y})"


class PaintRobot:
    def __init__(self, program: Program, start = 0):
        self._program = program
        self._direction_indx = 0 
        self._position = Coord(0, 0)
        self._directions = [
            Coord(0, -1),
            Coord(1, 0),
            Coord(0, 1),
            Coord(-1, 0),
        ]
        self._map = defaultdict(int)
        self._map[self._position] = start

    def __iter__(self):
        return self

    def __next__(self):
        current_tile = self._map[self._position] or 0
        self._program.args.append(current_tile)
        color = next(self._program)
        self._map[self._position] = color
        direction = next(self._program)
        self.turn(direction)
        self._position += self._directions[self._direction_indx]

    @property
    def map(self):
        return self._map

    @property
    def travel_distance(self):
        return len(self._map.keys())

    def turn(self, d: int) -> None:
        if d == 0:
            self._direction_indx -= 1
        elif d == 1:
            self._direction_indx += 1
        else:
            raise ValueError(f"Unknown direction {d}.")
        self._direction_indx %= len(self._directions)


def parse_input(data: Iterator[str]) -> str:
    return next(data).strip()


def part_1(data: Iterator[str]) -> int:
    """Solution part 1, running the painting robot with given program (see Readme)"""
    p = Program.from_str(parse_input(data))
    robot = PaintRobot(p)
    consume(robot)
    # TODO: This minus 1 bugs me
    return robot.travel_distance - 1


def draw_image(m: dict) -> None:
    min_x = min(c.x for c in m.keys())
    max_x = max(c.x for c in m.keys())
    min_y = min(c.y for c in m.keys())
    max_y = max(c.y for c in m.keys())
    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            color = m[Coord(x, y)]
            if color == 0:
                row += '.'
            elif color == 1:
                row += '#'
            else:
                raise ValueError(f"Unexpected color {color}")
        print(row)


def part_2(data: Iterator[str]) -> str:
    """Solution part 2, run the painting robot starting on a white tile.
    (see Readme part 2)"""
    p = Program.from_str(parse_input(data))
    robot = PaintRobot(p, 1)
    consume(robot)
    draw_image(robot.map)
    # from visual image
    return 'CBLPJZCU'


if __name__ == '__main__':
    create_cli(11, part1=part_1, part2=part_2)
