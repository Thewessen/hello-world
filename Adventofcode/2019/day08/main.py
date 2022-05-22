#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator
from itertools import dropwhile
from more_itertools import windowed
from collections import Counter

def parse_input(data: Iterator[str]) -> str:
    return next(data).strip()


def part_1(data: Iterator[str]) -> int:
    """Solution part 1 (see Readme)"""
    enc = parse_input(data)
    size = 25 * 6
    layers = (Counter(layer) for layer in windowed(enc, size, step=size))
    count = min(layers, key=lambda c: c['0'])
    return count['1'] * count['2']


def color_image(image: Iterator[str|None]) -> Iterator[str|None]:
    """Map every pixel to a representive ascii char. 1 is 'black' and 0 is
    'white'."""
    c_map = {
        '1': '྿',
        '0': ' '
    }
    
    for pixel in image:
        if pixel is not None:
            yield c_map[pixel]


def part_2(data: Iterator[str]) -> None:
    """Prints the decoded image to screen (see README part 2)"""
    enc = parse_input(data)
    width = 25
    height = 6
    size = width * height
    pixels = zip(*windowed(enc, size, step=size))
    image = (next(dropwhile(lambda p: p == '2', layer))
             for layer in pixels)
    for row in windowed(color_image(image), width, step=width):
        print(''.join(row))


if __name__ == '__main__':
    create_cli(8, part1=part_1, part2=part_2)
