#!/usr/bin/env python3

import sys
sys.path.append('..')
sys.path.append('../intcode_computer')
from cli import create_cli
from Program import Program
from typing import Iterator
from enum import IntEnum


class Tile(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Joystick(IntEnum):
    LEFT = -1
    RIGHT = 1
    NEUTRAL = 0


class Screen:
    def __init__(self):
        self.screen = [[]]
        self.score = 0

    def __repr__(self):
        return ('\n'.join(''.join(line)
                       for line in self.screen) +
                f'\nSCORE={self.score}')
    
    def set(self, x: int, y: int, value: str):
        while y > len(self.screen) - 1:
            self.screen.append([])
        while x > len(self.screen[y]) - 1:
            self.screen[y].append(' ')
        self.screen[y][x] = value


def parse_input(data: Iterator[str]) -> str:
    return next(data).strip()


def translate_tile(t: Tile) -> str:
    if t == Tile.EMPTY:
        return ' '
    if t == Tile.WALL:
        return '|'
    if t == Tile.BLOCK:
        return 'x'
    if t == Tile.PADDLE:
        return '-'
    if t == Tile.BALL:
        return 'o'
    raise ValueError(f'Unknown tile to translate: {t}')


def part_1(data: Iterator[str]) -> int:
    """Solution part 1, count blocks on screen. (see Readme)"""
    coords = dict()
    p = Program.from_str(parse_input(data), 1, 0, 0, 0, 0, 0, 0)
    while True:
        try:
            x = next(p)
            y = next(p)
            code = next(p)
        except StopIteration:
            break
        coords[f"({x}, {y})"] = Tile(code)
    return sum(1 for code in coords.values()
                 if code == Tile.BLOCK)


def part_2(data: Iterator[str]) -> int:
    """Solution part 2, running the given program in sensor boost mode
    (see Readme part 2)"""
    p = Program.from_str(parse_input(data), 0)
    p.mem.write(0, 2)
    screen = Screen()
    while True:
        try:
            x = next(p)
            y = next(p)
            code = next(p)
        except StopIteration:
            break
        if x == -1 and y == 0:
            screen.score = code
            print(screen)
        else:
            screen.set(x, y, translate_tile(Tile(code)))
    return 0


if __name__ == '__main__':
    create_cli(13, part1=part_1, part2=part_2)
