#!/usr/bin/env python3

import sys
sys.path.append('..')
from cli import create_cli
from typing import Iterator

def parse_input(data: Iterator[str]) -> Iterator[int]:
    """Parses Elve calibrate document from puzzle input"""
    for line in data:
        n = ''.join(ch for ch in line.strip() if ch.isdigit())

        if len(n) == 0:
            continue

        yield int(n[0] + n[-1])

def translate_line_digits(line: str) -> Iterator[str]:
    """Translate calibrate documents digit words from puzzle input"""
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    while len(line) > 0:
        if line[0].isdigit():
            yield line[0]
            line = line[1:]
            continue

        for key, value in digits.items():
            if line.startswith(key):
                yield value
                break

        # move to next character
        line = line[1:]

def translate_digits(data: Iterator[str]) -> Iterator[str]:
    """Translate calibrate documents digit words from puzzle input"""
    for line in data:
        yield ''.join(translate_line_digits(line))

def calibrate(data: Iterator[str]) -> int:
    """Calibrate document"""
    return sum(parse_input(data))

def adv_calibrate(data: Iterator[str]) -> int:
    """Calibrate document with advanced rules"""
    digits = translate_digits(data)
    return sum(parse_input(digits))

if __name__ == '__main__':
    create_cli(1, part1=calibrate, part2=adv_calibrate)
